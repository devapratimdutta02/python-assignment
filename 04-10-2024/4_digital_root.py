def digital_root(num):
    while num>=10:
        digit_sum = 0
        while num!=0:
            rem = num % 10
            digit_sum += rem
            num //= 10
        num=digit_sum
    return num

n=int(input("Enter a number: "))
res = digital_root(n)
print("Digital root of the number is: ",res)