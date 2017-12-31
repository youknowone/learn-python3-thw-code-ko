
# argv를 쓴 스크립트와 비슷한 함수
def 둘_출력(*args):
    실행인자1, 실행인자2 = args
    print(f"실행인자1: {실행인자1}, 실행인자2: {실행인자2}")

# 좋아요. 사실 *args는 필요가 없습니다. 그냥 이렇게 하죠.
def 둘_출력_다르게(실행인자1, 실행인자2):
    print(f"실행인자1: {실행인자1}, 실행인자2: {실행인자2}")

# 이 함수는 실행인자를 하나만 받습니다
def 하나_출력(실행인자1):
    print(f"실행인자1: {실행인자1}")

# 이 함수는 실행인자를 하나도 받지 않습니다
def 안_출력():
    print("아무것도 받지 않음")


둘_출력('제드', '쇼')
둘_출력_다르게('제드', '쇼')
하나_출력('하나!')
안_출력()
