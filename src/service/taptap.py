import requests

from time import time
from datetime import datetime
from icecream import ic

from src.utils.fileIO import File
from src.utils.logs import logger


class TapTap:
    def __init__(self) -> None:

        self.__file = File()

        self.DOMAIN = 'www.taptap.io'
        self.MAIN_URL = 'https://www.taptap.io/'

        self.API_TRANDING = 'https://www.taptap.io/webapiv2/i/sidebar/v1/list?type=landing&X-UA=V%3D1%26PN%3DWebAppIntl2%26LANG%3Den_US%26VN_CODE%3D114%26VN%3D0.1.0%26LOC%3DCN%26PLT%3DPC%26DS%3DAndroid%26UID%3D1fd19460-0178-4964-891a-a75496cf5e21%26CURR%3DID%26DT%3DPC%26OS%3DWindows%26OSV%3DNT%252015.0.0'
        
        ...

    def extract_data(self) -> dict:

        results = {
            "domain": self.DOMAIN,
            "url": self.MAIN_URL,
            "crawling_time": str(datetime.now()),
            "crawling_time_epoch": int(time()),
            "apps": {

            }
        }
        ...

    def main(self):
        response = requests.get(self.API_TRANDING)
        ic(response)

        apps = response.json()
        self.__file.write_json(path='data/first.json', content=apps)
        ...