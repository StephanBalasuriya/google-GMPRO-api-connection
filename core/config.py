import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_ID = os.getenv("GCP_PROJECT_ID")
    LOCATION = os.getenv("GCP_LOCATION")
    TIMEOUT = int(os.getenv("GMPRO_TIMEOUT_SECONDS", 30))

settings = Settings()
