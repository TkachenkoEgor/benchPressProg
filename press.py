
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"key": "Hello"}


@app.get("/slot/")
def calc_press(num: float):
    coef = (0.6, 0.7, 0.8, 0.9)
    weak = ("1 и 2 неделя",  round(num * (coef[0])),"кг 4 подхода 10 повторений"
            "3 и 4 неделя", round(num * (coef[1])), "кг 4 подхода 10 повторений"
            "5 и 6 неделя", round(num * (coef[2])), "кг 6 подхода 5 повторений"
            "7 и 8 неделя", round(num * (coef[3])), "кг 3 подхода 3 повторений")
    qweak = str (weak)
    with open("f.txt", "w") as f:
        f.write(qweak)
    with open("f.txt", "r") as q:
        ini_list = q.read().strip(')(').split(', ')

    return {"program": ini_list}