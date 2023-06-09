 #!/usr/bin/python
"""
Python  Functions
"""

"""
Question 1: 

Finish the function valid_brackets() to solve the following question.

Given a string s containing just the characters '(', ')' determine if the input string is valid.
An input string is valid if:
1.All brackets are closed in the correct order.
2.Open bracket must be placed before close bracket.

Example 1:
 Input: s = "()"
 Output: True
Example 2:
 Input: s = "("
 Output: False
Example 3:
 Input: s = "(()"
 Output: False
Example 4:
 Input: s = ")("
 Output: False
Example 5:
 Input: s = "()()"
 Output: True
Example 6:
 Input: s = "(()())"
 Output: True
Example 7:
 Input: s = ""
 Output: True
"""
def valid_brackets(s):
    if len(s)==0:
        return True
    if s[0]==")" or s.count(")")!= s.count("(") or s[-1] != ")":
        return False
    return True



"""
Question 2:

Finish the function is_prime() to solve the following question.

Given a number n determine if the number string is Prime number.

Example 1:
    Input: n = 1
    Output: False
    
Example 2:
    Input: n = 2
    Output: True
    
Example 3:
    Input: n = 6
    Output: False

Example 4:
    Input: n = 97
    Output: True
    
Example 5:
    Input: n = 9973
    Output: True

"""
def is_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2,n):
            if n%i ==0:
                return False
    return True



"""
Question 3:

Finish the function GCD() to solve the following question.
 
Find Greatest Common Divisor of two positive integer a and b. 

Example 1:
    Input: a = 6 , b = 12
    Output: 6
    
Example 2:
    Input: a = 9 , b = 12
    Output: 3

Example 3:
    Input: a = 42 , b = 12
    Output: 6
    
Example 4:
    Input: a = 97 , b = 7
    Output: 1
"""


def GCD(a, b):
    if a%b == 0:
        return b
    if b%a == 0:
        return a
    else:
        for i in range (1,int(a/2 + 1)):
            if a%i==0 and b%i==0:
                output=i
        return output

