import sys


def get_primes(lower, upper):
    print("Prime numbers between", lower, "and", upper, "are:")
    primes = []
    for num in range(lower, upper + 1):
        # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)

    return primes


if __name__ == "__main__":
    lower = int(sys.argv[1])
    upper = int(sys.argv[2])
    print(get_primes(lower, upper))
