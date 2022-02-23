# Simulação do modelo neuronal dinâmico de Hindmarsch-Rose

Projeto desenvolvido durante a disciplina de Física Computacional pertencente ao bacharelado em Física Médica da FFCLRP-USP. A íntegra do texto se encontra nos arquivos do repositório.

## Resumo

s potenciais de ação das membranas das células nervosas podem ser modelados matematicamente. O modelo de Hindmarsch-Rose (HR) é um sistema dinâmico com a proposta de descrever essa atividade celular. Deste modo, o objetivo do presente projeto é estudar e simular o comportamento do sistema dinâmico de HR com base no trabalho de Lima et al.**[1]**. O principal parâmetro a avaliar no modelo HR é a intensidade de estimulação externa I. Simulamos o modelo para três diferentes valores de _I_: 1,1, 1,2 e 3,0. Observamos que, para _I_ = 1,1, o sistema aproxima de um ponto fixo; para _I_ = 1,2 o sistema aproxima de um ciclo limite; e para _I_ = 3,0 o sistema é um atrator caótico. Os resultados obtidos apenas se divergem com o resultado esperado para _I_ = 1,3, pois, pelo artigo base, o sistema já deveria se mostrar caótico. Porém, o sistema se demonstrou caótico para valores de _I_ maiores que 3,0. 

**Palavras-chave**: sistema dinâmico; potencial de ação; modelo de HR.

## Modelo de Hindmarsch-Rose

![](/imagens-readme/modelo-hr.png)

## Evolução das formas dos potenciais de ação ao variar o _I_

![](/imagens-readme/var-tempo-animado.gif)

## Exemplos de resultados para _I = 1,2_

![](/imagens-readme/graficos-exemplo-11.png)


### Referências Bibliográficas
[1] LIMA, R. S. de; CHAVARETTE, F. R.; ROÉFERO, L. G. P. Estudo do comportamento dinâmico do modelo neuronal de hindmarsh-rose. In: _Colloquium Exactarum. ISSN: 2178-8332_. [S.l.: s.n.], 2019. v. 11, n. 4, p. 122–130.
