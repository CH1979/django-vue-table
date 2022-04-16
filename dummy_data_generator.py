import json
import random
from datetime import date, timedelta


MAX_TIMEDELTA = 365
FINISH_DATE = date.today()
MIN_QUANTITY = 10.0
MAX_QUANTITY = 1000.0
MIN_DISTANCE = 100.0
MAX_DISTANCE = 10000.0

def generate_row():
    """
    Generate random row for table
    """
    rand_delta = random.randint(1, MAX_TIMEDELTA)
    row_date = date.strftime(
        FINISH_DATE - timedelta(days=rand_delta),
        "%Y-%m-%d"
    )
    quantity = round(
        MIN_QUANTITY + random.random() * (MAX_QUANTITY - MIN_QUANTITY),
        2
    )
    distance = round(
        MIN_DISTANCE + random.random() * (MAX_DISTANCE - MIN_DISTANCE),
        2
    )
    row = {
        "date": row_date,
        "quantity": quantity,
        "distance": distance
    }
    return row

if __name__ == "__main__":
    data = []
    row_id = 1

    with open("city_names.txt") as f_input:
        for line in f_input:
            name = line.rstrip()
            row = generate_row()
            row["name"] = name
            row_record = {
                "model": "api.row",
                "pk": row_id,
                "fields": row
            }
            data.append(row_record)
            row_id += 1

    with open("backend/data.json", "w") as f_output:
        json.dump(data, f_output)
