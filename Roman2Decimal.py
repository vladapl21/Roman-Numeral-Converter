class Solution(object):
  def romanToInt(self, s):

      total = 0
      dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
      for i in range((len(s)-1), -1, -1):
          if i == (len(s)-1) or dict[s[i]] >= dict[s[i+1]]: 
          # If rightmost character or character is larger than the one to the right of it
              total += dict[s[i]]
          else:
          # If left character is smaller than right, it should be subtracted from total
              total -= dict[s[i]]

      return total