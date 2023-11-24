start :-
    write('Bem-vindo ao mistério do assassinato do Sr. Richard!'), nl,
    write('O Sr. Richard era conhecido por sua coleção valiosa de obras raras na biblioteca,'), nl,
    write('Na mansão, oito suspeitos estão sob investigação: Sra. Scarlett, Sr. Green, Sra. White, Dr. Plum, Sr. Mustard, Sra. Peacock, Sr. Brown e Srta. Blue.'), nl,
    write('O assassinato aconteceu na biblioteca, onde foi encontrada uma taça de vinho derramada, a suspeita é de envenenamento.'), nl,
    write('A Sra. Scarlett foi vista saindo da biblioteca pouco antes do assassinato.'), nl,
    write('Sr. Green estava presente na biblioteca durante a noite do assassinato e notou que uma das obras favoritas do Sr. Richard não estava na biblioteca,'), nl,
    write('Dr. Plum foi visto manuseando objetos cortantes pouco antes do incidente,'), nl,
    write('Sra. White serviu a taça de vinho que foi encontrada derramada na cena do crime,'), nl,
    write('Sra. Peacock foi ouvida discutindo com o Sr. Richard na noite do assassinato,'), nl,
    write('Sr. Brown, jardineiro e marido da  Sra. Scarlett disse que estava na cidade comprando fertilizante a maior parte do dia,'), nl,
    write('O Sr. Mustard, um colecionador rival, havia ameaçado o Sr. Richard para tentar adquirir suas obras.'), nl,
    write('e a Sra. Scarlett também tinha interesse especial pela coleção do Sr. Richard.'), nl,
    write('e a Srta. Blue tinha uma reunião marcada com o Sr.Richard naquela noite.'), nl,
    write('A policia descobriu que na estufa tem plantas venenosas mas trancada,'), nl,
    write('Havia uma atmosfera de tensão na biblioteca, mas apenas um indivíduo parecia estar perdido em pensamentos.'), nl,
    write('Digite "culpado(X)." para descobrir quem é o culpado pelo assassinato.'), nl.


% Fatos dos suspeitos
suspeito(sra_scarlett).
suspeito(sr_green).
suspeito(sra_white).
suspeito(dr_plum).
suspeito(sr_mustard).

% quem estava em casa? 
% tinha acesso a estufa
% Fatos das atividades dos suspeitos
atividade(sra_scarlett, estava_mudando_roupa).
atividade(sr_green, estava_fazendo_negocios).
atividade(sra_white, estava_cozinhando).
atividade(dr_plum, estava_lendo_livros).
atividade(sr_mustard, estava_andando_jardim).

% lista de perguntas que o usuario pode fazer
% suspeitos_no_local(biblioteca).
% sabe_fatos(policia). // o envenenamento pode ter ocorrido usando as plantas da estufa e pra ter o acesso a ela tinha que ter a chave

% Local onde o assassinato aconteceu
local(escritorio).

% Fatos sobre a vítima e o local do assassinato
vitima(sr_richard).
taça_vinho_derramada(escritorio).

% Fatos sobre a senha do cofre
senha_cofre(sra_scarlett). % Suposição de que apenas ela tinha a senha do cofre.

% Regra para determinar o culpado
culpado(Suspeito) :-
    suspeito(Suspeito),
    atividade(Suspeito, estava_mudando_roupa),
    local(escritorio),
    taça_vinho_derramada(escritorio),
    senha_cofre(Suspeito).
