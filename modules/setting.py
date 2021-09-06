# %%
import os
from dotenv import load_dotenv
load_dotenv()

# %%
import logging
logging.basicConfig(level = logging.INFO)
# %%
DATABASE_PATH  = os.getenv('DATABASE_PATH')
TABLE_NAME = os.getenv('TABLE_NAME')
logging.info('Database path:' + DATABASE_PATH)
logging.info('Table name:' + TABLE_NAME)
