# create list
subway = [10, 20, 30]
print(subway)
print(subway.index(20)) # 1

# append item at the end
subway.append(40)
print(subway)

# insert item at the given index
subway.insert(1, 50)
print(subway)

# delete the last element
print(subway.pop())
print(subway)

# count the element
subway.append(10)
print(subway)
print(subway.count(10)) # 2

# list sorting and reversing
num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)
num_list.reverse()
print(num_list)

# empting the list
num_list.clear()
print(num_list)

# mix data type
mix_list = ["name", 25, True]
print(mix_list)

# extend/merge list
num_list = [5, 2, 3, 1, 4]
num_list.extend(mix_list)
print(num_list)