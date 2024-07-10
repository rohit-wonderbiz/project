from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine, Sessionlocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind = engine)

class EmployersBase(BaseModel):
    id: int    
    username: str
    # password_hash = Column(String(50))
    email: str
    first_name: str
    last_name: str
    phone: int
    address: str
    created_at: str
    updated_at: str

class Employer_ProfilesBase(BaseModel):
    id: int
    employer_id: int  #To make Foreign key
    company_name: str
    company_description:str
    website: str
    created_at: str
    updated_at: str

class Job_PostingsBase(BaseModel):
    id: int
    employer_id: int #To make Foreign key  
    job_type: str
    job_title: str
    job_description: str
    no_of_positions: int
    skills: str
    location: str
    salary: int
    posted_at: str
    apply_before: str

def get_db():
    db = Sessionlocal()
    try: 
        yield db

    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]



# Employers Table GET Method ALL
@app.get("/emp/", status_code= status.HTTP_200_OK)
async def read_all_employee(db: db_dependency):
    employee_profile = db.query(models.Employers).all()
    if not employee_profile:
        raise HTTPException(status_code=404, detail='No employee profiles were found')
    return employee_profile


# Employers Table GET Method
@app.get("/emp/{emp_Id}", status_code= status.HTTP_200_OK)
async def read_employee(emp_Id: int, db: db_dependency):
    post = db.query(models.Employers).filter(models.Employers.id == emp_Id).first()
    if post is None:
        HTTPException(status_code=404, detail='Employee was not found')
    return post

#Employers Table POST Method
@app.post("/emp/", status_code=status.HTTP_201_CREATED)
async def create_employee(emp: EmployersBase, db: db_dependency):
    db_post = models.Employers(**emp.model_dump())
    db.add(db_post)
    db.commit()

#Employers Table DELETE Method
@app.delete("/emp/{emp_Id}", status_code= status.HTTP_200_OK)
async def delete_employee(emp_Id: int, db: db_dependency):
    db_post = db.query(models.Employers).filter(models.Employers.id == emp_Id).first()
    if db_post is None:
        raise HTTPException(status_code=404, detail='Employee was not found')
    db.delete(db_post)
    db.commit()

#Employers Table EDIT Method
@app.put("/emp/{emp_Id}", status_code=status.HTTP_200_OK)
async def update_employee(emp_Id: int, updated_post: EmployersBase, db: db_dependency):
    db_post = db.query(models.Employers).filter(models.Employers.id == emp_Id).first()
    if db_post is None:
        raise HTTPException(status_code=404, detail='Employee was not found')

    for key, value in updated_post.model_dump().items():
        setattr(db_post, key, value)

    db.commit()
    db.refresh(db_post)
    return db_post