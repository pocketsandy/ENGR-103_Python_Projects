def fibonacci_seq (fib):

    fib_1 = 1
    fib_2 = 1

    print (fib_1)
    print (fib_2)

    for i in range (2,fib):
        fib_3 = fib_1 + fib_2
        fib_1 = fib_2
        fib_2 = fib_3


        print(fib_3)

term = fibonacci_seq (17)