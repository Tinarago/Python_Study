# Quiz) 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오.

# 예) http://naver.com
# 규칙 1 : http:// 부분은 제외 => naver.com 
# 규칙 2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성

# 예) 생성된 비밀번호 : nav51!

naver = "http://naver.com"
google = "http://google.com"
daum = "http://daum.net"

pw1 = naver.replace("http://", "")
pw1 = pw1[:pw1.index(".")]
pw1 = pw1[:3] + str(len(pw1)) + str(pw1.count("e")) + "!"
print("{}의 비밀번호는 {}입니다".format(naver, pw1))

pw1 = google[7:]
pw1 = pw1[:pw1.index(".")]
pw1 = pw1[:3] + str(len(pw1)) + str(pw1.count("e")) + "!"
print("{}의 비밀번호는 {}입니다".format(google, pw1))

pw1 = daum[7:]
pw1 = pw1[:pw1.index(".")]
pw1 = pw1[:3] + str(len(pw1)) + str(pw1.count("e")) + "!"
print("{}의 비밀번호는 {}입니다".format(daum, pw1))