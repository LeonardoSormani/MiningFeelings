NLTK: Natural Language Tool Kit

Para instalar a biblioteca NLTK: Abrir o Prompt de comando, e ir onde está a instalação do Python, No meu caso é: Appdata\Local\Programs\Python37-32\Scripts (Caminho padrão). E dar o comando: pip install nltk Dentro da pasta Scripts.

Ao abrir o código no arquivo mining.py encontrará na linha 3, nltk.download() Isso serve p/ atualizar o NLTK, execute este comando e uma janela se abrirá, clique em ALL e depois em DOWNLOAD.

O vetor base_train contem todas as frases que utilizei para realizar o treinamento do algoritmo. Utilizei uma base de dados pequena, pois o meu computador é antigo e não tem poder computacional para processar uma base de dados boa.

Foi inserido um total de 44 frases, sendo 22 em cada prioridade, (Alta e Normal), quanto maior a base de dados e mais detalhes obter a frase, mais inteligente o algoritmo fica.

Já o vetor base_test contem os dados para validarmos o algoritmo.

Usei os seguintes critérios, 70% para treinamento e 30% para teste, validação das frases.

Obtive um percentual de accuracy dê: 0.7142857142857143, ou 71% de precisão. Este teste se encontra comentado na linha 135.

Já na linha 137 é onde deverá ser inserido a frase/comentário á ser analisada pelo algoritmo. Lembrando que, Prioridade Alta: Cliente Insatisfeito / Irritado; Prioridade Normal: Cliente Satisfeito / Bom-Humor.

Prioridade Alta: Cliente Insatisfeito / Irritado
Prioridade Normal: Cliente Satisfeito / Bom-Humor

Linha a ser modificada com a mensagem/comentário do ticket -> 137
