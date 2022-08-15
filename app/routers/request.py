from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm.session import Session
from .. import models, schemas, utils

# post request
# get request
# patch request
# get all reequests
# bulk patch request? - approve/deny many at a time https://www.mscharhag.com/api-design/bulk-and-batch-operations#:~:text=Bulk%20(or%20batch)%20operations%20are,more%20requests%20with%20less%20data.
# ^ is very goo