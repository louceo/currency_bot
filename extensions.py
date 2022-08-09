import requests
import json
from config import currency

class ConvertException(Exception):
    pass

class Conversion():
    @staticmethod
    def conversion(amount, quote, base):
        try: 
            amount = float(amount)
        except ValueError: raise ConvertException(f'{amount} - не количество')
        if amount <= 0:
            raise ConvertException('Неверное количество')
        if quote == base: 
            raise ConvertException('Нельзя конвертировать одинаковую валюту') 
        try: 
            quote_val = currency[quote]
        except KeyError: raise ConvertException(f'Неправильно введена валюта {quote}')
        try:
            base_val = currency[base]
        except KeyError: raise ConvertException(f'Неправильно введена валюта {base}')

        url = f'https://api.exchangerate.host/convert?from={quote_val}&to={base_val}'
        response = requests.get(url).content
        data = json.loads(response)['result']
        result = float(data) * float(amount)
        return result 
