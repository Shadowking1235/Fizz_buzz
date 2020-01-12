def Fizz_Buzz():
    for i in range(0, 101):
        if i % 2 == 0:
            print('Fizz')

        elif i % 4 == 0:
            print('Buzz')


        elif i % 3 == 0 and i % 5 == 0:
            print('Fizz BuZZ')
    else:
        print(i)


Fizz_Buzz()
