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
---
## Exercicio 3:
1. Ao adicionar os eventos do exercicio e ralizar uma busca para conferir se foram inseridos, ocorreu um erro. Estava realizando um `find({})` para listar tudo, mas aparentemente, o programa estava considerando todas as coleções.
como delcarar uma coleção especifica?
>**resposta:**
>Como reaproveitei o codigo, atribui para `eventsoDb` o nome de `["vulnerabilidades"`, misturando as coleções.
>Houve ainda uma sugestão de filtro para utilizar dentro do `find({})`. Não a utilizei depos de corrigir o nome da coleção, mas achei uma excelente feature 
>'''python
>filtro = {"ip": {"$exists": True}, "tipo": {"$exists": True}} # Sugerido pela IA para evitar buscas globais incompativeis
>'''

