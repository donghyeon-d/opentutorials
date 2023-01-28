#python string formating
#positional formating
    #위치기만
print('one {}. two {}. three {}.'.format('apple', 'MS', 'dongchoi'))

#Named placeholder
    #{}의 지점에 어떤 값이 나올지 대략 알 수 있음
print('one {name}. two {age}. three {nickname}.'.format(name='dong', age=20, nickname='dongchoi'))

#Named placeholder
    #{}안에서 자료형을 지정해줄 수 있음 :d로하면 digit -> 컴파일 에러뜸
print('one {name}. two {age:d}. three {nickname}.'.format(name='dong', age=20a, nickname='dongchoi'))