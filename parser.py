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
		result = self.parseRule(self.rules['START'])
		print('======================')

	def parseRule(self, rule):
		for symbol in rule:
			if self.isTerminal(symbol):
				return self.match(symbol)
			else:
				matched = False
				alternatives = self.rules[symbol]
				print(alternatives)
				for part in self.rules[symbol]:
					if not matched:
						matched = self.parseRule(self.rules[symbol])
				return matched

	def isTerminal(self, symbol):
		for t in self.terminals:
			if t == symbol: return True
		return False
	
	def match(self, token):
		if self.tokens[self.tokIndex] == token:
			self.tokIndex += 1
			return True 