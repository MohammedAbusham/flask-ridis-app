from flask import Flask
import redis

app = Flask(__name__)

@app.route('/')
def welcome_message()
    # Displays a welcome message.
    return 'Hello, you are connected to My Fask App'


@app.route('/count')
def vist_count()
    # Connect and displays a visit count stored in RedisDB.
    r = redis.Redis(host='redisdb', port=6379, db=0, decode_responses=True)

    # Increment the page visit counter
    visits = r.incr('page_visits')

    # Retrieve the counted vists
    count = r.get('page_visits')

    return f"<h1>WOW!</h1><p>Moe's web App has been visited <b>{count}</b> times.

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)