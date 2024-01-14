#Leap
"""Given a year, report if it is a leap year.

The tricky thing here is that a leap year in the Gregorian calendar occurs:

on every year that is evenly divisible by 4
  except every year that is evenly divisible by 100
    unless the year is also evenly divisible by 400
For example, 1997 is not a leap year, but 1996 is. 1900 is not a leap year, but 2000 is."""

def leap_year(year):
    return year%4 == 0 and not(year%100 == 0 and year%400 != 0)

#Triangle
"""Determine if a triangle is equilateral, isosceles, or scalene.

An equilateral triangle has all three sides the same length.
An isosceles triangle has at least two sides the same length. (It is sometimes specified as having exactly two sides the same length, but for the purposes of this exercise we'll say at least two.)
A scalene triangle has all sides of different lengths."""

def equilateral(sides):
    return len(set(sides)) == 1 and 0 not in set(sides)

def isosceles(sides):
    return len(set(sides)) <= 2 and (min(sides)*2) >= max(sides)

def scalene(sides):
    return sum(sorted(sides)[:-1]) >= max(sides) and len(set(sides)) == 3

#Grains
"""Calculate the number of grains of wheat on a chessboard given that the number on each square doubles.

There once was a wise servant who saved the life of a prince. The king promised to pay whatever the servant could dream up. Knowing that the king loved chess, the servant told the king he would like to have grains of wheat. One grain on the first square of a chess board, with the number of grains doubling on each successive square.

There are 64 squares on a chessboard (where square 1 has one grain, square 2 has two grains, and so on).

Write code that shows:

how many grains were on a given square, and
the total number of grains on the chessboard"""

def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2**(number-1)

def total():
    return 2**64-1

#Armstrong sum
"""An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.

For example:

9 is an Armstrong number, because 9 = 9^1 = 9
10 is not an Armstrong number, because 10 != 1^2 + 0^2 = 1
153 is an Armstrong number, because: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153"""

def is_armstrong_number(number):
    digits = str(number)
    return number == sum(int(digit)**len(digits) for digit in digits)

#Collatz Conjecture
"""The Collatz Conjecture or 3x+1 problem can be summarized as follows:

Take any positive integer n. If n is even, divide n by 2 to get n / 2. If n is odd, multiply n by 3 and add 1 to get 3n + 1. Repeat the process indefinitely. The conjecture states that no matter which number you start with, you will always reach 1 eventually.

Given a number n, return the number of steps required to reach 1."""

def steps(number):
    count = 0
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    while number != 1:
            if number%2 == 0:
                number //= 2
            else:
                number = number*3+1
            count += 1
    return count

#Bob
"""Your task is to determine what Bob will reply to someone when they say something to him or ask him a question.

Bob only ever answers one of five things:

"Sure." This is his response if you ask him a question, such as "How are you?" The convention used for questions is that it ends with a question mark.
"Whoa, chill out!" This is his answer if you YELL AT HIM. The convention used for yelling is ALL CAPITAL LETTERS.
"Calm down, I know what I'm doing!" This is what he says if you yell a question at him.
"Fine. Be that way!" This is how he responds to silence. The convention used for silence is nothing, or various combinations of whitespace characters.
"Whatever." This is what he answers to anything else."""

def response(hey_bob):
    if hey_bob.strip() == "":
        return "Fine. Be that way!"
    if hey_bob.strip()[-1] == "?":
        if hey_bob.isupper():
            return "Calm down, I know what I'm doing!"
        return "Sure."
    if hey_bob.isupper():
        return "Whoa, chill out!"
    return "Whatever."

#Raindrops
"""Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors. A factor is a number that evenly divides into another number, leaving no remainder. The simplest way to test if one number is a factor of another is to use the modulo operation.

The rules of raindrops are that if a given number:

has 3 as a factor, add 'Pling' to the result.
has 5 as a factor, add 'Plang' to the result.
has 7 as a factor, add 'Plong' to the result.
does not have any of 3, 5, or 7 as a factor, the result should be the digits of the number."""

def convert(number):
    conversion = [(3, "Pling"), (5, "Plang"), (7,"Plong")]
    result = ""
    for value, word in conversion:
        if number%value == 0:
            result += word
    return result or str(number)

#Darts
"""Write a function that returns the earned points in a single toss of a Darts game.
In our particular instance of the game, the target rewards 4 different amounts of points, depending on where the dart lands:

If the dart lands outside the target, player earns no points (0 points).
If the dart lands in the outer circle of the target, player earns 1 point.
If the dart lands in the middle circle of the target, player earns 5 points.
If the dart lands in the inner circle of the target, player earns 10 points."""

def score(x, y):
    scores = [(0.8, 10), (3.6, 5), (7.1, 1)]
    avg = (abs(x)+abs(y))/2
    for position, points in scores:
        if avg < position:
            return points
    return 0
        
