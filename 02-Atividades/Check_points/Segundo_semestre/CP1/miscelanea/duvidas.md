# 🐍 Arquivo para registrar observações e dúvidas durante a atividade

---
## Exercício 1:
1. A cláusula `SELECT * FROM <tabela> WHERE <coluna>` eu compreendi. Mas o `fetchall()` e o porquê de a consulta não ter dado certo sem o `dictionary=True` no `cursor.connect()` eu não entendi.

2. Não tenho certeza se as queries estão bem parametrizadas.

---

## Exercício 2:
1. Como trabalhar com datas na hora de inserir e, principalmente, consultar um dado no MongoDB (ou qualquer outro banco)?

2. Como realizar comandos direto no MongoDB sem o DBeaver?

3. Gostaria de conseguir escrever melhor os códigos com uma linguagem mais pythonica. Se puder comentar, novamente, como condições em linha única funcionam, pensando em semântica e estrutura, eu agradeço.
Exemplo: Quando atualizei tudo que tinha como "teste" no banco para `True`, eu pesquisei como ficaria a saída usando o `.format()` com uma condicional:
```python
print("CVE {0[cve_id]} está: {1}".format(vuln, "Corrigida" if vuln.get("corrigida") else "Pendente"))
```

4. Pode ser interessante realizar o fechamento da conexão após todas as queries.

---
## Exercício 3:
1. Ao adicionar os eventos do exercício e realizar uma busca para conferir se foram inseridos, ocorreu um erro. Estava realizando um `find({})` para listar tudo, mas aparentemente, o programa estava considerando todas as coleções.
Como declarar uma coleção específica?

> **Resposta:**
> Como reaproveitei o código, atribuí para `eventsDb` o nome de `"vulnerabilidades"`, misturando as coleções.
> 
> Houve ainda uma sugestão de filtro para utilizar dentro do `find({})`. Não a utilizei depois de corrigir o nome da coleção, mas achei uma excelente feature:
> 
> ```python
> filtro = {"ip": {"$exists": True}, "tipo": {"$exists": True}} # Sugerido pela IA para evitar buscas globais incompatíveis
> ```

2. Uma boa dificuldade em saber onde declarar o `$` durante algumas declarações ao MongoDB, principalmente na hora de realizar o pipeline.

---
## Exercício 4:
1. A tabela é criada, porém, inserir, pelo Python, os usuários da lista está retornando um erro de sintaxe, mesmo que esteja semelhante ao `Exercicio_01.py`.
> **Resposta:**
> Tinha uma vírgula a mais no último `%s`.
> 
> ```python
> cursor.executemany("INSERT INTO users (nome, email) VALUES (%s, %s)", usuarios)
> ```

2. A conexão estava sendo fechada em todas as chamadas. Parece mais inteligente fechar a conexão após todas as queries, ao invés de iniciar uma nova.

