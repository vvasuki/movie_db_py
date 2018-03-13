import json
import tmdbsimple as tmdb
import logging

logging.basicConfig(
  level=logging.DEBUG,
  format="%(levelname)s: %(asctime)s %(message)s"
)


local_config = json.load(open('local_config.json'))
tmdb.API_KEY = local_config["tmdb_api_key"]


def get_release_date(query):
  response = tmdb.Search().movie(query = query)
  if len(response) == 1:
    return response.release_date
  else:
    return None





if __name__ == '__main__':
  logging.debug(get_release_date(query = "Bourne"))