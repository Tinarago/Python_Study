class Unit:
    # constructor
    def __init__(self, name, hp, damage):
        # 멤버 변수
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# 객체 (instance)
marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank1 = Unit("탱크", 150, 35)
# marine3 = Unit("탱크") # 갯수가 달라서 만들 수 없음. 오류

# 레이스 : 공중 유닛, 비행기. 클로킹(상대에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름: {0}, 공격력 {1}".format(wraith1.name, wraith1.damage))

# 마인드컨트롤 : 상대방 유닛을 내 것으로 만드는 것
wraith2 = Unit("레이스", 80, 5)
wraith2.clocking = True
# Class에는 없는 외부 변수를 추가로 만들어 사용함
if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))

# wraith1에게는 clocking 변수가 없기 때문에 오류가 발생
# if wraith1.clocking == True:
#     print("{0}는 현재 클로킹 상태입니다.".format(wraith1.name))
