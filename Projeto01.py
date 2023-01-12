from random import choice
from os import system, name
from time import sleep

q1 = "(VUNESP/2014) - Assinale a alternativa em que a pontuação está de acordo \ncom a norma padrão. \n A) Falar mal " \
     "dos colegas, é falta de ética.\n B) inveja, causa problemas, nas relações humanas.\n C) A fofoca, comportamento "\
     "humano deplorável, deve ser evitada.\n [A/B/C]? "
r1 = 'C'
q2 = "(INSTITUTO AOCP) Assinale a alternativa em que a palavra contenha um prefixo e um sufixo. \n A) Lembrança.\n B) "\
     "Lentamente.\n C) Interminável.\n D) Trepadeiras.\n [A/B/C/D]? "
r2 = 'D'
q3 = "(COPEVE-UFAL) A única opção em que a concordância verbal pode se dar no singular ou no plural: \n A) A maioria " \
     "dos alunos prefere aulas com uso de tablets e celulares\n B) Faz 22 anos que aconteceu o primeiro Enem \n C) A " \
     "escola, os professores, a turma, tudo agradou o novo Diretor\n D) 100% dos professores de nossa escola foram " \
     "selecionados através de concurso público.\n [A/B/C/D] "
r3 = 'B'
q4 = 'Trata-se de um fenômeno moderno, originado a partir do grande desenvolvimento de centros urbanos altamente ' \
     'industrializados. \nCom a liberação de poluentes à atmosfera pelas diversas fontes de poluentes gasosos, ' \
     'há a combinação destes poluentes \ncom o vapor de água existente na atmosfera. \nO texto refere-se:\n A) às ' \
     'frentes frias que ocorrem na zona de convergência intertropical. \n B) à formação de chuvas orográficas no ' \
     'nordeste brasileiro. C) à ocorrência de geadas na região sul do país, que provoca vários problemas ' \
     'respiratórios nas áreas afetadas.\n D) ao feônomeno da formação das chuvas ácidas, muito comum no continente ' \
     'europeu \n [A/B/C/D] '
r4 = 'C'
q5 = 'Acerca de suas características físicas, o continente africano\n A) ao norte, é banhado pelo Oceano Atlântico na '\
     'costa ocidental e, pelo Oceano Pacíco, na costa oriental.\n B) É o maior continente do mundo.\n C) É cortado ' \
     'pelos trópicos de Câncer e de Capricórnio.\n D) Não apresenta cadeias de montanhas por estar localizado em uma ' \
     'única placa tectônica. \n[A/B/C/D] '
r5 = 'D'
q6 = 'O meio ambiente hoje está sendo alvo de muito estudo devido ao aquecimento global que está contribuindo para a ' \
     'matança de animais e paisagens. \nO dia do meio ambiente é comemorado em:\n A) 05 de abril.\n B) 05 de maio.\n ' \
     'C) 05 de junho.\n D) 05 de agosto.\n [A/B/C/D] '
r6 = 'C'
q7 = 'Em 2006, o IBGE completou 70 anos de sua fundação.\n Esse instituto foi criado no contexto histórico da(o):\n' \
     'A) Ditadura Militar, de Costa e Silva\n B) Transição Democrática, de José Sarney\n C) Estado Novo, de Getúlio ' \
     'Vargas\n D) Plano de Metas, de Juscelino Kubitschek\n [A/B/C/D]'
r7 = 'C'
q8 = 'Em 2007 foi lançado no Brasil o PAC Programa de Aceleração do Crescimento. \n A execução desse programa tem uma '\
     'abrangência:\n' \
     ' A) municipal\n B) distrital\n C) estadual\n D) nacional\n [A/B/C/D]'
r8 = 'D'
q9 = 'Em qual banco de dados fica a tabela de sistema "syslogins"?\n A) Todos os bancos possuem esta tabela.\n B) ' \
     'Somente o banco MASTER possui esta tabela.\n C) Os bancos "MASTER" e "MSDB" possuem esta tabela.\n [A/B/C]'
r9 = 'B'
q10 = '(OBJETIVA) Em relação à expressão numérica abaixo, assinalar a alternativa que apresenta o seu resultado:\n 1 ' \
      '- 2 x 4 + 0 x 7' \
      '\n A) 0\n B) -7\n C) -14\n D) -28\n [A/B/C/D]'
r10 = 'B'
q11 = '(VUNESP) Se a temperatura cair, então precisarei me agasalhar. Se me agasalhar, então não poderei correr.\n ' \
      'Se puder correr, então não chegarei tarde. A temperatura caiu. Desse modo, é correto concluir que \n A) não ' \
      'corri e precisei me agasalhar.\n B) corri e não cheguei tarde.\n C) não corri e não precisei me agasalhar.\n ' \
      'D) cheguei tarde e precisei me agasalhar.\n [A/B/C/D]'
r11 = 'A'
q12 = '(OBJETIVA) Em uma caixa de leite, há 12 litros do produto. Se uma pessoa comprar três caixas e meia, ' \
      'ela comprará:\n A) 36 litros de leite.\n B) 42 litros de leite.\n C) 40 litros de leite.\n D) 46 litros de ' \
      'leite.\n [A/B/C/D]'
r12 = 'B'
q13 = '(QUADRIX) A probabilidade de certa jogadora de basquetebol converter um lance livre é de 90%.\n Com base nessa '\
      'situação hipotética, julgue o item.\n A) Certo.\n B) Errado.\n [A/B]'
