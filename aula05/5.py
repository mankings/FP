def countDigits(s):
   digitCount = 0
   for char in s:
      if char.isdigit():
         digitCount += 1
   return digitCount