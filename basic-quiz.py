#Quiz 1
# station = "사당"
# print(station,"행 열차가 들어오고 있습니다.")
# station = "신도림"
# print(station,"행 열차가 들어오고 있습니다.")
# station = "인천공항"
# print(station,"행 열차가 들어오고 있습니다.")

# Quiz 2
# from random import *
# print("오프라인 스터디 모임 날짜는 매월",randint(4,28),"일로 선정되었습니다.")

# Quiz 3
# my solution
# adrs = "http://naver.com"
# adrs = adrs[7:]
# adrs = adrs[:5]
# password = adrs[:3]+str(len(adrs))+str(adrs.count("e"))+"!"
# print(password)

# solution in lecture
# url = "http://naver.com"
# my_str=url.replace("http://","")
# my_str=my_str[:my_str.index(".")]
# password = my_str[:3]+str(len(my_str))+str(my_str.count("e"))+"!"
# print("{0}의 비밀번호는 {1} 입니다." .format(url,password))

# Quiz 4
# #my solution
# from random import *
# list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# chicken=randint(1,20)
# list.remove(chicken)
# shuffle(list)

# print(" -- 당첨자 발표 --")
# print("치킨 당첨자 :",chicken)
# print("커피 당첨자 :",sample(list,3))
# print(" -- 축하합니다 --")

#solution in lecture
# from random import *
# users = range(1,21) #1부터 20까지 숫자 생성
# users = list(users)
# shuffle(users)

# winners = sample(users,4)
# print(" -- 당첨자 발표 --")
# print("치킨 당첨자 : {0}".format(winners[0]))
# print("커피 당첨자 : {0}".format(winners[1:]))
# print(" -- 축하합니다 --")

#Quiz 5
# my_solution
# from random import *
# cnt=0
# for i in range(1,51):
#     num=randint(5,50)
#     print("{0} {1}".format(i, num))
#     if(num>=5 and num<=15): #혹은 if 5<=num<=15 로도 표현 가능
#         print("[O] {0}번째 손님 (소요시간 : {1})".format(i,num))
#         cnt+=1
#     else:
#         print("[ ] {0}번째 손님 (소요시간 : {1})".format(i,num))
# print("총 탑승 승객 : {0} 분".format(cnt))

#Quiz 6
# my_solution
# def std_weight(height,gender):
#     if(gender == "남자"):
#         std_w = round(height*height*22/10000,2)
#     else:
#         std_w = round(height*height*21/10000,2)
#     print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다." .format(height,gender,std_w))    

# std_weight(175,"남자")

#solution in lecture
# def std_weight(height,gender): # 키 m 단위 (실수), 성별 "남자"/"여자"
#     if(gender=="남자"):
#         return height*height*22
#     else:
#         return height*height*21

# height = 175 # cm 단위
# gender = "남자"
# weight = round(std_weight(height / 100,gender),2)
# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다." .format(height,gender,weight))    