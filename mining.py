import nltk

#nltk.download() # Serve para atualizar o NLTK, Ao executar abrirá uma janela, Clique em "ALL e depois em "DOWNLOAD".

base_train = [
    ('vou reclamar no reclame aqui','alta'),
    ('péssimo atendimento não recomendo','alta'),
    ('vou acionar o procon atendimento péssimo não era o que eu esperava','alta'),
    ('decepcionante este serviço não recomendo ','alta'),
    ('quero meu dinheiro de volta','alta'),
    ('Eu acho um descaso pois quando solicitei paguei uma taxa para dar incio e em nenhum momento foi informado que quando fosse utilizar o serviço eu teria que pagar outra taxa, Tendo em vista que outras empresas com o mesmo serviço não cobra esse tipo de taxa abusiva', 'alta'),
    ('Fiquei mais de uma hora no telefone ligando para tentar solucionar o meu problema com o serviço prestado e quando finalmente atenderam, só falaram para aguardar e a ligação simplesmente caiu! Isso é uma total falta de respeito com o consumidor que já está com um problema e ninguém se prontifica para resolver', 'alta'),
    ('Sou cliente já faz dois anos e o serviço que solicitei vive dando problema e toda vez que tento entrar em contato para solução é a mesma enrolação de sempre! Falta de suporte técnico e atendimento rápido, vou procurar outro lugar pois esse já deu o que tinha que dar', 'alta'),
    ('Eu contratei o serviço, paguei e até agora não recebi nada! Já se passaram dez dias e não obtive nem sequer respostas! Vou abrir uma reclamação no procon pois isso é uma total falta de caráter com quem estava disposto a usufruir dos serviços prestados e investiu confiança onde não deveria ter', 'alta'),
    ('Muita falta de informação, falam as coisas de qualquer maneira e depois fecham serviços que não foram bem explicados com um valor abusivo! Além de ser o serviço errado que fecharam para mim, ainda fizeram de péssima qualidade, tentei entrar em contato e a atendente não soube nem sequer responder minhas perguntas. Total falta de profissionalismo', 'alta'),
	('Demora para entregar, sistema lento não aconselho e não recomendo', 'alta'),
    ('Sistema muito lento, chat bot fica falando as coisas aleatórias', 'alta'),
    ('Estou com problema, o chat bugou, fica escrevendo sem parar', 'alta'),
	('Estou tentando entrar em contato para eles resolverem meu problema e até agora nada! Já se passou uma semana sem respostas, quero explicações do porque toda essa demora para resolver algo tão simples', 'alta'),
    ('Eu vi que a minha fatura tinha aumentado então percebi que tinham renovado, tentei conversar com eles para perguntar o porquê disso sendo que eu havia solicitado cancelamento do serviço, eu só quero cancelar, isso é um descaso com o consumidor', 'alta'),
	('não gostei do produto estou insatisfeito','alta'),
    ('este ticket esta aqui há dias e ninguem me respondeu ainda','alta'),
    ('vou abrir reclamação contra a empresa','alta'),
    ('irei entrar com processo pois não era esse o serviço que me falaram','alta'),
    ('péssima qualidade serviço horrível e não me respondem', 'alta'),
    ('Não entregaram aquilo que prometeram quero meu dinheiro de volta', 'alta'),
    ('Meu problema ainda não foi solucionado ainda estou com o problema', 'alta'),
    ('Não gostei do produto, quero meu dinheiro de volta', 'alta'),
    ('Vendedor péssimo', 'alta'),
    ('Vendedor ruim', 'alta'),
    ('Não oferece um bom serviço', 'alta'),

	('Serviço de qualidade e entrega rápida! Solicitei o serviço hoje e em poucos dias já me contataram para avaliar se era realmente isso que eu desejava. Foram muito profissionais e atenderam todas as minhas expectativas! Com certeza voltarei a fazer negócio e recomendarei', 'normal'),
    ('Tive um pequeno problema de suporte técnico, entrei em contato e me atenderam muito bem, esclareceram todas as minhas dúvidas e resolveram meu problema de imediato, estou muito satisfeito com o atendimento e profissionalismo, voltarei com certeza a fazer negócio', 'normal'),
    ('Todos os serviços prestados são muito bons, não tenho do que reclamar. Sempre me atenderam bem, realizarem o informado e esclareceram todas as minhas dúvidas a respeito de suporte, pacotes, renovação e valores. Os preços também são muito bons, tive uma ótima experiência, recomendo', 'normal'),
    ('Entregam o que prometem, desde que comecei o serviço já aumentou os atendimentos exponêncialmente', 'normal'),
	('Produto realmente cumpre com o que promete, uma ótima escolha', 'normal'),
    ('Contratei o serviço já faz um ano e nunca deu problema, muito pelo contrário, foi realizado de acordo com a proposta e bem feito, só tenho a agradecer o compromisso com o consumidor', 'normal'),
    ('Atendimento rápido e de qualidade', 'normal'),
    ('Realmente o serviço prestado foi muito bom a rapidez e agilidade para ser atendido é fora do comum', 'normal'),
	('fiz uma ótima compra', 'normal'),
    ('realizei uma boa compra', 'normal'),
	('estou totalmente satisfeito com o produto', 'normal'),
    ('atendeu todas as minhas expectativas parabéns', 'normal'),
    ('parabéns melhor investimento que fiz', 'normal'),
    ('Desde que peguei o serviço de vocês me ajudou muito parabéns', 'normal'),
    ('Excelente serviço um dos melhores que já usei', 'normal'),
    ('Uma ótima opção para aqueles que procuram esse mesmo tipo de serviço', 'normal'),
    ('me surpreendi com o produto ótima qualidade', 'normal'),
    ('gostei muito com certeza comprarei de novo', 'normal'),
    ('era exatamente isso que precisava recomendo', 'normal'),
    ('realmente muito bom o serviço', 'normal'),
    ('atendimento excelente esclareceram todas as minhas duvidas serviço de otima qualidade', 'normal'),
    ('Produto muito bom, vendedores estão de parabéns', 'normal'),
    ('Gostei muito', 'normal'),
    ('realmente muito bom o serviço', 'normal')]

