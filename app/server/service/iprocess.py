from abc import ABCMeta, abstractmethod

from app.server.api.request_process_api import RequestProcessApi
from app.server.api.response_process_api import ResponseProcessApi
from app.server.dto.etl_process_dto import EtlProcessDto
from app.server.dto.http_response_dto import HttpResponseDto
from app.server.dto.scrapy_process_dto import ScrapyProcessDto

class IProcess(metaclass=ABCMeta):

    @abstractmethod
    def start_process(self, process_dto: RequestProcessApi) -> ResponseProcessApi:
        pass

    @abstractmethod
    def invoke_etl_process(self, process_etl: EtlProcessDto) -> HttpResponseDto:
        pass

    @abstractmethod
    def invoke_scrapy_process(self, process_scrapy: ScrapyProcessDto) -> HttpResponseDto:
        pass

    @abstractmethod
    def invoke_webservices(self):
        pass
    
