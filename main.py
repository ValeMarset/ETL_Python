import etl

if __name__ == '__main__':
  result = etl.extraction_data_from_api('https://hp-api.onrender.com/api/characters')
  transformed_data = etl.transformation_data(result)
  etl.load_data_to_csv(transformed_data)

