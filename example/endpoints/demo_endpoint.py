from typing import List
# import phonenumbers

from aiohttp.web_response import Response
from aiohttp.web import Request

from aiohttp_rest.rest_endpoint import AioHTTPRestEndpoint


class DemoEndpoint(AioHTTPRestEndpoint):

    def connected_routes(self) -> List[str]:
        """
        """
        return [
            '/demo'
        ]

    async def get(self, request: Request) -> Response:
        """
        ---
        description: Method returns a crypt key for  device registration. Each key can be used only once
        produces:
        - application/protobuf
        responses:
            "200":
                description: successful operation. Secret key was produced
        """

        return Response(
            status=200,
            body='Hello world',
            content_type='text/plain'
        )
