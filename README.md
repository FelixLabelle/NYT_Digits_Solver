# Brute Force Solution to NYT Digits

Do you want to check how your solution to [Digits](https://www.nytimes.com/games/digits) compares to all the possible combinations?

This Python script calculates all the possible combinations and returns
1) All number operations combinations that achieve a number, shortest first
2) How many valid combinations exist

It runs under a second on my computer, probably a few seconds on older hardware.

You just need Python 3.6+ and you're in business.

## Reading the output

The output is a list of operations, which look like this:
'19*25+5-3'

Read this as 
((19 * 25) + 5) - 3)

In other words, operations are right to left pair wise (do 19*25 first, then add 5 to the result, and substract 3 from that)