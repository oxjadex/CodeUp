import time
import random

WORD_LIST = [
    "위대한 것을 이루려면 우리는 행동할 뿐 아니라 꿈도 꾸어야 하고, 계획할 뿐 아니라 믿기도 해야 한다.",
    "인생에서 중요한 법칙은 만사에 중용을 지키는 일이다.",
    "한나라의 진정한 재산은 땀 흘려 일하는 부지런한 주민의 수에 있다.",
    "자유는 획득하는 것보다 간직하는 것이 더 어렵다.",
    "당신이 살면서 어떤 부침을 겪든 간에 생각이 당신의 기본 자산이 되어야 한다.",
    "참된 삶을 맛보지 못한 자만이 죽음을 두려워하는 것이다.",
    "나는 대단한 인간이 아니다. 노력하는 노인일 뿐이다."
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