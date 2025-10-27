
def fetch_windchill_data(request_type):
    # Simulated API response
    return {
        "type": request_type,
        "id": "6e93350d-f6ad-4f83-b996-62f09d4510b8",
        "status": "Open",
        "created": str(datetime.now()),
        "stakeholders": ["John Doe", "Jane Smith"]
    }