---
## Exercício 5:
1. Alice está sendo extorquida, pois o `Rollback` não está sendo efetuado. As simulações de transferências estão ocorrendo, porém, o banco não retorna erro por não encontrar o ID 99 na lista.
2. Não consegui simular um rollback na aplicação. O banco não retorna nenhum erro, mesmo que o commit seja realizado ao final dos 4 `UPDATE`s, na simulação das transações.
=(

---
## Exercício 6:
1. Realizei uma função `for` para geração de eventos, passando alguns parâmetros para a IA, de forma resumida:
> Enviei uma lista de IPs genéricos para utilização.
> Solicitei que ela estruturasse um loop com um preenchimento básico de uma lista.
> Adicionei uma condição para verificar se o contador do loop era par ou ímpar, para inserir um valor diferente para o índice `tipo` da coleção que pretendia usar.
> Baseado nessa decisão, solicitei que a IA fizesse uma condição para verificar se o contador é primo e, caso seja, colocar em `tipo` o valor de `SUSPEITO`.
> Solicitei a inserção de uma simulação de data e hora aleatórios.
> Transformei tudo em uma função chamada `geraEventos()`.
> A IA sugeriu passar um parâmetro para a função, podendo controlar a quantidade de eventos gerados.
> A função retorna uma lista com os eventos preenchidos. Utilizo esse retorno para a variável `eventos`, para preenchimento da coleção.
> Espero, sinceramente, que funcione bem...

2. Não ficou tão claro se a aplicação pegou a consulta por index ou não. Considerando verificar alguma forma de fazer um relatório para verificar, de alguma forma. Mas ficará para o futuro. Porém, caso eu tenha realizado a consulta sem ser por index, favor informar a maneira correta.
3. Por conta do exercício 2, achei interessante realizar a limpeza de todas as coleções do exercício. A função de limpeza foi adicionada mas não testei, porque no meio do caminho achei interessante ter uma "sujeira" durante o exercício. Testarei mais tarde.

---
## Exercício 7:
1. Tem uma maneira de verificar qual o número ideal de árvores participam da decisão. Futuramente pode ser interessante experimentar.
2. Os dados devem ser poucos. Independente da quantidade de árvores que coloquei, a acurácia não modificou. Seria interessante experimentar com uma amostra maior de dados.

---
## Exercício 8:
1. Na primeira tentativa tive uma saída contrária ao esperado. Poderia inverter a condição do `if`, mas não me parece a abordagem mais correta. Verificar o que está imprimindo em `r` pode ajudar. No fim das contas o `r` imprime o valor esperado. Acabei por inverter a lógica do `if` mesmo. =V
2. Tal qual o Random Forest do exercício anterior, pode ser interessante, futuramente, explorar as classificações com dados mais aleatórios e abundantes.

---
## Exercício 9:
1. No caso do exercício, foram utilizados dois parâmetros predefinidos para a matriz de confusão. No caso prático, como poderíamos utilizar a matriz para verificar a qualidade da análise dos nossos modelos? Seria, no caso do programa `Exercicio_07.py`, a variável `previsoes`?
> ```python
> # ...saída omitida...
> # Previsões e avaliações
> previsoes = modelo.predict(x_test)
> print("\nAcurácia: {:.2f}".format(accuracy_score(y_test, previsoes)))
> # ...saída omitida...
> ```

2. Fica nítido, após organizar os dados, que a acurácia pode enganar, mascarando o que seria um ataque real. Para segurança, analisar as saídas geradas com as métricas do `sklearn` pode ser muito útil para filtrar falsos positivos e refinar a precisão do modelo.

---
## Exercício 10 (Desafio):
1. A normalização do arquivo foi feita por IA. Pode ser passível de refatoração (ou posso procurar a normalização no arquivo da GS...).
2. Reutilizei os módulos do MongoDB feitos nos exercícios anteriores para cadastrar os logs no arquivo `auth.log`. O nome da coleção ficou como `logs_db = db["logs"]`.
3. O pipeline e a agregação também foram reaproveitados dos exercícios anteriores, e funcionam.
4. Aproveitei a iteração do pipeline para realizar o preenchimento das listas de treino `dataset_treino[]` e `rotulo[]`. Coloquei as condições de preenchimento do rótulo direto na linha do `append`. ~~Quero muito praticar a forma pythonica~~.
5. Preparei o modelo de Machine Learning, inicialmente, com o modelo `RandomForestClassifier`, já que rotulamos as saídas.
6. Realizado o treino da máquina. Houve um erro:
> Preparando o aprendizado de máquina...
> Modelo falhou: Expected 2D array, got 1D array instead:
> array=[5. 3.].
> Reshape your data either using array.reshape(-1, 1) if your data has a single feature or array.reshape(1, -1) if it contains a single sample.
> 
> Particularmente não entendi o que isso significa. Mas funcionou aplicar o reshape no momento de preparar os dados em:
> ```python
> # ...saída omitida...
> x = np.array(dataset_treino).reshape(-1, 1)
> y = np.array(rotulo)
> # ...saída omitida...
> ```

7. Não gostei de como apliquei o caso novo, mas o `predict` parece funcionar.
8. Acho que isso é o mínimo necessário para atender o desafio.
---

Majoritariamente, nenhuma IA realizou a atividade, exceto nos momentos descritos. O modelo que mais utilizei foi o Gemini.
De modo geral, utilizei a apostila e reciclei códigos que já haviamos trabalhado.
Melhorei meu processo de commits, adicionando mensagens, e fazendo commits com mais frequência, agradeço se puder avaliar como ficou.
Também gostei de interagir com o arquivo markdown. Foi ótimo marcar as observações aqui.
No fim, utilizei muito a IA para tentar corrigir formatações no código, e para me incentivar a escrever os trabalhos de forma mais `pythonica`, apesar de eu ter escrito pouca coisa desse maneira.
Também a utilizei para tentar automatizar os processos de commits com mensgens padronizadas. Não apliquei dessa vez, mas aprendi que da para fazer `aliases` de comandos para o terminal. Pedi para a IA gerar um markdown pra deixar registrado, no próximo CP o utilizo.

Por fim, uma reflexão sobre eu tentar fazer as coisas por conta ou não.
Difícil competir contra esse treco de IA. E imaginar que muitos já devem ter entregue o CP sem nem suar... Até que ponto esse esforço em codar, ou realizar algumas atividades por conta, pode ser válido? =S
Ainda não sei a melhor forma de usar a IA a meu favor, sem eu me sentir uma ameba. Porém, nesse CP, acho que fiz um uso legal. Preciso ver mais formas de tornar meu estado de produtividade mais fluído.
