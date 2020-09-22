score_file = open("file/score.txt", "w", encoding="utf8")
print("수학: 0", file=score_file)
print("영어: 50", file=score_file)
score_file.close()

# append
score_file = open("file/score.txt", "a", encoding="utf8")
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()