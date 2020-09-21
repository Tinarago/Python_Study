# 당신은 택시 기사입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건1: 승객별 운행 소요시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건2: 당신은 소요시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

# (출력문 예제)
# [0] 1번째 손님 (소요시간: 15분)
# [ ] 2번째 손님 (소요시간: 50분)
# [0] 3번째 손님 (소요시간: 5분)
# ...
# [ ] 50번째 손님 (소요시간: 16분)

# 총 탑승 승객 : 2 명

from random import *
cust = []
for i in range(1, 51):
    cust.append(randint(5, 50))

realcust = 0
for j in range(0, 50):
    if cust[j] >= 5 and cust[j] <= 15:
        print(f"[O] {j+1}번째 손님 (소요시간 : {cust[j]}분)")
        realcust += 1
    else:
        print(f"[ ] {j+1}번째 손님 (소요시간 : {cust[j]}분)")

print(f"\n총 탑승 승객 : {realcust} 명")


# 더 짧은 방법
cnt = 0
for i in range(1, 51):
    time = randrange(5, 51)
    if 5 <= time <= 15:
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

print("\n총 탑승 승객 : {0}명".format(cnt))