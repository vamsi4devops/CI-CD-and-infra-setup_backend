from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask Backend!"

@app.route('/metrics')
def metrics():
    return "my_custom_metric 1\n", 200, {'Content-Type': 'text/plain; version=0.0.4'}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
