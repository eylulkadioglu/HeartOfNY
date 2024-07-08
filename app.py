from flask import Flask, jsonify, request, render_template, abort
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from models import db, County, Society

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://hony_owner:w8mlc0PMiNxI@ep-tight-sun-a4ajzyif.us-east-1.aws.neon.tech/hony?sslmode=require'
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/societies', methods=['GET'])
def get_societies():
    county_id = request.args.get('county_id', type=int)
    if not county_id:
        return jsonify({'error': 'Missing county_id'}), 400

    county = County.query.get(county_id)
    if not county:
        return jsonify({'error': 'County not found'}), 404

    societies = [
        {'name': s.society_name, 'website': s.website, 'location': s.location, 'email': s.email, 'phone': s.phone}
        for s in county.societies
    ]
    return jsonify({'county_name': county.county_name, 'societies': societies})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Remember to comment this out after the first run
    app.run(host='0.0.0.0', port=5000, debug=True)