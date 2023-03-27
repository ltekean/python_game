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

    # 플레이어의 물리딜
    def attack(self, other):
        damage = random.randint(self.power - 2, self.power + 2)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    # 몬스터의 물리딜
    def monster_attack(self, other):
        monster_damage = random.randint(self.power - 1, self.power + 3)
        other.hp = max(other.hp - monster_damage, 0)
        print(f"{other.name}의 공격! {self.name}에게 {monster_damage}의 데미지를 입혔습니다.")
        if self.hp == 0:
            print(f"{self.name}이(가) 쓰러졌습니다.")
    # 몬스터 함수이니까 몬스터 클래스에 넣어서 오버라이딩 해도 좋을것 같아요, 그러면 damage변수를 monster_damage로 새로 쓸 필요없이 그대로 damage로 써도 됩니다.
    # 또 self, other는 항상 함수가 속해있는 클래스 기준이기 때문에 다시 바꿔서 써주시면 될것 같습니다.

    #상태창(플레이어)
    def player_show_status(self):
        print(f"{self.name}의 상태: HP {int(self.hp)}/{self.max_hp} MP {self.mp}/{self.max_mp}")

    #상태창(몬스터)
    def monster_show_status(self):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}")


class Player(Character):
    # 모체 캐릭터의 성능을 가진 자식 플레이어의 특성

    # 플레이어의 마법딜
    def magic_attack(self, other):
        magic_damage = random.randint(self.magic_power + 6, self.magic_power + 12)
        other.hp = max(other.hp - magic_damage, 0)
        self.mp = max(self.mp - 10, 0)

        print(f"{self.name}의 공격! {other.name}에게 {magic_damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")
        
class Monster(Character):
    # 모체 캐릭터의 성능을 가진 자식 몬스터의 특성 ##
    def monster_attack(self, other):
        damage = random.randint(self.power - 1, self.power + 3)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if self.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")


# 전투
print("플레이어의 이름을 입력하세요!!")
Player_name = input("Player name: ") 

# #각 캐릭터별 능력치 (name, hp, mp, power, magic_power)                  #아래에서 클래스를 지정해주기 때문에 주석처리했습니다!
# P1 = Player('Warrior', 100, 40, 15, 20)
# P2 = Player('Assassin', 70, 40, 25, 15)
# P3 = Player('Wizard', 80, 60, 10, 30)

m1 = Monster('Killer', 120, 0, 20, 0)                #몬스터는 그대로 변수에 넣었습니다! M1으로 해도 상관없으실것 같은데 저는 파란색뜨는게 거슬려서 바꿨습니다!

# 플레이어 1, 2, 3 중에 픽할 것
print('플레이어를 선택하시오')
print('1. Warrior')
print('2. Assassin')
print('3. Wizard')

# 번호값 input할 시 캐릭터 배정
Player_select = int(input('플레이어를 선택하시오. '))
if Player_select == 1:
    Character_name = Player('Warrior', 100, 40, 15, 20)
elif Player_select == 2:
    Character_name = Player('Assassin', 70, 40, 25, 15)
elif Player_select == 3:
    Character_name = Player('Wizard', 80, 60, 10, 30)
print(f'{Player_name} 님의 캐릭터는 {Character_name.name}입니다.')
                                                                # 여기서 바로 클래스를 지정해서 생성하면 좋을 것 같습니다.
                                                                # Character_name = Player('Warrior', 100, 40, 15, 20) 이런식으로 하시면
                                                                # 바로 클래스에서 인스턴스를 생성하면서 Character_name 변수에 넣을 수 있습니다.



# turn을 짝수 홀수로 하여 플레이어와 몬스터의 순번을 정함
turn = 1

# 플레이어 차례
print('fight!')
while True:
    if turn % 2 == 1:
        print('My turn!')
        print('몬스터에게 어떤 공격을 하시겠습니까?')
        player_action = int(input("1.일반공격 2.마법공격 ")) #int빠짐. player_action이라는 함수명이 위에 있어서 변수명으로 작동하지 않았음.
        if player_action == 1:
            Character_name.attack(m1) 
        elif player_action == 2:
            if Character_name.mp < 10:
                print('마나도 없는 게 공격을?')
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
    elif turn % 2 == 0:
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