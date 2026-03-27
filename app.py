from flask import Flask
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379)

@app.route('/')
def home():
    count = r.incr('visits')
    return f"""
    <h1>Hello from Docker!</h1>
    <h2>Name: Srishti Gupta</h2>
    <h2>Roll No: 13501032024</h2>
    <h3>Visits: {count}</h3>
    """

app.run(host='0.0.0.0', port=5000)