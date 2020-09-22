# 표준체중을 구하는 프로그램을 작성하시오.

# * 표준 체중: 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
# 남자: 키(m) x 키(m) x 22
# 여자: 키(m) x 키(m) x 21

# 조건1: 표준 체중은 별도의 함수 내에서 계산
#         * 함수명 : std_weight
#         * 전달값 : 키(height), 성별(gender)
# 조건2: 표준 체중은 소수점 둘째자리까지 표시

# (출력 에제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

def std_weight(height, gender):
    if gender == "female":
        var = 21
    else:
        var = 22
    weight = (height/100) ** 2 * var
    print("Height {0}cm of {1}'s standard weight is {2:.2f}kg.".format(height,gender,weight))

std_weight(165, "female")
std_weight(170, "male")

def std_weight_sh(height, gender):
    if gender == "female":
        return height * height * 21
    else:
        return height * height * 22

height = 175
gender = "female"
weight = round(std_weight_sh(height/100, gender),2)
print("Height {0}cm of {1}'s standard weight is {2}kg.".format(height,gender,weight))