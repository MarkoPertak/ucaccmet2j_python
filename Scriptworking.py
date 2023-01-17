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

total_sum = sum(sum_list)

relative_sum = []
for entry in sum_list:
    relative_sum.append(entry/total_sum)

dic1 = {
    "Seattle": {
        "station": "GHCND:US1WAKG0038",
        "state": "WA",
        "total_monthly_precipitation": (sum_list),
        "total_yearly_precipitation": (total_sum),
        "relative_precipitation": (relative_sum),
    } }

with open('Results.json', 'w') as l:
    json.dump(dic1, l, indent=4, sort_keys=True)
