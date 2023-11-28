start :-
    write('Bem-vindo ao mistério do assassinato do Sr. Richard!'), nl,
    write('O Sr. Richard era conhecido por sua coleção valiosa de obras raras na biblioteca,'), nl,
    write('Na mansão, dez suspeitos estão sob investigação: Sra. Scarlett, Sr. Greg, Sra. White, Dr. Felix, Sr. Mustang, Sra. Pires, Sr. Boris, Srta. Belmont, Sr. Pretz e Sra. Luz.'), nl,
    write('O assassinato aconteceu na biblioteca, onde foi encontrada uma taça de vinho derramada.'), nl,
    write('o Dr Felix foi fazer uma visita médica ao sr Richard naquela tarde.'), nl,
    write('O Sr Pretz, o mordomo, viu alguém saindo da biblioteca na tarde do assassinato.'), nl,
    write('Sr. Greg estava presente na biblioteca durante a noite do assassinato e notou algo suspeito,'), nl,
    write('Sra. Pires foi ouvida discutindo com o Sr. Richard na noite do assassinato,'), nl,
    write('Sr. Boris, o jardineiro da mansão, disse que estava na cidade comprando fertilizante a maior parte do dia,'), nl,
    write('e a Sra. Belmont tinha uma reunião marcada com o Sr.Richard naquela noite pra discutir a venda de algumas obras.'), nl,
    write('O Sr. Mustang, um colecionador rival, havia tentando entrar em contato com Sr Richard naquela tarde.'), nl,
    write('e a Sra. Scarlett também tinha interesse especial pela coleção do Sr. Richard.'), nl,
    write('e a Sra. Luz estava viajando e ao chegar na sua mansão, encontrou o corpo sem vida do sr Richard.'), nl,
    write('Havia uma atmosfera de tensão na biblioteca, mas apenas um indivíduo parecia estar perdido em pensamentos.'), nl,
    write('Lista de Perguntas que o jogador pode fazer:'), nl,
    write('Digite "estava_na_casa(X)." para descobrir quem estava na casa.'), nl,
    write('Digite "relacao_com_o_assassinado(X,R)." para descobrir a relação do suspeito com o assassinado.'), nl,
    write('Digite "relacao_entre_os_suspeitos(X, Y, R)." para descobrir a relação entre os suspeitos.'), nl,
    write('Digite "imprimir_fatos_conhecidos_policia." para descobrir os fatos conhecidos pela polícia.'), nl,
    write('Digite "culpado(X)." para descobrir quem é o culpado pelo assassinato.'), nl.


% Fatos dos suspeitos
suspeito(sra_scarlett).
suspeito(sr_greg).
suspeito(sra_white).
suspeito(dr_felix).
suspeito(sr_mustang).
suspeito(sra_pires).
suspeito(sr_boris).
suspeito(sra_belmont).
suspeito(srt_pretz).
suspeito(sra_luz).






















% Fatos sobre quem estava na casa
estava_na_casa(sra_pires).
estava_na_casa(sra_scarlett).
estava_na_casa(sra_white).
estava_na_casa(sra_luz).
estava_na_casa(dr_felix).

% Fatos sobre quem tinha interesse na obra
interesse_na_obra(sra_scarlett).
interesse_na_obra(sr_greg).
interesse_na_obra(sra_belmont).
interesse_na_obra(sr_mustard).

% Fatos sobre quem possuia a Chave
possui_chave(sr_richard).
possui_chave(sr_boris).
possui_chave(sra_scarlett).
possui_chave(sra_luz).

% Relações com o assassinado
relacao_com_o_assassinado(sra_scarlett,funcionaria).
relacao_com_o_assassinado(sra_white,funcionaria).
relacao_com_o_assassinado(dr_felix,medico).
relacao_com_o_assassinado(sr_boris,funcionario).
relacao_com_o_assassinado(sr_pretz,funcionario).
relacao_com_o_assassinado(sr_greg,funcionario).
relacao_com_o_assassinado(sr_mustang,concorrente).
relacao_com_o_assassinado(sra_belmont,cliente).
relacao_com_o_assassinado(sra_luz,eposa).
relacao_com_o_assassinado(sra_pires,parceira_comercial).

