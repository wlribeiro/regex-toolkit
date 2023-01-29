import re
import json

datas = open('infos.txt', 'r').readlines()

final_parsed_data = []

for data in datas:
    response = re.findall('(?:[A-Za-z\s]+)[^\n|^\|]', data)
    date = re.findall('([\d\/]+)', data)
    cep = re.findall('([0-9]{5}-[0-9]{3})', data)
    number = re.findall('(?<=\|)(\d{1,4})(?=\|)', data)

    parsed_data = {
        'name': response[0],
        'address': response[1],
        'city': response[2],
        'date': date[0],
        'cep': cep[0],
        'number': number[0]
    }
    
    final_parsed_data.append(parsed_data)

data_json = json.dumps(final_parsed_data, indent=4)
print(data_json)
