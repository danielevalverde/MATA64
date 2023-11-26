start :-
    write('Bem-vindo ao mistério do assassinato do Sr. Richard!'), nl,
    write('O Sr. Richard era conhecido por sua coleção valiosa de obras raras na biblioteca,'), nl,
    write('Na mansão, dez suspeitos estão sob investigação: Sra. Scarlett, Sr. Green, Sra. White, Dr. Plum, Sr. Mustard, Sra. Peacock, Sr. Brown, Srta. Blue, Sr. Pretz e Sra. Luz.'), nl,
    write('O assassinato aconteceu na biblioteca, onde foi encontrada uma taça de vinho derramada.'), nl,
    write('o Dr Plum foi fazer uma visita médica ao sr Richard naquela tarde.'), nl,
    write('O Sr Pretz, o mordomo, viu alguém saindo da biblioteca na tarde do assassinato.'), nl,
    write('Sr. Green estava presente na biblioteca durante a noite do assassinato e notou algo suspeito,'), nl,
    write('Sra. Peacock foi ouvida discutindo com o Sr. Richard na noite do assassinato,'), nl,
    write('Sr. Brown, jardineiro disse que estava na cidade comprando fertilizante a maior parte do dia,'), nl,
    write('e a Srta. Blue tinha uma reunião marcada com o Sr.Richard naquela noite pra discutir a venda de algumas obras.'), nl,
    write('O Sr. Mustard, um colecionador rival, havia tentando entrar em contato com Sr Richard naquela tarde.'), nl,
    write('e a Sra. Scarlett também tinha interesse especial pela coleção do Sr. Richard.'), nl,
    write('e a Sra. Luz encontrou o corpo sem vida do sr Richard.'), nl,
    write('Havia uma atmosfera de tensão na biblioteca, mas apenas um indivíduo parecia estar perdido em pensamentos.'), nl,
    write('Lista de Perguntas que o jogador pode fazer:'), nl,
    write('Digite "estava_na_casa(X)." para descobrir quem estava na casa.'), nl,
    write('Digite "relacao_com_assassinado(X)." para descobrir a relação do suspeito com o assassinado.'), nl,
    write('Digite "relacao_entre_os_suspeitos(X, Y, R)." para descobrir a relação entre os suspeitos.'), nl,
    write('Digite "imprimir_fatos_conhecidos_policia." para descobrir os fatos conhecidos pela polícia.'), nl,
    write('Digite "culpado(X)." para descobrir quem é o culpado pelo assassinato.'), nl.


% Fatos dos suspeitos
suspeito(sra_scarlett).
suspeito(sr_green).
suspeito(sra_white).
suspeito(dr_plum).
suspeito(sr_mustard).
suspeito(sra_peacock).
suspeito(sr_brown).
suspeito(srt_blue).
suspeito(srt_pretz).
suspeito(sra_luz).

% Relações de quem estava na casa
estava_na_casa(sra_peacock).
estava_na_casa(sra_scarlett).
estava_na_casa(sra_white).
estava_na_casa(dr_plum).


% interesse na obra
interesse_na_obra(sra_scarlett).
interesse_na_obra(sr_green).
interesse_na_obra(srt_blue).
interesse_na_obra(srt_mustard).
interesse_na_obra(sra_luz).

% Chave
possui_chave(sr_richard).
possui_chave(sr_brown).
possui_chave(sra_scarlett).
possui_chave(sra_luz).

% Relações com o assassinado
relacao_com_o_assassinado(sra_scarlett,funcionaria).
relacao_com_o_assassinado(sra_white,funcionaria).
relacao_com_o_assassinado(dr_plum,medico).
relacao_com_o_assassinado(sr_brown,funcionario).
relacao_com_o_assassinado(sr_pretz,funcionario).
relacao_com_o_assassinado(sr_green,funcionario).
relacao_com_o_assassinado(sr_mustard,concorrente).
relacao_com_o_assassinado(sra_blue,cliente).
relacao_com_o_assassinado(sra_luz,eposa).
relacao_com_o_assassinado(sra_peacock,parceira_comercial).

% Relações entre os suspeitos
relacao_entre_suspeitos(sr_brown, sra_scarlett, esposo).
relacao_entre_suspeitos(sra_scarlett, sr_brown, esposa).
relacao_entre_suspeitos(sra_scarlett, sr_luz, funcionaria).
relacao_entre_suspeitos(sra_luz, sra_scarlett, patroa).

% Fatos conhecidos pela polícia
imprimir_fatos_conhecidos_policia :-
    write('Fatos conhecidos pela polícia:'), nl,
    write('1. A policia descobriu que na estufa tem plantas venenosas mas que a mesma estava trancada.'), nl,
    write('2. Dr. Plum foi visto manuseando objetos cortantes pouco antes do incidente.'), nl,
    write('3. Sra. Scarlett foi vista saindo da biblioteca pouco antes do assassinato.'), nl,
    write('4. Sra. White serviu a taça de vinho que foi encontrada derramada na cena do crime,'), nl,
    write('5. A suspeita da causa da morte é envenenamento.'), nl.


interrogar_suspeito(sr_brown) :-
    write('Foi descoberto que outra pessoa além dele tem a chave, sua esposa.'),
    nl.

interrogar_suspeito(sr_green) :-
    write('Foi descoberto que o sr Green notou que uma das obras favoritas do Sr Richard não estava na biblioteca.'),
    nl.

interrogar_suspeito(sr_pretz) :-
    write('Foi descoberto que o sr Pretz viu a senhora Scarlett saindo da biblioteca na tarde do assassinato.'),
    nl.

interrogar_suspeito(sra_luz) :-
    write('Foi descoberto que o sr Mustard estava ameaçando o sr Richard.'),
    nl.

interrogar_suspeito(dr_plum) :-
    write('Dr. Plum afirmou que o Sr. Richard estava em boa saúde.'),
    nl.

interrogar_suspeito(sr_mustard) :-
    write('A polícia não conseguiu contatar o sr Mustard.'),
    nl.

interrogar_suspeito(sr_mustard) :-
    write('Foi descoberto que o senhor Richard estava com problemas financeiros e este foi o motivo da discussão com a sua parceira comercial.'),
    nl.

interrogar_suspeito(sra_blue) :-
    write('Foi descoberto que o senhor Richard estava pretendendo vender algumas obras.'),
    nl.

interrogar_suspeito(sra_white) :-
    write('Foi descoberto que o dr Plum foi visto manuseando objetos cortantes pouco antes do incidente.'),
    nl.

interrogar_suspeito(sra_scarlett) :-
    write('A senhora Scarlett chorava muito e não conseguiu prestar depoimento.'),
    nl.

culpado(Suspeito) :-
    suspeito(Suspeito),
    possui_chave(Suspeito),
    esteve_na_casa(Suspeito),
    interesse_na_obra(Suspeito).