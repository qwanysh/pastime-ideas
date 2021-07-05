import typing

from fastapi import APIRouter

from src.sxodim import schemas, utils

router = APIRouter()


@router.get(
    '/popular-places', response_model=typing.List[schemas.PopularPlace],
)
async def get_popular_places():
    return utils.get_sxodim_popular_places()
