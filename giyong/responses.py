from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder



class Response(JsonResponse):
    """
    response
    """

    def __init__(
            self,
            status=200,
            title="",
            data="",
            msg="",
            code="S0000",
            count=None,
            has_next=None,
            page=None,
            encoder=DjangoJSONEncoder,
            safe=False,
            **kwargs
    ):

        response_data = {}
        if title:
            response_data["title"] = title
        if data:
            response_data["data"] = data

        if msg:
            response_data["msg"] = msg

        if code:
            response_data["code"] = code

        if count is not None:
            response_data["count"] = count

        if has_next is not None:
            response_data["has_next"] = has_next

        if page is not None:
            response_data["page"] = page


        super().__init__(
            response_data,
            encoder=encoder,
            status=status,
            safe=safe,
            **kwargs
        )


class ErrorResponse(Response):
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


class ExceptionResponse(ErrorResponse):
    """
    error response
    """

    def __init__(self, ex):
        super().__init__(msg=ex.detail, code=ex.code)