base_test = [ # Usado para validar a accuracy do programa.
    ('Empresa péssima, não condiz com aquilo que propoe', 'alta'),
    ('Atendimento ruim, serviço mal feito', 'alta'),
    ('alem do serviço mal feito, até hoje estou aguardando o meu chargeback', 'alta'),
    ('Não devolveram o meu dinheiro ainda, estou aguardando', 'alta'),
    ('Irei entrar com ação judicial, pois não querem resolver o meu problema amigavelmente', 'alta'),
    ('Estou indo reclamar no procon, já deixei o meu recado no reclame aqui, empresa totalmente mal organizada', 'alta'),
    ('Estou indignado com a falta de respeito e compromentimento com os clientes, sem condições de continuar com essa empresa', 'alta'),

    ('Aprovado o serviço, realmente a melhor aquisição que fiz', 'normal'),
    ('Já estou recomendando para os meus contatos, excelente trabalho de vocês, continuem assim', 'normal'),
    ('É um prazer fazer negócio com vocês, empresa que leva os clientes á sério e passam uma confiança exemplar', 'normal'),
    ('Graças a essa empresa, meu objetivo está sendo alcançado com qualidade, obrigado! sucesso', 'normal'),
    ('Já foi cliente desta empresa, cinco anos depois, estou voltando e vejo que estão cada vez melhor, parabéns', 'normal'),
    ('Melhor empresa do ramo, com toda certeza recomendarei á todos', 'normal'),
    ('Sou cliente de vocês há muito tempo, e sempre tive um grande retorno, suporte rápido e de qualidade, continuem assim', 'normal')]

# StopWords é as palavras que não tem relevância no treinamento do algoritmo.

