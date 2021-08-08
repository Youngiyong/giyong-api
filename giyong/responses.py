from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework import status
from rest_framework.exceptions import _get_error_details, APIException

API_RESPONSE = [
    # 공통
    {"code": "S0000", "name": "요청성공", "msg": "처리되었습니다."},
    {"code": "S0001", "name": "처리중", "msg": "처리중입니다."},
    {"code": "S0002", "name": "내부처리에러", "msg": "처리할 수 없습니다. 관리자에게 문의하세요."}
]

class BackOfficeResponse(JsonResponse):
    """
    response
    """

    def __init__(
            self,
            data="",
            pagination="",
            code="S0000",
            **kwargs
    ):

        response_data = {}

        if code:
            response_data["code"] = code

        if data:
            response_data["data"] = data

        if pagination:
            response_data["pagination"] = pagination

        super().__init__(
            response_data,
            **kwargs
        )


class BackOfficeErrorResponse(BackOfficeResponse):
    """
    error response
    """

    def __init__(
            self,
            status=400,
            msg="",
            code="",
            encoder=DjangoJSONEncoder,
            safe=False,
            json_dumps_params={"ensure_ascii": True},
            **kwargs
    ):
        super().__init__(
            msg=msg,
            code=code,
            encoder=encoder,
            status=status,
            safe=safe,
            json_dumps_params=json_dumps_params,
            **kwargs
        )


class BackOfficeExceptionResponse(BackOfficeErrorResponse):
    """
    error response
    """

    def __init__(self, ex):
        super().__init__(msg=ex.detail, code=ex.code)


class BackOfficeException(APIException):
    """
    default response exception
    """

    # status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    status_code = status.HTTP_400_BAD_REQUEST


    def __init__(
            self, status=status.HTTP_400_BAD_REQUEST, detail=None, code=None
    ):

        if status is not None:
            self.status_code = status

        if code is None:
            code = self.default_code

        else:
            self.detail = (
                _get_error_details(detail, code)
                if detail
                else _get_error_details(self.default_detail, code)
            )
