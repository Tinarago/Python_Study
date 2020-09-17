sentence = 'hello'
print(sentence)

sentence2 = "world"
print(sentence2)

sentence3 = """
multi line
string
writing\
"""
print(sentence3)

# slicing

jumin = "940403-2134567"
print("성별: " + jumin[7])
print("연: " + jumin[0:2])
print("월: " + jumin[2:4])
print("일: " + jumin[4:6])
print("생년월일: " + jumin[:6])
print("뒤 7자리: " + jumin[7:])
print("뒤 7자리: " + jumin[-7:])

# functions
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index) # 5
index = python.index("n", index + 1) #(text, start)
print(index)

print(python.find("n"))

print(python.find("Java")) #-1
# print(python.index("Java")) #오류가 남

print(python.count("n"))
print(python.count("i"))

# 문자열 포맷
# 방법1
print("a" + "b")
print("a", "b")

print("나는 %d살입니다" % 20) #정수값만 가능
print("나는 %s을 좋아해요" % "파이썬")
print("Apple은 %c로 시작해요" %"A")
# %s
print("나는 %s살입니다" % 20)

print("나는 %s색과 %s색을 좋아해요" % ("파란", "빨간"))

# 방법2
print("나는 {}살입니다".format(20))
print("나는 {}색과 {}색을 좋아해요".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요".format("파란", "빨간"))

# 방법3
print("나는 {age}살이며, {color}색을 좋아해요".format(age = 20, color = "빨간"))

# 방법4 (v3.6 이상~)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요")


#탈출문자
print("백문이 불여일견 \n백견이 불여일타")

