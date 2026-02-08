from coordinate import Coordinate

# --- Example Usage ---

# Valid coordinates
try:
    location = Coordinate(lat=40.7128, long=-74.0060)
    print("Successfully created coordinate object for New York City.")
    print(f"Latitude: {location.latitude}")
    print(f"Longitude: {location.longitude}")
except ValueError as e:
    print(e)

print("--------------------")

# Example with invalid latitude
try:
    print("Attempting to create a coordinate with invalid latitude...")
    invalid_location = Coordinate(lat=100, long=50)
except ValueError as e:
    print(f"Caught expected error: {e}")

