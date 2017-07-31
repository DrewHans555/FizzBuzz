"""

My simple solution to Imran Ghory's FizzBuzz challenge.

Challenge:
Write a program that prints the numbers from 1 to 100. But for multiples of three
print “Fizz” instead of the number and for the multiples of five print “Buzz”. For
numbers which are multiples of both three and five print “FizzBuzz”.

Source:
https://imranontech.com/2007/01/24/using-fizzbuzz-to-find-developers-who-grok-coding/

"""

for i in range(100):
    output = ""

    if (i+1) % 3 == 0:
        output += "Fizz"
    if (i+1) % 5 == 0:
        output += "Buzz"
    if output == "":
        output = i+1

    print(output)
