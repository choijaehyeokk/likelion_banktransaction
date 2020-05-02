import sys

persons = []

class account:    
    def __init__(self):
        print("======계좌개설======")
        print("계좌번호:")
        self.accountnum = input()
        print("이름:")
        self.name = input()
        print("예금:")
        self.money = input()
        total_money = self.money
        print("##계좌개설을 완료하였습니다##")

def lookup():
    print("======전체조회======")
    for person in persons:
        print("계좌번호:",person.accountnum,"/","이름:",person.name,"/","잔액",person.money,"원","/")
    print("===================")

while(True):
    print("======Bank Menu======")
    print("1. 계좌개설")
    print("2. 입금하기")
    print("3. 출금하기")
    print("4. 전체조회")
    print("5. 프로그램 종료")
    print("=====================")

    a = input()
    if a == '1':
        newaccount = account()
        persons.append(newaccount)
    elif a=='4':
        lookup()
    elif a == '5':
        sys.exit()
    else:
        print("제공되지 않는 기능입니다. 다시 골라주세요")

print("Hello world")