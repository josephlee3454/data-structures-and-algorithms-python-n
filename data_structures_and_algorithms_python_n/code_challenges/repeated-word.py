
class RepeatWord:
  def split(string, delimiters=' \t\n'):
      result = []
      word = ''
      for c in string:
          if c not in delimiters:
              word += c
          elif word:
              result.append(word)
              word = ''

      if word:
          
          result.append(word)
      
      print(result)
      return result


  def check(result):
    res = [] 
    checker = []
    for i in result: 
      if i not in res: 
        res.append(i) 
      else:
        checker.append(i)
        print(checker[0])

    
  
x = RepeatWord.split("he lo no my home y h a x no")
y = RepeatWord.check(x)
