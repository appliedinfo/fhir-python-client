# A Driver to test functionality

from fhir.client import Client

if __name__ == "__main__":

    epic_url = "https://open-ic.epic.com/Argonaut-Fixed/api/FHIR/Argonaut"
    allscripts_url = "https://cloud.allscriptsunity.com/FHIR"
    intersys_url = "https://argonaut.intersystems.com/fhir"
    client_id = ""
    epic_secret = "bX8YB9sTLy3Bcc1nG50NMKcDas8MOT7efaMvqljDd9XwUz5xTbsCFkIYnOM5E2uDosnvFYGkfAaQcTFZU4To3ylrcCPj2VvSOTJ"
    allscripts_secret = "6D1A05FF-4DA7-46CA-8E60-2DCD38A183B2"
    intersys_secret = "L6vV9Ewd7r9M6nBXBuxtfVVdoh4lHFrDySFC/ufj8xqnAKGFbFRpdAqpXPIVXWjuElRz3atcPMz16Fhv8UL10Q==" # intersys

    epic_patient_id = "RVBUOyAgICAgWjU2OTI7Ozs7dGVybWluYXRl" #epic
    intersys_patient_id = "pat-1" # intersystems

    api_url = intersys_url
    client_secret = intersys_secret
    patient_id = intersys_patient_id

    c = Client(api_url, client_id, client_secret)

    patient = c.get_patient_resource()

    print patient.get(patient_id=patient_id)

    print patient.list(given="John")
