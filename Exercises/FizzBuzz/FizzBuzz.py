#FizzBuzz

for index in range(1, 101):
    if index % 3 == 0:
        if index % 5 == 0:
            print ('FizzBuzz')
            continue
        print('Fizz')
    elif index % 5 == 0:
        print('Buzz')
    elif index % 7 == 0:
        print('Bang')
    else:
        print(index)