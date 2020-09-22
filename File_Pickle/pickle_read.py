import pickle
profile_file = open("file_pickle/profile.pickle", "rb")
# file의 정보를 profile에 불러옴
profile = pickle.load(profile_file)
print(profile)
profile_file.close()
