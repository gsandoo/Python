def make_a_list():
    Test=open("./phone.txt","r",encoding="UTF-8")
    while True:
        readFile=Test.readline()
        if readFile != "":
            name,phone,phone2,num=list(map(str,readFile.split(":")))
            print(f"name:{name}\nphone:{phone}\nphone2:{phone2}\nnum:{num}\n")
        else:
            break
    Test.close()

def add():
    Test=open("./phone.txt","a",encoding="UTF-8")
    Test.write("\n")
    data=input("이름: 전화번호 : 전화번호2 : 넘버 작성")
    Test.write(data)
    Test.close()


def search():
    find=input("찾을단어 검색:")
    Test=open("./phone.txt","r",encoding="UTF-8")
    while True:
        line=Test.readline()
        if find not in line:
            continue
        else:
            print(line)
            break




            
    



add()
search()
make_a_list()


