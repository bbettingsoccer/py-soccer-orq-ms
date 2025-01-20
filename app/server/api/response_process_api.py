from dataclasses import dataclass

from app.server.common.match_constants import MatchConstants


@dataclass
class ResponseProcessApi:
    response_code: int
    status: str
    message: str
    data: []

    @staticmethod
    def ResponseModel(response_code, status, message, data):
        return {
            "response_code": response_code,
            "status": status,
            "message": message,
            "data": [data]
        }

    @staticmethod
    def http_fail_response():
        responseFail = ResponseProcessApi(
            message=MatchConstants.HTTP_CLIENT_ERROR_500,
            response_code = MatchConstants.HTTP_ERROR_INTERNAL_CODE,
            status=MatchConstants.HTTP_FAIL,
            data=None,
        )
        return responseFail

    @staticmethod
    def http_success_func_response():
        responseSuccess = ResponseProcessApi(
            message=MatchConstants.HTTP_CLIENT_SUCCESS_200,
            response_code=MatchConstants.HTTP_SUCCESS_STATUS,
            status=MatchConstants.HTTP_SUCCESS,
            data=None,
        )
        return responseSuccess


    @staticmethod
    def http_error_func_response():
        responseError = ResponseProcessApi(
            message=MatchConstants.HTTP_CLIENT_ERROR_422,
            response_code=MatchConstants.HTTP_ERROR_UNPROCESSABLE_ENTITY,
            status=MatchConstants.HTTP_ERROR,
            data=None,
        )
        return responseError