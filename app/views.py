from app import app, db, FormData
from flask import render_template, request, jsonify

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form.to_dict()
        form_data = FormData(data=data)
        db.session.add(form_data)
        db.session.commit()
        return jsonify({'message': 'Data saves successfully!'})
    return render_template('form.html')

@app.route('/data', methods=['GET'])
def get_data():
    all_data = FormData.query.all()
    return render_template('data.html', all_data=all_data)