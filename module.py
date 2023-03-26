from requests import get

def get_manor(p_id):
    response = get(f'https://opendomesday.org/api/1.0/place/{p_id}')
    json_data = response.json()
    return json_data.get('manors', [])
