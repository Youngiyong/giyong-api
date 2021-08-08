from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder



class BackOfficeResponse(JsonResponse):
    """
    response
    """

    def __init__(
            self,
            items="",
            pagination=None,
            code="S0000",
            **kwargs
    ):

        response_data = {}
        if pagination is not None:
            response_data["pagination"] = pagination

        if code:
            response_data["code"] = code

        if items:
            response_data["data"] = items

        super().__init__(
            response_data,
            **kwargs
        )


class BacfOfficeErrorResponse(BackOfficeResponse):
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
            **kwargs
    ):
        super().__init__(
            msg=msg,
            code=code,
            encoder=encoder,
            status=status,
            safe=safe,
            **kwargs
        )


class BackOfficeExceptionResponse(BacfOfficeErrorResponse):
    """
    error response
    """

    def __init__(self, ex):
        super().__init__(msg=ex.detail, code=ex.code)
