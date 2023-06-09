import datetime

# Calculate current age from the birth year
def current_age(birth_year):
    current_year = datetime.datetime.now().year
    age = current_year - birth_year
    return age

# Find the next prime number
def next_prime(num):
    if num < 0:
        print('Can\'t have negative age')
        return

    prime_list = [2]
    i = 2
    while prime_list[-1] <= num:
        prime = True
        for j in prime_list:
            if i % j == 0:
                prime = False
                break
        if prime:
            prime_list.append(i)
        i += 1

    return prime_list[-1]


try:
    yr = int(input("Please enter birth year (eg. 1990): "))
    age = current_age(yr)
    prime_age = next_prime(age)
    print(prime_age + yr)  # Show the sum of birth year and the next prime age
# Show error when input is not a valid interger
except ValueError:
    print("Please input the right format")
