import os
import csv
import pandas as pd

import logging
import movie_db_py

logging.basicConfig(
  level=logging.DEBUG,
  format="%(levelname)s: %(asctime)s %(message)s"
)


LOCAL_DATA_DIR_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'local_data')


def get_rinema_file():
  """

  rinema expects a csv like:
  Title: Name of the movie (Required)
  Release Year: Release year for the movie (Required)
  Rating: Rating for the movie out of 5 (Optional)
  Review: Review for the movie (Optional)
  Collections: Name of rinema collections separated by comma in which the movie should be added (Optional)
  """
  input_file = os.path.join(LOCAL_DATA_DIR_PATH, "movie_data.tsv")
  movie_data_df = pd.read_table(input_file, dtype=str)
  # logging.debug(movie_data_df['nAma'])
  movie_data_out_df = pd.DataFrame()
  movie_data_out_df["Title"] = movie_data_df["Title"]

  def get_review(row):
    row = row.fillna('')
    review = "\n".join(["Synopsis__: " + str(row['viShayaH']), "Comments__: " +  str(row['tolana-TippaNiH'])]).replace("Synopsis__: \nComments__: ", "")
    return review.strip()


  def get_rating(rating_str):
    import math
    score = float(str(rating_str).replace("/4.",""))*5.0/4.0
    if math.isnan(score):
      score = ""
    return str(score)


  def get_collections(row):
    row = row.fillna('')
    collections = str(row['gaNa']) + ":" + str(row['upagaNa']) + ":" + str(row['upopagaNa']) + ":"
    collections = collections.replace(":::", "").replace("::", "")
    collections = ",".join(set([collections] + collections.split(":")))
    return collections

  movie_data_out_df["Review"] = movie_data_df[['viShayaH', 'tolana-TippaNiH']].apply(get_review, axis=1)
  movie_data_out_df["Collections"] = movie_data_df[["gaNa", "upagaNa", "upopagaNa"]].apply(get_collections, axis=1)
  # movie_data_out_df["Rating"] = movie_data_df['tolanam'].map(get_rating)

  # Add release dates.
  # release_years = [movie_db_py.get_release_year(show_name) for show_name in movie_data_df['nAma']]
  # movie_data_out_df["Release Year"] = release_years

  movie_data_out_df.to_csv(os.path.join(LOCAL_DATA_DIR_PATH, "movie_data_rinema.csv"), sep=',')
  logging.debug(movie_data_out_df)


if __name__ == '__main__':
  get_rinema_file()