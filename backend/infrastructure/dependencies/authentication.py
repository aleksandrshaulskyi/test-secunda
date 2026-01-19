from fastapi import Header, HTTPException, status

from settings import settings


async def get_static_api_key(
    x_api_key: str | None = Header(default=None, alias='X-API-Key'),
) -> str:
    if x_api_key is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='API key is missing',
        )

    if x_api_key != settings.security_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid API key',
        )

    return x_api_key
