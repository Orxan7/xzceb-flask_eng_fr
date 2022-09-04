"""Module contain functions to translate text from English to French
and from French to English"""
import os

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv


load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# Prepare the Authenticator
authenticator = IAMAuthenticator(apikey=apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(english_text):
    """function return translation from english to french"""
    if not english_text:
        return ""
    french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()['translations'][0]['translation']
    return french_text


def frenchToEnglish(french_text):
    """function return translation from french to english"""
    if not french_text:
        return ""
    english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()['translations'][0]['translation']
    return english_text