stopwordsnltk = nltk.corpus.stopwords.words('portuguese') # Maneira automática pela biblioteca NLTK
stopwordsnltk.append('vou') # Algumas stopwords que não contém na biblioteca, estou adicionando manualmente
stopwordsnltk.append('tão')
stopwordsnltk.append('vai')
stopwordsnltk.append('é')

def removestopwords(texto):
    frases = []
    for(palavras, prioridade) in texto: # palavras vai pegar cada elemento preditivo das frases, já a prioridade a classe "Alta ou Normal"
        semstop = [p for p in palavras.split() if p not in stopwordsnltk] # split vai "quebrar" cada uma das frases. Jogando a frase sem o stopwords para a variável semstop
        frases.append((semstop, prioridade)) # Adicionando dentro da variável frases. Passando a classe como parâmetro.
    return frases

def aplicastemmer(texto): # Stemmer serve para retirar o radical das palavras, exemplo LIVRo, LIVRinho, LIVRete, etc..
    stemmer = nltk.stem.RSLPStemmer() # RSLPS é específico para a língua portuguesa.
    frasesstemming = []
    for(palavras, prioridade) in texto:
        comstemming = [str(stemmer.stem(p)) for p in palavras.split() if p not in stopwordsnltk] # Função stem aplicado para retirar o radical da palavra
        frasesstemming.append((comstemming, prioridade))
    return frasesstemming # Nova lista já com as frases tratadas com o radical e sem as stopwords.

frasescomstemming_train = aplicastemmer(base_train)
frasescomstemming_test = aplicastemmer(base_test)

def buscapalavras(frases):
    todaspalavras = []
    for (palavras, prioridade) in frases:
        todaspalavras.extend(palavras) # Está recebendo sem a prioridade associada, ou seja, somente as palavras.
    return todaspalavras

palavras_train = buscapalavras(frasescomstemming_train)
palavras_test = buscapalavras(frasescomstemming_test)

def buscafrequencia(palavras):
    palavras = nltk.FreqDist(palavras)
    return palavras

frequencia_train = buscafrequencia(palavras_train)
frequencia_test = buscafrequencia(palavras_test)

def buscapalavrasunicas(frequencia):
    freq = frequencia.keys() # Vai pegar somente as chaves que já tem os valores, sem a repetição.
    return freq

palavrasunicas_train = buscapalavrasunicas(frequencia_train)
palavrasunicas_test = buscapalavrasunicas(frequencia_test)

def extratorpalavras(documento):
    doc = set(documento) # Associando a variável com o valor que está chegando com o parâmetro.
    caracteristicas = {}
    for palavras in palavrasunicas_train:
        caracteristicas['%s' % palavras] = (palavras in doc) # Percorrendo cada uma das palavrasunicas e verificando quais delas existem na frase passada como parâmetro.
    return caracteristicas

basecompleta_train = nltk.classify.apply_features(extratorpalavras, frasescomstemming_train) # Pegando cada uma das frases e aplicando no extrator de palavras
basecompleta_test = nltk.classify.apply_features(extratorpalavras, frasescomstemming_test)

classificador = nltk.NaiveBayesClassifier.train(basecompleta_train) # Criando o classificador Naive Bayes já com a base processada. Montando a tabela de probabilidade.
#print('Accuracy do programa é dê: %s' % nltk.classify.accuracy(classificador, basecompleta_test))

ticket = 'gostei do serviço prestado' # Mensagem / Comentário aqui
testestemming = []
stemmer = nltk.stem.RSLPStemmer()
for (palavras_train) in ticket.split():
    comstem = [p for p in palavras_train.split()]
    testestemming.append(str(stemmer.stem(comstem[0])))
novo = extratorpalavras(testestemming)

print('Propriedade do Ticket: %s ' % classificador.classify(novo))
distribuicao = classificador.prob_classify(novo) # Fazendo uma estimativa dos tickets
for classe in distribuicao.samples():
    print("%s: %f" % (classe, distribuicao.prob(classe)))