import os
from IPython import get_ipython
from sqlalchemy import create_engine


DATABASE_URL = os.environ["DATABASE_URL"]

# create the connection so the user does not have to
engine = create_engine(DATABASE_URL)

get_ipython().magic("load_ext sql")
