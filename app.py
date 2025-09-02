from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Your IBM Watson NLU API key and URL
api_key = 'YOUR_IBM_WATSON_API_KEY'
url = 'YOUR_IBM_WATSON_URL'

# Setup authenticator and service
authenticator = IAMAuthenticator(api_key)
nlu = NaturalLanguageUnderstandingV1(version='2021-08-01', authenticator=authenticator)
nlu.set_service_url(url)

# Sample legal text
legal_text = """
This Agreement shall commence on the Effective Date and shall continue for a period of two years,
unless terminated earlier in accordance with the provisions herein.
"""

# Analyze text for entities and keywords
response = nlu.analyze(
    text=legal_text,
    features=Features(
        entities=EntitiesOptions(sentiment=True, limit=5),
        keywords=KeywordsOptions(sentiment=True, limit=5)
    )
).get_result()

print(response)
