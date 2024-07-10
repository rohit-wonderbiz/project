from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = "mssql+pymssql://sa:user123@DESKTOP-LC5JOPD/EmployerDB"


engine = create_engine(URL_DATABASE, pool_size= 10, max_overflow= 30)

Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind= engine)

Base = declarative_base()
