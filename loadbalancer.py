from flask import Flask, request
import requests, time, docker

app = Flask(__name__)
client = docker.from_env()

# Keep track of running containers
servers = []
current = 0
request_count = 0
last_check = time.time()

# Thresholds
MAX_REQUESTS = 10   # requests per 10 sec before scaling up
MIN_REQUESTS = 3    # requests per 10 sec before scaling down

def add_server():
    """Start a new backend container."""
    global servers
    server_id = len(servers) + 1
    port = 5000 + server_id
    container = client.containers.run(
        "backend-server", 
        ["python", "backend.py", str(server_id)], 
        ports={f"{port}/tcp": port}, 
        detach=True
    )
    servers.append((f"http://127.0.0.1:{port}", container))
    print(f"✅ Started server {server_id} on port {port}")

def remove_server():
    """Stop the last backend container."""
    global servers
    if len(servers) > 1:  # keep at least 1 server
        server, container = servers.pop()
        container.stop()
        print(f"🛑 Stopped {server}")

@app.route("/")
def load_balance():
    global current, request_count, last_check

    if not servers:
        add_server()

    # Round-robin
    server, _ = servers[current]
    current = (current + 1) % len(servers)

    try:
        response = requests.get(server)
    except:
        response = f"{server} is down!"

    # Count requests
    request_count += 1
    now = time.time()
    if now - last_check >= 10:  # check every 10s
        if request_count > MAX_REQUESTS:
            add_server()
        elif request_count < MIN_REQUESTS:
            remove_server()
        request_count = 0
        last_check = now

    return response if isinstance(response, str) else response.text

if __name__ == "__main__":
    app.run(port=5000)
