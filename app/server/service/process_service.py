import os
from abc import ABC

from app.server.api.request_process_api import RequestProcessApi
from app.server.api.response_process_api import ResponseProcessApi
from app.server.component.build_body_request import BuildBodyRequest
from app.server.dto.etl_process_dto import EtlProcessDto
from app.server.dto.http_response_dto import HttpResponseDto
from app.server.dto.scrapy_process_dto import ScrapyProcessDto
from app.server.common.http_request_response import HttpRequestResponse
from app.server.common.match_constants import MatchConstants

class ProcessService(ABC):

    def start_process(self, process_api: RequestProcessApi) -> ResponseProcessApi:
        index = 0
        httpSuccess = ResponseProcessApi.http_success_func_response()
        httpError = ResponseProcessApi.http_error_func_response()
        errorStatus = False
        httpResponse = HttpResponseDto(status=MatchConstants.HTTP_SUCCESS,
                                       response_code=200,
                                       message="ok",
                                       data=None)
        try:
            for order in process_api.execution_order:
                match order.type_process:
                    case MatchConstants.PROCESS_TYPE_SCRAPY:
                        index = int(order.position)
                        print("___PROCESS_TYPE_SCRAPY ", process_api.scrapy_process[index])
                        responseScrapy = self.invoke_scrapy_process(scrapy_dto=process_api.scrapy_process[index])
                        if responseScrapy.status is not MatchConstants.HTTP_SUCCESS:
                            errorStatus = True
                            break
                    case MatchConstants.PROCESS_TYPE_ETL:
                        index = int(order.position)
                        print("___PROCESS_TYPE_ETL ", process_api.etl_process[index])
                        responseEtl = self.invoke_etl_process(etl_dto=process_api.etl_process[index])
                        if responseEtl.status is not MatchConstants.HTTP_SUCCESS:
                            errorStatus = True
                            break
                    case MatchConstants.PROCESS_TYPE_WS:
                        pass
            if errorStatus:
                return httpError
            else:
                return httpSuccess

        except Exception as e:
            print("[ERROR]-[MatchResultProcessService][start_process] :: ", e)
            return httpError


    def invoke_scrapy_process(self, scrapy_dto: ScrapyProcessDto) -> HttpResponseDto:
        httpRequest = HttpRequestResponse()
        url_scrapy = os.environ['API_SOCCER_SCRAPY']
        try:
            body = scrapy_dto.__dict__
            response = httpRequest.handle_request(request_type=MatchConstants.POST_REQ_TYPE, request_url=url_scrapy, data=body)
            return response
        except Exception as error:
            print(error)
            raise

    def invoke_etl_process(self, etl_dto: EtlProcessDto) -> HttpResponseDto:
        httpRequest = HttpRequestResponse()
        etl_url = os.getenv('API_SOCCER_ETL')
        try:
            body = BuildBodyRequest.build_body_etl(etl_dto=etl_dto)
            httpResponse = httpRequest.handle_request(request_type=MatchConstants.POST_REQ_TYPE,
                                                  request_url=etl_url,
                                                  data=body)
            return httpResponse
        except Exception as e:
            print("[ERROR]-[SoccerScrapyService][instance_batch_etl] :: ", e)




    def invoke_webservices(self):
        pass