import requests
from typing import List, Dict

API_ENDPOINT = "https://api.trafikinfo.trafikverket.se/v2/data.json"

class TrafikverketAPIError(Exception):
    """Custom exception for Trafikverket API errors."""
    pass


def get_train_announcements(api_key: str, limit: int = 5) -> List[Dict]:
    """Query the TrainAnnouncement endpoint and return a list of announcements.

    Parameters
    ----------
    api_key : str
        Your Trafikverket API key.
    limit : int, optional
        Maximum number of announcements to return. Default is 5.

    Returns
    -------
    list of dict
        List containing announcement dictionaries.
    """
    if not api_key:
        raise ValueError("API key is required")

    payload = {
        "REQUEST": {
            "LOGIN": {"authenticationkey": api_key},
            "QUERY": [
                {
                    "objecttype": "TrainAnnouncement",
                    "orderby": "AdvertisedTimeAtLocation",
                    "schemaversion": "1.6",
                    "limit": limit,
                }
            ],
        }
    }

    response = requests.post(API_ENDPOINT, json=payload)
    if response.status_code != 200:
        raise TrafikverketAPIError(f"HTTP {response.status_code}: {response.text}")

    data = response.json()
    try:
        return data["RESPONSE"]["RESULT"][0]["TrainAnnouncement"]
    except (KeyError, IndexError) as exc:
        raise TrafikverketAPIError("Unexpected response format") from exc

