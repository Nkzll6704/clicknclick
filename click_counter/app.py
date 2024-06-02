from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clicks.db'
db = SQLAlchemy(app)

class ClickCounter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, default=0)

# Veritabanı tablolarını oluşturmak için Flask uygulamasının başlangıcında create_all() fonksiyonunu çağırın
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/count', methods=['GET'])
def get_count():
    counter = ClickCounter.query.first()
    if counter is None:
        counter = ClickCounter(count=0)
        db.session.add(counter)
        db.session.commit()
    return jsonify({'count': counter.count})

@app.route('/increment', methods=['POST'])
def increment_count():
    counter = ClickCounter.query.first()
    if counter is None:
        counter = ClickCounter(count=0)
    counter.count += 1
    db.session.add(counter)
    db.session.commit()
    return jsonify({'count': counter.count})

if __name__ == '__main__':
    app.run(debug=True)
