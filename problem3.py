#! python3

"""
##### Problem 3
Have the user enter an integer that is smaller than 10
Find the sum of the series:
1 + 11 + 111 + 1111 + ....
for the n terms, where the nth term has n number of 1's

input:
int number that is smaller than 10

output:
the sum of the series is xxxx

example:
enter a number: 4
the sum of the series is 1234
"""

integer=(input("Enter a number")).strip()
integer=int(integer)
series=1
print("the sum of the series is",end=' ')
for i in range(1,integer+1):
    print(series,end='')
    series=series+1
