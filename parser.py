class Parser:
	"""docstring for Parser"""
	def __init__(self, terminals, rules):
		super(Parser, self).__init__()
		self.tokens = []
		self.terminals = terminals
		self.rules = rules[1]
		print(self.rules)
		self.tokIndex = 0
		self.ast = []

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
		node = []
		for symbol in rule:
			expr = []
			if self.isTerminal(symbol):
				print('Terminal symbol: '+symbol+ ' in rule ' + str(rule) + ', index: ' + str(self.tokIndex))
				expr = self.match(symbol)
			else:
				print('Nonterminal symbol ' + str(symbol) + ' in rule ' + str(rule) + ', index: ' + str(self.tokIndex))
				goodalternative = False
				alternatives = self.rules[symbol]
				for alternative in alternatives:
					tokIndex = self.tokIndex		
					print('	Alternative: ' + str(alternative))
					expr = self.parseRule(alternative)
					goodalternative = len(expr) > 0
					if not goodalternative:
						self.tokIndex = tokIndex

			if len(expr) == 0:
				return []
			else:
				node.append(expr)
		
		print('Node after parse %s' % str(node))
		return node

	def isTerminal(self, symbol):
		for t in self.terminals:
			if t == symbol: return True
		if symbol == 'EPS': return True
		return False
	
	def match(self, token):
		if self.tokIndex >= len(self.tokens): return []
		if (self.tokens[self.tokIndex][0] == token) or token == 'EPS':
			print('Match token ' + str(self.tokens[self.tokIndex]) + ' at index ' + str(self.tokIndex))
			self.tokIndex += 1
			return [token]
		else:
			return []