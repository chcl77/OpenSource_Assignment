###################

# 프로그램명 : 성적관리프로그램
# 작성자 : 소프트웨어학부 / 이충희
# 작성일 : 2025-03-16
# 프로그램 설명 : 5명의 학생의 세개의 교과목 (영어, C-언어, 파이썬)에 대해 입력받아 총점, 평균, 학점, 등수를 계산하는 프로그램 작성

###################

#index가 0이면 영어 교과목의 합, 1이면 C언어 교과목의 합, 2이면 Python 교과목의 합을 반환
def get_total(arr, index) :
    sum = 0
    for i in range(0,5) :
        sum += arr[i][index]
    return sum

#index가 0이면 영어 교과목의 평균, 1이면 C언어 교과목의 평균, 2이면 Python 교과목의 평균을 반환
def get_average(arr, index) :
    return get_total(arr,index) / 5

#매개변수인 grade에 따라 학점 반환 
def get_score(grade) : 
    if grade >= 90 : return 'A'
    elif grade >= 80 : return 'B'
    elif grade >= 70 : return 'C'
    elif grade >= 60 : return 'D'
    else : return 'F'
#각 과목별 등수 출력, index = 0이면 영어, index = 1이면 C언어, index = 2이면, Python 과목의 각 학생별 등수를 출력 
def Show_Rank(arr, index) : 
    
    index_grade = [] 

    #index에 해당하는 과목안에서의 학생들의 교과목 성적 추출
    for i in range(0, 5) :
        index_grade.append(arr[i][index])
    #내림차순으로 정렬
    list = sorted(index_grade, reverse = True)

    result = []
    #내림차순으로 정렬한 list를 바탕으로 등수 추출
    for i in index_grade :
        result.append(list.index(i) + 1)
    #등수 출력
    if(index == 0) :
        print("-------- 영어 교과목 등수 -----------")
        for i in range(0,5) :
            print(str(i + 1) + "번째 학생의 등수 : " + str(result[i]) + "등")
    elif(index == 1) : 
        print("-------- C언어 교과목 등수 -----------")
        for i in range(0,5) :
            print(str(i + 1) + "번째 학생의 등수 : " + str(result[i]) + "등")
    elif(index == 2) :
        print("-------- Python 교과목 등수 -----------")
        for i in range(0,5) :
            print(str(i + 1) + "번째 학생의 등수 : " + str(result[i]) + "등")

#각 학생들의 영어, C언어, Python 성적을 받는 list
set = []

for i in range(1,6) :
    grade = []
    a = int(input(str(i) + "번째 학생의 영어 교과목의 점수를 입력하세요 : "))
    b = int(input(str(i) + "번째 C언어 교과목의 점수를 입력하세요 : "))
    c = int(input(str(i) + "번째 Python 교과목의 점수를 입력하세요 : "))
    grade.append(a)
    grade.append(b)
    grade.append(c)
    set.append(grade)

print("\n")

print("영어 교과목 총점 : " + str(get_total(set, 0)))
print("C언어 교과목 총점 : " + str(get_total(set, 1)))
print("Python 교과목 총점 : " + str(get_total(set, 2)))

print("\n")
print("영어 교과목 평균 : " + str(get_average(set, 0)))
print("C언어 교과목 평균 : " + str(get_average(set, 1)))
print("Python 교과목 평균 : " + str(get_average(set, 2)))

print("\n")
for i in range(0, 5) :
    print(str(i + 1) + "번째 학생의 학점")
    print("영어 : " + get_score(set[i][0]) + ", C언어 : " + get_score(set[i][1]) + ", Python : " + get_score(set[i][2]))

print("\n")
Show_Rank(set, 0)
Show_Rank(set, 1)
Show_Rank(set, 2)
