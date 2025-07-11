import random
des_forca = ['''
   +---+
   |   |
       |
       |
       |
       |
=========''', '''
   +---+
   |   |
   \033[0;31mO\033[0m   |
       |
       |
       |
=========''', '''
   +---+
   |   |
   \033[0;31mO\033[0m   |
   \033[0;31m|\033[0m   |
       |
       |
=========''', '''
   +---+
   |   |
   \033[0;31mO\033[0m   |
  \033[0;31m/|\033[0m   |
       |
       |
=========''', '''
   +---+
   |   |
\033[0;31m   O\033[0m   |
\033[0;31m  /|\ \033[0m |
       |
       |
=========''', '''
   +---+
   |   |
   \033[0;31mO\033[0m   |
 \033[0;31m /|\ \033[0m |
  \033[0;31m/\033[0m    |
       |
=========''', '''
   +---+
   |   |
   \033[0;31mO  \033[0m |
 \033[0;31m /|\ \033[0m |
  \033[0;31m/ \ \033[0m |
       |
=========''']
continuar = 'sim'
while continuar == 'sim':
    print("Alunos desenvolvedores:\n - Eduardo Bento\n - Geovana Rochal\n - João Vitor\n - José Migue\n - Karoline Ramos")
    tema = input('Informe o tema que desjea jogar:\n - cores\n - animais\n - comidas\n - frutas\n - artistas\n').lower()
    if tema == 'cores':
        listaEscolha = ["Azul", "Vermelho", "Verde", "Amarelo", "Laranja", "Roxo", "Rosa", "Cinza", "Marrom", "Preto","Branco", "Dourado", "Prata", "Turquesa", "Vinho", "Coral", "Magenta", "Ciano", "Oliva", "Bege"]
        dicas = ["É a cor do céu e do mar.", "É a cor de maçãs e do amor.", "É a cor das folhas e da grama.","É a cor do sol e de bananas.", "É a cor das laranjas e do pôr do sol.","É a cor das uvas e de algumas flores.", "É a cor de algodão-doce e de muitos brinquedos.","É a cor das nuvens e de pedras.", "É a cor do chocolate e da terra.","É a cor do espaço e de muitos animais.", "É a cor da neve e de nuvens fofas.","É a cor do ouro e de estrelas brilhantes.", "É a cor de coisas brilhantes e de alguns carros.","É a cor de águas claras e de algumas pedras.", "É a cor de sucos de frutas e de algumas flores.","É a cor de peixes coloridos e de conchas.", "É uma cor bem viva, como um doce de frutas.","É uma cor azul clara, como o céu em um dia bonito.", "É a cor de azeitonas e de algumas folhas.","É uma cor suave, como areia na praia."]
        numero = random.randint(0, 19)
        escolhido = listaEscolha[numero].lower()
        dica = dicas[numero]
        tamanho = len(escolhido)
        branco = []
        letrasErradas = []
        acerto = 0
        existe = 0
        for i in range(tamanho):
            branco.append("_")
        print(branco[1])
        erros = 0
        while erros < 6 and acerto < tamanho:
            existe = 0
            tamanhoErros = len(letrasErradas)
            print(des_forca[erros])
            for i in range(tamanho):
                print(f'{branco[i]} ', end='')
            print("\n")
            encontrado = 0
            print("Letras erradas:")
            # Mostra as letras erradas
            for i in range(tamanhoErros):
                print(f'\033[0;31m{letrasErradas[i]}\033[0m ', end='')
            # Mostra uma dica quando chega a três erros
            if erros == 2:
                print(f'\n{dica}')
            chute = input("\nEscolha uma letra:\n")
            # Procura na palavra a encontrar e nas letras erradas se a letra já foi digitada anteriormente
            for i in range(tamanho):
                if chute == branco[i]:
                  existe +=1
            for i in range(tamanhoErros):
                if chute == letrasErradas[i]:
                    existe +=1
            # Se não existir vê se está errada ou se está correta
            if existe == 0:
                for i in range(tamanho):
                    if chute == escolhido[i]:
                        encontrado += 1
                for j in range(tamanho):
                    if chute == escolhido[j]:
                        branco[j] = chute
                        erro = 0
                        acerto += 1
                    elif encontrado == 0:
                        erro = 1
            else:
                print("\033[0;31mLetra já foi inserida, escolha outra letra.\033[0m")
            if erro == 1:
                letrasErradas.append(chute)
            erros += erro
        if erros == 6:
            print(des_forca[erros])
            print("\033[0;31mVocê perdeu!\033[0m")
            print(f"A palavra era: {escolhido}")
        if acerto == tamanho:
            print("\033[0;34mVocê ganhou!\033[0m")
    elif tema == "animais":
        listaEscolha = ["Leao", "Elefante", "Tigre", "Golfinho", "Cavalo", "aguia", "Urso-pardo", "Canguru", "Lobo","Jacare", "Pinguim", "Coruja", "Gato", "Cachorro", "Tartaruga", "Camaleao", "Rinoceronte", "Zebra","Arraia", "Tamandua-bandeira"]
        dicas = ["É conhecido como o rei da selva.", "Maior animal terrestre, com tromba longa.","Felino listrado que vive na Ásia.", "Vivo no mar, sou fofinho e pulo fora d’água.","Usado para montaria e transporte há séculos.", "Ave de rapina com visão excelente.","Sou grande, peludo e adoro mel.", "Tenho uma bolsinha e dou pulos bem altos.","Parente selvagem do cachorro, vive em matilha.", "Réptil com mandíbula forte, vive em rios.","Ave que não voa, vive em regiões frias.", "Ave noturna conhecida pelos olhos grandes.","Animal doméstico que adora caçar ratos.", "Melhor amigo do homem, muito leal.","Ando devagar e carrego minha casa nas costas.", "Muda de cor e tem língua pegajosa.","Sou grande e tenho um chifre no nariz.", "Parece um cavalo com listras pretas.","Tenho forma de pipa e vivo no fundo do mar.", "Tenho nariz comprido e como muitas formigas."]
        numero = random.randint(0, 19)
        escolhido = listaEscolha[numero].lower()
        dica = dicas[numero]
        tamanho = len(escolhido)
        branco = []
        letrasErradas = []
        acerto = 0
        existe = 0
        for i in range(tamanho):
            branco.append("_")
        print(branco[1])
        erros = 0
        while erros < 6 and acerto < tamanho:
            existe = 0
            tamanhoErros = len(letrasErradas)
            print(des_forca[erros])
            for i in range(tamanho):
                print(f'{branco[i]} ', end='')
            print("\n")
            encontrado = 0
            print("Letras erradas:")
            # Mostra as letras erradas
            for i in range(tamanhoErros):
                print(f'\033[0;31m{letrasErradas[i]}\033[0m ', end='')
            # Mostra uma dica quando chega a três erros
            if erros == 2:
                print(f'\n{dica}')
            chute = input("\nEscolha uma letra:\n")
            # Procura na palavra a encontrar e nas letras erradas se a letra já foi digitada anteriormente
            for i in range(tamanho):
                if chute == branco[i]:
                  existe +=1
            for i in range(tamanhoErros):
                if chute == letrasErradas[i]:
                    existe +=1
            # Se não existir vê se está errada ou se está correta
            if existe == 0:
                for i in range(tamanho):
                    if chute == escolhido[i]:
                        encontrado += 1
                for j in range(tamanho):
                    if chute == escolhido[j]:
                        branco[j] = chute
                        erro = 0
                        acerto += 1
                    elif encontrado == 0:
                        erro = 1
            else:
                print("\033[0;31mLetra já foi inserida, escolha outra letra.\033[0m")
            if erro == 1:
                letrasErradas.append(chute)
            erros += erro
        if erros == 6:
            print(des_forca[erros])
            print("\033[0;31mVocê perdeu!\033[0m")
            print(f"A palavra era: {escolhido}")
        if acerto == tamanho:
            print("\033[0;34mVocê ganhou!\033[0m")
    elif tema == "comidas":
        # Palavras e dicas
        listaEscolha = ["Feijoada", "Moqueca", "Acaraje", "Pamonha", "Tapioca", "Farofa", "Cuscuz", "Dobradinha","Maniçoba", "Churrasco", "Vatapa", "Arroz doce", "Canjica", "Baiao", "Quindim", "Buchada","Escondidinho", "Galinhada", "Tutu", "Paçoca"]

        dicas = ["Prato típico com feijão preto, carne seca e linguiça.", "Prato baiano com peixe, leite de coco e dendê.","Bolinho frito de feijão-fradinho recheado com vatapá ou camarão.","Feita com milho verde e cozida na palha.","Feita com goma de mandioca e recheada, geralmente doce ou salgada.","Acompanhamento crocante feito com farinha de mandioca.", "Prato nordestino feito com flocos de milho.","Prato com bucho de boi, tradicional em festas.", "Prato paraense feito com folhas de mandioca cozidas.","Carne assada na brasa, muito comum em festas e reuniões.","Prato baiano cremoso à base de pão, camarão e dendê.", "Sobremesa feita com arroz, leite e canela.","Feita com milho branco, leite e coco.", "Prato nordestino com arroz, feijão verde e queijo coalho.","Doce amarelo feito com gemas e coco ralado.", "Prato forte feito com vísceras de carneiro.","Purê de mandioca com carne seca desfiada.", "Arroz cozido com pedaços de frango e temperos.","Feijão engrossado com farinha e temperado.", "Doce feito com amendoim triturado, açúcar e farinha."]

        # Sorteio da palavra e dica
        numero = random.randint(0, 19)
        escolhido = listaEscolha[numero].lower()
        dica = dicas[numero]

        # Preparação do jogo
        tamanho = len(escolhido)
        branco = ["_" if c != " " else " " for c in escolhido]
        letrasErradas = []
        acerto = branco.count(" ")  # já conta os espaços como acertos

        erros = 0

        # Loop do jogo
        while erros < 6 and acerto < tamanho:
            print(des_forca[erros])
            print("Palavra: ", ' '.join(branco))
            print("Letras erradas:", ' '.join(f'\033[0;31m{l}\033[0m' for l in letrasErradas))

            if erros == 2:
                print(f"Dica: {dica}")

            chute = input("Escolha uma letra: ").lower()

            if chute in letrasErradas or chute in branco:
                print("Você já tentou essa letra.")
                continue

            if chute in escolhido:
                for i in range(tamanho):
                    if escolhido[i] == chute:
                        branco[i] = chute
                        acerto += 1
            else:
                letrasErradas.append(chute)
                erros += 1

        # Fim do jogo
        if acerto == tamanho:
            print("\033[0;34mVocê ganhou!\033[0m")
        else:
            print(des_forca[erros])
            print("\033[0;31mVocê perdeu!\033[0m")
            print(f"A palavra era: {escolhido}")
    elif tema == "frutas":
        listaEscolha = ['banana', 'maça', 'laranja', 'mamao', 'abacaxi', 'manga', 'melancia', 'uva', 'morango', 'goiaba','coco', 'limao', 'acerola', 'maracuja', 'pera', 'kiwi', 'caqui', 'caju', 'jabuticaba', 'pitanga']
        dicas = ['é amarela e macaco gosta', 'é vermelha e doce', 'tem suco e vitamina C', 'papinha do café da manhã','tem coroa e é azedo', 'amarela, doce e escorregadia', 'grande, vermelha e refrescante','pequenina e roxa ou verde', 'vermelha e cheia de sementes', 'verde por fora, rosa por dentro','branco por dentro e duro fora', 'azedo e faz careta', 'pequena, vermelha e azedinha','azedo e tem muitas sementes', 'tem formato engraçado', 'verde por fora, doce por dentro','vermelho por fora, doce por dentro', 'parece uma castanha com suco', 'pretinha e cresce no pé','vermelha e bem brasileira']

        numero = random.randint(0, 19)
        escolhido = listaEscolha[numero].lower()
        dica = dicas[numero]
        tamanho = len(escolhido)
        branco = []
        letrasErradas = []
        acerto = 0

        for i in range(tamanho):
            branco.append("_")

        erros = 0
        while erros < 6 and acerto < tamanho:
            tamanhoErros = len(letrasErradas)
            print(des_forca[erros])
            for i in range(tamanho):
                print(f'{branco[i]} ', end='')
            print("\n")
            encontrado = 0
            print("Letras erradas:")
            for i in range(tamanhoErros):
                print(f'\033[0;31m{letrasErradas[i]}\033[0m ', end='')
            if erros == 2:
                print(f'\n{dica}')

            chute = input("\nEscolha uma letra:\n").lower()

            if chute in branco or chute in letrasErradas:
                print("Essa letra já foi digitada, portanto foi considerado um erro.")
                erros += 1
            else:
                erro =1
                for i in range(tamanho):
                    if chute == escolhido[i] and branco[i] == "_":
                        branco[i] = chute
                        acerto += 1
                        encontrado += 1
                        erro = 0
                if erro == 1:
                    letrasErradas.append(chute)
                erros += erro

        if erros == 6:
            print(des_forca[erros])
            print("\033[0;31mVocê perdeu!\033[0m")
        if acerto == tamanho:
            print("\033[0;34mVocê ganhou!\033[0m")
    elif tema == "artistas":
        artistas = ["beyonce", "michael jackson", "jennie", "madona", "jorge e matheus","taylor swift", "rihanna", "shakira", "jennifer lopez", "bruno mars","lady gaga", "matheus e kauan", "henrique e juliano","queen", "adele", "coldplay", "bts", "ed sheeran","dua lipa", "the weeknd", "nirvana", "blackpink", "red hot chili peppers","ariana grande"]

        dicas = [
            ["Brilha em mais de um palco", "Já teve um anel no dedo e uma coreografia marcante","É casada com um grande nome do rap"],
            ["Mudou o mundo com passos invertidos", "Transformou o terror em pop", "Seu moonwalk é inesquecível"],
            ["Tem talento exportado de onde o sol nasce", "Canta em grupo e também sozinha", "É integrante do BLACKPINK"],
            ["Sempre foi 'nova', mesmo sendo antiga", "Explorou o amor como se fosse pela primeira vez","É chamada de rainha do pop"],
            ["Dupla que virou multidão", "Sucesso em barzinhos e grandes palcos","Cantam 'Logo Eu' e outros hits sertanejos"],
            ["Contou histórias com o violão e depois com sintetizador", "Se reinventou da fazenda para o palco pop","É loira, americana e escreve sobre ex-namorados"],
            ["Não vem dos Estados Unidos, mas conquistou o mundo", "Seu guarda-chuva virou hino","Tem uma marca que vale bilhões"],
            ["Movimenta o mundo com quadris e ritmos", "Fez do futebol uma dança", "É colombiana e já brilhou na Copa"],
            ["É conhecida por três letras", "Fez o chão tremer com hits e coreografias","Mistura música, dança e cinema em sua carreira"],
            ["Pequeno no nome, gigante no talento", "Tem charme, tem funk, tem soul","Cantou sobre amores do jeitinho que eles são"],
            ["Tem nome de realeza, mas nasceu pra brilhar", "Fez de uma música sobre romance um hino","É a Mother Monster"],
            ["Tem um 'coração apertado' em muitas canções", "Estouraram em shows sertanejos", "Cantam 'Que Sorte a Nossa'"],
            ["São irmãos e contam histórias cantando", "Música romântica no DNA", "São sucesso nas playlists do Brasil"],
            ["Nome imponente, repertório mais ainda", "Fez estádio inteiro cantar junto", "É de Freddie Mercury"],
            ["Silenciosa e potente", "Fez chorar ao dizer 'Hello'", "Britânica com voz de ouro"],
            ["Levam o público a outro universo", "Têm hits com nomes de cores", "Banda de 'Yellow' e 'Viva la Vida'"],
            ["Explodiram do outro lado do mundo", "Fizeram a juventude dançar com DNA","Grupo de K-pop com sete integrantes"],
            ["Tímido no visual, gigante no som", "Toca violão com coração", "Canta 'Perfect' e 'Thinking Out Loud'"],
            ["Pop de atitude", "Música para dançar sozinha", "Cantora de 'Levitating'"],
            ["Não vem do fim de semana", "Misterioso e talentoso", "Cantor de 'Blinding Lights'"],
            ["Barulhento e revolucionário", "Trouxe o grunge à tona", "Banda de Kurt Cobain"],
            ["Mistura rosa com atitude", "Explodiu com batidas fortes", "Girl group coreano"],
            ["Misturam pimenta com som", "Californianos no DNA", "Banda de 'Californication'"],
            ["Seu nome soa como algo enorme", "Já foi estrela de TV antes de dominar os palcos","Cantora de voz potente, famosa por '7 rings' e 'thank u, next'"]
        ]

        indice = random.randint(0, len(artistas) - 1)
        palavra = artistas[indice]
        dicas_palavra = dicas[indice]

        branco = []
        letrasErradas = []
        acerto = 0
        palavra_sem_espacos = palavra.replace(" ", "")
        tamanho = len(palavra_sem_espacos)

        for i in range(len(palavra)):
            if palavra[i] == " ":
                branco.append(" ")
            else:
                branco.append("_")

        erros = 0
        while erros < 6 and acerto < tamanho:
            print(des_forca[erros])
            print("Palavra:", end=" ")
            for letra in branco:
                print(letra, end=" ")
            print("\n")

            print("Letras erradas:", end=" ")
            for letra in letrasErradas:
                print(f"\033[0;31m{letra}\033[0m", end=" ")
            print("\n")

            if erros == 2 and len(dicas_palavra) >= 1:
                print("Dica 1:", dicas_palavra[0])
            if erros == 4 and len(dicas_palavra) >= 2:
                print("Dica 2:", dicas_palavra[1])
            if erros == 5 and len(dicas_palavra) >= 3:
                print("Dica 3:", dicas_palavra[2])

            chute = input("Escolha uma letra: ").lower()

            if chute in palavra and chute not in branco:
                for i in range(len(palavra)):
                    if palavra[i] == chute:
                        branco[i] = chute
                        acerto += 1
            elif chute in letrasErradas or chute in branco:
                print("Você já tentou essa letra.")
            else:
                letrasErradas.append(chute)
                erros += 1

        if erros == 6:
            print(des_forca[erros])
            print("\033[0;31mVocê perdeu!\033[0m")
            print("A palavra era:", palavra)
        else:
            print("\033[0;34mVocê ganhou!\033[0m")
            print("A palavra era:", palavra)
    continuar = input("Deseja jogar novamente?\n").lower()