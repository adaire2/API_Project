# Capital City Time API Documentation

This API returns the current local time and UTC offset for a given capital city.

## Requirements

- A valid Bearer Token must be included in the request header.
- The city must be one of the supported capital cities.

## Authentication

All requests to the `/api/time/<city>` endpoint must include a valid Authorization header:

```
Authorization: Bearer supersecrettoken123
```

## Endpoint

**GET** `/api/time/<city>`

Returns the current local time and UTC offset for the specified capital city.

### Example Request

```bash
curl -H "Authorization: Bearer supersecrettoken123" http://34.69.140.73:5002/api/time/London
```

### Example Successful Response

```json
{
  "city": "London",
  "local_time": "2025-04-21 22:10:56",
  "utc_offset": 1.0
}
```

## Error Responses

**401 Unauthorized** (Missing or invalid token):

```json
{
  "error": "Unauthorized"
}
```

**404 City Not Found** (City is not in the database):

```json
{
  "error": "City <CityName> not found in database."
}
```

## Supported Cities

- London
- New York
- Tokyo
- Paris
- Sydney

## API Host

**Base URL**: `http://34.69.140.73:5002`
