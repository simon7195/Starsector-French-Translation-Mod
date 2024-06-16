import json
import csv
 
with open('./data/strings/tips.json') as json_file:
    jsondata = json.load(json_file)
 
data_file = open('./csv/en/tips.csv', 'w', newline='')
csv_writer = csv.writer(data_file)

csv_string = "freq,tip\n"

for data in jsondata['tips']:
    if type(data) == dict:
        csv_string += str(data['freq']) + ", \"" + data['tip'].replace("\"", "\"\"") + "\"" + "\n"
    else:
        csv_string += "," + "\"" + data.replace("\"", "\"\"") + "\"" + "\n"

data_file.write(csv_string)
 
data_file.close()