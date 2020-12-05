import json

data = {
    "id": 1,
    "name":"jay",
    "age" : 20,
    "subjects":["english","maths"],
    "marks":{
        "english": 80,
        "maths" : 90
    },
    "avg_marks" :  85.5,
    "result" : True,
    "grade": None
}

d = json.dumps(data)
print(d)
print(json.dumps(('c','c++','java')))
print(json.dumps(list(range(10))))