def bracket_stuff(expr):
  stack = []

  for brack in expr:
    if brack in ["(", "{", "["]: # for every bracket in the array 
      stack.append(brack) # append ittem brack
    else: 
      if not stack: # if not stack return false 
        return False 
    current_brack = stack.pop() #assign the pop function to current_brac 
    if current_brack = '(': 
      if brack != ")":
        return False# if you have an opening parens and its not a closing parens  return false
    if current_brack == '{':
      if brack != "}":
        return False# if you have an opening squigly brac and its not a closing sguigly brac return false
    if current_brack == '[':
      if brack != "]":
        return False# if you have an opening brac and its not a closing brac  return false

