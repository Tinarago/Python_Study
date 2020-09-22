import pickle

# wb: write, binary
# 인코딩 따로 지정해 줄 필요 없음
profile_file = open("File_Pickle\profile.pickle", "wb")
profile = {"Name":"Andy", "Age":30, "Hobby":["Football", "Golf", "Coding"]}
print(profile)
# profile의 정보를 file에 저장
pickle.dump(profile, profile_file)
profile_file.close()
