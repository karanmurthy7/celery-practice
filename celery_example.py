from flask import Flask
from flask_celery_example import make_celery

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'amqp://localhost://'
app.config['CELERY_BACKEND'] = 'db+sqlite:///celery_db.db'

celery = make_celery(app)

@app.route('/process/<name>')
def process(name):
    reverse.delay(name)
    return 'I sent an async request'

@celery.task(name='celery_example.reverse')
def reverse(s):
    return s[::-1]


if __name__ == '__main__':
    app.run(debug=True)