# Arquivo para registrar observações e dúidas durante a atividade

---
## Exercicio 1:
1. A clausula `SELECT*FROM <tabela> WHERE <coluna>` eu compreendi.
Mas o "feetch all", e porque a consulta não deu certo sem o "dictionary=True" no `cursor.connect()` eu não entendi.

2. Não tenho certeza se as querys estão bem parametrizadas.

---

## Exercicio 2:
1. Como trabalhar com datas na hora de inserir e, principalmente, consultar um dado no mongo (ou qqr outro banco)?

2. Como realizar comandos direto no mongoDB sem o Dbeaver?

3. Gostaria de conseguir escrever melhor os códigos com uma linguagem mais pythonica.
Se puder comentar, novamente, como condições em linha unica funcionam, pensando em semantica e estrutura, eu agradeço.
ex. Quando atualizei tudo que teinha como "teste" no banco para "True", eu pesquisei como ficaria a saida usando o .format() com uma condicional:
```
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
> filtro = {"ip": {"\(exists": True}, "tipo": {"\)exists": True}} # Sugerido pela IA para evitar buscas globais incompatíveis
> ```
2. Uma boa dificuldade em saber onde declarar o `$` durante algumas declarações ao mongo.
principalmente na hora de realizar o pipeline.
---
## Exercicio 4:
1. A tabela é criada, porém, inserir, pelo python, os usuarios da lista, está retornando um erro de sintaxe, mesmo que esteja semelhante ao `Exercicio_01.py`.
> **Resposta:**
> Tinha uma vírgula a mais no último `%s`
>
```python
> cursor.executemany("INSERT INTO users (nome, email) VALUES (%s, %s",usuarios)
```
>
2. A conexão estava sendo fechada em todas as chamadas, parece mais inteligente fechar a conexão apóes todas as querys, ao invés de iniciar uma nova.
---

