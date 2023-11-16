import pytest
from unittest import mock
from modules import webhook 

@mock.patch('requests.post')
def test_send(mock_post):
    mock_post.return_value.status_code = 200

    url = 'https://example.com/webhook'
    imgPath = 'output/example.jpg'
    webhook.send(url, imgPath)

    mock_post.assert_called_once_with(
        url,
        data={'payload_json': mock.ANY},
        files={'file': (imgPath, mock.ANY)}
    )

