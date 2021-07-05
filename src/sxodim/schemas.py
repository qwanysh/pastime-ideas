import pydantic


class PopularPlace(pydantic.BaseModel):
    title: str
    description: str
    price: str = None
