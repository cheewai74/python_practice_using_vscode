
def data_from_response(response: dict) -> dict:
    if response["status"] != 200:
        raise ValueError("Invalid status in response")
    return {"data": response["payload"]}


# Usage example

# 1. Create a dictionary
successful_response = {
    "status": 200,
    "payload": {"user_id": 123, "username":"testuser"}
}

# 2. Assigning the dictionary to the helper
data = data_from_response(successful_response)

# 3. Print out the helper response.
print(f"Successfully extracted data: {data}")