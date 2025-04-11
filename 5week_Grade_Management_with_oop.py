###################

# 프로그램명 : 성적관리프로그램 (객체지향)
# 작성자 : 소프트웨어학부 / 이충희
# 작성일 : 2025-04-12
# 프로그램 설명 : 기존의 절차지형으로 작성된 성적관리프로그램을 객체지향으로 작성

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

#Grade class 생성
class Grade :
    grade_list = []

    def get_lists(self, arr) :
        self.grade_list = arr

    #총점 계산 메서드
    def get_total(self, arr, index) :
        sum = 0
        for i in range(2, 5) : 
            sum += arr[index][i]
        return sum
    #평균 계산 메서드
    def get_average(self, arr, index) :
        return self.get_total(arr,index) // 3

    #학점 계산 메서드
    def get_score(self, grade) : 
        
        if grade >= 95 : return 'A+'
        elif grade >= 90 : return 'A'
        elif grade >= 85 : return 'B+'
        elif grade >= 80 : return 'B'
        elif grade >= 75 : return 'C+'
        elif grade >= 70 : return 'C'
        elif grade >= 65 : return 'D+'
        elif grade >= 60 : return 'D'
        else : return 'F'
        
    #등수 계산 메서드
    def Show_Rank(self) : 
        
        index_grade = [] 
        sum = 0
        for i in range(0, 5) :
            sum = 0
            for j in range(2, 5) :
                sum += self.grade_list[i][j]
            index_grade.append(sum)
        list = sorted(index_grade, reverse = True)
        result = []
        for i in index_grade :
            result.append(list.index(i) + 1)
        return result

    #정렬 메서드
    def sorting(self) : 
        lists = []
        for i in range(0, 5) :
            lists.append(self.get_total(self.grade_list, i))
        print(lists)
        lists.sort()
        return lists
    #탐색메서드
    def search(self, arr, idx) :
        result = []
        result.append(arr[idx][0])
        result.append(arr[idx][1])
        return result 
    #80점 이상 학생 카운트 메서드
    def search_over_80(self, arr) :
        count = 0
        lists = []
        for i in range(0, 5) :
            lists.append(self.get_average(arr, i))
        print(lists)
        for i in lists :
                if i >= 80 :
                    count += 1
        return count 
    #삭제 메서드
    def delete_idx(self, arr, row, col) :
        arr[row].pop(col)
        return arr
    #삽입 메서드
    def insert_to_arr(self, arr, row, col, data) :
        arr[row].insert(col, data)
        return arr
    #출력 메서드
    def printing(self) :
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
    
        rank = self.Show_Rank()
        for i in  range(0, 5) : 
            for j in range(0, 5) :
                if(j >= 2) : 
                    print(self.grade_list[i][j], end = "        ")
                else : 
                    print(self.grade_list[i][j], end = "      ")
            print(self.get_total(self.grade_list, i) , end = "        ")
            print(self.get_total(self.grade_list, i) // 3 , end = "        ")
            print(self.get_score(self.get_total(self.grade_list, i)//3) , end = "        ")
            print(rank[i] , end = "        ")
            print("\n")

    



set = []

for i in range(1,6) :
    set.append(insert())

grades = Grade()
grades.get_lists(set)

grades.printing()



