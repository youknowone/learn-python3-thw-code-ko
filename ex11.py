### @export "fake"
import fake_input
input, input = fake_input.create(['38', '188cm', '82kg'])

### @export "code"
print("몇 살이죠?", end=' ')
나이 = input()
print("키는 얼마죠?", end=' ')
키 = input()
print("몸무게는 얼마죠?", end=' ')
몸무게 = input()

print(f"네, 나이는 {나이}살, 키는 {키}, 몸무게는 {몸무게}이네요.")

# see this is nessessary or not
# print "뜬금없지만, 태양의 각지름은 %r입니다." % '''32'10"'''