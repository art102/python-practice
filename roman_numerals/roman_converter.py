digit = int(input())

numbers = {
    1: 'I',
    2: 'II',
    3: 'III',
    4: 'IV',
    5: 'V',
    6: 'VI',
    7: 'VII',
    8: 'VIII',
    9: 'IX',
    10: 'X'
}

if digit not in range(1,11):
    print("error")
else:
    print(numbers[digit])
