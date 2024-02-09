import requests


def extraction_data_from_api(url_api):
  r = requests.get(url_api)
  data = r.json()
  return data