import json
import os
import pytest
import logging

logging.basicConfig(
  level=logging.DEBUG,
  format="%(levelname)s: %(asctime)s %(message)s"
)

TEST_DATA_PATH = os.path.join(os.path.dirname(__file__), 'data', 'approxDeduplicationTests.json')
LOCAL_DATA_DIR_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'local_data')

