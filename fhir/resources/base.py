import json
from fhir.constants import XML, JSON


class FHIRResourceBase:
    """ A base class of an FHIR Resource Base
    """

    def __init__(self, api_url, token, op_format):
        self.api_url = api_url
        self.token = token
        self.op_format = op_format

    def gen_headers(self):
        headers = {
            "Authorization": "Bearer " + self.token,
            "Accept": self.op_format
        }

        return headers

    def gen_response(self, response):
        if self.op_format == JSON:
            # TODO: create a pt object
            return json.loads(response.text)
        if self.op_format == XML:
            # TODO: create a pt object
            return response.text
