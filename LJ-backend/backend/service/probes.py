
from fastapi import APIRouter, Depends, HTTPException
from dependencies import get_session

router = APIRouter(
    prefix='/probes',
    tags=['probes'],
    dependencies=[Depends(get_session)],
    responses={404: {'description': 'Not found'}}
)

@router.get("/healthz")
def health_check():
    return 200