% Relações entre os suspeitos
relacao_entre_suspeitos(sra_scarlett, sr_boris, esposa).
relacao_entre_suspeitos(sr_boris, sra_scarlett, esposo).
relacao_entre_suspeitos(sra_scarlett, sra_luz, patroa).
relacao_entre_suspeitos(sra_luz, sra_scarlett, funcionaria).
relacao_entre_suspeitos(sra_luz, sra_scarlett, patroa).
relacao_entre_suspeitos(sra_scarlett, sra_white, colegas).
relacao_entre_suspeitos(sra_white, sra_scarlett, colegas).
relacao_entre_suspeitos(sr_pretz, sra_luz, funcionario).
relacao_entre_suspeitos(sra_luz, sr_pretz, patroa).
relacao_entre_suspeitos(sr_boris, sra_luz, funcionario).
relacao_entre_suspeitos(sra_luz, sr_boris, patroa).
relacao_entre_suspeitos(sra_white, sra_luz, funcionario).
relacao_entre_suspeitos(sra_luz, sra_white, patroa).
relacao_entre_suspeitos(sra_scarlett, srt_pretz, colega).
relacao_entre_suspeitos(srt_pretz, sra_scarlett, colega).


% Fatos conhecidos pela polícia
imprimir_fatos_conhecidos_policia :-
    write('Fatos conhecidos pela polícia:'), nl,
    write('1. A policia descobriu que na estufa tem plantas venenosas mas que a mesma estava trancada.'), nl,
    write('2. Dr. Felix foi visto manuseando objetos cortantes pouco antes do incidente.'), nl,
    write('3. Sra. Scarlett foi vista saindo da biblioteca pouco antes do assassinato.'), nl,
    write('4. Sra. White serviu a taça de vinho que foi encontrada derramada na cena do crime,'), nl,
    write('5. A suspeita da causa da morte é envenenamento.'), nl.


interrogar_suspeito(sr_boris) :-
    write('Foi descoberto que outra pessoa além dele tem a chave, sua esposa.'),
    nl.

interrogar_suspeito(sr_greg) :-
    write('Foi descoberto que o sr Greg notou que uma das obras favoritas do Sr Richard não estava na biblioteca.'),
    nl.

interrogar_suspeito(sr_pretz) :-
    write('Foi descoberto que o sr Pretz viu a senhora Scarlett saindo da biblioteca na tarde do assassinato.'),
    nl.

interrogar_suspeito(sra_luz) :-
    write('Foi descoberto que o sr Mustang estava ameaçando o sr Richard por mensagens.'),
    nl.

interrogar_suspeito(dr_felix) :-
    write('Dr. Felix afirmou que o Sr. Richard estava em boa saúde.'),
    nl.

interrogar_suspeito(sr_mustang) :-
    write('A polícia não conseguiu contatar o sr Mustang.'),
    nl.

interrogar_suspeito(sra_pires) :-
    write('Foi descoberto que o senhor Richard estava com problemas financeiros e este foi o motivo da discussão com a sua parceira comercial.'),
    nl.

interrogar_suspeito(sra_belmont) :-
    write('Foi descoberto que o senhor Richard estava pretendendo vender algumas obras.'),
    nl.

interrogar_suspeito(sra_white) :-
    write('Foi descoberto que o dr Felix foi visto manuseando objetos cortantes pouco antes do incidente.'),
    nl.

interrogar_suspeito(sra_scarlett) :-
    write('A senhora Scarlett chorava muito e não conseguiu prestar depoimento.'),
    nl.

culpado(Suspeito) :-
    suspeito(Suspeito),
    possui_chave(Suspeito),
    esteve_na_casa(Suspeito),
    interesse_na_obra(Suspeito).