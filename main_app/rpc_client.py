import json
import requests
import tempfile
from django.conf import settings


def rpc(method, params):
    if params:
        try:
            params = json.loads(params)

        except json.JSONDecodeError:
            params = {}

    else:
        params = {}

    payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": 1
    }

    # Создание временных файлов для сертификата и ключа
    with tempfile.NamedTemporaryFile(delete=False) as cert_file, tempfile.NamedTemporaryFile(
            delete=False) as key_file:
        cert_file.write(settings.CLIENT_CERT.encode())
        key_file.write(settings.CLIENT_KEY.encode())
        cert_file.flush()
        key_file.flush()

        try:
            response = requests.post(
                "https://slb.medv.ru/api/v2/",
                json=payload,
                cert=(cert_file.name, key_file.name),
                headers={"Content-Type": "application/json"}
            )

            try:
                response_data = response.json()

            except ValueError:
                response_data = {"error": "Invalid response from server"}

        finally:
            # Удаление временных файлов
            cert_file.close()
            key_file.close()

    return response_data
