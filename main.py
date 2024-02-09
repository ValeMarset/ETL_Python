import etl

if __name__ == '__main__':
  result = etl.extraction_data_from_api('https://hp-api.onrender.com/api/characters')
  print(result)