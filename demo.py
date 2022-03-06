from nocap import NoCap

solver = NoCap(api_key="API_KEY")
try:
    solution = solver.hcaptcha(mode=3, host="host", sitekey="sitekey", proxy="http://user:pass@ip:port")
    print(solution)
except Exception as e:
    print(e)
