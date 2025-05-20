import json
import os

def handler(request, response):
    # Enable CORS
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'

    # Parse names from query string
    names = request.query.getlist('name')
    if not names:
        response.status_code = 400
        return response.json({"error": "No names provided"})

    # Read marks.json in the same directory
    with open(os.path.join(os.path.dirname(__file__), 'marks.json')) as f:
        data = json.load(f)
    marks_dict = {entry['name']: entry['marks'] for entry in data}
    marks = [marks_dict.get(name, None) for name in names]

    return response.json({"marks": marks})

