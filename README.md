## TRABALHO PERCEPTRON

Aluno: Micael Luan Conti


### Dataset

O dataset escolhido foi o ['Breast Cancer Wisconsin'](https://archive.ics.uci.edu/dataset/15/breast+cancer+wisconsin+original), um dataset clássico utilizado para dizer se um câncer de mama é benigno ou maligno.

O data set conta com 9 features:

| Nº | Atributo                       | Faixa / Descrição                             |
|----|--------------------------------|-----------------------------------------------|
| 1  | Número da amostra              | Identificador numérico                        |
| 2  | Espessura do aglomerado        | Valor entre 1 e 10                            |
| 3  | Uniformidade do tamanho celular| Valor entre 1 e 10                            |
| 4  | Uniformidade do formato celular| Valor entre 1 e 10                            |
| 5  | Aderência marginal             | Valor entre 1 e 10                            |
| 6  | Tamanho da célula epitelial    | Valor entre 1 e 10                            |
| 7  | Núcleos descobertos            | Valor entre 1 e 10                            |
| 8  | Cromatina pouco densa          | Valor entre 1 e 10                            |
| 9  | Nucléolos normais              | Valor entre 1 e 10                            |
| 10 | Mitose                          | Valor entre 1 e 10                            |
| 11 | Classe                         | 2 = benigno, 4 = maligno                      |

Porém foram necessários alguns tratamentos no dataset para torná-lo __linearmente separado__ e usá-lo com um __Perceptron Simples__. Os seguintes tratamentos foram feitos:

1. Removidas linhas com dados vazios (?)
2. Removida coluna de ID
3. Substituido classes, a classe 2 foi trocado para 0 e a classe 4 para 1
4. Removidas linhas que tornavam o dataset não linearmente separável:
[  1   3  12  41  49  61  99 190 216 226 244 251 265 285 306 334 342 419
 474 479]

