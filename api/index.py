import os
import json

def read_marks(names):
    # Load JSON data
    with open(os.path.join(os.path.dirname(__file__), '..', 'marks.json')) as f:
        data = json.load(f)
    marks_dict = {entry['name']: entry['marks'] for entry in data}
    # Return marks for each requested name, or None if not found
    return [marks_dict.get(name, None) for name in names]

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

    marks = read_marks(names)
    return response.json({"marks": marks})
