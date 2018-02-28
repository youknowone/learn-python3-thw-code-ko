# 도이름에서 약자로의 매핑(mapping)을 만듭니다
states = {
    '충청북도': '충북',
    '경상북도': '경북',
    '전라남도': '전남',
    '경기도': '경기',
    '강원도': '강원'
}

# 기본적인 도와 도시 묶음을 만듭니다.
cities = {
    '전남': '광주',
    '강원': '원주',
    '경북': '대구'
}

# 도시 몇 개를 더 씁니다
cities['경기'] = '인천'
cities['충북'] = '충주'

# 도시를 출력합니다
print('-' * 10)
print("경기도에는 ", cities['경기'])
print("충청북도에는 ", cities['충북'])

# 도를 출력합니다
print('-' * 10)
print("강원도의 약자는 ", states['강원도'])
print("경상북도의 약자는 ", states['경상북도'])

# 도 이름 사전과 도시 사전을 차례로 써 봅니다
print('-' * 10)
print("강원도에는 ", cities[states['강원도']])
print("경상북도에는 ", cities[states['경상북도']])

# 도 이름 약자를 모두 출력해 봅니다
print('-' * 10)
for state, abbrev in states.items():
    print(f"{state}의 줄임말은 {abbrev}입니다")

# 도에 있는 도시를 모두 출력해 봅니다
print('-' * 10)
for abbrev, city in cities.items():
    print(f"{abbrev}에는 {city}시가 있습니다")

# 둘을 한번에 해봅니다
print('-' * 10)
for state, abbrev in states.items():
    print(f"{state}의 줄임말은 {abbrev}이고")
    print(f"거기엔 {cities[abbrev]}시가 있습니다")

print('-' * 10)
# 없을 수도 있는 도 이름 약자를 안전하게 받아옵니다
state = states.get('제주도', None)

if not state:
    print("제주도는 없습니다.")

# 도시를 기본 값을 넣고 가져옵니다
city = cities.get('제주', '없습니다')
print(f"'제주'의 도시는 {city}")

