from tokenizer import tokenize
import re

def parseGrammar(grammarFile):
	file = open(grammarFile)
	source = file.read()
	print(source)
	#source.find(r"\s}")
	rawTokens = source[source.find('{') + 1:source.find('}')].strip().split(',')[:-1]
	tokens = {}
	for tok in rawTokens:
		ttype = tok[tok.find('<')+1:tok.find(':')]
		ttype = ttype.strip()
		tregex = tok[tok.find(':')+1:tok.find('>')]
		tregex = tregex.strip()
		tokens[ttype] = re.compile(tregex)

	print(tokens)
	file.close()
	return tokens

def main():
	code = "4 + 2 + 4+ 4+6 +7 ++8"
	grammar = parseGrammar("toypiler.grammar")
	tokens = tokenize(code, grammar)
	print(tokens)

main()
