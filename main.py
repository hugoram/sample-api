import falcon
import json
import requests

WEATHER_API_BASE_URL = "https://www.metaweather.com/api/location"


class MainResource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = "Hello World"


class WeatherResource(object):
    def on_get(self, req, resp, location):
        try:
            location_search_response = self._api_call(f"/search/?query={location}")
            if not len(location_search_response):
                resp.status = falcon.HTTP_404
                resp.body = json.dumps(
                    {"message": "The location you are looking for could not be found."}
                )
                return

            location_id = location_search_response[0].get("woeid")

            location_weather_response = self._api_call(f"/{location_id}/")
            current_weather = location_weather_response.get("consolidated_weather")[0]

            resp.status = falcon.HTTP_200
            resp.body = json.dumps(
                {
                    "location": location_weather_response.get("title"),
                    "timezone": location_weather_response.get("timezone"),
                    "date": current_weather.get("applicable_date"),
                    "min_temp": f"{round(current_weather.get('min_temp'))}°C",
                    "max_temp": f"{round(current_weather.get('max_temp'))}°C",
                    "average_temp": f"{round(current_weather.get('the_temp'))}°C",
                }
            )

        except:
            resp.status = falcon.HTTP_500
            resp.body = json.dumps(
                {
                    "message": "There was a problem retrieving the weather. Try again later."
                }
            )

    def _api_call(self, path):
        return requests.get(f"{WEATHER_API_BASE_URL}{path}").json()


app = falcon.API()
app.add_route("/", MainResource())
app.add_route("/weather/{location}", WeatherResource())
