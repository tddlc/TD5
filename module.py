from requests import get
import pandas as pd

def get_manor(place_ids):
    response = get(f'https://opendomesday.org/api/1.0/place/{place_ids}')
    json_data = response.json()
    return json_data.get('manors', [])

def main():
    place_ids = place_id()
    print(place_ids)
    all_manor_ids = get_all_manor_ids_in_derbyshire(place_ids)
    manors_data = get_manor(all_manor_ids)
    manors_df = pd.DataFrame(manors_data)
    print(manors_df)
    
    total_geld = manors_df['geld'].sum()
    total_ploughs = manors_df['total_ploughs'].sum()
    print("Total Geld Paid:", total_geld)
    print("Total Ploughs Owned:", total_ploughs)

if __name__ == '__main__':
    main()
