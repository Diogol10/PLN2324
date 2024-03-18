# PLN_2324
Repositório Processamento de Linguagem Natural em Engenharia Biomédica

## TPC 5 - Tradução de conceitos de um livro médico

Objetivo - O objetico era apresentar o livro de conceitos médicos. Os conceitos têm de ter uma descrição em português e o seu nome em inglês.

A tarefa consiste em desenvolver o código para a tradução de certos conceitos médicos que estão presentes num livro médico. Assim, elaborei um código que efetuasse a tradução automática dos termos presentes no ficheiro json. Posteriormente, estes vão ser dispostos no livro bem como a descrição em português. 

### Procedimento

O código foi desenvolvido para processar um documento JSON com termos médicos. Assim, existe uma série de questõs que devem ser abordadas para que o script seja melhor compreendido:

1. Importação de Bibliotecas: O script requer a importação de diversas bibliotecas para funcionar corretamente. Isso inclui o módulo json para manipulação de arquivos JSON, o módulo re para lidar com expressões regulares e a biblioteca "deep_translator" para facilitar a tradução de palavras.

2. Carregamento de Dados: Ao utilizar a  função json.loads, o conteúdo de um arquivo JSON específico, neste caso o "conceitos.json", é lido e carregado em uma estrutura de dados Python.

3. Configuração da Blacklist: A blacklist é uma lista de palavras que devem ser excluídas do processo de tradução ou não devem ser incluídas nos tooltips. Esta lista pode ser aumentada, neste caso adapatada a conteudos em portugues, como "de", "se", etc.

4. Função de Tradução: A biblioteca "deep_translator" é utilizada para criar uma instância do tradutor do Google. Através dela, a função translate_word é configurada para traduzir uma palavra do português para o inglês.

5. Função Etiquetadora: A função etiquetadora é responsável por processar todas as palavras presentes no texto HTML. Ela adiciona tooltips que contêm a descrição e a tradução do termo médico, desde que a palavra esteja na lista de termos médicos e não conste na blacklist. Caso contrário, a palavra permanece inalterada.

6. Processamento do Texto HTML: As quebras de linha no texto HTML são substituídas por tags apropriadas. Além disso, a função etiquetadora é aplicada a cada palavra do texto para adicionar tooltips conforme necessário.

7. Escrita do Texto Processado: O texto processado é então escrito em um arquivo HTML denominado "livro.html".


### Conclusão

Concluindo, a tradução automática foi efetuada com sucesso.