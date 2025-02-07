import json
import pytest

def test_read(test_client):
    response = test_client.get("/conversations/2")
    print(response)
    assert response.status_code == 200

with open('tests/response_2.json') as f:
    response_2_data = json.load(f)

@pytest.mark.parametrize("expected_response", [[{'chat_id': 2, 'message_counter': 1, 'message_text': 'Hello'}]])
def test_api(test_client, expected_response):
    response = test_client.get(f"/conversations/{2}")
    print(response.json())
    assert response.status_code == 200
    assert response.json() == expected_response