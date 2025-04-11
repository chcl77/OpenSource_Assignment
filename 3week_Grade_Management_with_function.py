###################

# 프로그램명 : 성적관리프로그램 (함수)
# 작성자 : 소프트웨어학부 / 이충희
# 작성일 : 2025-03-23
# 프로그램 설명 : 기존의 성적관리프로그램를 함수로 나누어 구현 

###################


def insert() :
    grade = []
    
    grade.append(input("학번 : "))
    grade.append(input("이름 : "))
    grade.append(int(input("영어 : ")))
    grade.append(int(input("C-언어 : ")))
    grade.append(int(input("파이썬 : ")))
    return grade

def get_total(arr, index) :
    sum = 0
    for i in range(2, 5) : 
        sum += arr[index][i]
    return sum

def get_average(arr, index) :
    return get_total(arr,index) / 5


def get_score(grade) : 
    
    if grade >= 95 : return 'A+'
    elif grade >= 90 : return 'A'
    elif grade >= 85 : return 'B+'
    elif grade >= 80 : return 'B'
    elif grade >= 75 : return 'C+'
    elif grade >= 70 : return 'C'
    elif grade >= 65 : return 'D+'
    elif grade >= 60 : return 'D'
    else : return 'F'

def Show_Rank(arr) : 
    
    index_grade = [] 
    sum = 0
    for i in range(0, 5) :
        sum = 0
        for j in range(2, 5) :
            sum += arr[i][j]
        index_grade.append(sum)
    list = sorted(index_grade, reverse = True)
    result = []
    for i in index_grade :
        result.append(list.index(i) + 1)
    return result
    

def printing(arr) :
    print("                           성적관리 프로그램                            ")
    print("=" * 100)
    print("학번           ", end = ' ')
    print("이름      ", end = ' ')
    print("영어    ", end = ' ')
    print("C-언어    ", end = ' ')
    print("파이썬     ", end = ' ')
    print("총점     ", end = ' ')
    print("평균      ", end = ' ')
    print("학점     ", end = ' ')
    print("등수      " )
    print("=" * 100)
  
    rank = Show_Rank(arr)
    for i in  range(0, 5) : 
        for j in range(0, 5) :
            if(j >= 2) : 
                print(arr[i][j], end = "        ")
            else : 
                print(arr[i][j], end = "      ")
        print(get_total(arr, i) , end = "        ")
        print(get_total(arr, i) // 3 , end = "        ")
        print(get_score(get_total(arr, i)//3) , end = "        ")
        print(rank[i] , end = "        ")
        print("\n")



set = []
test = ["2022021234" , "가우스" , "90", "90", "90", "100", "100", "100", "1"]
for i in range(1,6) :
    set.append(insert())

printing(set)

    
    

