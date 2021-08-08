from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder



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
