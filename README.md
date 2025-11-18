# TRABALHO PERCEPTRON

Aluno: Micael Luan Conti

## Desenvolvimento

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

### Perceptron

Foi criado a classe Perceptron que recebe os parâmetros:
1. __data__, list[float] -> A lista de dados de entrada (inputs) que o perceptron irá processar.
2. __weights__, list[float] -> A lista dos pesos iniciais que serão ajustados durante o aprendizado.
3. __bias__, float -> O valor do viés (bias), que permite deslocar a fronteira de decisão.
4. __learning_rate__, float -> A taxa de aprendizado (α ou η) que define o tamanho do passo na atualização dos pesos.
5. __max_epochs__, int -> O número máximo de épocas (iterações de treinamento) permitido.

### Treinamento

O conjunto de dados foi dividido, reservando-se os últimos 10 registros para a avaliação (dataset de teste). O modelo foi treinado com os dados restantes (dataset de treinamento).

## Resultados

Os resultados foram bem satisfatórios, foi obtido uma acurácia de 100% com todas as taxas de aprendizado. Porém o número de épocas necessário para convergência alterou muito conforme a taxa de aprendizado.

![alt text](/Docs/image.png)