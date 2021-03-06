class SpellChecker:
	def __init__(self):
		self.words = []
	def load_words(self,file_name):
		self.words = open(file_name).readlines()
		self.words = map(lambda x: x.strip(), self.words)
		return self.words
	
	def check_word(self,word):
		return word.strip('.').lower() in self.words
	def check_words(self, sentence):
		words_to_check = sentence.split(' ')
		for word in words_to_check:
			if not self.check_word(word):
				print('Word is misspelt : ' + word)
				return False
		return True
		
if __name__ =='main':
	spell_check = SpellChecker()
	spell_check.load_words("spell.words")
	print spell_check.check_word('zygotic')
	print spell_check.check_word('mistasdas')
	print spell_check.check_words('zygotic mistasdas elementary')