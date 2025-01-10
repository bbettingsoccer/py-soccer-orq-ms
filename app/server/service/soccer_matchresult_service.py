import json
import os
import requests

from app.server.common.enviroment_conf import get_path_file
from app.server.common.http_request_response import HttpRequestResponse
from app.server.common.match_constants import MatchConstants


class SoccerMatchResultService:

    def process_orq(self, crawl: str, championship: str, job_instance: str, date_match: str):

        self.process_match_result_scrapy(crawl, championship, job_instance, date_match)
        self.process_match_result_etl(date_match, championship)

    @staticmethod
    def process_match_result_scrapy(crawl: str, championship: str, job_instance: str, date_match: str):
        try:
            scrapy_url = os.getenv('API_SOCCER_SCRAPY')
            http_util = HttpRequestResponse()
            url = scrapy_url.format(crawl=crawl, championship=championship, job_instance=job_instance,
                                    date_match=date_match)
            response = requests.get(url)
            response_http = http_util.check_http_status_code(response)
            return response_http
        except Exception as e:
            print("[ERROR]-[SoccerScrapyService][scrapy_runtime] :: ", e)
            response_http = MatchConstants.HTTP_CLIENT_ERROR_500
            return response_http

    @staticmethod
    def process_match_result_etl(date_match: str, championship: str):
        path_file = get_path_file(folder1="env", folder2="ApiSpark_Invoke", file="post_body_matchresult_etl.json")
        try:
            spark_url = os.getenv('API_SOCCER_ETL')
            with open(path_file, 'r') as f:
                body = json.load(f)
                appArgs = body['appArgs']
                appArgs[3] = date_match
                appArgs[4] = championship
                body['appArgs'] = appArgs
                print("body body_matchresult ", body)
            response = requests.post(spark_url, json=body)
            print("REQUEST", response.text)
        except Exception as e:
            print("[ERROR]-[SoccerScrapyService][instance_batch_etl] :: ", e)
