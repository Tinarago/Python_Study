class SoldOutError(Exception):
    pass

chicken = 10
waiting = 0
while(True):
    print("[남은 치킨 : {0} 마리, 총 대기인 수 {1} 명]".format(chicken, waiting))
    try:
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order > chicken:
            print("재료가 부족합니다.")
        elif order <= 0:
            raise ValueError
        else:
            waiting += 1
            chicken -= order
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다."\
                .format(waiting, order))
        
        if chicken == 0:
            raise SoldOutError
    except ValueError:
        print("올바른 값을 입력해주세요. (1 ~ {0})".format(chicken))
    except SoldOutError:
        print("재료 소진으로 주문 마감합니다. 총 대기인 수 : {0} 명".format(waiting))
        break

