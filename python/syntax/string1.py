print("문자열")
print('Hello World') 
print("Hello World")
print("Hell'o' World")
print('Hell"o" World')
#escape 문자
print('Hell"o" \'W\'orld')

# '' "" 둘다 똑같음. 근데 쌍이 맞아야됨
# ''를 문자로 쓰고 싶으면 "" 안에서 쓰고
# ""를 문자로 쓰고 싶으면 '' 안에서 씀
# \ escape 문자를 쓸 수 있음

print("\n줄바꿈")
# 줄바꿈
print("H\ne\nl\nl\no\n")

#dockstring
#문자열을 여러줄에 걸쳐서 쓸 수 있음
#개행 기준으로 알아서 개행('\n')을 넣어 줄력함
print('''docstring
h
e
l
l
o''')