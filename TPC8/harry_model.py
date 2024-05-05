import re
from gensim.models import Word2Vec
from gensim.utils import tokenize

f1 = open("Harry_Potter_Camara_Secreta-br.txt", encoding="utf-8")
f2 = open("Harry_Potter_e_A_Pedra_Filosofal.txt", encoding="utf-8")


harry_text = f1.read()
harry_text2 = f2.read()

harry = harry_text + ' ' + harry_text2

linhas = harry_text.split("\n")
linhas2= harry.split("\n")


tokens = []
tokens2 =[]
for linha in linhas:
    re.sub(r'[-!?.,]',"", linha)     #remoçao de pontuacao para maior eficacia
    linha = list(tokenize(linha, lower=True))
    tokens.append(linha)

for linha in linhas2:
    linha = re.sub(r'[-!?.,]',"", linha)
    linha = list(tokenize(linha, lower=True))
    tokens2.append(linha)

model = Word2Vec(tokens, vector_size= 300, window= 5, min_count= 1, epochs= 20)
model3 = Word2Vec(tokens, vector_size= 150, window= 10, min_count= 1, epochs= 30) #igual ao model mas com parametros alterados
model2 = Word2Vec(tokens2, vector_size= 300, window= 5, min_count= 1, epochs= 20)

print('---------------model original------------')
print('-------------------harry--------------------')
print(model.wv.most_similar("harry"))
print('-------------------draco--------------------')
print(model.wv.most_similar("draco"))
print('------------------hermione--------------------')
print(model.wv.most_similar("hermione"))
print('-----------------dumbledore--------------------')
print(model.wv.most_similar("dumbledore"))
print('-------------model com parametros alterados-------------')
print('-------------------harry--------------------')
print(model3.wv.most_similar("harry"))
print('-------------------draco--------------------')
print(model3.wv.most_similar("draco"))
print('------------------hermione--------------------')
print(model3.wv.most_similar("hermione"))
print('-----------------dumbledore--------------------')
print(model3.wv.most_similar("dumbledore"))
print('-----------Fusão de ambos os textos-------------')
print('-------------------harry--------------------')
print(model2.wv.most_similar("harry"))
print('-------------------draco--------------------')
print(model2.wv.most_similar("draco"))
print('------------------hermione--------------------')
print(model2.wv.most_similar("hermione"))
print('-----------------dumbledore--------------------')
print(model2.wv.most_similar("dumbledore"))
print('-----------------Analogia:--------------------')
print(model.wv.most_similar(positive=["harry", "hermione"], negative=["draco"]))






"""
[['this', 'is', 'the', 'first', 'sentence', 'for', 'word2vec'],
			['this', 'is', 'the', 'second', 'sentence'],
			['yet', 'another', 'sentence'],
			['one', 'more', 'sentence'],
			['and', 'the', 'final', 'sentence']]
"""


