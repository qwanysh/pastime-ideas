from fastapi import APIRouter

from src.sxodim import utils

router = APIRouter()


@router.get('/popular-places')
def get_places():
    return utils.get_sxodim_popular_places()
