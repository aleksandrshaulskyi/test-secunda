from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    #DB
    database_url: str = Field(validation_alias='DATABASE_URL')
    #SECURITY
    security_key: str = Field(validation_alias='SECURITY_KEY')

    model_config = {
        'env_file': '.env',
        'extra': 'allow',
    }

settings = Settings()