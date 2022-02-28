from nocap import NoCap

solver = NoCap(api_key="API_KEY")
solution = solver.hcaptcha(mode=3, host="host", sitekey="sitekey", proxy="http://user:pass@ip:port")
print(solution)