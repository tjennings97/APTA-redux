from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm.session import Session
from .. import models, schemas, utils

# get assignment
# get assignments all - for specified user
# get assignments all - for specified dates - for specified user & generically(?)
# patch assignment
# bulk patch assignments
# delete assignment
# bulk delete assignments