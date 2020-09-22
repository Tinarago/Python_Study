def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("name: {0}\tage: {1}\t".format(name, age), end=" ")
    print(lang1, lang2, lang3, lang4, lang5)

# variable argument
def profile_var(name, age, *language):
    print("name: {0}\tage: {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("Andy", 20, "Python", "Java", "C", "C++", "C#")
profile("Max", 25, "Kotlin", "Swift", "", "", "")

profile_var("Andy", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile_var("Max", 25, "Kotlin", "Swift")