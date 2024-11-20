# TODO решите задачу
import json
filename = "input.json"
def task() -> float:
    sum = 0
    with open(filename) as file:
        data = json.load(file)
        for i in range(len(data)):
           sum += data[i].get("score")*data[i].get("weight")
    return round(sum, 3)
print(task())
