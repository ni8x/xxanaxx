import requests

class Language:
    Arabic = 'ara'
    Bulgarian = 'bul'
    Chinese_Simplified = 'chs'
    Chinese_Traditional = 'cht'
    Croatian = 'hrv'
    Danish = 'dan'
    Dutch = 'dut'
    English = 'eng'
    Finnish = 'fin'
    French = 'fre'
    German = 'ger'
    Greek = 'gre'
    Hungarian = 'hun'
    Korean = 'kor'
    Italian = 'ita'
    Japanese = 'jpn'
    Norwegian = 'nor'
    Polish = 'pol'
    Portuguese = 'por'
    Russian = 'rus'
    Slovenian = 'slv'
    Spanish = 'spa'
    Swedish = 'swe'
    Turkish = 'tur'


class API:
    def __init__(
        self, api_key='helloworld', language=Language.English, **kwargs
    ):
        """
        :param api_key: API key string
        :param language: document language
        :param **kwargs: other settings to API
        """
        self.payload = {
            'isOverlayRequired': True,
            'apikey': api_key,
            'language': language,
            'OCREngine': 2,
            **kwargs
        }
    def _parse(self, raw):
      if type(raw) == str:
          raise Exception(raw)
      if raw['IsErroredOnProcessing']:
          raise Exception(raw['ErrorMessage'][0])
      return raw['ParsedResults'][0]['ParsedText']


    def ocr_url(self, url):
            """
            Process an image at a given URL.
            :param url: Image url
            :return: Result in JSON format.
            """
            data = self.payload
            data['url'] = url
            r = requests.post(
                'https://api.ocr.space/parse/image',
                data=data,
            )
            return self._parse(r.json())
