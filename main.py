import csv
import xml.etree.ElementTree as ET
import json

csv_file = 'liste1.csv'
csv_data = []
error_occurred = False

# Reading CSV file
try:
    with open(csv_file, mode='r', newline='', encoding='utf-8-sig') as file:
        csv_reader = csv.DictReader(file, delimiter=';')
        for row in csv_reader:
            email = []
            for i in range(1, 4):
                email_key = f'email{i}'
                email_value = row.get(email_key)
                if email_value:
                    email.append(email_value)
            csv_data.append({
                'nom': row.get('nom', 'N/A'),
                'prenom': row.get('prenom', 'N/A'),
                'email': email,
            })
except FileNotFoundError:
    print(f"Error: File {csv_file} not found.")
    error_occurred = True
except csv.Error as e:
    print(f"Error while reading CSV file: {e}")
    error_occurred = True

# Reading XML file
xml_file = 'liste2.xml'
xml_data = []

try:
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for client in root.findall('client'):
        email = client.find('email').text if client.find('email') is not None else None
        xml_data.append({
            'nom': client.find('nom').text if client.find('nom') is not None else 'N/A',
            'prenom': client.find('prenom').text if client.find('prenom') is not None else 'N/A',
            'email': [email] if email else [],
        })
except FileNotFoundError:
    print(f"Error: File {xml_file} not found.")
    error_occurred = True
except ET.ParseError as e:
    print(f"Error while reading XML file: {e}")
    error_occurred = True

# Writing to a JSON file only if no critical error occurred
if not error_occurred:
    all_data = csv_data + xml_data
    json_file = 'data.json'
    try:
        with open(json_file, mode='w', encoding='utf-8') as file:
            json.dump(all_data, file, indent=4, ensure_ascii=False)
        print(f'Data of {json_file} has been saved')
    except IOError as e:
        print(f"Error while writing JSON file: {e}")
else:
    print("No data has been saved to the JSON file due to previous errors.")