#Perfect Numbers
"""Determine if a number is perfect, abundant, or deficient based on Nicomachus' (60 - 120 CE) classification scheme for positive integers.

Perfect
A number is perfect when it equals its aliquot sum. For example:
6 is a perfect number because 1 + 2 + 3 = 6

Abundant
A number is abundant when it is less than its aliquot sum. For example:
12 is an abundant number because 1 + 2 + 3 + 4 + 6 = 16

Deficient
A number is deficient when it is greater than its aliquot sum. For example:
8 is a deficient number because 1 + 2 + 4 = 7"""

def classify(number):
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    sum = 0
    for div in range(1, number):
        if number%div == 0:
            sum += div
    if sum == number:
        return "perfect"
    if sum > number:
        return "abundant"
    return "deficient"

#Square Root
"""Given a natural radicand, return its square root.

Note that the term "radicand" refers to the number for which the root is to be determined. That is, it is the number under the root symbol.

Python offers a wealth of mathematical functions in the form of the math module and built-ins such as pow() and sum(). However, we'd like you to consider the challenge of solving this exercise without those built-ins or modules."""

def square_root(number):
    result, value = 0, 0
    while value < number:
        result += 1
        value = result*result
    return result

#Pig Latin
"""Implement a program that translates from English to Pig Latin.

Rule 1: If a word begins with a vowel sound, add an "ay" sound to the end of the word. Please note that "xr" and "yt" at the beginning of a word make vowel sounds (e.g. "xray" -> "xrayay", "yttria" -> "yttriaay").
Rule 2: If a word begins with a consonant sound, move it to the end of the word and then add an "ay" sound to the end of the word. Consonant sounds can be made up of multiple consonants, such as the "ch" in "chair" or "st" in "stand" (e.g. "chair" -> "airchay").
Rule 3: If a word starts with a consonant sound followed by "qu", move it to the end of the word, and then add an "ay" sound to the end of the word (e.g. "square" -> "aresquay").
Rule 4: If a word contains a "y" after a consonant cluster or as the second letter in a two letter word it makes a vowel sound (e.g. "rhythm" -> "ythmrhay", "my" -> "ymay")."""

def translate(text):
    text = text.split()
    new_text = ""
    for word in text:
        if word[0] in {"a", "e", "i", "o", "u"} or word[0:2] in {"xr", "yt"}:
            new_text += word+"ay"+" "
        elif word[0:3] in {"squ", "thr", "sch"}:
            new_text += word[3:]+word[0:3]+"ay"+" "
        elif word[0:2] in {"ch", "st", "qu", "th", "rh"}:
            new_text += word[2:]+word[0:2]+"ay"+" "
        else:
            new_text += word[1:]+word[0:1]+"ay"+" "
    return new_text.strip()

#Matching Brackets
"""Given a string containing brackets [], braces {}, parentheses (), or any combination thereof, verify that any and all pairs are matched and nested correctly. The string may also contain other characters, which for the purposes of this exercise should be ignored.

Without using RegEx"""

def is_paired(input_string):
    brackets = {"}": "{", ")": "(", "]": "["}
    open_brackets = ["(", "{", "["]
    open_pile = []
    for char in input_string:
        if char in open_brackets:
            open_pile.append(char)
        elif char in brackets:
            if not open_pile or brackets[char] != open_pile.pop():
                return False
    return not open_pile

#Sublist
"""Given any two lists A and B, determine if:

List A is equal to list B; or
List A contains list B (A is a superlist of B); or
List A is contained by list B (A is a sublist of B); or
None of the above is true, thus lists A and B are unequal"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 0

def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    if max(len(list_one), len(list_two)) == len(list_one):
        for element in range(len(list_one)-(len(list_two)-1)):
            if list_one[element:len(list_two)+element] == list_two:
                return SUPERLIST
    if max(len(list_one), len(list_two)) == len(list_two):
        for element in range(len(list_two)-(len(list_one)-1)):
            if list_two[element:len(list_one)+element] == list_one:
                return SUBLIST
    return UNEQUAL

#All Your Base
"""Convert a number, represented as a sequence of digits in one base, to any other base.

Implement general base conversion. Given a number in base a, represented as a sequence of digits, convert it to base b.

Note
Try to implement the conversion yourself. Do not use something else to perform the conversion for you."""

def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if digits and check_digits(digits, input_base):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if input_base == output_base:
        return digits
    digits = base10(digits, input_base)
    if output_base != 10:
        digits = n_base(digits, output_base)
    return list(map(int, str(digits))) if isinstance(digits, int) else digits

def check_digits(digits, input_base):
    sorted = digits.copy()
    sorted.sort()
    return sorted[0] < 0 or sorted[-1] >= input_base

def n_base(number, base):
    binary = []
    while number > 0:
        residue = number%base
        binary.insert(0, residue)
        number //= base
    return binary or [0]

def base10(digits, base):
    digits_len = len(digits)
    number = 0
    for item in digits:
        digits_len -= 1
        number += item*(base**digits_len)
    return number