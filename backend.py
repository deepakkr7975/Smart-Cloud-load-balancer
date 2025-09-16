from flask import Flask
import sys

app = Flask(__name__)

@app.route("/")
def home():
    return f"Hello from backend server {server_id}!"

if __name__ == "__main__":
    # Get server ID from command-line argument
    server_id = sys.argv[1] if len(sys.argv) > 1 else "1"
    app.run(host="0.0.0.0", port=5000 + int(server_id))
