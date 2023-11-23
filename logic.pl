start :-
    write('Bem-vindo ao mistério da Mansão Ravenwood!'), nl,
    write('Na noite do assassinato do senhor Alfred, um baile extravagante estava em pleno andamento na suntuosa mansão.'), nl,
    write('Entre os eventos da noite, os convidados desfrutavam de um cardápio refinado com iguarias como filé mignon, camarões grelhados e sobremesas luxuosas.'), nl,
    write('O mordomo, conhecido por sua atenção aos detalhes, supervisionava pessoalmente o serviço de bebidas e os talheres de prata.'), nl,
    write('A esposa do senhor Alfred encantava a todos com sua simpatia e seu vestido luxoso.'), nl,
    write('A senhora da casa, uma entusiasta de música clássica, encantava os convidados tocando piano na sala principal.'), nl,
    write('O professor da filha do Sr. Black, um aficionado por astronomia, foi visto observando as estrelas no jardim.'), nl,
    write('O coveiro local, que adora jardinagem, estava examinando as flores do jardim de inverno.'), nl,
    write('A governanta, responsável pela organização do evento, circulava entre os convidados, atendendo às suas necessidades.'), nl,
    write('O jardineiro, frequentemente visto cuidando do jardim, estava especialmente ocupado com a manutenção das plantas durante o baile.'), nl,
    write('Apesar de todo o glamour, os detalhes sobre as atividades de cada suspeito durante o baile são um tanto nebulosos.'), nl,
    write('Várias testemunhas relataram que o culpado estava usando uma camisa vermelha na noite do crime.'), nl,
    write('Digite "suspeito_no_local(X, Local)." para saber se um suspeito esteve em um local específico.'), nl,
    write('Digite "suspeitos_no_local(Local)." para saber quem estava no local do crime.'), nl,
    write('Digite "culpado(X)." para verificar quem é o culpado.'), nl,
    write('Digite "cor_da_camisa_do_suspeito(Suspeito, Cor)." para descobrir a cor da camisa de um suspeito.'), nl.


% Suspeitos
suspeito(professor).
suspeito(mordomo).
suspeito(senhora).
suspeito(coveiro).
suspeito(filha_professor).
suspeito(guarda_florestal).
suspeito(cozinheiro).
suspeito(advogado).
suspeito(garcom).
suspeito(motorista).
suspeito(esposa_assassinado).

% Armas
arma(faca).
arma(corda).
arma(revolver).
arma(candelabro).

% Locais
local(estudo).
local(cozinha).
local(sala).
local(jardim).
local(jardim_2).
local(piscina).
local(biblioteca).
local(observatorio).

% Relações de quem esteve onde
esteve(professor, estudo).
esteve(mordomo, cozinha).
esteve(senhora, sala).
esteve(coveiro, jardim).

% Relações de quem usou qual arma
usou(professor, faca).
usou(mordomo, corda).
usou(senhora, revolver).
usou(coveiro, candelabro).

/* Defina regras sobre a cor da camisa de cada suspeito */
cor_da_camisa(professor, vermelha).
cor_da_camisa(mordomo, azul).
cor_da_camisa(senhora, verde).
cor_da_camisa(coveiro, amarela).
cor_da_camisa(filha_professor, branca).
cor_da_camisa(guarda_florestal, preto).
cor_da_camisa(cozinheiro, vermelha).
cor_da_camisa(advogado, azul).
cor_da_camisa(garcom, preto).
cor_da_camisa(motorista, vermelha).
cor_da_camisa(esposa_assassino, vermelha).


/* Defina regras sobre onde cada suspeito estava */
onde_estava(mordomo, sala_principal).
onde_estava(senhora, cozinha).
onde_estava(professor, biblioteca).
onde_estava(coveiro, jardim).
onde_estava(filha_professor, estudo).
onde_estava(guarda_florestal, jardim_2).
onde_estava(cozinheiro, cozinha).
onde_estava(advogado, biblioteca).

/* Pergunta ao usuário sobre um suspeito em um local específico */
suspeito_no_local(Suspeito, Local) :-
    onde_estava(Suspeito, Local),
    write(Suspeito), write(' estava na '), write(Local), write('.'), nl.

/* Pergunta ao usuário sobre os suspeitos no local do crime */
suspeitos_no_local(Local) :-
    onde_estava(Suspeito, Local),
    write('O(s) suspeito(s) no local '), write(Local), write(' são: '), write(Suspeito), nl,
    fail.
suspeitos_no_local(_).

% Regras para determinar o culpado
/* Atualize a regra para determinar o culpado */
% Regras para determinar o culpado
culpado(X) :- suspeito(X), esteve(X, estudo), usou(X, faca), usava_camisa_vermelha(X).