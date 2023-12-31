def validate(hand):
    if hand < 0 or hand > 2:
        return False
    return True

def print_hand(hand, name='guest'):
    hands = ["바위","가위", "보"]
    print(name + '는' + hands[hand] + '을냈습니다')

print('가위 바위 보 하자!')
player_name = input('이름을 입력해주세요：')
print('무엇을 내겠습니까?（0: 바위, 1: 가위, 2: 보）')
player_hand = int(input('숫자를 입력해주세요：'))

if validate(player_hand):
    computer_hand = 1
   
    if player_name == '':
        print_hand(player_hand)
    else:
        print_hand(player_hand, player_name)
    
    print_hand(computer_hand, "컴퓨터")

else:
    print("0-2 숫자를 입력해주세요")
