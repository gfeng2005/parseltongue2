import random
import os
import time

categories = ["animals", "colors", "numbers"]
random.choice(categories)
answers = []
choice = random.choice(categories)
start = time.time()
for i in range(10):
    tt = input(choice + ": ")
    answers.append(tt)
done = time.time()
elapsed = done - start

def columns_list(answers):
    rows, columns = os.popen('stty size', 'r').read().split()
    columns = int(columns)
    for i in range(len(answers)):
        print(int(columns/2) * " " + answers[i] + int(columns/2) * " ")

columns_list(answers)
print("You took: " + str(round(elapsed, 2)) + "seconds")

