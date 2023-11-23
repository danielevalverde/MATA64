start :-
    write('Bem-vindo ao mistério da Mansão Ravenwood!'), nl,
    write('Um assassinato chocante aconteceu na casa do famoso magnata, Sr. Black.'), nl,
    write('Seu corpo foi descoberto na sala principal da mansão.'), nl,
    write('A polícia identificou quatro suspeitos: o mordomo, a senhora da casa, o professor da filha do Sr. Black e o coveiro local.'), nl,
    write('Além disso, quatro armas foram encontradas perto do local do crime: uma faca, uma corda, um revólver e um candelabro.'), nl,
    write('Digite "suspeito_no_local(X, Local)." para saber se um suspeito esteve em um local específico.'), nl,
    write('Digite "suspeitos_no_local(X)." para saber quem estava no local do crime.'), nl,
    write('Digite "culpado(X)." para verificar quem é o culpado.'), nl.

% Suspeitos
suspeito(professor).
suspeito(mordomo).
suspeito(senhora).
suspeito(coveiro).

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

/* Defina regras sobre onde cada suspeito estava */
onde_estava(mordomo, sala_principal).
onde_estava(senhora, cozinha).
onde_estava(professor, biblioteca).
onde_estava(coveiro, jardim).

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
culpado(X) :- suspeito(X), esteve(X, estudo), usou(X, faca).