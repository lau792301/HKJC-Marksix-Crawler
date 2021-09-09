# %%
from sqlalchemy import Column, Integer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd

from .setting import DATABASE_PATH, TABLE_NAME
# %%
# Dataclass
engine = create_engine(f'sqlite:///{DATABASE_PATH}', echo=False)
Base = declarative_base(bind=engine)
class Marksix(Base):
    __tablename__ = TABLE_NAME
    year = Column(Integer, primary_key=True)
    times = Column(Integer, primary_key=True)
    N1 = Column(Integer)
    N2 = Column(Integer)
    N3 = Column(Integer)
    N4 = Column(Integer)
    N5 = Column(Integer)
    N6 = Column(Integer)
    S1 = Column(Integer)

Base.metadata.create_all()
Session = sessionmaker(bind=engine)

class Data:
    def __init__(self):
        self.session = Session()
        self.data = get_data()

    def get_data(self):
        qry = self.session.query(Marksix)
        res = qry.all()
        datas = [record.__dict__ for record in res]
        df = pd.DataFrame(datas)
        df = df[['year', 'times', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'S1']]
        return df
