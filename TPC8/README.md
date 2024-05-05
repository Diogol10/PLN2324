# PLN_2324
Análise de dois livros da série Harry Potter através da biblioteca Gensim

## TPC 8 - Tradução de conceitos de um livro médico

Objetivo - O objetivo deste script é aplicar técnicas de processamento de linguagem natural (PLN) para analisar dois livros da série Harry Potter em língua portuguesa. Ele utiliza a biblioteca Gensim para treinar modelos Word2Vec com os textos dos livros e explorar a similaridade entre palavras e fazer analogias.

## Desenvolvimento 

### Pré-processamento dos Textos

Os textos dos livros "Harry Potter e a Câmara Secreta" e "Harry Potter e a Pedra Filosofal" são carregados e pré-processados. Isso inclui a remoção de pontuação e a tokenização das linhas, passos estes que permitem uma melhor extração das palavras propriamente ditas.

### Treinamento dos Modelos Word2Vec

Dois modelos Word2Vec são treinados com os tokens dos textos dos livros. Um modelo (model) é treinado com os tokens do primeiro livro, enquanto o outro modelo (model2) é treinado com os tokens combinados de ambos os livros. Além disso, um terceiro modelo (model3) é treinado com parâmetros de vetor e épocas diferentes para comparação e experimentação da diferença que a alteração de parâmetros faz.

### Exploração dos Modelos

O script imprime a similaridade entre algumas palavras-chave dos livros, como "harry", "draco", "hermione" e "dumbledore", para cada modelo treinado. Além disso, uma analogia ("harry" é para "hermione" como "draco" é para") é realizada no modelo original.

## Conclusão

Este script oferece uma demonstração prática da aplicação de técnicas de Processamento de Linguagem Natural (PLN) na análise de textos literários. Ao treinar modelos Word2Vec com os textos dos livros "Harry Potter e a Câmara Secreta" e "Harry Potter e a Pedra Filosofal", pudemos explorar a similaridade entre palavras-chave e realizar analogias, revelando insights interessantes sobre os personagens e o universo da série.

Além disso, a comparação entre modelos treinados com diferentes parâmetros permite-nos entender como esses parâmetros afetam a qualidade dos vetores de palavras e, consequentemente, as relações semânticas capturadas pelos modelos.

Este projeto exemplifica não apenas o potencial do PLN na análise de textos literários, mas também destaca a importância da experimentação com diferentes configurações de modelos para obter resultados mais robustos e significativos.






