import json
import pytest
import responses

from trafikverket import get_train_announcements, TrafikverketAPIError, API_ENDPOINT


@responses.activate
def test_get_train_announcements_success():
    mocked_response = {
        "RESPONSE": {
            "RESULT": [
                {
                    "TrainAnnouncement": [
                        {"ActivityId": "1"},
                        {"ActivityId": "2"},
                    ]
                }
            ]
        }
    }

    responses.post(API_ENDPOINT, json=mocked_response, status=200)

    result = get_train_announcements("dummy", limit=2)
    assert result == [{"ActivityId": "1"}, {"ActivityId": "2"}]
    sent_payload = json.loads(responses.calls[0].request.body)
    assert "REQUEST" in sent_payload


@responses.activate
def test_get_train_announcements_http_error():
    responses.post(API_ENDPOINT, json={}, status=500)

    with pytest.raises(TrafikverketAPIError):
        get_train_announcements("dummy")

