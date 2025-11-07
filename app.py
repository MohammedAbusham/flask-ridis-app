from flask import Flask
import redis

app = Flask(__name__)

@app.route('/')
def welcome_message():
    # Displays a welcome message.
    return 'Hello, you are connected to My Fask App'


@app.route('/count')
def vist_count():
    # Connect and displays a visit count stored in RedisDB.
    r = redis.Redis(host='redis', port=6379, db=0)

    # Increment the page visit counter
    visits = r.incr('page_visits')

    return f"<h1>WOW!</h1><p>Moe's web App has been visited <b>{visits}</b> times."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)