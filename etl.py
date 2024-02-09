import csv
import requests
import pandas as pd


def extraction_data_from_api(url_api):
  r = requests.get(url_api)
  data = r.json()
  return data


def transformation_data(data):
  reduced_data = [{k: v for k, v in d.items() if k in ['actor', 'alternate_names', 'dateOfBirth', 'gender', 'house', 'name']} for d in data]

  data_harry_potter = pd.DataFrame(reduced_data)

  #Aquí crearé un índice por "casa" y lo ordenaré de manera ascendente
  data_harry_potter.set_index('house', inplace=True)
  data_harry_potter.sort_values(by='house', inplace=True)

  print(data_harry_potter)
  return data_harry_potter


def load_data_to_csv(data):
  columns = list(data[0].keys())

  with open('datos_harry_potter.csv', 'w', newline='') as archivo:
    writer_csv = csv.DictWriter(archivo, fieldnames=columns)
    writer_csv.writeheader()
    writer_csv.writerows(data)

  print('Se ha creado el archivo CSV correctamente')
