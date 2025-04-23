from fastapi import APIRouter
from fastapi_xml import add_openapi_extension
from fastapi_xml import XmlRoute
from fastapi_xml import XmlAppResponse
from fastapi_xml import XmlBody
from serializers.apple import CreateApple,AppleResponse

router = APIRouter(default_response_class=XmlAppResponse)
route_class = XmlRoute
add_openapi_extension(router)



@router.post("/", response_model=AppleResponse, tags=["Apples"])
def echo(new_apple: CreateApple = XmlBody()) -> AppleResponse:
    app_response=AppleResponse(**new_apple)
    return app_response