import json



def add(data):
    recv_data = json.loads(data)
    number = data["num"] + 10
    return number


def send():
    data = {}
    number = add()
    data["num"] = number
    print number
    # should send as json.dumps(data)

while True:
    send()