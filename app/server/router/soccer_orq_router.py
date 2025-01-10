from fastapi import APIRouter

from ..common.http_request_response import HttpRequestResponse
from ..common.match_constants import MatchConstants
from ..service.soccer_matchresult_service import SoccerMatchResultService

router = APIRouter()


@router.get("/matchresult/{crawl}/championship/{championship}/job/{job_instance}/date_match/{date_match}",
            response_description="Match retrieved")
async def get_process_match_result(crawl: str, championship: str, job_instance: str, date_match: str):
    service = SoccerMatchResultService()
    http_util = HttpRequestResponse()
    try:
        response_code = await service.process_orq(crawl, championship, job_instance, date_match)
        response_http = http_util.check_http_status_code(response_code)
        return response_http
    except Exception as e:
        response_http = http_util.check_http_status_code(MatchConstants.HTTP_ERROR_INTERNAL_CODE)
        return response_http


@router.get("/callback/matchresult/status/{status}", response_description="Match retrieved")
async def callback_process_match_result(crawl: str, championship: str, job_instance: str, date_match: str):
    service = SoccerMatchResultService()
    http_util = HttpRequestResponse()
    try:
        response_code = await service.process_orq(crawl, championship, job_instance, date_match)
        response_http = http_util.check_http_status_code(response_code)
        return response_http
    except Exception as e:
        response_http = http_util.check_http_status_code(MatchConstants.HTTP_ERROR_INTERNAL_CODE)
        return response_http
