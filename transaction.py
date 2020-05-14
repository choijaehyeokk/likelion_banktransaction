from Likelionperson import Person
persons = []

class Account(Person):    
    def __init__(self):
        print("\n======계좌개설======")
        print("계좌번호:")
        self.accountnum = input()
        print("이름:")
        self.name = input()
        print("예금:")
        self.money = int(input())
        total_money = self.money
        print("##계좌개설을 완료하였습니다##")
        print("=====================\n")

def lookup():
    print("\n======전체조회======")
    for person in persons:
        print("계좌번호:",person.accountnum,"/","이름:",person.name,"/","잔액",person.money,"원","/")
    print("===================\n")

def deposit():
    print("\n======입금하기======")
    deposit_account = input("입금하실 계좌번호를 입력하세요:")

    if not persons:
        print("개설된 계좌가 없습니다.\n")
        return
    for person in persons:
        if person.accountnum == deposit_account:
            print("계좌이름:",person.name)
            print("계좌잔고:",person.money,"원")
            deposit_money = int(input("입금하실 금액을 입력해주세요:"))
            person.money += deposit_money
            print("##계좌잔고:",person.money,"원##")
            print("##입금이 완료되었습니다.##")
            print("=====================\n")
            break
        

def withdraw():
    print("\n======출금하기======")

    withdraw_account = input("출금하실 계좌번호를 입력하세요:")
    if not persons:
        print("개설된 계좌가 없습니다.\n")
    for person in persons:
        if person.accountnum == withdraw_account:
            print("계좌이름:",person.name)
            print("계좌잔고:",person.money,"원")
            withdraw_money = int(input("출금하실 금액을 입력해주세요:"))
            person.money -= withdraw_money
            if person.money < 0:
                print("계좌잔액이 부족합니다")
                print("=====================")                
                person.money += withdraw_money
                break
            print("##계좌잔고:",person.money,"원##")
            print("##출금이 완료되었습니다.##")
            break
        
def deposit_interest():
    current = ''
    print("======예금이자 계산하기======")
    interets_account =input("계좌를 입력해주세요: ")
    if not persons:
        return 0
    else:
        for person in persons:
            if person.accountnum == interets_account:
                current = person
            
        if not current:
            return 1
               
        year = int(input("몇 년으로 하시겠습니까 : "))
        interest_rate = float(input("금리가 몇 %입니까 :"))
        a= input("단리 / 복리 중에 선택해주세요:")
        if a=='단리':
            fv = current.money * (1+((0.01*interest_rate) * year))
            return fv
        elif a == '복리':
            fv = current.money * ((1+(0.01*interest_rate))**year)
            return round(fv,2)
        else:
            return 2

def transfer():
    print("\n======이체하기======")

    transfer_account = int(input("본인 계좌번호를 입력하세요:"))
    if not persons:
        print("개설된 계좌가 없습니다.\n")
        break
    a = person

    receive_account = int(input("받을 계좌번호를 입력하세요:"))
    if not persons:
        print("개설된 계좌가 없습니다.\n")
        break

    t_money = int(input("이체할 금액을 입력하세요:"))

            person.money += t_money
            a.money -= t_money

            print("##본인 계좌잔고:", a.money, "원##")
            print("##이체한 계좌잔고:", person.money, "원##")
            print("##이체가 완료되었습니다.##")
    break


while(True):
    print("======Bank Menu======")
    print("1. 계좌개설")
    print("2. 입금하기")
    print("3. 출금하기")
    print("4. 전체조회")
    print("5. 프로그램 종료")
    print("6. 예금 연이자 계산하기")
    print("7. 이체하기")
    print("=====================\n")

    a = input("어떤 업무를 수행하시겠습니까?")
    if a == '1':
        newaccount = Account()
        persons.append(newaccount)
    elif a== '2':
        deposit()
    elif a == '3':
        withdraw()
    elif a=='4':
        lookup()
    elif a == '5':
        print("\n##은행프로그램을 종료합니다.##\n")
        break
    elif a== '6':
        result = deposit_interest()
        if result == 0:
            print("등록된 계좌가 없습니다")
        elif result == 1:
            print("해당 계좌가 없습니다.")
        elif result == 2:
            print("잘못된 입력입니다.")
        else:
            print("세전 %.2f 원입니다." %result)
    elif a =='7'
        transfer()
    else:
        print("제공되지 않는 기능입니다. 다시 골라주세요")

