from app.server.common.enviroment_conf import get_path_file
import json

from app.server.dto.etl_process_dto import EtlProcessDto
from app.server.dto.scrapy_process_dto import ScrapyProcessDto


class BuildBodyRequest:

    @staticmethod
    def build_body_etl(etl_dto: EtlProcessDto):
        path_file = get_path_file(folder1="env", folder2="spark_api", file="post_body_etl.json")
        try:
            with open(path_file, 'r') as f:
                body = json.load(f)
                appResource = etl_dto.dir_spark+etl_dto.appResource
                appArgs = body['appArgs']
                appArgs[1] = etl_dto.dir_spark+etl_dto.appResource
                appArgs[2] = etl_dto.dir_spark+etl_dto.appResource+'/'+etl_dto.main_spark
                appArgs[3] = etl_dto.date_match
                appArgs[4] = etl_dto.championship
                body['appResource'] = appResource
                body['appArgs'] = appArgs
            print("FILE ETL ", body)
            return body
        except Exception as e:
            print("[ERROR]-[SoccerScrapyService][instance_batch_etl] :: ", e)



    @staticmethod
    def build_body_scrapy(spark_body: ScrapyProcessDto):
        return spark_body.__dict__
