from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm.session import Session
from .. import models, schemas, utils

# get course
# get courses all
# patch course
# delete course
# bulk delete courses ? - might be worthwhile to delete one at a time w/ a confirmation each time