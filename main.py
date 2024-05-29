import csv
import xml.etree.ElementTree as ET
import json

csv_file = 'liste1.csv'
csv_data = []
with open(csv_file, mode='r', newline='', encoding='utf-8-sig') as file:
    csv_reader = csv.DictReader(file, delimiter=';')
    for row in csv_reader:
        emails = []
        for i in range(1, 4):
            email_key = f'email{i}'
            email_value = row[email_key]
            if email_value:
                emails.append(email_value)
        csv_data.append({
            'nom': row['nom'],
            'prenom': row['prenom'],
            'emails': emails,
        })

xml_file = 'liste2.xml'
tree = ET.parse(xml_file)
root = tree.getroot()
xml_data = []
for client in root.findall('client'):
    xml_data.append({
        'nom': client.find('nom').text,
        'prenom': client.find('prenom').text,
        'email': client.find('email').text,
    })

all_data = csv_data + xml_data

json_file = 'data.json'
with open(json_file, mode='w', encoding='utf-8') as file:
    json.dump(all_data, file, indent=4, ensure_ascii=False)

print(f'Data of {json_file} has been saved')
