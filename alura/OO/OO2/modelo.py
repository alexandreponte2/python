class Filme:
	def __init__(self, nome, ano, duracao):
		self.nome = nome
		self.ano = ano
		self.duracao = duracao


class Serie:
	def __init__(self, nome, ano, temporadas):
		self.nome = nome
		self.ano = ano
		self.temporadas = temporadas



vingadores = Filme('vingadores - guerra infinita', 2018, 160)

print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duracao {vingadores.duracao}')





fringe = Serie('Fringe', 2008, 5)

print(f'Nome: {fringe.nome} - Ano: {fringe.ano} - Temporadas {fringe.temporadas}')
