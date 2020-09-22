# 한번에 불러오기
score_file = open("file/score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()

# 한줄씩 불러오기
score_file = open("file/score.txt", "r", encoding="utf8")
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()

# 몇 줄인지 모를 경우
score_file = open("file/score.txt", "r", encoding="utf8")
while(True):
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()
print()

# list에 저장하기
score_file = open("file/score.txt", "r", encoding="utf8")
lines = score_file.readlines() # list 로 저장
for line in lines:
    print(line, end="")
score_file.close()