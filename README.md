# Brute Force Solution to NYT Digits

Do you want to check how your solution to [Digits](https://www.nytimes.com/games/digits) compares to all the possible solutions?

This Python script calculates all the possible solutions and returns
1) All solutions that achieve the target number, those with the smallest number of operations being shown first (if you are interested in finding the shortest solution(s))
2) How many valid solutions exist

It runs under a second on my computer, probably a few seconds on older hardware.

You just need Python 3.6+ and you're in business.
## Usage

Update the 'num_list' and 'target' variables with your number list and target value respectively

## Reading the output

The output is a list of operations, which look like this:
'19*25+5-3'

Read this as 
((19 * 25) + 5) - 3)

In other words, operations are right to left pair wise (do 19*25 first, then add 5 to the result, and substract 3 from that)
