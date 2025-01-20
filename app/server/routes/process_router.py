from fastapi import APIRouter, Body

from app.server.api.response_process_api import ResponseProcessApi
from app.server.common.http_request_response import HttpRequestResponse
from app.server.api.request_process_api import RequestProcessApi
from app.server.service.process_service import ProcessService

router = APIRouter()

@router.post(path="/start",response_description="Process Execute Successfully")
async def start_process(data: RequestProcessApi = Body(...)):
    service = ProcessService()
    try:
        http_response = service.start_process(data)
        return http_response
    except Exception as e:
        print("Exception Process::", e)
        response_error = ResponseProcessApi.http_error_func_response()
        return response_error
