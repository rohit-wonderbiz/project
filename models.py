from sqlalchemy import Table, Boolean, Column, Integer, String
from database import Base

class Employers(Base):
    __tablename__ = 'Employers'

    id = Column(Integer, primary_key=True, index = True, autoincrement=True)
    # id = Column(Integer, primary_key=True, index = True)
    username = Column(String(50), unique=True)
    # password_hash = Column(String(50))
    email = Column(String(100), unique=True)
    first_name = Column(String(20))
    last_name = Column(String(20))
    phone = Column(Integer)
    address  = Column(String(255))
    created_at = Column(String(20))
    updated_at = Column(String(20))

class Employer_Profiles(Base):
    __tablename__ = 'Employer_Profiles'

    id = Column(Integer, primary_key=True, index = True, autoincrement=True)
    # id = Column(Integer, primary_key=True, index = True)
    employer_id = Column(Integer)  #To make Foreign key
    company_name = Column(String(20))
    company_description = Column(String(2000))
    website = Column(String(255))
    created_at = Column(String(20))
    updated_at = Column(String(20))

class Job_Postings(Base):
    __tablename__ = 'Job_Postings'

    id = Column(Integer, primary_key=True, index = True, autoincrement=True)
    # id = Column(Integer, primary_key=True, index = True)
    employer_id = Column(Integer) #To make Foreign key  
    job_type = Column(String(20))
    job_title = Column(String(100))
    job_description = Column(String(1000))
    no_of_positions = Column(Integer)
    skills = Column(String(100))
    location = Column(String(50))
    salary = Column(Integer)
    posted_at = Column(String(20))
    apply_before = Column(String(20))






