# python3

import sys

#text = '[](0))'
#text = '[](()'
#text = '{}}'
#text = '())'
#text = '{}[]'
text = 'foo(bar)'

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def isMatch(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False
        
        
def isBalanced(text):
	"""
	If the code in 'text' uses brackets correctly, output “Success”. 
	Otherwise, output the 1-based index of the first unmatched closing bracket, 
	and if there are no unmatched closing brackets, 
	output the 1-based index of the first unmatched opening bracket.
	"""
	opening_brackets_stack = []

	balanced = True

	for i, next in enumerate(text):
		if next == '(' or next == '[' or next == '{':
			opening_brackets_stack.append(Bracket(next, i))
		
		if next == ')' or next == ']' or next == '}':
			new_closing_bracket = Bracket(next,i)	
		
			if len(opening_brackets_stack) == 0:
				balanced = False
				return(new_closing_bracket.position + 1)
			
			else:
				top_bracket = opening_brackets_stack.pop()	
				if not top_bracket.isMatch(new_closing_bracket.bracket_type):
					balanced = False
					return(new_closing_bracket.position + 1)
						
				elif top_bracket.isMatch(new_closing_bracket.bracket_type):
					balanced = True
					
			

	if len(opening_brackets_stack) != 0:
		balanced = False
		top_bracket = opening_brackets_stack.pop()
		return(top_bracket.position + 1)
	
	elif balanced:
		success = 'Success'
		return(success)
		
print(isBalanced(text))
	
