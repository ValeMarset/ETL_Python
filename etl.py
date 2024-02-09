import csv
import requests
import pandas as pd


def extraction_data_from_api(url_api):
  data = pd.read_json(url_api)
  return data


def transformation_data(data):

  data_harry_potter = data[['actor', 'alternate_names', 'dateOfBirth', 'gender', 'house', 'name']].copy()
  data_harry_potter.set_index('house', inplace=True)  # Aquí crearé un índice por "casa"
  data_harry_potter.sort_values(by='house', ascending=False, inplace=True)  # Lo ordenaré de manera descendente

  print(data_harry_potter)
  return data_harry_potter


def load_data_to_csv(data):
  columns = list(data[0].keys())

  with open('datos_harry_potter.csv', 'w', newline='') as archivo:
    writer_csv = csv.DictWriter(archivo, fieldnames=columns)
    writer_csv.writeheader()
    writer_csv.writerows(data)

  print('Se ha creado el archivo CSV correctamente')
