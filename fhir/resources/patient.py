import requests
from base import FHIRResourceBase


class Patient(FHIRResourceBase):

    def get(self, patient_id=None):
        """ Retrieve a patient's basic demographics and identifiers, given a unique patient id."""

        res_url = self.api_url+"/Patient/"+str(patient_id)
        resp = requests.get(res_url, headers=self.gen_headers())

        print resp
        return self.gen_response(resp)

    def list(self, name=None, family=None, given=None,
             identifier=None, gender=None, birthdate=None):
        """ Find patients based on a variety of demographic criteria."""

        qry_url = self.api_url+"/Patient?"

        qparams = []
        if name:
            qparams.append("name="+name)
        if family:
            qparams.append("family="+family)
        if given:
            qparams.append("given="+given)
        if identifier:
            qparams.append("identifier="+identifier)
        if gender:
            qparams.append("gender="+gender)
        if birthdate:
            qparams.append("birthdate="+birthdate)

        qry_url += "&".join(qparams)

        print qry_url
        resp = requests.get(qry_url, headers=self.gen_headers())
        print resp
        return self.gen_response(resp)
