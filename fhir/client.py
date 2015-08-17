from fhir.resources import Patient
from fhir.constants import XML, JSON


class Client:
    """ An API Client object

        The API endpoint and other credentials
        will be set through this object
    """

    def __init__(self, api_url, client_id, client_secret):
        """ Parameters:
                api_url: The API Endpoint with no trailing slash
                client_id: The client ID
                client_secret: The client secret
        """

        self.api_url = api_url
        self.client_id = client_id
        self.client_secret = client_secret
        # TODO: do oauth dance and get auth token
        self.token = self.client_secret  # temp
        self.op_format = JSON

    def get_patient_resource(self, patient_id=None):
        """ Get the Patient Resource
        """
        return Patient(api_url=self.api_url, token=self.token, op_format=JSON)
