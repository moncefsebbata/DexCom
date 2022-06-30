import requests
from requests.structures import CaseInsensitiveDict

CLIENT_ID = "nilepatest001"
CLIENT_SECRET = "Password@1"
CLIENT_CREDENTIALS = "client_credentials"

url = "https://clarity.dexcom.com/api/subject/15949506208472640/analysis_session"



headers = CaseInsensitiveDict()
headers["Authorization"] = "OAuth2"

data = {
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "grant_type": CLIENT_CREDENTIALS,
    "scope": "read:org",
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodHRwczovL3N3ZWV0c3BvdGRpYWJldGVzLmNvbSIsInN1YiI6IlN3ZWV0c3BvdCIsImlhdCI6MTY1NjYwODQ3MiwiY29uc2VudFBlcm1pc3Npb24iOiJsaW5rZWRTdWJqZWN0cyIsImRleGNvbUlkIjoiNWQ0ZWZkZTEtNzg4NC00Y2YzLWJlYjctMzllNTM4OGFjNDBkIiwiZXhwIjoxNjU2Njk0ODcyLCJyb2xlIjoiT3duZXIiLCJzdWJqZWN0SWQiOiIxNTk0OTUwNjIwODQ3NDcyNjQwIn0.jeoY4FRMCG1eM5o4pmBCRQW2Suk1nWvuvgYTGe39Ivctzoi6QmXVzjh2AQvTCGgr4pbFuuPoC0NIApRujueICAz85jIGlPQLvmdXxMlPio5hJ-MfFdlftMf_RUH9ruoUC8_eWGc3QQxKinZ4mWbqIJ28rTQwo8hBKgHSPUj9t0_f3CIJDeIY60JiIrGQhqDZSZ7uddehmtjWL2SOgdlLygUTV8YIyBBl87drrjxzg9bD7_iG9iYAGA4C25jN9DvZF9HRIEHQIRpWx0MMNBRVXwtKph2m6q56s_gz1Kbn7zJPrGWGqlXxVITXq8tzRe6e5PLXgILDmcZSoBI4LJHmAg"
}
with requests.Session() as s:
    s.post(url)
resp = requests.post(url, headers=headers, data=data)
print(resp)

print(resp.status_code)