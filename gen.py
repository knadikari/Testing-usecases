import json
from random import randint


def gen():
    num = randint(0,9)
    return num

def send():
    data = {}
    number = gen()
    data["num"]= number
    print number
    # should send as json.dumps(data)


while True:
    send()