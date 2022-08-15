from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm.session import Session
from sqlalchemy import update
import os

path = os.getcwd()
#print(path)

from database import get_db
import schemas, utils, models

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

# post user - create user
# get user - get user
# patch user - update user
# get users - get all users
# batch patch users? - change status of multiple users at once
# delete user - with confirmation for each - no bulk

# Action: create user
# Actor: faculty
# Effect: user data added to db
# http method: POST
@router.post("", status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db) ):

    generated_password = utils.random_password()

    new_user = models.User(password=generated_password, **user.dict()) #** unpacks the fields for dict object

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"data": new_user}

# Action: get user
# Actor: Faculty/Student
# Effect: user data is returned
# http method: GET
@router.get("/{id}")
def get_user(id:int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} does not exist")
    
    return user

# Action: get users
# Actor: Faculty
# Effect: all user data is returned
# http method: GET
@router.get("")
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

# Action: update user
# Actor: Faculty
# Effect: modify user data
# http method: PATCH
# ---there is definitely a better way to do this. do i know what that way is? no.---
# ---what if user tried to sent 1000 fields in json body of request?---
@router.patch("/{id}")
def update_user(id: int, data: schemas.UserUpdate, db: Session = Depends(get_db)):
    if not data.dict(exclude_unset=True):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Bad request - user cannot be updated")
    
    user_query = db.query(models.User).filter(models.User.id == id).first()
    if not user_query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} does not exist")

    for pair in data.dict(exclude_unset=True):
        setattr(user_query, pair, data.dict()[pair])
    db.commit()
    return data.dict(exclude_unset=True)

# Action: delete user
# Actor: Faculty
# Effect remove user data from DB
# http method: DELETE
# ---INCOMPLETE---