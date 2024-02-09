import pandas as pd


def extraction_data_from_api(url_api):
  data = pd.read_json(url_api)
  return data


def transformation_data(data):

  data_harry_potter = data[['actor', 'alternate_names', 'dateOfBirth', 'gender', 'house', 'name']].copy()  # Copia del DataFrame sin afectar el original
  data_harry_potter.set_index('house', inplace=True)  # Aquí crearé un índice por "casa"
  data_harry_potter.sort_values(by='house', ascending=False, inplace=True)  # Lo ordenaré de manera descendente

  return data_harry_potter


def load_data_to_csv(data):
  data.to_csv('datos_harry_potter.csv', index=True)
  print('Se ha creado el archivo CSV correctamente')
