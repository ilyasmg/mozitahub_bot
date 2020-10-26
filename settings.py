import os
from dotenv import load_dotenv
load_dotenv()

def is_env_defined(variable):
    if variable in os.environ:
        r = os.getenv(variable)

        if r is "":
            raise Exception(variable + " is null. Check your .env file and try again!")

        return r
    else:
        raise Exception(variable + " is not present. Check your .env file and try again!")

TOKEN = is_env_defined("TOKEN")
NEWS_CHANNEL = is_env_defined("NEWS_CHANNEL")
