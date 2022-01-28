def collatz(number):
    try:
        while True:
            if int(number) == 1:
                break
            elif int(number) % 2 == 0:
                number = int(number) // 2
                print(number)
            elif int(number) % 2 == 1:
                number = 3 * int(number) + 1
                print(number)
    except ValueError:
        print('Error: You must enter a number.')

print('Enter number:')
number = input()
collatz(number)