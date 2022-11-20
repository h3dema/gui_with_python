Este é um layout padrão do PySimpleGUI. Você pode colocar dois (ou mais) elementos de tamanhos distintos, um ao lado do outro em uma única linha.

![1 linha, duas colunas](imgs/ex01.png "ex01.py")


Este é também um layout padrão do PySimpleGUI, pois você pode colocar dois (ou mais) elementos de tamanhos distintos, cada um em uma linha.

![duas linhas e 1 coluna](imgs/ex02.png "ex02.py")

As linhas são independentes. Os objetos são colocados um ao lado do outro e alinhados pelo tamanho.
Assim podemos ter a impressão que as colunas possuem quebras, mas na verdade, os elementos são considerados dentro da linha onde são criados.
Por isto vemos os blocos vermelhos como se estivessem em colunas sobrepostas, mas precisamos lembrar que a criação dos elementos é feita por linha.

![duas linhas, duas colunas](imgs/ex03.png "ex03.py")

Isto fica um pouco mais claro neste exemplo. Trocamos o bloco azul da segunda linha por uma columa com duas linhas. Cada linha tem um elemento.
Troque o tamanho destes dois elementos para ver melhor como o alinhamento funciona.
No que os dois novos elementos fazer a altura da segunda linha fique um pouco maior.

![duas linhas, duas colunas (célula inferior com duas linhas)](imgs/ex04.png "ex04.py")

Este exemplo reforça a alteração na altura das linhas.

![duas linhas, duas colunas (duas células com duas linhas)](imgs/ex05.png "ex05.py")

Trocamos o bloco azul da esquerda por duas elementos (na mesma linha). Não é necessário criar uma coluna adicional, pois o PySimpleGUI, sempre permite colocar um objeto ao lado do outro em uma linha.

![duas linhas, duas colunas (última combinação)](imgs/ex06.png "ex06.py")

> 1. Note que os blocos não encostam um no outro. Isto porque existe um default de espaçamento entre objetos em uma janela.
> 2. O tamanho dos botões é definido em caracteres !!!!
