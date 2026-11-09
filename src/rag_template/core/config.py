# never hardcode database URL / API keys, read it from .env
# we use pydantic_settings , "settings" class loads .env -> python object .
# if database_url is missing, the app fails fast at startup not during the request !

