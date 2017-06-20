'''

Given a string, find its first non-repeating character
Given a string, find the first non-repeating character in it. 
For example, if the input string is “GeeksforGeeks”, then output should be ‘f’ and if input string is “GeeksQuiz”,
then output should be ‘G’.

We can use string characters as index and build a count array. Following is the algorithm.

1) Scan the string from left to right and construct the count array.
2) Again, scan the string from left to right and check for count of each
 character, if you find an element who's count is 1, return it.
Example:

Input string: str = geeksforgeeks
1: Construct character count array from the input string.
   ....
  count['e'] = 4
  count['f'] = 1
  count['g'] = 2
  count['k'] = 2
  ……
2: Get the first character who's count is 1 ('f').

'''
NB_OF_CHAR = 256
def getCharCountArray(string):
    count = [0]* NB_OF_CHAR 
    for i in string:
        count[ord(i)] +=1
    return count
    
def firstNonRepeating(string):
    count = getCharCountArray(string)
    index= -1
    k=0
    for i in string:
        if count[ord(i)] == 1:
            index =k
            break
        k+=1
    return index
   
string = "geeksforgeeks"
index=firstNonRepeating(string)

print (string[index])
