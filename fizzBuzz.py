def fizzbuzz(x):
    fizz = (x % 3 == 0)
    buzz = (x % 5 == 0)

    if fizz and buzz:
        return "FizzBuzz"
    elif buzz:
        return "Buzz"
    elif fizz:
        return "Fizz"
    else:
        return x

for num in range(1, 101):
    print(fizzbuzz(num))
