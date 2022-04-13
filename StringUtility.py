class StringUtility:
  
  def __init__ (self,string):
    self.string=string

  def __str__(self):
    return str(self.string)
##PartB##
  def vowels(self):
    vowels= "aeiouAEIOU"
    result=0
    for i in self.string:
      if i in vowels:
        result += 1
        if (result>=5):
          return ("many")
    return str(result)
    
  def bothEnds(self):
    size = len(self.string)
    if size <= 2:
      return""
    result = self.string[0:2] + self.string[-2:]
    for i in self.string:
      return str(result)
  
  def fixStart(self):

    size = len(self.string)
    for i in self.string:
      capital = self.string[0]
      for i in capital:
        word = self.string[1:].replace(capital, "*")
        result = capital + word
        return str(result)
    if size <= 1:
      return ""

      
  def asciiSum(self):
    result=0
    for i in self.string:
      result += ord(i)
    return result

  def cipher(self):
    cipher = ""
    for i in self.string:
      if i.isalpha():
        if i.isupper():
          alphabet = (ord(i) - 65 + len(self.string)) % (26)
          alphabet += 65
        if i.islower():
          alphabet = (ord(i) - 97 + len(self.string)) % (26)
          alphabet += 97
        letter = chr(alphabet)
      else:
        letter = i
      cipher += letter
    return cipher
  