import json
import requests


def correcto(text):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer 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',
    }

    data = """
    {
        """
    data += f'"prompt": "Corrige moi le text \'{text}\'",'
    data += """
        "temperature": 0,
        "max_tokens": 60,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0
    }
    """

    response = requests.post('https://api.openai.com/v1/engines/text-davinci-002/completions', headers=headers,
                             data=data)

    if response.ok:
        response_json = json.loads(response.text)
        corrected_text = response_json['choices'][0]['text']
        return corrected_text
    else:
        return f"Une erreur s'est produite: {response.text}"
