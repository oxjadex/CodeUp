def pr(list):
    if not list:
        return  # 리스트가 비어있으면 재귀를 종료합니다.
    else:
        print(list.pop())
        pr(list)  # 재귀 호출


n = list(map(int, input().split()))
pr(n)
