import random

#기본 설정 class

class Character:
    """
    모든 캐릭터의 모체가 되는 클래스
    """
    def __init__(self, name, hp, mp, power, magic_power):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.power = power
        self.magic_power = magic_power
    
    #상태창(플레이어)
    def player_show_status(self):
        print(f"{self.name}의 상태: HP {int(self.hp)}/{self.max_hp} MP {self.mp}/{self.max_mp}")

    #상태창(몬스터)
    def monster_show_status(self):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}")


class Player(Character):
    # 모체 캐릭터의 성능을 가진 자식 플레이어의 특성

    # 플레이어의 물리딜
    def attack(self, other):
        damage = random.randint(self.power - 2, self.power + 2)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    # 플레이어의 마법딜
    def magic_attack(self, other):
        magic_damage = random.randint(self.magic_power + 6, self.magic_power + 12)
        other.hp = max(other.hp - magic_damage, 0)
        self.mp = max(self.mp - 10, 0)

        print(f"{self.name}의 공격! {other.name}에게 {magic_damage}의 데미지를 입혔습니다.")
        if other.hp <= 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")
        
class Monster(Character):
    # 모체 캐릭터의 성능을 가진 자식 몬스터의 특성 ##
    def monster_attack(self, other):
        damage = random.randint(self.power - 2, self.power + 2)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if self.hp <= 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")


# 전투
print("플레이어의 이름을 입력하세요!!")
Player_name = input("Player name: ") 

#몬스터 변수(고유값보단 소문자 넣어서 m1 넣는 게 맞는 듯)
m1 = Monster('Killer', 350, 0, 30, 0)

# 플레이어 1, 2, 3 중에 픽할 것
print('플레이어를 선택하시오')
print('1. Warrior')
print('2. Assassin')
print('3. Wizard')

# 번호값 input할 시 캐릭터 배정(name, hp, mp, power, magic_power)
Player_select = int(input('플레이어를 선택하시오. '))
if Player_select == 1:
    Character_name = Player('Warrior', 300, 80, 30, 28)
elif Player_select == 2:
    Character_name = Player('Assassin', 220, 70, 40, 25)
elif Player_select == 3:
    Character_name = Player('Wizard', 250, 80, 20, 40)
print(f'{Player_name} 님의 캐릭터는 {Character_name.name}입니다.')
                                                                



# turn을 짝수 홀수로 하여 플레이어와 몬스터의 순번을 정함
turn = 0

# 플레이어 차례
print('fight!')
while True:
    if turn % 2 == 0:
        print('My turn!')
        print('몬스터에게 어떤 공격을 하시겠습니까?')
        player_action = int(input("1.일반공격 2.마법공격 ")) #int빠짐. player_action이라는 함수명이 위에 있어서 변수명으로 작동하지 않았음.
        if player_action == 1:
            if Player_select == 2:
                if turn % 4 == 2:
                    Character_name.attack(m1)
                    Character_name.attack(m1)
                else:
                    Character_name.attack(m1)
            else:
                Character_name.attack(m1) 
        elif player_action == 2:
            if Character_name.mp < 10:
                print('마나도 없는 게 공격을?')
            else:
                if Player_select == 2:
                    if turn % 4 ==2:
                        Character_name.magic_attack(m1)
                        Character_name.magic_attack(m1)
                    else:
                        Character_name.magic_attack(m1)
                else:
                    Character_name.magic_attack(m1)

        m1.monster_show_status()

        if m1.hp <= 0:
            print('Game over')
            print('You win!')
            break
        else:
            turn += 1

# 몬스터 차례
    elif turn % 2 == 1:
        print('Monster turn!')
        m1.monster_attack(Character_name)
        Character_name.player_show_status()
        if Character_name.hp <= 0:
            print('Game over')
            print('You lose..')
            break
        else:
            turn += 1




# 픽 다 했으면 바로 전투로 들어갈 것 = 해결
# 전투에서 while 반복문에 따라 턴제공격 실시, = 해결
# 직업 이름이 왜 틀렸을까? = 해결 (Character_name.name 으로 인자를 추가하면 된다.)
# 턴제공격
#     - 물리공격 or 마법공격 중 선택 = 해결
#     - 선택하면 공격이 들어가면서 상대 체력 감소 = 해결
#     - 마법 공격 사용 시 내 mp도 같이 감소 = 해결
#     - 몬스터는 물리딜만 가능 = 해결
#     - 이 과정을 반복해서 둘 중 하나의 피가 0이 되면 경기 종료 = 해결
#     - 내가 이길 시 "you win", 질 시 "you lose" 문구 print = 해결

# 필수 추가 사항
# 1. 한 쪽이 죽으면 턴제와 게임이 종료되도록 해야 함 = 해결 (if 문에 break를 쓰면 해결됨.)
# 2. def show_status가 이루어져야 함 = 해결 Character_name.player_show_status(), m1.monster_show_status()

# 추가 능력치 투입
# 1. assassin은 두 번째 공격마다 멀티 딜이 들어간다.
# 2. 