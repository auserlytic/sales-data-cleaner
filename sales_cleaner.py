import json

clean_data = []
seen_items = set()

file = open("sales.csv", "r")
for line in file:
    line = line.strip()
    if not line:
        continue

    parts = line.split(",")
    product = parts[1].replace('"', '').strip()
    price_text = parts[2].replace('$', '').strip()
    country = parts[3].strip()

    price = float(price_text)
    key = (product, price)

    if key in seen_items:
        continue

    seen_items.add(key)
    price_inr = price * 83

    record = {
        "product": product,
        "price_inr": price_inr,
        "country": country
    }

    clean_data.append(record)

file.close()

output_file = open("clean_sales.json", "w")
json.dump(clean_data, output_file, indent=4)
output_file.close()

   