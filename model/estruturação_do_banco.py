from model.crud import conectar
from os import path


def banco_de_dados():
    carregar_estrutura()
    inserir_registros()


def carregar_estrutura():
    banco, cursor = conectar(False)
    conjunto = (
        'create database Pokedex;',
        'create table Pokedex.tb_tipos(' +
        'id int (10) not null auto_increment primary key ,' +
        'nome varchar(10) not null' +
        ');',
        'create table Pokedex.tb_regioes(' +
        'id int(3) not null auto_increment primary key,' +
        'nome varchar(30) not null,' +
        'offset int(3) not null' +
        ');',
        'create table Pokedex.tb_pokemons(' +
        'numero_geral int(10) not null auto_increment primary key,' +
        'nome varchar(50) not null,' +
        'tipo_1 int(10) not null,' +
        'tipo_2 int(10),' +
        'foto varchar(100) not null,' +
        'vida int not null,' +
        'defesa int not null,' +
        'ataque int not null,' +
        'região int(3) not null,' +
        'descrição varchar(500),' +
        'foreign key (tipo_2) references tb_tipos(id),' +
        'foreign key (tipo_1) references tb_tipos(id),' +
        'foreign key (região) references tb_regioes(id)' +
        ');'
    )
    for instrucao in conjunto:
        cursor.execute(instrucao)
    cursor.close()
    banco.close()


