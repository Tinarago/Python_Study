import pickle

with open("File_Pickle\profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

# close() 해줄 필요 없음