import cfbd
import os

configuration = cfbd.Configuration(
    access_token=os.environ["BEARER_TOKEN"]
)