def inserir_registros():
    banco, cursor = conectar(True)
    SEPARADOR = '\\'
    endereco = path.dirname(path.realpath(__file__)).removesuffix('model') + 'assets' + SEPARADOR + 'fotos_pokemons' + SEPARADOR
    tipos = (
        'Aço', 'Dragão', 'Elétrico', 'Fada', 'Fantasma',
        'Fogo', 'Gelo', 'Grama', 'Inseto', 'Lutador',
        'NULL', 'Normal', 'Pedra', 'Psíquico', 'Terrestre',
        'Venenoso', 'Voador', 'Água'
    )
    regioes = (
        ('Kanto', 0),
        ('Jotho', 151),
        ('Hoen', 251),
        ('Sinnoh', 386),
        ('Unova', 494),
        ('Kalos', 649),
        ('Alola', 721),
        ('Galar', 809),
    )
    pokemons = (
        (1, 'Bulbassauro', 8, 16, endereco + '1.png', 49, 49, 45, 'Um Pokémon de planta e veneno que possui uma semente em suas costas. Conforme cresce, a semente se desenvolve em uma flor, ganhando força e habilidades que refletem seu vínculo com a natureza.', 1),
        (2, 'Ivyssauro', 8, 16, endereco + '2.png', 63, 62, 60, 'A evolução de Bulbasaur, com uma planta em crescimento nas costas. Quando está pronto para evoluir, a planta floresce.', 1),
        (3, 'Venussauro', 8, 16, endereco + '3.png', 83, 82, 80, 'A forma final de Bulbasaur, com uma grande flor que floresce em suas costas. A flor libera uma fragrância calmante que atrai Pokémon.', 1),
        (4, 'Charmander', 6, 11, endereco + '4.png', 43, 52, 39, 'Um Pokémon de fogo que possui uma chama na ponta da cauda. O calor da chama reflete a saúde e as emoções de Charmander; quanto mais saudável e confiante, mais intensa a chama brilha.', 1),
        (5, 'Charmeleon', 6, 11, endereco + '5.png', 58, 64, 58, 'A evolução de Charmander, com uma chama ainda maior e mais intensa na cauda. Ele é conhecido por sua natureza feroz e batalhadora.', 1),
        (6, 'Charizard', 6, 17, endereco + '6.png', 78, 84, 78, 'A forma final de Charmander, um poderoso Pokémon de fogo e voo. Seus ataques de fogo são devastadores, e ele é capaz de voar a grandes altitudes.', 1),
        (7, 'Squirtle', 18, 11, endereco + '7.png', 65, 48, 44, 'Um Pokémon de água que se protege dentro de seu casco. Ele expulsa água a alta pressão de sua boca para atacar inimigos e apagar incêndios.', 1),
        (8, 'Wartortle', 18, 11, endereco + '8.png', 80, 63, 59, 'A evolução de Squirtle, com um casco mais robusto e uma cauda maior. Ele é um nadador ágil e forte.', 1),
        (9, 'Blastoise', 18, 11, endereco + '9.png', 100, 83, 79, 'A forma final de Squirtle, equipado com canhões de água em seu casco. Ele usa esses canhões para lançar jatos de água poderosos.', 1),
        (10, 'Caterpie', 9, 11, endereco + '10.png', 35, 30, 45, 'Este pequeno Pokémon de inseto se alimenta vorazmente para ganhar energia necessária para evoluir. Ele pode exalar seda pegajosa para se proteger contra predadores.', 1),
        (11, 'Metapod', 9, 11, endereco + '11.png', 55, 20, 50, 'Após evoluir de Caterpie, este Pokémon endurece sua casca para se preparar para sua próxima evolução. Ele permanece imóvel, focando toda sua energia na transformação.', 1),
        (12, 'Butterfree', 9, 17, endereco + '12.png', 50, 45, 60, 'Um Pokémon de inseto e voo que possui asas cobertas de escamas. Essas escamas podem liberar um pó paralisante quando ele bate suas asas.', 1),
        (13, 'Weedle', 9, 16, endereco + '13.png', 30, 35, 40, 'Um Pokémon de inseto e veneno com um ferrão venenoso na cabeça. Ele se move através da vegetação rasteira, sempre em busca de folhas para mastigar.', 1),
        (14, 'Kakuna', 9, 16, endereco + '14.png', 50, 25, 45, 'A evolução de Weedle, que se envolve em uma casca dura enquanto seu corpo interno passa por uma grande transformação.', 1),
        (15, 'Beedrill', 9, 16, endereco + '15.png', 40, 90, 65, 'Um feroz Pokémon de inseto e veneno com três ferrões afiados. Ele é rápido e ataca com precisão, utilizando seus ferrões para proteger seu território.', 1),
        (16, 'Pidgey', 12, 17, endereco + '16.png', 40, 45, 40, 'Um Pokémon pássaro que é frequentemente encontrado em florestas e áreas urbanas. Ele usa suas asas para criar redemoinhos de areia para se proteger.', 1),
        (17, 'Pidgeotto', 12, 17, endereco + '17.png', 55, 60, 63, 'A evolução de Pidgey, maior e mais robusto, com visão aguçada para detectar presas à distância. Ele é um caçador habilidoso.', 1),
        (18, 'Pidgeot', 12, 17, endereco + '18.png', 75, 80, 83, 'A forma final de Pidgey, um Pokémon majestoso e extremamente rápido, capaz de voar a grandes altitudes e velocidades.', 1),
        (19, 'Rattata', 12, 11, endereco + '19.png', 35, 56, 30, 'Um Pokémon rato que se adapta rapidamente a qualquer ambiente. Seus dentes afiados podem roer praticamente qualquer coisa que encontrar.', 1),
        (20, 'Raticate', 12, 11, endereco + '20.png', 60, 81, 55, 'A evolução de Rattata, com dentes ainda mais poderosos e uma atitude agressiva. Ele é territorial e defende seu espaço ferozmente.', 1),
        (21, 'Spearow', 12, 17, endereco + '21.png', 30, 60, 40, 'Um pequeno pássaro conhecido por seu temperamento agressivo. Ele tem um grito penetrante que usa para intimidar adversários.', 1),
        (22, 'Fearow', 12, 17, endereco + '22.png', 65, 90, 65, 'A evolução de Spearow, um pássaro grande e intimidador com asas poderosas. Ele voa longas distâncias em busca de presas.', 1),
        (23, 'Ekans', 16, 11, endereco + '23.png', 44, 60, 35, 'Uma cobra venenosa que desliza silenciosamente pelo solo. Ele pode se enrolar para se proteger e ataca com um ferrão venenoso.', 1),
        (24, 'Arbok', 16, 11, endereco + '24.png', 69, 85, 60, 'A evolução de Ekans, com padrões intimidadores em seu corpo. Ele é forte e usa seu corpo para constranger inimigos.', 1),
        (25, 'Pikachu', 3, 11, endereco + '25.png', 40, 55, 35, 'Este Pokémon elétrico é conhecido por suas bochechas carregadas de eletricidade. Ele libera descargas elétricas para se defender e sinalizar emoções.', 1),
        (26, 'Raichu', 3, 11, endereco + '26.png', 55, 90, 60, 'A evolução de Pikachu, mais poderoso e com uma cauda que atua como um para-raios. Ele armazena energia elétrica em suas bochechas.', 1),
        (27, 'Sandshrew', 15, 11, endereco + '27.png', 85, 75, 50, 'Um Pokémon terrestre que cava túneis para se abrigar. Ele se enrola em uma bola para se proteger de ataques.', 1),
        (28, 'Sandslash', 15, 11, endereco + '28.png', 110, 100, 75, 'A evolução de Sandshrew, com garras afiadas para cavar e atacar. Sua pele é dura como aço.', 1),
        (29, 'NidoranF', 16, 11, endereco + '29.png', 52, 47, 55, 'Um Pokémon venenoso com pequenas orelhas e espinhos que usa para se defender.', 1),
        (30, 'Nidorina', 16, 11, endereco + '30.png', 67, 62, 70, 'A evolução de NidoranF, maior e com mais espinhos. Ela é protetora com seus companheiros.', 1),
        (31, 'Nidoqueen', 16, 15, endereco + '31.png', 87, 92, 90, 'A forma final de NidoranF, poderosa e defensiva. Seu corpo é coberto de escamas duras.', 1),
        (32, 'NidoranM', 16, 11, endereco + '32.png', 40, 57, 46, 'Um Pokémon venenoso com espinhos afiados e agressivos. Ele é rápido e sempre em alerta.', 1),
        (33, 'Nidorino', 16, 11, endereco + '33.png', 57, 72, 61, 'A evolução de NidoranM, maior e mais agressivo. Seus espinhos são venenosos e perigosos.', 1),
        (34, 'Nidoking', 16, 15, endereco + '34.png', 77, 102, 81, 'A forma final de NidoranM, forte e intimidador. Ele usa sua cauda e chifres para atacar.', 1),
        (35, 'Clefairy', 4, 11, endereco + '35.png', 48, 45, 70, 'Um Pokémon fada que adora a luz da lua. Ele usa sua dança mágica para atrair boa sorte e felicidade.', 1),
        (36, 'Clefable', 4, 11, endereco + '36.png', 73, 70, 95, 'A evolução de Clefairy, graciosa e encantadora. Suas asas permitem que ele salte levemente.', 1),
        (37, 'Vulpix', 6, 11, endereco + '37.png', 40, 41, 38, 'Um Pokémon de fogo com várias caudas que se iluminam brilhantemente. Quando evolui, suas caudas multiplicam-se, cada uma carregando uma chama interna.', 1),
        (38, 'Ninetales', 6, 11, endereco + '38.png', 75, 76, 73, 'A evolução de Vulpix, com nove caudas e habilidades místicas. Dizem que cada cauda contém poderes mágicos.', 1),
        (39, 'Jigglypuff', 12, 4, endereco + '39.png', 20, 45, 115, 'Um Pokémon fada que usa seu canto melodioso para fazer os oponentes dormirem. Sua voz suave é impossível de resistir.', 1),
        (40, 'Wigglytuff', 12, 4, endereco + '40.png', 45, 70, 140, 'A evolução de Jigglypuff, com uma voz ainda mais poderosa e uma pele incrivelmente macia.', 1),
        (41, 'Zubat', 16, 17, endereco + '41.png', 35, 45, 40, 'Um morcego que vive em cavernas escuras. Ele usa ecolocalização para navegar e encontrar presas no escuro.', 1),
        (42, 'Golbat', 16, 17, endereco + '42.png', 70, 80, 75, 'A evolução de Zubat, maior e com mordida venenosa. Ele é ágil e ataca rapidamente.', 1),
        (43, 'Oddish', 8, 16, endereco + '43.png', 55, 75, 45, 'Um Pokémon planta que se esconde no solo durante o dia, saindo à noite para absorver luz da lua.', 1),
        (44, 'Gloom', 8, 16, endereco + '44.png', 70, 85, 60, 'A evolução de Oddish, exalando um cheiro forte para se proteger. Seu cheiro pode ser tóxico.', 1),
        (45, 'Vileplume', 8, 16, endereco + '45.png', 85, 110, 75, 'A forma final de Oddish, com uma flor grande e tóxica que libera pólen venenoso.', 1),
        (46, 'Paras', 9, 8, endereco + '46.png', 55, 70, 35, 'Um Pokémon de inseto e planta que cultiva cogumelos em suas costas. Ele usa os cogumelos para se defender.', 1),
        (47, 'Parasect', 9, 8, endereco + '47.png', 80, 95, 60, 'A evolução de Paras, completamente dominado pelos cogumelos. Seus ataques são venenosos.', 1),
        (48, 'Venonat', 9, 16, endereco + '48.png', 50, 55, 60, 'Um inseto com olhos grandes que detectam presas no escuro. Ele emite uma luz fraca para atrair insetos.', 1),
        (49, 'Venomoth', 9, 16, endereco + '49.png', 60, 65, 70, 'A evolução de Venonat, uma mariposa que libera pó venenoso de suas asas.', 1),
        (50, 'Diglett', 15, 11, endereco + '50.png', 25, 55, 10, 'Um Pokémon terrestre que vive em túneis subterrâneos. Ele emerge ocasionalmente para procurar alimentos na superfície.', 1),
        (51, 'Dugtrio', 15, 11, endereco + '51.png', 50, 100, 35, 'A evolução de Diglett, três cabeças que trabalham juntas para cavar rapidamente.', 1),
        (52, 'Meowth', 12, 11, endereco + '52.png', 35, 45, 40, 'Um gato travesso que adora objetos brilhantes. Ele pode andar em duas patas e é conhecido por roubar moedas.', 1),
        (53, 'Persian', 12, 11, endereco + '53.png', 60, 70, 65, 'A evolução de Meowth, elegante e ágil como um felino. Ele é rápido e silencioso.', 1),
        (54, 'Psyduck', 18, 11, endereco + '54.png', 50, 52, 50, 'Um pato com poderes psíquicos que aparecem quando ele tem dores de cabeça intensas. Ele é frequentemente visto com uma expressão confusa.', 1),
        (55, 'Golduck', 18, 11, endereco + '55.png', 75, 82, 80, 'A evolução de Psyduck, um nadador ágil com poderes psíquicos controlados.', 1),
        (56, 'Mankey', 10, 11, endereco + '56.png', 35, 80, 40, 'Um macaco agitado que luta com força e velocidade. Ele é facilmente irritável e feroz em combate.', 1),
        (57, 'Primeape', 10, 11, endereco + '57.png', 60, 105, 65, 'A evolução de Mankey, ainda mais furioso e poderoso. Ele canaliza sua raiva em ataques devastadores.', 1),
        (58, 'Growlithe', 6, 11, endereco + '58.png', 45, 70, 55, 'Um cachorro de fogo leal e protetor. Ele é ferozmente devotado ao seu treinador e defenderá seu território com coragem.', 1),
        (59, 'Arcanine', 6, 11, endereco + '59.png', 80, 110, 90, 'A evolução de Growlithe, majestoso e rápido como um vento feroz. Suas lendas dizem que ele pode correr por dias sem se cansar.', 1),
        (60, 'Poliwag', 18, 11, endereco + '60.png', 40, 50, 40, 'Um girino com uma espiral na barriga que usa para hipnotizar. Ele é ágil tanto na terra quanto na água.', 1),
        (61, 'Poliwhirl', 18, 11, endereco + '61.png', 65, 65, 65, 'A evolução de Poliwag, com braços fortes e uma espiral hipnótica. Ele é um lutador versátil em terra e na água.', 1),
        (62, 'Poliwrath', 18, 10, endereco + '62.png', 95, 95, 90, 'A forma final de Poliwag, com músculos poderosos e habilidades de luta. Ele é um mestre nas batalhas aquáticas.', 1),
        (63, 'Abra', 14, 11, endereco + '63.png', 15, 20, 25, 'Um Pokémon psíquico que dorme a maior parte do tempo. Ele usa teletransporte para evitar perigo e se mover rapidamente.', 1),
        (64, 'Kadabra', 14, 11, endereco + '64.png', 30, 35, 40, 'A evolução de Abra, com habilidades psíquicas mais desenvolvidas. Ele carrega uma colher que amplifica seus poderes.', 1),
        (65, 'Alakazam', 14, 11, endereco + '65.png', 45, 50, 55, 'A forma final de Abra, um mestre dos poderes psíquicos. Seus cérebros altamente desenvolvidos concedem habilidades incríveis.', 1),
        (66, 'Machop', 10, 11, endereco + '66.png', 50, 80, 70, 'Um Pokémon lutador com músculos desenvolvidos. Ele está constantemente treinando para aumentar sua força.', 1),
        (67, 'Machoke', 10, 11, endereco + '67.png', 70, 100, 80, 'A evolução de Machop, ainda mais forte e musculoso. Ele usa cintos para controlar sua imensa força.', 1),
        (68, 'Machamp', 10, 11, endereco + '68.png', 80, 130, 90, 'A forma final de Machop, com quatro braços para lutas poderosas. Ele é capaz de realizar movimentos de luta extremamente complexos.', 1),
        (69, 'Bellsprout', 8, 16, endereco + '69.png', 35, 75, 50, 'Um Pokémon de planta que se move como uma videira. Ele captura insetos e outros pequenos Pokémon para se alimentar.', 1),
        (70, 'Weepinbell', 8, 16, endereco + '70.png', 50, 90, 65, 'A evolução de Bellsprout, com um corpo em forma de sino. Ele secreta uma substância ácida para dissolver suas presas.', 1),
        (71, 'Victreebel', 8, 16, endereco + '71.png', 65, 105, 80, 'A forma final de Bellsprout, com uma boca grande que engole presas inteiras. Seus líquidos digestivos são incrivelmente potentes.', 1),
        (72, 'Tentacool', 18, 16, endereco + '72.png', 35, 40, 40, 'Um Pokémon aquático com tentáculos venenosos. Ele vive no mar e usa seus tentáculos para se defender.', 1),
        (73, 'Tentacruel', 18, 16, endereco + '73.png', 65, 70, 80, "A evolução de Tentacool, com ainda mais tentáculos venenosos. Ele é conhecido como o 'Terror dos Mares'.", 1),
        (74, 'Geodude', 13, 15, endereco + '74.png', 100, 80, 40, 'Uma rocha viva que usa seu corpo robusto para rolar por terrenos difíceis. Ele é frequentemente encontrado em montanhas e cavernas.', 1),
        (75, 'Graveler', 13, 15, endereco + '75.png', 115, 95, 55, 'A evolução de Geodude, com um corpo maior e mais robusto. Ele rola por encostas de montanhas e estradas rochosas.', 1),
        (76, 'Golem', 13, 15, endereco + '76.png', 130, 110, 80, 'A forma final de Geodude, uma rocha gigante com imensa força. Ele pode se enrolar em uma bola e rolar a alta velocidade.', 1),
        (77, 'Ponyta', 6, 11, endereco + '77.png', 55, 85, 50, 'Um cavalo de fogo que corre a altas velocidades. Sua crina e cauda são feitas de chamas ardentes.', 1),
        (78, 'Rapidash', 6, 11, endereco + '78.png', 70, 100, 65, 'A evolução de Ponyta, ainda mais rápido e com uma crina de fogo. Ele é conhecido por sua velocidade incrível.', 1),
        (79, 'Slowpoke', 18, 14, endereco + '79.png', 65, 65, 90, 'Um Pokémon aquático que se move lentamente. Ele tem uma natureza relaxada e muitas vezes parece desatento.', 1),
        (80, 'Slowbro', 18, 14, endereco + '80.png', 110, 75, 95, 'A evolução de Slowpoke, com um parasita em sua cauda. Ele ganha poderes adicionais graças à simbiose.', 1),
        (81, 'Magnemite', 3, 1, endereco + '81.png', 95, 35, 25, 'Um Pokémon elétrico e metálico que flutua usando campos magnéticos. Ele pode gerar eletricidade para atacar.', 1),
        (82, 'Magneton', 3, 1, endereco + '82.png', 120, 60, 50, 'A evolução de Magnemite, três unidades que trabalham juntas. Ele emite poderosos campos magnéticos.', 1),
        (83, "Farfetch'd", 12, 17, endereco + '83.png', 55, 65, 52, 'Um pato que usa um alho-poró como arma. Ele é conhecido por sua habilidade em combate com este acessório.', 1),
        (84, 'Doduo', 12, 17, endereco + '84.png', 45, 85, 35, 'Um pássaro com duas cabeças que corre rapidamente. As cabeças pensam independentemente, mas trabalham em harmonia.', 1),
        (85, 'Dodrio', 12, 17, endereco + '85.png', 70, 110, 60, 'A evolução de Doduo, com três cabeças e habilidades de corrida aumentadas. Ele é extremamente rápido e alerta.', 1),
        (86, 'Seel', 18, 11, endereco + '86.png', 55, 45, 65, 'Um Pokémon aquático que nada graciosa e rapidamente. Sua pele é lisa e brilhante.', 1),
        (87, 'Dewgong', 18, 7, endereco + '87.png', 80, 70, 90, 'A evolução de Seel, com habilidades de natação ainda mais aprimoradas. Ele é gracioso e forte na água.', 1),
        (88, 'Grimer', 16, 11, endereco + '88.png', 50, 80, 80, 'Um Pokémon de lama e veneno que se move em áreas poluídas. Ele emite um odor forte e nocivo.', 1),
        (89, 'Muk', 16, 11, endereco + '89.png', 75, 105, 105, 'A evolução de Grimer, ainda maior e mais tóxico. Seu corpo é feito de substâncias nocivas e perigosas.', 1),
        (90, 'Shellder', 18, 11, endereco + '90.png', 180, 65, 30, 'Um Pokémon aquático com uma concha dura. Ele se fecha rapidamente para se proteger.', 1),
        (91, 'Cloyster', 18, 7, endereco + '91.png', 180, 95, 50, 'A evolução de Shellder, com uma concha ainda mais dura. Ele é conhecido por sua defesa impenetrável', 1),
        (92, 'Gastly', 5, 16, endereco + '92.png', 35, 35, 30, 'Um Pokémon fantasma feito de gás. Ele pode atravessar paredes e é conhecido por pregar peças assustadoras.', 1),
        (93, 'Haunter', 5, 16, endereco + '93.png', 55, 50, 45, 'A evolução de Gastly, com mãos flutuantes que ele usa para atacar. Ele é assustador e brincalhão.', 1),
        (94, 'Gengar', 5, 16, endereco + '94.png', 60, 65, 60, 'A forma final de Gastly, um Pokémon fantasma poderoso. Ele é conhecido por sua habilidade de se esconder nas sombras.', 1),
        (95, 'Onix', 13, 15, endereco + '95.png', 160, 45, 35, 'Uma cobra de rocha gigante que cava através do solo. Ele é forte e resistente.', 1),
        (96, 'Drowzee', 14, 11, endereco + '96.png', 45, 48, 60, 'Um Pokémon psíquico que adora sonhos. Ele pode hipnotizar seus oponentes e se alimentar de seus sonhos.', 1),
        (97, 'Hypno', 14, 11, endereco + '97.png', 70, 73, 85, 'A evolução de Drowzee, com habilidades hipnóticas mais avançadas. Ele carrega um pêndulo para amplificar seus poderes.', 1),
        (98, 'Krabby', 18, 11, endereco + '98.png', 105, 105, 30, 'Um caranguejo que vive nas praias. Ele usa suas grandes pinças para se defender e procurar alimentos.', 1),
        (99, 'Kingler', 18, 11, endereco + '99.png', 115, 130, 55, 'A evolução de Krabby, com pinças ainda maiores e mais fortes. Ele é conhecido por sua força impressionante.', 1),
        (100, 'Voltorb', 3, 11, endereco + '100.png', 50, 30, 40, 'Um Pokémon elétrico que se assemelha a uma Pokébola. Ele pode explodir quando perturbado.', 1),
        (101, 'Electrode', 3, 11, endereco + '101.png', 70, 50, 60, 'A evolução de Voltorb, com uma carga elétrica ainda maior. Ele é conhecido por sua capacidade de gerar explosões poderosas.', 1),
        (102, 'Exeggcute', 8, 14, endereco + '102.png', 80, 40, 60, 'Um grupo de ovos que trabalham em conjunto. Eles compartilham um vínculo telepático.', 1),
        (103, 'Exeggutor', 8, 14, endereco + '103.png', 95, 95, 95, 'A evolução de Exeggcute, uma palmeira com múltiplas cabeças. Ele é poderoso e utiliza ataques de planta e psíquico.', 1),
        (104, 'Cubone', 15, 11, endereco + '104.png', 95, 50, 50, 'Um Pokémon solitário que usa o crânio de sua mãe como capacete. Ele é conhecido por seu choro triste.', 1),
        (105, 'Marowak', 15, 11, endereco + '105.png', 110, 80, 60, 'A evolução de Cubone, que se tornou mais forte e determinado. Ele usa um osso como arma.', 1),
        (106, 'Hitmonlee', 10, 11, endereco + '106.png', 53, 120, 50, 'Um lutador especializado em chutes. Suas pernas podem se estender para realizar ataques poderosos.', 1),
        (107, 'Hitmonchan', 10, 11, endereco + '107.png', 79, 105, 50, 'Um lutador especializado em socos. Ele usa luvas de boxe para proteger suas mãos.', 1),
        (108, 'Lickitung', 12, 11, endereco + '108.png', 75, 55, 90, 'Um Pokémon com uma língua longa e pegajosa. Ele usa sua língua para capturar alimentos e se defender.', 1),
        (109, 'Koffing', 16, 11, endereco + '109.png', 95, 65, 40, 'Um Pokémon de gás venenoso que flutua no ar. Ele emite gases tóxicos de seu corpo.', 1),
        (110, 'Weezing', 16, 11, endereco + '110.png', 120, 90, 65, 'A evolução de Koffing, com dois corpos conectados. Ele libera gases venenosos ainda mais potentes.', 1),
        (111, 'Rhyhorn', 15, 13, endereco + '111.png', 95, 85, 80, 'Um Pokémon de rocha e terra com uma pele dura. Ele é forte e ataca com investidas poderosas.', 1),
        (112, 'Rhydon', 15, 13, endereco + '112.png', 120, 130, 105, 'A evolução de Rhyhorn, ainda mais forte e resistente. Ele pode perfurar rochas sólidas com seu chifre.', 1),
        (113, 'Chansey', 12, 11, endereco + '113.png', 5, 5, 250, 'Um Pokémon gentil e carinhoso que carrega um ovo nutritivo. Ele é frequentemente encontrado em centros Pokémon, ajudando a cuidar dos feridos.', 1),
        (114, 'Tangela', 8, 11, endereco + '114.png', 115, 55, 65, 'Um Pokémon de planta coberto por vinhas. Ele usa essas vinhas para prender inimigos.', 1),
        (115, 'Kangaskhan', 12, 11, endereco + '115.png', 80, 95, 105, 'Um Pokémon marsupial que carrega seu filhote em uma bolsa. Ela é extremamente protetora com seu jovem.', 1),
        (116, 'Horsea', 18, 11, endereco + '116.png', 70, 40, 30, 'Um pequeno cavalo-marinho que nada graciosamente. Ele dispara jatos de tinta para se defender.', 1),
        (117, 'Seadra', 18, 11, endereco + '117.png', 95, 65, 55, 'A evolução de Horsea, com espinhos venenosos em seu corpo. Ele é rápido e ágil, nadando graciosamente e disparando jatos de água potentes para afastar predadores.', 1),
        (118, 'Goldeen', 18, 11, endereco + '118.png', 60, 67, 45, 'Um belo peixe de água doce, conhecido por sua graciosidade ao nadar. Suas barbatanas são afiadas e podem ser usadas para atacar se necessário.', 1),
        (119, 'Seaking', 18, 11, endereco + '119.png', 65, 92, 80, 'A evolução de Goldeen, com um corpo mais robusto e um chifre afiado. Ele é conhecido por sua força e habilidade em enfrentar correntes fortes.', 1),
        (120, 'Staryu', 18, 11, endereco + '120.png', 85, 45, 30, 'Uma estrela-do-mar que brilha intensamente à noite. Ela pode regenerar qualquer parte de seu corpo que tenha sido danificada.', 1),
        (121, 'Starmie', 18, 14, endereco + '121.png', 85, 75, 60, 'A evolução de Staryu, ainda mais brilhante e com habilidades psíquicas. Seu núcleo emite uma luz mística que pode hipnotizar inimigos.', 1),
        (122, 'Mr. Mime', 14, 4, endereco + '122.png', 65, 45, 40, 'Mime: Um Pokémon que se especializa em criar barreiras invisíveis. Ele usa suas habilidades para confundir e proteger.', 1),
        (123, 'Scyther', 9, 17, endereco + '123.png', 80, 110, 70, 'Um Pokémon inseto voador com lâminas afiadas nos braços. Ele é extremamente rápido e mortal em combate.', 1),
        (124, 'Jynx', 7, 14, endereco + '124.png', 35, 50, 65, 'Um Pokémon psíquico e gelo com uma dança hipnotizante. Suas habilidades psíquicas são aprimoradas por sua dança.', 1),
        (125, 'Electabuzz', 3, 11, endereco + '125.png', 57, 83, 65, 'Um Pokémon elétrico que gera eletricidade em seu corpo. Ele é conhecido por sua velocidade e poderosos ataques elétricos.', 1),
        (126, 'Magmar', 6, 11, endereco + '126.png', 57, 95, 65, 'Um Pokémon de fogo que vive perto de vulcões. Seu corpo emite calor intenso e seus ataques são devastadores.', 1),
        (127, 'Pinsir', 9, 11, endereco + '127.png', 100, 125, 65, 'Um Pokémon inseto com grandes chifres. Ele usa seus chifres para esmagar e capturar suas presas.', 1),
        (128, 'Tauros', 12, 11, endereco + '128.png', 95, 100, 75, 'Um touro selvagem e agressivo. Ele é conhecido por sua força e velocidade ao correr.', 1),
        (129, 'Magikarp', 18, 11, endereco + '129.png', 55, 10, 20, 'Um peixe aparentemente fraco que salta incansavelmente. Dizem que com treinamento adequado, ele pode se transformar em algo incrível.', 1),
        (130, 'Gyarados', 18, 17, endereco + '130.png', 79, 125, 95, 'A evolução de Magikarp, um dragão de água temível e poderoso. Ele é conhecido por sua força devastadora e comportamento agressivo.', 1),
        (131, 'Lapras', 18, 7, endereco + '131.png', 80, 85, 130, "Um Pokémon de água e gelo, gentil e inteligente. Ele é frequentemente visto transportando pessoas e Pokémon através de corpos d'água.", 1),
        (132, 'Ditto', 12, 11, endereco + '132.png', 48, 48, 48, 'Um Pokémon que pode se transformar em qualquer outro Pokémon. Sua habilidade de transformação é quase perfeita.', 1),
        (133, 'Eevee', 12, 11, endereco + '133.png', 50, 55, 55, 'Um Pokémon com muitas possibilidades de evolução. Sua adaptabilidade o torna único entre os Pokémon.', 1),
        (134, 'Vaporeon', 18, 11, endereco + '134.png', 60, 65, 130, 'Uma das evoluções de Eevee, especializada em habilidades aquáticas. Suas nadadeiras e cauda o tornam um excelente nadador.', 1),
        (135, 'Jolteon', 3, 11, endereco + '135.png', 60, 65, 65, 'Uma das evoluções de Eevee, especializada em habilidades elétricas. Seu pelo emite descargas elétricas potentes.', 1),
        (136, 'Flareon', 6, 11, endereco + '136.png', 60, 130, 65, 'Uma das evoluções de Eevee, especializada em habilidades de fogo. Seu pelo é incrivelmente quente e emite calor intenso.', 1),
        (137, 'Porygon', 12, 11, endereco + '137.png', 70, 60, 65, 'Um Pokémon criado artificialmente que pode entrar em ciberespaços. Ele é composto de dados e pode mudar sua forma.', 1),
        (138, 'Omanyte', 13, 18, endereco + '138.png', 100, 40, 35, 'Um antigo Pokémon de água com uma concha espiral. Ele é frequentemente encontrado em fósseis e pode ser ressuscitado.', 1),
        (139, 'Omastar', 13, 18, endereco + '139.png', 125, 60, 70, 'A evolução de Omanyte, com tentáculos poderosos e uma concha dura. Ele é um predador eficiente e usa seus tentáculos para capturar presas.', 1),
        (140, 'Kabuto', 13, 18, endereco + '140.png', 90, 80, 30, 'Um antigo Pokémon de água com uma carapaça dura. Ele é frequentemente encontrado em fósseis e pode ser ressuscitado.', 1),
        (141, 'Kabutops', 13, 18, endereco + '141.png', 105, 115, 60, 'A evolução de Kabuto, com lâminas afiadas em seus braços. Ele é um predador ágil e letal.', 1),
        (142, 'Aerodactyl', 13, 17, endereco + '142.png', 65, 105, 80, 'Um antigo Pokémon voador que se assemelha a um pterodáctilo. Ele é rápido e tem habilidades de voo impressionantes.', 1),
        (143, 'Snorlax', 12, 11, endereco + '143.png', 65, 110, 160, 'Um Pokémon gigante e preguiçoso que adora dormir. Quando acordado, ele é incrivelmente forte e pode ser um poderoso aliado.', 1),
        (144, 'Articuno', 7, 17, endereco + '144.png', 100, 85, 90, 'Um dos pássaros lendários de Kanto, com habilidades de gelo. Suas asas emitem uma nevasca gelada.', 1),
        (145, 'Zapdos', 3, 17, endereco + '145.png', 85, 90, 90, 'Um dos pássaros lendários de Kanto, com habilidades elétricas. Suas asas geram relâmpagos e trovões.', 1),
        (146, 'Moltres', 6, 17, endereco + '146.png', 90, 100, 90, 'Um dos pássaros lendários de Kanto, com habilidades de fogo. Suas asas emitem chamas ardentes.', 1),
        (147, 'Dratini', 2, 11, endereco + '147.png', 50, 64, 41, 'Um Pokémon dragão pequeno e raro. Ele é tímido e vive em profundezas aquáticas.', 1),
        (148, 'Dragonair', 2, 11, endereco + '148.png', 70, 84, 61, 'A evolução de Dratini, com um corpo elegante e habilidades místicas. Ele é conhecido por seu comportamento pacífico.', 1),
        (149, 'Dragonite', 2, 17, endereco + '149.png', 95, 134, 91, 'A forma final de Dratini, um dragão poderoso e nobre. Ele é gentil e protetor, mas pode ser feroz em combate.', 1),
        (150, 'Mewtwo', 14, 11, endereco + '150.png', 90, 110, 106, 'Um Pokémon psíquico criado artificialmente. Ele é incrivelmente poderoso e possui habilidades psíquicas imensas.', 1),
        (151, 'Mew', 14, 11, endereco + '151.png', 100, 100, 100, 'Um Pokémon místico e raro, conhecido por ser a base genética de Mewtwo. Ele é pequeno, mas possui todas as habilidades dos outros Pokémon.', 1)
    )
    banco.commit()
    for tipo in tipos:
            cursor.execute('insert into tb_tipos (id, nome) values (default, %s);',
                           (tipo, ))
    banco.commit()
    for info in regioes:
        cursor.execute('insert into tb_regioes (id, nome, offset) ' +
                       'values (default, %s, %s);',
                       info)
    banco.commit()
    for pokemon in pokemons:
        cursor.execute('insert into tb_pokemons (numero_geral, nome, tipo_1, tipo_2, foto, ataque, defesa, vida, descrição, região) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);', pokemon)
    banco.commit()
    cursor.close()
    banco.close()
