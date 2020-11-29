import fastapi
from typing import Optional
from models.location import Location
from fastapi import Depends

router = fastapi.APIRouter()

@router.get('/api/weather/{city}')
def weather(
    loc:Location=Depends(),
    units:Optional[str] = 'metric'
):
    return f"{loc.city}, {loc.state}, {loc.country} in {units}"
