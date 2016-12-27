import json



def sub(data):
    recv_data = json.loads(data)
    number = data["num"] - 10
    return number
