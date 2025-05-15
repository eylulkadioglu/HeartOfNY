from flask import request, jsonify
from flask import current_app as app
from app import db
from app.models import County, Society

@app.route('/societies', methods=['GET'])
def get_societies():
    county_id = request.args.get('county_id', type=int)
    if not county_id:
        return jsonify({'error': 'Missing county_id'}), 400

    county = County.query.get(county_id)
    if not county:
        return jsonify({'error': 'County not found'}), 404

    societies = [
        {
            'name': s.society_name,
            'website': s.website,
            'location': s.location,
            'email': s.email,
            'phone': s.phone
        }
        for s in county.societies
    ]

    return jsonify({
        'county_name': county.county_name,
        'societies': societies
    })
