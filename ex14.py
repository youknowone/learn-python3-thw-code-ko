### @export "setup"
import fake_input
input, input = fake_input.create(
    ['네', "샌프란시스코", 'Tandy 1000'])

### @export "code"
from sys import argv

스크립트, 사용자_이름 = argv
프롬프트 = '> '

print(f"안녕 {사용자_이름}, 나는 {스크립트} 스크립트야.")
print("몇 가지 질문을 할게.")
print(f"{사용자_이름}, 나를 좋아해?")
좋아 = input(프롬프트)

print(f"{사용자_이름}, 어디에 살아?")
살아 = input(프롬프트)

print("무슨 컴퓨터를 갖고 있어?")
컴퓨터 = input(프롬프트)

print(f"""
좋아, 나를 좋아하냐는 질문에는 {좋아}.
{살아}에 살아.  어딘지는 모르겠지만.
그리고 {컴퓨터} 컴퓨터를 가졌어.  근사한걸.
""")
