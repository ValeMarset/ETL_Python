import etl
import pprint as p

if __name__ == '__main__':
  result = etl.extraction_data_from_api('https://hp-api.onrender.com/api/characters')
  transformed_data = etl.transformation_data(result)
