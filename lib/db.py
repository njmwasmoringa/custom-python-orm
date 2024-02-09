from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:R00t-123@localhost:3306/school")
BASE = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()