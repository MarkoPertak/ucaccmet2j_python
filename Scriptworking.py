import json
with open('precipitation.json') as f:
    precipitation_data = json.load(f)

x = range(1,13)
precipitation = []
for month in x:
    monthly_value = []
    precipitation.append(monthly_value)

for entry in precipitation_data:
    if entry["station"] == "GHCND:US1WAKG0038":
        date = str(entry["date"])
        date = date.split("-")
        for month in x:
            if int(date[1]) == month:
                precipitation[month-1].append(entry["value"])

sum_list = []
for list in x:
    summed = sum(precipitation[list-1])
    sum_list.append(summed)

dic1 = {
    "Seattle": {
        "station": "GHCND:US1WAKG0038",
        "state": "WA",
        "total_monthly_precipitation": (sum_list),
    } }

print(sum_list)

with open('Results.json', 'w') as l:
    json.dump(dic1, l, indent=4, sort_keys=True)

precipitation_cinc = []
for entry in precipitation_data:
    if entry["station"] == "GHCND:USW00093814":
        date = str(entry["date"])
        date = date.split("-")
        for month in x:
            if int(date[1]) == month:
                precipitation_cinc[month-1].append(entry["value"])

sum_list_cinc = []
for list in x:
    summed = sum(precipitation[list-1])
    sum_list_cinc.append(summed)

precipitation_Maui = []
for entry in precipitation_data:
    if entry["station"] == "GHCND:USC00513317":
        date = str(entry["date"])
        date = date.split("-")
        for month in x:
            if int(date[1]) == month:
                precipitation_Maui[month-1].append(entry["value"])

sum_list_Maui = []
for list in x:
    summed = sum(precipitation_Maui[list-1])
    sum_list_Maui.append(summed)

precipitation_SD = []
for entry in precipitation_data:
    if entry["station"] == "GHCND:US1CASD0032":
        date = str(entry["date"])
        date = date.split("-")
        for month in x:
            if int(date[1]) == month:
                precipitation_SD[month-1].append(entry["value"])

sum_list_SD = []
for list in x:
    summed = sum(precipitation_SD[list-1])
    sum_list_SD.append(summed)
