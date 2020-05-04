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
        self.money = int(input())
        total_money = self.money
        print("##계좌개설을 완료하였습니다##")

def lookup():
    print("======전체조회======")
    for person in persons:
        print("계좌번호:",person.accountnum,"/","이름:",person.name,"/","잔액",person.money,"원","/")
    print("===================")

def deposit():
    print("======입금하기======")
    deposit_account = input("입금하실 계좌번호를 입력하세요:")
    for person in persons:
        if person.accountnum == deposit_account:
            print("계좌이름:",person.name)
            print("계좌잔고:",person.money,"원")
            deposit_money = int(input("입금하실 금액을 입력해주세요:"))
            person.money += deposit_money
            print("##계좌잔고:",person.money,"원##")
            print("##입금이 완료되었습니다.##")
            break

def withdraw():
    print("======출금하기======")
    withdraw_account = input("출금하실 계좌번호를 입력하세요:")
    for person in persons:
        if person.accountnum == withdraw_account:
            print("계좌이름:",person.name)
            print("계좌잔고:",person.money,"원")
            withdraw_money = int(input("출금하실 금액을 입력해주세요:"))
            person.money -= withdraw_money
            if person.money < 0:
                break
            print("##계좌잔고:",person.money,"원##")
            print("##출금이 완료되었습니다.##")
            break


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
    elif a== '2':
        deposit()
    elif a == '3':
        withdraw()
    elif a=='4':
        lookup()
    elif a == '5':
        print("##은행프로그램을 종료합니다.##")
        sys.exit()
    else:
        print("제공되지 않는 기능입니다. 다시 골라주세요")

