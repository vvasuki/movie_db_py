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
  if len(response["results"]) >= 1:
    return response["results"][0]["release_date"]
  else:
    return ""


def get_release_year(query):
  return get_release_date(query=query).split("-")[0]


if __name__ == '__main__':
  logging.debug(get_release_date(query = "Bourne"))