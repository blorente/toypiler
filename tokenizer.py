import re
def tokenize(source, tokDefs):
	print("TOKENIZER ===============")
	print(tokDefs)	
	print(source)
	tokens = []
	source = source.replace(' ', '')
	while len(source) != 0:
		matched = False
		print(source)
		for tok in tokDefs:	
			if not matched:
				match = tokDefs[tok].match(source)
				if match:
					lexeme = source[:match.end()]
					tokens.append((tok, lexeme))
					source = source[match.end():]
					matched = True	
	print("DONE: " + str(tokens))
	print("=============================")
	return tokens		
