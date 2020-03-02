import os
import redis
from flask import Flask, render_template, request


app = Flask(__name__)

redis_host = os.environ.get('REDIS', 'localhost')
pool = redis.ConnectionPool(host=redis_host, port=6379, db=1)


@app.route('/')
@app.route('/msg', methods=['POST', 'GET'])
def msg():
    red = redis.Redis(connection_pool=pool)

    if request.method == 'POST':
        new_msg = request.form['message']
        red.rpush('msg', new_msg)

    msg = red.lrange("msg", 0, -1)
    return render_template('index.html', msg=msg)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
