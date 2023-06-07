import random
import sys
modes = ["캐주얼", "트라이리밋", "머니리밋", "종료"]
suits = ["클로버", "하트", "스페이드", "다이아몬드"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
answer_kind = ["y", "n"]

card = 0
money = 0
correct = 0
betting = 0
best = 0
count = 0
case = 1
print("카드맞추기 게임에 오신 것을 환영합니다!")
def cardmain():  #메인 게임
    global money
    global correct
    global betting
    global best
    x = random.choice([1,2,3])
    y = random.choice([1,2,3])
    z = random.choice([1,2,3])
    p = x * y * z #조커 여부 확인

    if p == 1:
        a = random.choice([1, 2])
        if a == 1:
            print("축하합니다! 컬러 조커를 뽑으셨습니다. 베팅금의 5배를 즉시 지급합니다!")
            betting = betting * 5
            money += betting
            if best < money:
                best = money
        else:
            print("축하합니다! 흑백 조커를 뽑으셨습니다. 베팅금의 3배를 즉시 지급합니다!")
            betting = betting * 3
            money += betting
            if best < money:
                best = money
            
    else:
        shape = random.choice(suits)  # 카드 모양을 랜덤하게 선택
        number = random.choice(ranks)  # 카드 숫자를 랜덤하게 선택
        
        chances = 4  # 초기 기회 횟수
        while chances > 0:
            guess_suit = input("뽑은 카드의 모양을 맞혀보세요 (클로버, 하트, 스페이드, 다이아몬드 중 하나): ")
            while True:
                if guess_suit not in suits:
                    if guess_suit == "다이아":
                        guess_suit = "다이아몬드"
                        break
                    guess_suit = input("입력값에 오류가 있습니다. 모양을 다시 맞혀보세요 (클로버, 하트, 스페이드, 다이아몬드 중 하나): ")
                else:
                    break
            guess_rank = input("뽑은 카드의 숫자를 맞혀보세요 (A, 2, 3, ..., 10, J, Q, K 중 하나): ").upper()
            while True:
                if guess_rank not in ranks:
                    if guess_rank == "1":
                        guess_rank = "A"
                        break
                    if guess_rank == "j":
                        guess_rank = "J"
                        break
                    if guess_rank == "q":
                        guess_rank = "Q"
                        break
                    if guess_rank == "k":
                        guess_rank = "K"
                        break
                    guess_rank = input("입력값에 오류가 있습니다. 숫자를 다시 맞혀보세요 (A, 2, 3, ..., 10, J, Q, K 중 하나): ").upper()
                else:
                    break
            if guess_suit == shape and guess_rank == number:
                if chances == 4:
                    win_amount = betting * 3  # 첫 번째 기회에는 3배
                    print("축하합니다! 뽑은 카드를 정확하게 맞히셨습니다. {}원을 즉시 지급합니다!".format(int(win_amount)))
                    money += int(win_amount)
                    correct += 1
                    if best < money:
                        best = money
                    break
                elif chances == 3:
                    win_amount = betting * 2  # 두 번째 기회에는 2배
                    print("축하합니다! 뽑은 카드를 정확하게 맞히셨습니다. {}원을 즉시 지급합니다!".format(int(win_amount)))
                    money += int(win_amount)
                    correct += 1
                    if best < money:
                        best = money
                    break
                elif chances == 2:
                    win_amount = betting * 1.5 # 세 번째 기회에는 1.5배
                    print("축하합니다! 뽑은 카드를 정확하게 맞히셨습니다. {}원을 즉시 지급합니다!".format(int(win_amount)))
                    money += int(win_amount)
                    correct += 1
                    break
                elif chances == 1:
                    win_amount = betting   # 네 번째 기회에는 원금
                    print("축하합니다! 뽑은 카드를 정확하게 맞히셨습니다. {}원을 즉시 지급합니다!".format(int(win_amount)))
                    money += int(win_amount)
                    correct += 1
                    break
            else:
                chances -= 1
                if chances == 0:
                    print("기회를 모두 소진하였습니다. 정답은 {} {} 였습니다.".format(shape, number))
                    break
                else:
                    if shape == guess_suit:
                        print("\033[1;36m============================================\033[m")
                        print("\n컴퓨터가 뽑은 카드의 모양은 당신의 대답과 \033[1;32m일치합니다\u25ef\033[m")
                    else:
                        print("\033[1;36m============================================\033[m")
                        print("\n컴퓨터가 뽑은 카드의 모양은 당신의 대답과 \033[1;31m일치하지 않습니다\u2716\033[m")
                    if ranks.index(number) < ranks.index(guess_rank):
                        print("컴퓨터가 뽑은 카드의 숫자는 당신의 대답보다 \033[1;31m작습니다\u2193\u2193\u2193\033[m\n")
                        print("\033[1;36m============================================\033[m")
                    elif ranks.index(number) > ranks.index(guess_rank):
                        print("컴퓨터가 뽑은 카드의 숫자는 당신의 대답보다 \033[1;31m큽니다\u2191\u2191\u2191\033[m\n")
                        print("\033[1;36m============================================\033[m")
                    else:
                        print("컴퓨터가 뽑은 카드의 숫자는 당신의 대답과 \033[1;32m일치합니다\u25ef\033[m\n")
                        print("\033[1;36m============================================\033[m")
                    
                    print("다시 맞혀보세요. (남은 기회: {}번)\n".format(chances))
    return


def cardForTrylimit():  #트라이리밋 게임
    global correct
    global betting
    global best
    global count

    shape = random.choice(suits)  # 카드 모양을 랜덤하게 선택
    number = random.choice(ranks)  # 카드 숫자를 랜덤하게 선택
    # print(shape)
    # print(number)
    chances = 4  # 초기 기회 횟수
    while chances > 0:
        guess_suit = input("뽑은 카드의 모양을 맞혀보세요 (클로버, 하트, 스페이드, 다이아몬드 중 하나)(종료:N): ")
        while True:
            if guess_suit.upper() == 'N':
                print("게임을 종료합니다.")
                return guess_suit  # guess_suit 값을 반환하도록 수정
            elif guess_suit not in suits:
                if guess_suit not in suits:
                    if guess_suit == "다이아":
                        guess_suit = "다이아몬드"
                        break
                guess_suit = input("입력값에 오류가 있습니다. 모양을 다시 맞혀보세요 (클로버, 하트, 스페이드, 다이아몬드 중 하나)(종료:N): ")
            else:
                break
        if chances == 0:
            break
        guess_rank = input("뽑은 카드의 숫자를 맞혀보세요 (A, 2, 3, ..., 10, J, Q, K 중 하나): ")
        while True:
            if guess_rank not in ranks:
                if guess_rank not in ranks:
                    if guess_rank == "1":
                        guess_rank = "A"
                        break
                    if guess_rank == "j":
                        guess_rank = "J"
                        break
                    if guess_rank == "q":
                        guess_rank = "Q"
                        break
                    if guess_rank == "k":
                        guess_rank = "K"
                        break
                guess_rank = input("입력값에 오류가 있습니다. 숫자를 다시 맞혀보세요 (A, 2, 3, ..., 10, J, Q, K 중 하나): ")
            else:
                break
        if guess_suit == shape and guess_rank == number:
            if chances <= 3 and case < 5:
                correct += 1
                print("축하합니다! 뽑은 카드를 정확하게 맞히셨습니다.")
                break
            else:
                print("아쉽습니다. 뽑은 카드를 맞히지 못하셨습니다.")
                break                
        else:
            chances -= 1
            if chances == 0:
                print("기회를 모두 소진하였습니다. 정답은 {} {} 였습니다.".format(shape, number))
                break
            else:
                if shape == guess_suit:
                    print("\033[1;36m============================================\033[m")
                    print("\n컴퓨터가 뽑은 카드의 모양은 당신의 대답과 \033[1;32m일치합니다\u25ef\033[m")
                else:
                    print("\033[1;36m============================================\033[m")
                    print("\n컴퓨터가 뽑은 카드의 모양은 당신의 대답과 \033[1;31m일치하지 않습니다\u2716\033[m")
                if ranks.index(number) < ranks.index(guess_rank):
                    print("컴퓨터가 뽑은 카드의 숫자는 당신의 대답보다 \033[1;31m작습니다\u2193\u2193\u2193\033[m\n")
                    print("\033[1;36m============================================\033[m")
                elif ranks.index(number) > ranks.index(guess_rank):
                    print("컴퓨터가 뽑은 카드의 숫자는 당신의 대답보다 \033[1;31m큽니다\u2191\u2191\u2191\033[m\n")
                    print("\033[1;36m============================================\033[m")
                else:
                    print("컴퓨터가 뽑은 카드의 숫자는 당신의 대답과 \033[1;32m일치합니다\u25ef\033[m\n")
                    print("\033[1;36m============================================\033[m")
                
                print("\n다시 맞혀보세요. (남은 기회: {}번)\n".format(chances))
    return guess_suit  # guess_suit 값을 반환

def tryLimit():
    print("5번의 기회 중 당신은 과연 몇 번을 맞힐 수 있을까요?")
    print("당신의 직감을 테스트해보세요!")
    for count in range(5, 0, -1):
        guess_suit = cardForTrylimit()  # cardForTrylimit 함수의 반환값을 저장
        if guess_suit.upper() == 'N':
            break
        print("\n{}회 맞히셨고 {}회 남았습니다.\n".format(correct, count - 1))
    if guess_suit != 'N':
        print("게임이 종료되었습니다. 5회 중 {}회 맞히셨습니다. ".format(correct))




def casual():
    global card
    global money
    global correct
    global betting
    global best
    print("기본적인 모드로, 설정한 자금으로 횟수 제한없이 즐기는 모드입니다.")
    print("베팅금액을 입력하시고 랜덤하게 나온 카드를 맞히시면 됩니다. 조커를 뽑으시면 그 즉시 색에 따라 베팅금의 배수로 돌려드립니다.")
    while True:
        try:
            money = input("초기자금을 설정해주세요: ")
            if not money.isdigit() or int(money) <= 0:
                raise ValueError
            break
        except ValueError:
            print("초기자금은 0 이하이거나 숫자가 아닐 수 없습니다. 다시 입력해주세요.")
    money = int(money)
    start = money
    correct = 0
    card = 0
    best = money
    while True:
        print("현재 {}원을 가지고 계십니다.".format(money))
        while True:
            try:
                betting = input("베팅금액을 정해주세요: ")
                if not betting.isdigit() or int(betting) <= 0:
                    raise ValueError
                if int(betting) > money:
                    raise ValueError("자금이 부족합니다.")
                money -= int(betting)
                break
            except ValueError as e:
                print("입력값에 오류가 있습니다. 다시 입력해주세요.")
                print(str(e))
        betting = int(betting)
        card += 1            
        cardmain()
        if money == 0:
            print("자본금을 전부 소진하였습니다. 게임을 종료합니다.")
            answer = input("다시 시작하시겠습니까? (y/n)")
            while True:
                if answer.lower() in answer_kind:
                    break
                else:
                    answer = input("다시 입력해주세요 (y/n)")           
            if answer.lower() == 'y':
                while True:
                    try:
                        money = input("초기자금을 설정해주세요: ")
                        if not money.isdigit() or int(money) <= 0:
                            raise ValueError
                        break
                    except ValueError:
                        print("초기자금은 0 이하이거나 숫자가 아닐 수 없습니다. 다시 입력해주세요.")
                money = int(money)
                start += money
                if best < money:
                    best = money
                continue
            else:
                print("게임을 종료합니다.")
                break
        else :
            answer = input("계속 하시겠습니까? (y/n)").lower()
            while True:
                if answer.lower() in answer_kind:
                    break
                else:
                    answer = input("다시 입력해주세요 (y/n)").lower()            
            if answer.lower() == 'y':
                continue
            elif answer.lower() == 'n':
                print("게임을 종료합니다.")
                break
    print("게임이 종료되었습니다. 총 ",start,"원을 가지고 게임을 하셨으며, 최고 금액은",best,"원이었습니다. 게임을 ",card,"번 하셨으며, ",correct,"번 맞추셨고, ",money,"원 남으셨습니다.")
    return

def moneyLimit():
    global card
    global money
    global correct
    global betting
    global best
    print("정해진 금액만으로 얼마나 빠르게 늘릴 수 있을까요?")
    print("10만원으로 50만원까지 순식간에 늘려봅시다!")
    money = 100000
    while money < 500000:
        print("현재 ", money, "원을 가지고 계십니다.")
        if money >= 500000:
            print("축하합니다! 500000만원 이상 모으는데 성공하셨습니다! 게임을 ",card,"번 하셨으며, ",correct,"번 맞추셨습니다!")
            break
        elif money > 0:
            while True:
                betting = input("베팅금액을 정해주세요(종료:N): ")
                if betting.upper() == 'N':
                    print("게임을 종료합니다.")
                    return
                try:
                    if not betting.isdigit() or int(betting) <= 0:
                        raise ValueError
                    if int(betting) > money:
                        raise ValueError("자금이 부족합니다.")
                    money -= int(betting)
                    break
                except ValueError as e:
                    print("입력값에 오류가 있습니다. 다시 입력해주세요.")
                    print(str(e))
            betting = int(betting)
            card += 1            
            cardmain()
        else:
            print("안타깝지만 돈을 전부 소진해버리고 말았습니다...")
            print("게임이 종료되었습니다. 총 100000원을 가지고 게임을 하셨으며, 최고 금액은",best,"원이었습니다. 게임을 ",card,"번 하셨으며, ",correct,"번 맞추셨습니다.")
            break
while True:
    mode = input("메뉴를 선택해주세요. (캐주얼/트라이리밋/머니리밋/종료): ")
    while True:
        if mode not in modes:
            mode = input("메뉴를 다시 선택해주세요. (캐주얼/트라이리밋/머니리밋/종료):")
        else:
            if mode == "종료":
                print("게임을 종료합니다\n")
                sys.exit()
            else:
                break
    print(mode,"모드를 선택하셨습니다.\n")
    if mode == "캐주얼":
        casual()
    if mode == "트라이리밋":
        tryLimit()
    if mode == "머니리밋":
        moneyLimit()
    if mode == "종료":
        sys.exit()
    continue
   
