# %%
import datetime
import requests
from bs4 import BeautifulSoup
import re

from .data import Marksix, Session

# %%
import logging
logging.basicConfig(level = logging.INFO)

# %%
CURRENT_YEAR = datetime.datetime.today().year
# %%
class MarksixCrawler:
    def __init__(self):
        self.session = Session()
        self.updated_years = self._get_data_years()

    # Get the year information of data from database
    def _get_data_years(self):
        qry = self.session.query(Marksix.year).distinct()
        res = qry.all()
        years = [year[0] for year in res]
        return years
    
    # Clean the string result in crawling process
    def _re_string(self, string, delimiter = ''):
        string = re.sub('\t', delimiter, string)
        string = re.sub('\n', delimiter, string)
        string_return = re.sub(' ', delimiter, string)
        return string_return
    
    # Scarping and update current year data
    def scrape(self):
        # Data from 1996 to Current Year
        YEARS = [year for year in range(1996, CURRENT_YEAR + 1)]
        logging.info('Data Checking:')
        for year in YEARS:
            # Check history data
            if (year != CURRENT_YEAR) & (year in self. updated_years):
                logging.info(f' {year} is exist')
                continue
            logging.info(f' updating {year}')
            # nfd.com.tw
            website = f'http://www.nfd.com.tw/house/year/F{year}.htm'
            html = requests.get(website)
            bs = BeautifulSoup(html.content, "html.parser")
            table = bs.find_all('table')[0]
            rows = table.find_all('tr')
            #Get each Row Data
            for row in rows[1:]:
                data_dict = {}
                row = row.find_all('td')
                try:
                    data_dict['year'] = int(self._re_string(row[0].text))
                    data_dict['times'] = int(self._re_string(row[1].text))
                    data_dict['N1'] = int(self._re_string(row[2].text))
                    data_dict['N2'] = int(self._re_string(row[3].text))
                    data_dict['N3'] = int(self._re_string(row[4].text))
                    data_dict['N4'] = int(self._re_string(row[5].text))
                    data_dict['N5'] = int(self._re_string(row[6].text))
                    data_dict['N6'] = int(self._re_string(row[7].text))
                    data_dict['S1'] = int(self._re_string(row[8].text))
                    # Upsert data into database
                    self.session.merge(Marksix(**data_dict))
                except:
                    logging.info(f'{year}:Row Data Issue') # Closed COVID-19:2020/02/01 - 2020/09/24
                    logging.info(row)
            self.session.commit()
            logging.info('Updated')