def profile(name, age, main_lang):
    print("name: {0}\tage: {1}\t\tmain language: {2}"\
        .format(name, age, main_lang))

profile("Andy", 20, "Python")
profile("Max", 25, "Java")

def profile_default(name, age=17, main_lang="Python"):
    print("name: {0}\tage: {1}\t\tmain language: {2}"\
        .format(name, age, main_lang))

profile_default("Tina")
profile_default("Lily", 25)