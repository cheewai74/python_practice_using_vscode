import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created successfully.")

s.connect(('google.com', 80))
print(f"Connection to google.com successful.")

# Prepare the HTTP GET request
request = "GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"
print("\nSending HTTP GET request...")

# Send the request
s.send(request.encode('utf-8'))

# Receive the response (in chunks)
response = b""
while True:
    chunk = s.recv(4096)
    if not chunk:
        break
    response += chunk

# Close the connection
s.close()

# Print the HTTP response
print("Response received fully.")

# 5. Print the decoded response to the terminal
print("\n--- SERVER RESPONSE ---\n")
print(response.decode('utf-8', errors='ignore'))
print("\n--- END OF RESPONSE ---")