import time
import random

WORD_LIST = [
    "10월 25일에는 암기빵이 나온다.",
    "It turns out, i hate apple",
    "When i was young, i was student."
]

random.shuffle(WORD_LIST)

for q in WORD_LIST:
    Start = time.time()
    Input = input(q + '\n').strip()
    Speed = time.time() - Start

    정확도 = 0
    for c, a in zip(Input, q):
        정확도 = 정확도 + 1 if c == a else 정확도

    Len = len(q)
    c = 정확도 / Len * 100
    e = (Len - 정확도) / Len * 100
    speed = float(정확도 / Speed) * 60

    print(f"타수: {speed:0.2f} 정확도: {c:0.2f}% 오타: {e:0.2f}%")
