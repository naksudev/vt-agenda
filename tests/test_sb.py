import pytest
from unittest import mock
from modules import webhook  # Importe ta fonction send depuis ton module

# Utilise un mock pour requests.post()
@mock.patch('requests.post')
def test_send(mock_post):
    # Configuration du mock pour simuler une réponse 200
    mock_post.return_value.status_code = 200

    # Appel à la fonction send avec des valeurs factices
    url = 'https://example.com/webhook'
    imgPath = 'output/example.jpg'
    webhook.send(url, imgPath)

    # Vérification que requests.post() a été appelé avec les bonnes valeurs
    mock_post.assert_called_once_with(
        url,
        data={'payload_json': mock.ANY},
        files={'file': (imgPath, mock.ANY)}
    )

