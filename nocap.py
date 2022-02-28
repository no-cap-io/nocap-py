import requests 
import time 

class NoCap:
    
    def __init__(self, api_key, poll=1):
        self.session = requests.Session()
        # Server settings
        self.server = "https://no-cap.io"
        self.api    = self.server + "/hcaptcha"
        # Client settings
        self.api_key = api_key
        self.poll = poll

    def create_task(self, **kwargs):
        """
        Upload a task to the NoCap API

        **kwargs:
            mode     (int): Mode used for solving captcha (1/2/3)
            proxy    (str): Proxy used for the task. Format: https://user:pass@ip:port
            host     (str): Host to solve the captcha for
            sitekey  (str): Sitekey for the host
            version  (str, optional): hCaptcha version to use
            imgproxy (str, optional): Proxy to use when fetching images. Defaults to proxy
            href     (str, optional): Page you are solving the captcha for
            rqdata   (str, optional): Rqdata to use for the task

        Returns:
            task_id (str): Task ID used for polling the task status
        """
        url = f"{self.api}/create?api_key={self.api_key}"
        resp = self.session.post(url, json=kwargs)
        task_id = resp.json()['task']
        return task_id
    
    def get_status(self, task_id):
        """
        View the status of an active task

        Args:
            task_id (str): Task ID to poll status of

        Returns:
            Captcha token or None if an error occurred
        """
        url = f"{self.api}/status?api_key={self.api_key}&task_id={task_id}"
        r = None
        while r == None or r['status'] == "solving":
            time.sleep(self.poll)
            r = self.session.get(url).json()
        if r['status'] == "success":
            return r['answer']
        return None 
        
    def hcaptcha(self, **kwargs):
        task_id = self.create_task(**kwargs)
        result = self.get_status(task_id)
        return result