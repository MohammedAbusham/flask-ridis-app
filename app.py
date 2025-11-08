from flask import Flask
import os
import redis

app = Flask(__name__)
# Connect RedisDB.
redis_host= os.getenv('REDIS_HOST','redis')
redis_port= int(os.getenv('REDIS_PORT', 6379))
r = redis.Redis(host=redis_host, port=redis_port)

@app.route('/')
def welcome_message():
    # Displays a welcome message.
    return 'Hello, you are connected to My Fask App'


@app.route('/count')
def vist_count():
    # Dsplays a visit count stored in RedisDB.
    r = redis.Redis(host=redis_host, port=redis_port, db=0)
    # Increment the page visit counter
    visits = r.incr('page_visits')

    return f"<h1>WOW!</h1><p>Moe's web App has been visited <b>{visits}</b> times."

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)