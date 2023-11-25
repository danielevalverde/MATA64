start :-
    write('Bem-vindo ao mistério do assassinato do Sr. Richard!'), nl,
    write('O Sr. Richard era conhecido por sua coleção valiosa de obras raras na biblioteca,'), nl,
    write('Na mansão, oito suspeitos estão sob investigação: Sra. Scarlett, Sr. Green, Sra. White, Dr. Plum, Sr. Mustard, Sra. Peacock, Sr. Brown e Srta. Blue.'), nl,
    write('O assassinato aconteceu na biblioteca, onde foi encontrada uma taça de vinho derramada.'), nl,
    write('o Dr Plum foi fazer uma visita médica ao sr Richard naquela tarde.'), nl,
    write('A Sra. Scarlett foi vista saindo da biblioteca pouco antes do assassinato.'), nl,
    write('Sr. Green estava presente na biblioteca durante a noite do assassinato e notou que uma das obras favoritas do Sr. Richard não estava na biblioteca,'), nl,
    write('Sra. Peacock foi ouvida discutindo com o Sr. Richard na noite do assassinato,'), nl,
    write('Sr. Brown, jardineiro e marido da  Sra. Scarlett disse que estava na cidade comprando fertilizante a maior parte do dia,'), nl,
    write('e a Sra. Scarlett também tinha interesse especial pela coleção do Sr. Richard.'), nl,
    write('e a Srta. Blue tinha uma reunião marcada com o Sr.Richard naquela noite.'), nl,
    write('Havia uma atmosfera de tensão na biblioteca, mas apenas um indivíduo parecia estar perdido em pensamentos.'), nl,
    write('Lista de Perguntas que o jogador pode fazer:'), nl,
    write('Digite "estava_na_casa(X)." para descobrir quem estava na casa.'), nl,
    write('Digite "relacao_com_assassinado(X)." para descobrir a relação do suspeito com o assassinado.'), nl,
    write('Digite "relacao_entre_os_suspeitos(X, Y)." para descobrir a relação entre os suspeitos.'), nl,
    write('Digite "fatos_conhecidos_pela_policia." para descobrir os fatos conhecidos pela polícia.'), nl,
    write('Digite "culpado(X)." para descobrir quem é o culpado pelo assassinato.'), nl.


% Fatos dos suspeitos
suspeito(sra_scarlett).
suspeito(sr_green).
suspeito(sra_white).
suspeito(dr_plum).
suspeito(sr_mustard).

% Relações de quem esteva na casa

esteve_na_casa(sra_peacock).
esteve_na_casa(sra_scarlett).
esteve_na_casa(sra_white).


% Chave
possui_chave(sr_Richard).
possui_chave(sr_brown).
possui_chave(sra_scarlett).


% Relações com o assassinado
relacao_com_o_assassinado(sra_scarlett,funcionaria).
relacao_com_o_assassinado(dr_plum,medico).

% Relações entre os suspeitos
relacao_entre_suspeitos(sr_brown, sra_scarlett, esposo).
relacao_entre_suspeitos(sra_scarlett, sra_brow, esposa).

% Fatos conhecidos pela polícia
imprimir_fatos_conhecidos_policia :-
    write('Fatos conhecidos pela polícia:'), nl,
    write('1. A policia descobriu que na estufa tem plantas venenosas mas que a mesma estava trancada.'), nl,
    write('2. Dr. Plum foi visto manuseando objetos cortantes pouco antes do incidente.'), nl,
    write('3. Sra. Scarlett foi vista saindo da biblioteca pouco antes do assassinato.'), nl,
    write('4. Sra. White serviu a taça de vinho que foi encontrada derramada na cena do crime,'), nl,
    write('5. A suspeita da causa da morte é envenenamento.'), nl.


interrogar_suspeito(sr_brown) :-
    possui_chave(sr_brown),
    relacao_entre_suspeitos(sr_brown, sra_scarlett, esposo),
    write('Foi descoberto que outra pessoa além dele tem a chave, sua esposa.'),
    nl.


