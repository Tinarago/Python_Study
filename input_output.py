print("Python", "Java") # 기본 띄어쓰기 한칸이 사이에 들어감

print("Python", "Java", "JavaScript", sep=" vs ") # sep에서 지정한 문자열이 사이사이에 들어감

print("Python", "Java", sep=", ", end="?") # end를 명시함으로써 두 문장이
print("무엇이 더 재밌을까요?") # 두줄에 나오지 않고 한줄에 출력됨

import sys
print("Python", "Java", file=sys.stdout) # 표준출력
print("Python", "Java", file=sys.stderr) # 표준에러

scores = {"Math":0, "Eng":50, "coding":100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")
    # ljust(n): n칸의 공간을 확보하고 왼쪽 정렬
    # rjust(n): n칸의 공간을 확보하고 오른쪽 정렬

# 은행 대기 순번표
# 001, 002, 003, ...
for num in range(1, 21):
    print("대기번호: " + str(num).zfill(3))
    #zfill(n): n개의 공간을 확보해서 빈 공간을 0으로 채움

# input 
answer = input("아무 값이나 입력하세요 : ")
print(type(answer))
print("입력하신 값은 " + answer + "입니다. ")
# input 을 통해 받은 값은 언제나 문자열 str로 저장됨