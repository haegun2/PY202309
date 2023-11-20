from Student import *

#데이터를 불러와 인덱스 처리 후 인스턴스 만들고 각 값 저장, ins_name 에 ins_name 객체 저장      
def load_data():
    lines = open("./students.csv", "r", encoding="utf8").readlines()
    for line in lines[1:]:
        a = line.strip().split(",")
        ins_name = Student(a[0], float(a[1]), float(a[2]), float(a[3]))
        ins_list.append(ins_name)
    return ins_list

ins_list = []
load_data()
stu_ave = []

#인스턴스로 구해진 평균을, stu_ave 리스트에 각 값을 저장
for i in ins_list:
    a = i.get_average()
    stu_ave.append(a)

#학생 평균 점수를 출력
print("-----학생들의 평균 점수-----")
for i in range(len(ins_list)):
    print(ins_list[i].name, "의 평균 점수는", stu_ave[i], "입니다.")

#학생 평균 점수를 csv 파일로도 쓰기
wr = open("./average.txt", 'w', encoding="utf8")
wr.write("-----학생들의 평균 점수-----\n")
for i in range(len(ins_list)):
    data = (f"{ins_list[i].name}의 평균 점수는 {stu_ave[i]}입니다.\n")
    wr.write(data)
wr.close()