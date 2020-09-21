# 집합
# 중복 안됨, 순서 없음

my_set = {1, 2, 3, 3, 3}
print(my_set) #print only 1, 2, 3

java = {"AAA", "BBB", "CCC"}
python = set(["AAA", "CCC", "DDD"])

# 교집합
print(java & python)
print(java.intersection(python))

# 합집합 (순서 x)
print(java | python)
print(java.union(python))

# 차집합 (java에는 있지만 python에는 없는)
print(java - python)
print(java.difference(python))

# add new
python.add("EEE")
print(python)

# delete
java.remove("BBB")
print(java)