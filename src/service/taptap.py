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
        self.API_APPS = 'https://www.taptap.io/webapiv2/i/app/v5/detail?X-UA=V%3D1%26PN%3DWebAppIntl2%26LANG%3Den_US%26VN_CODE%3D114%26VN%3D0.1.0%26LOC%3DCN%26PLT%3DPC%26DS%3DAndroid%26UID%3D1fd19460-0178-4964-891a-a75496cf5e21%26CURR%3DID%26DT%3DPC%26OS%3DWindows%26OSV%3DNT%252015.0.0&id='
        self.API_REVIEW = 'https://www.taptap.io/webapiv2/feeds/v1/app-ratings?limit=10&X-UA=V%3D1%26PN%3DWebAppIntl2%26LANG%3Den_US%26VN_CODE%3D114%26VN%3D0.1.0%26LOC%3DCN%26PLT%3DPC%26DS%3DAndroid%26UID%3D1fd19460-0178-4964-891a-a75496cf5e21%26CURR%3DID%26DT%3DPC%26OS%3DWindows%26OSV%3DNT%252015.0.0&app_id=82354'
        
        ...

    def __extract_data(self, id: int, type: str) -> None:
        response = requests.get(self.API_APPS+str(id))
        ic(response)

        app = response.json()

        review = requests.get(self.API_REVIEW)
        results = {
            "domain": self.DOMAIN,
            "url": self.MAIN_URL,
            "crawling_time": str(datetime.now()),
            "crawling_time_epoch": int(time()),
            "type": type,
            "apps": {
                "id": id,
                "title": app["data"]["app"]["title"],
                "price": app["data"]["app"]["price"],
                "update_date": app["data"]["app"]["update_date"],
                "descriptions": app["data"]["app"]["description"],
                "informations": [info for info in app["data"]["app"]["information"]],
                "official": app["data"]["app"]["has_official"],
                "tags": [tag["value"] for tag in app["data"]["app"]["tags"]],
                "developers": app["data"]["app"]["developers"],
                "alias": app["data"]["app"]["seo"]["alias_name"],
                "faq": app["data"]["app"]["seo"]["faq"],
                "events": app["data"]["app"]["seo"]["events"],
                "supported_platforms":[platform["key"] for platform in  app["data"]["app"]["supported_platforms"]],
            },
            "review": {

            }
        }
        ...

    def main(self) -> None:
        response = requests.get(self.API_TRANDING)
        ic(response)

        apps = response.json()
        ic(len(apps["data"]["list"][0]["data"]["data"]))
        
        for app in apps["data"]["list"][0]["data"]["data"]:
            self.__extract_data(id=app["id"], type=app["type"])

            break

        ...