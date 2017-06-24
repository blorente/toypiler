class Parser:
	"""docstring for Parser"""
	def __init__(self, terminals, rules):
		super(Parser, self).__init__()
		self.tokens = []
		self.terminals = terminals
		self.rules = rules[1]
		print(self.rules)
		self.tokIndex = 0

	def parse(self, tokens):
		print('PARSER ===============')
		self.tokens = tokens
		result = False
		tokIndex = self.tokIndex
		for rule in self.rules['START']:
			if not result:
				self.tokIndex = tokIndex
				result = self.parseRule(rule)
				print('Finished trial with rule '+str(rule)+', result: '+str(result))
		print('RESULT: '+ str(result))
		print('======================')

	def parseRule(self, rule):
		matched = False
		for symbol in rule:
			if self.isTerminal(symbol):
				print('Terminal symbol: '+symbol+ ' in rule ' + str(rule) + ', index: ' + str(self.tokIndex))
				matched = self.match(symbol)
			else:
				print('Nonterminal symbol ' + str(symbol) + ' in rule ' + str(rule) + ', index: ' + str(self.tokIndex))
				matchpart = False
				alternatives = self.rules[symbol]
				for alternative in alternatives:
					tokIndex = self.tokIndex		
					print('		Alternative: ' + str(alternative))
					matchpart = self.parseRule(alternative)
					if not matchpart:
						self.tokIndex = tokIndex
				matched = matchpart

			if not matched:
				break
		
		return matched

	def isTerminal(self, symbol):
		for t in self.terminals:
			if t == symbol: return True
		if symbol == 'EPS': return True
		return False
	
	def match(self, token):
		if self.tokIndex >= len(self.tokens): return False
		if (self.tokens[self.tokIndex][0] == token) or token == 'EPS':
			print('Match token ' + str(self.tokens[self.tokIndex]) + ' at index ' + str(self.tokIndex))
			self.tokIndex += 1
			return True
		else:
			return False