import os
import requests
from dotenv import load_dotenv

load_dotenv()

GOOGLE_PLACES_API_KEY = os.getenv(
    "GOOGLE_PLACES_API_KEY"
)


def search_venues(
    city,
    event_type="business event venue"
):

    query = f"{event_type} in {city}"

    url = (
        "https://maps.googleapis.com/maps/api/place/textsearch/json"
    )

    params = {
        "query": query,
        "key": GOOGLE_PLACES_API_KEY
    }

    response = requests.get(
        url,
        params=params
    )

    data = response.json()

    results = data.get("results", [])

    venues = []

    for place in results[:5]:

        venue = {
            "name": place.get("name"),
            "address": place.get("formatted_address"),
            "rating": place.get("rating"),
            "maps_link": (
                f"https://www.google.com/maps/place/"
                f"?q=place_id:{place.get('place_id')}"
            )
        }

        venues.append(venue)

    return venues

