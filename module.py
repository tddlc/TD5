from requests import get

def get_manor(place_ids):
    response = get(f'https://opendomesday.org/api/1.0/place/{place_ids}')
    json_data = response.json()
    return json_data.get('manors', [])

if __name__ == '__main__':
	place_ids=place_id()
	print(place_ids)
	manor_ids = get_all_manor_ids_in_derbyshire(place_ids)
	manor_info = get_manor_info(manor_ids)
	df = pd.DataFrame(manor_info)
	print(df)	
	total_geld_paid = df['geld'].sum()
	total_ploughs_owned = df['total_ploughs'].sum()
	print("total_geld_paid = ", total_geld_paid)
	print("total_ploughs_owned = ", total_ploughs_owned )
