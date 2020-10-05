# 패키지, 모듈의 위치
import inspect
import random
print(inspect.getfile(random))

from travel import *
print(inspect.getfile(thailand))