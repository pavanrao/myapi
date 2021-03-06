from typing import Optional
import httpx


api_key: Optional[str] = None

async def get_report(
    city:str,
    state:Optional[str],
    country:str,
    units:str
)->dict:
    if state:
        q=f'{city},{state},{country}'
    else:
        q=f'{city},{country}'

    key=api_key
    url=f'https://api.openweathermap.org/data/2.5/weather?q={q}&appid={api_key}&units={units}'
    print(url)
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()

    data = resp.json()

    print(data)
    return data