r13 = 'B'
q14 = 'A palavra CANCIONEIRO possui quantos fonemas:\n A) 4 fonemas\n B) 5 fonemas\n C) 6 fonemas\n D) 10 fonemas\n [' \
      'A/B/C/D] '
r14 = 'D'
q15 = 'Em: “Estão pedindo ajuda para os desabrigados das chuvas.” Sintaticamente, temos:\n A) Sujeito simples.\n B) ' \
      'Sujeito desinencial.\n C) Sujeito indeterminado.\n D) Oração sem sujeito.\n [A/B/C/D]'
r15 = 'C'
q16 = 'Corresponde a antônimos:\n A) Gracejo - Chalaça.\n B) Deletério - Benéfico\n C) Esmalte - Ornamento\n D) ' \
      'Fechar - Cerrar.\n [A/B/C/D] '
r16 = 'B'
q17 = 'Qual das alternativas abaixo não corresponde ao conceito de Usura:\n A) Juro ou rendimento capital.\n B) ' \
      'Agiotagem.\n C) Avareza.\n D) Generosidade.\n [A/B/C/D] '
r17 = 'D'
q18 = 'A redação oficial deve se caracterizar por impessoalidade, uso do padrão culto de linguagem,\n clareza, ' \
      'concisão, formalidade e uniformidade. Sabendo disso,\n qual é a característica da redação oficial que requer que ' \
      'se perceba certa hierarquia de ideias que existe\n em todo texto de alguma complexidade, as quais são divididas ' \
      'em ideias fundamentais e secundárias?\n A) Impessoalidade\n B) Uniformidade\n C) Formalidade\n D) Concisão\n [' \
      'A/B/C/D] '
r18 = 'D'
q19 = '(Funcab) Em situações de calamidade pública, é dever do Assistente Social segundo o código de ética que o ' \
      'rege:\n A) exercer a supervisão de aluno de Serviço Social.\n B) ter liberdade na realização de estudos e ' \
      'pesquisas.\n C) participar na elaboração e no gerenciamento das políticas sociais.\n D) participar de ' \
      'programas de socorro à população.\n [A/B/C/D] '
r19 = 'D'
q20 = 'A legitimidade profissional do assistente social é tencionada por duas dimensões emanadas do processo\n ' \
      'necessidade / demanda / resposta. Essas dimensões apontadas por Montaño (2009) são:\n A) Dimensão hegemônica e ' \
      'subalterna.\n B) Dimensão educativa e subalterna.\n C) Dimensão hegemônica e burguesa.\n D) Dimensão política ' \
      'e função. \n [A/B/C/D] '
r20 = 'A'
q21 = '(AOCP) Com base na Lei 8069/90 assinale a alternativa que preencha corretamente as lacunas abaixo.\n É ' \
      'assegurado atendimento ______________ à saúde da criança\n e do adolescente, por intermédio do _______________, ' \
      'garantido o acesso universal\n e igualitário às ações e serviços para promoção, proteção e recuperação da ' \
      'saúde.\n Aos portadores de deficiência receberão atendimento ______________.\n A) Integral / SUS / ' \
      'especializado.\n B) psicológico / município / especial\n C) clínico / estado / individualizado.\n D) integral ' \
      '/ estado / especializado '
r21 = 'A'
q22 = '(CEV) No que se refere à Educação de Jovens e Adultos, é correto afirmar que:\n A) Os sistemas de ensino ' \
      'manterão cursos e exames supletivos, que compreenderão aspectos regionais\n do currículo, habilitando ao ' \
      'prosseguimento de estudos em caráter regular.\n B) É destinada àqueles que tiveram acesso aos estudos ou sua ' \
      'continuidade no ensino fundamental e médio na idade própria.\n C) Deverá ser assegurada pelos sistemas de ' \
      'ensino, gratuitamente ou em forma remunerada,\n aos que não puderam efetuar os estudos na idade regular.\n D) ' \
      'Oferecerá oportunidades educacionais apropriadas,\n consideradas as características do alunado, interesses, ' \
      'condições\n de vida e de trabalho, mediante cursos e exames. '
r22 = 'D'

# - Ao adicionar questões, lembrar de marcar ambas as perguntas e respostas na variável abaixo
perguntas = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21]
respostas = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20, r21]
tamanho = len(perguntas)
# - Informações, deixar em 0
resultado = 0
erro = 0

# - O tamanho define a quantia de questões subtraídas. O valor de x subtrai o número de questões.
# - Quando sobrar x na lista, o while irá encerrar.
while tamanho != 11:
    pergunta = choice(perguntas)
    print(pergunta)
    resp = input('R: ')
    if resp != "A" and resp != "B" and resp != "C" and resp != "D" and resp != "X":
        print('Valor inválido')
        sleep(0.5)
        system('cls' if name == 'nt' else 'clear')
        continue
    if resp == 'X':
        system('cls' if name == 'nt' else 'clear')
        break
    if resp == respostas.pop(perguntas.index(pergunta)):
        print('Acertou!')
        resultado += 1
        sleep(0.5)
        system('cls' if name == 'nt' else 'clear')
    else:
        print('Errou.')
        erro += 1
        sleep(0.5)
        system('cls' if name == 'nt' else 'clear')
    perguntas.remove(pergunta)

    tamanho = len(perguntas)
print('Você acertou {}, e errou {} questões.'.format(resultado, erro))
sleep(5)
