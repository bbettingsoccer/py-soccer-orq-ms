from app.server.dto.etl_process_dto import EtlProcessDto
from app.server.dto.order_process_dto import OrderExecuteProcessDto
from app.server.dto.scrapy_process_dto import ScrapyProcessDto
from typing import List
from dataclasses import dataclass

@dataclass
class RequestProcessApi:

    name_process: str
    domain: str
    execution_order: List[OrderExecuteProcessDto]
    scrapy_process: List[ScrapyProcessDto]
    etl_process: List[EtlProcessDto]
