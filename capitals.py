from flask import Flask, jsonify, request
import pytz
from datetime import datetime

app = Flask(__name__)

# Pre-defined token for authorization
API_TOKEN = "supersecrettoken123"

# Simple database of capital cities with timezone info (you can expand this)
city_timezones = {
    'London': 'Europe/London',
    'New York': 'America/New_York',
    'Tokyo': 'Asia/Tokyo',
    'Paris': 'Europe/Paris',
    'Sydney': 'Australia/Sydney',
}


# Token required decorator
def token_required(f):
    def decorator(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]
            if token == API_TOKEN:
                return f(*args, **kwargs)
        return jsonify({"error": "Unauthorized"}), 401

    decorator.__name__ = f.__name__
    return decorator


@app.route('/api/time/<city>', methods=['GET'])
@token_required
def get_time(city):
    city = city.title()  # Ensure case-insensitive matching
    if city not in city_timezones:
        return jsonify({"error": f"City {city} not found in database."}), 404

    # Get the timezone for the city
    timezone = pytz.timezone(city_timezones[city])

    # Get the current time in that timezone
    local_time = datetime.now(timezone).strftime('%Y-%m-%d %H:%M:%S')

    # Get the UTC offset for that timezone
    utc_offset = datetime.now(timezone).utcoffset().total_seconds() / 3600

    return jsonify({
        "city": city,
        "local_time": local_time,
        "utc_offset": utc_offset
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)


