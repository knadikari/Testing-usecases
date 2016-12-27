import json



def add(data):
    recv_data = json.loads(data)
    number = data["num"] + 10
    return number
