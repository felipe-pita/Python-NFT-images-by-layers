"""
Gerador de NFT por camadas de PNG
author github.com/felipe-pita
"""
from PIL import Image
from os import walk
from itertools import product, chain
from progress.bar import Bar

layers = 4
print('{} camadas'.format(layers))

"""
Arquivos que devem ser ignorados.
ex: .DS_Store
"""
def ignoreOsFiles(filenames):
	exclude_prefixes = ('__', '.')
	return [filenames for filenames in filenames if not filenames.startswith(exclude_prefixes)]

"""
Passa pelas camadas e gera a lista de arquivos
"""
layerList = []

for layer in range(1, layers + 1):
	for (dirpath, dirnames, filenames) in walk('layers/' + str(layer)):
		filenames = ignoreOsFiles(filenames)
		layerList.append(list(map(lambda x: 'layers/' + str(layer) + '/' + x, filenames)))

print('Quantidade de arquivos: {}'.format(len(list(chain(*layerList)))))

"""
Gera todas as combinações possiveis
"""
unique_combinations = list(product(*layerList))
print('Combinacoes unicas {}'.format(len(unique_combinations)))

"""
Processa as imagens
"""
bar = Bar('Gerando imagens', max = len(unique_combinations))
for (index, unique_combination) in enumerate(unique_combinations):
	# Define a base
	background = Image.open(unique_combination[0])

	# Cola as layers
	for layer in unique_combination[1:]:
		foreground = Image.open(layer)
		background.paste(foreground, (0, 0), foreground)

	# Salva a imagem
	background.save('/Users/pro15/Desktop/NFT/layers/output/' + str(index + 1) + '.png')
	bar.next()

# Finaliza o processo
bar.finish()