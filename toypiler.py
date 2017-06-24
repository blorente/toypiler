from tokenizer import tokenize
import re

def parseTokenClasses(grammar):
	sectionEnd = grammar.find('}') + 1
	rawTokens = grammar[grammar.find('{') + 1:grammar.find('}')].strip().split(',')[:-1]
	tokens = {}
	for tok in rawTokens:
		ttype = tok[tok.find('<')+1:tok.find(':')]
		ttype = ttype.strip()
		tregex = tok[tok.find(':')+1:tok.find('>')]
		tregex = tregex.strip()
		tokens[ttype] = re.compile(tregex)
	return (tokens, sectionEnd)

def parseProductionRules(grammar):
	rulesSection = grammar[grammar.find('{')+1:grammar.find('}')].strip()
	print(rulesSection)
	rawsymbols = rulesSection[rulesSection.find('<Nonterminals:')+14:rulesSection.find('>')].split(',')
	nonterminals = []
	for symbol in rawsymbols:
		nonterminals.append(symbol.strip())
	print(nonterminals)

	rules = {}
	rulesSection = rulesSection[rulesSection.find('>')+1:].strip().split('>')[:-1]
	for rule in rulesSection:
		symbol = rule[rule.find('<')+1:rule.find(':')].strip()
		rawproductions = rule[rule.find(':')+1:].strip().split('|')	
		productions = []
		for prod in rawproductions:
			symbols = prod.strip().split(' ')
			productions.append(symbols)
		rules[symbol] = productions
	print(rules)
	return (nonterminals, rules)

def parseGrammar(grammarFile):
	file = open(grammarFile)
	source = file.read()
	(tokens, sectionEnd) = parseTokenClasses(source)
	source = source[sectionEnd:]
	rules = parseProductionRules(source)
	file.close()
	return (tokens, rules)

def main():
	code = "4 + 2 + 4+ 4+6 +7 ++8"
	(tokenClasses, rules) = parseGrammar("toypiler.grammar")
	tokens = tokenize(code, tokenClasses)

main()
