# %%
from modules import MarksixCrawler, Data

# %%
marksix_crawler = MarksixCrawler()
marksix_crawler.scrape()
# %%
# Read Data
data = Data()
df = data.get_data()
print(df)
# %%
