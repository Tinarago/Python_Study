# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# __init__.py 에서 공개범위 설정 해줘야함
from travel import *
trip_to = vietnam.VietnamPackage()
trip_to.detail()

trip_to = thailand.ThailandPackage()
trip_to.detail()
