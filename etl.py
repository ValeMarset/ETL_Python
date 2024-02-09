import csv

import requests


def extraction_data_from_api(url_api):
  r = requests.get(url_api)
  data = r.json()
  return data


def transformation_data(data):
  data_harry_potter = []

  for data_character in data:
    data_character = {
      'actor': data_character['actor'],
      'nombres_alternativos': data_character['alternate_names'],
      'cumpleaños': data_character['dateOfBirth'],
      'genero': data_character['gender'],
      'casa': data_character['house'],
      'nombre': data_character['name']
    }
    data_harry_potter.append(data_character)

  return data_harry_potter


def load_data_to_csv(data):
  columns = list(data[0].keys())

  with open('datos_harry_potter.csv', 'w', newline='') as archivo:
    writer_csv = csv.DictWriter(archivo, fieldnames=columns)
    writer_csv.writeheader()
    writer_csv.writerows(data)

  print('Se ha creado el archivo CSV correctamente')
