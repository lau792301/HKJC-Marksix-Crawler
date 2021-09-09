# %%
from modules import MarksixCrawler, Data

# %%
marksix_crawler = MarksixCrawler()
marksix_crawler.scrape()
# %%
# Read Data
data = Data()
df = data.data()
print(df)
# %%
