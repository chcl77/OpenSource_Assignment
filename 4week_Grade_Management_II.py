###################

# 프로그램명 : 성적관리프로그램 II
# 작성자 : 소프트웨어학부 / 이충희
# 작성일 : 2025-03-30
# 프로그램 설명 : 기존의 성적관리프로그램에 삭제 함수, 탐색함수, 정렬함수, 80점이상 학생 수 카운트 함수, 삽입함수를 추가

###################




#입력 함수
def insert() :
    grade = []
    
    grade.append(input("학번 : "))
    grade.append(input("이름 : "))
    grade.append(int(input("영어 : ")))
    grade.append(int(input("C-언어 : ")))
    grade.append(int(input("파이썬 : ")))
    return grade
#총점 계산 함수
def get_total(arr, index) :
    sum = 0
    for i in range(2, 5) : 
        sum += arr[index][i]
    return sum
#평균 계산 함수
def get_average(arr, index) :
    return get_total(arr,index) // 3

#학점 계산 함수
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
#등수 계산 함수
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

#정렬 함수
def sorting(arr) : 
    lists = []
    for i in range(0, 5) :
        lists.append(get_total(arr, i))
    print(lists)
    lists.sort()
    return lists
#탐색함수
def search(arr, idx) :
    result = []
    result.append(arr[idx][0])
    result.append(arr[idx][1])
    return result 
#80점 이상 학생 카운트 함수
def search_over_80(arr) :
    count = 0
    lists = []
    for i in range(0, 5) :
        lists.append(get_average(arr, i))
    print(lists)
    for i in lists :
            if i >= 80 :
                count += 1
    return count 
#삭제 함수
def delete_idx(arr, row, col) :
    arr[row].pop(col)
    return arr
#삽입 함수
def insert_to_arr(arr, row, col, data) :
    arr[row].insert(col, data)
    return arr


#출력 함수
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

for i in range(1,6) :
    set.append(insert())

printing(set)



