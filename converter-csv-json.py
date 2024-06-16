import csv
import json

csvFilePath = './csv/fr/tips.csv'
jsonFilePath = './data/strings/tips.json'

data = {"tips":[]}

with open(csvFilePath, encoding='utf-8') as csvf:
    csvReader = csv.DictReader(csvf)
    for row in csvReader:
        if row['freq'] == "":
            data["tips"].append(row['tip'])
        else:
            data["tips"].append({"freq": row['freq'], "tip": row['tip']})
    
with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
    jsonf.write(json.dumps(data, indent=4, ensure_ascii=False))