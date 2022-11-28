import interface
from datetime import datetime


def logger(information):
    time=datetime.now().strftime('%H:%M')
    with open('log.csv', 'a', encoding = "utf-8") as file:
        file.write("{} {} \n". format(time, information))
