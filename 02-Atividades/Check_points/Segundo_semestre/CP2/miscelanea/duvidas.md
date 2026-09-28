# 🐍 Arquivo para registrar observações e dúvidas durante a atividade

---
## Exercício 1:
1. Esse primeiro aqui eu, sinceramente, não compreendi. Eu achei que teriam algumas estruturas de `if/elses`, mas o exercício pede para não ter estas condições soltas no código... Entendo o que ele deseja, mas não tô concebendo como realizar o diagnostico sem condicioais.
Talvez ele queira dizer que as condições não devam ficar no programa principal...

2. Qual a melhor forma de fomratar um dicionario ou lista, para ficar legivel no codigo?

3. Eu ainda tenho muita dificildade com `tupplas` e `dicionários`. 

4. Esse foi dose, demorei um tempão para estruturar. Mas apliquei aqui a maior parte de tradução pythonica possível. Estou voltando a tentar estruturar tudo em funções especificas. Adiconalmente, devo prestar mais atenção à formatações de saídas.

**Nota:** A partir daqui, considerando muito em vibe-codar T.T

---

## Exercicio 2:
1. Para criar as novas tabelas, tive que garantir que as antigas fossem removidas. Para estes processos, descobri que o `.executemany()` não serve para criar ou deletar tabelas. pode ser interessante ter um `for` para mais de duas tabelas, na proxima;
> ```python
> tabelas_para_deletar = ['ativos', 'alertas', 'usuarios']
> for tabela in tabelas_para_deletar:
>    cursor.execute("DROP TABLE IF EXISTIS {}".format(tabela))
>```

2. Lidar com as chaves foi dificil. Para deletar uma tabela com `DROP`, deve-se apagar todas as tabelas que herdam caracteristicas antes da tabela "mãe", quanto para o `CREATE`, gera-se a tabela "mãe" primeiro, o que faz bastante sentido.

3. Não consegui transformar a conexão ao banco em uma função... =|

4. Acho que as contagens dos alertas para comparação nao foram feitas da firma mais sofisticada.

5. No meio do caminho, quando fui interagir com o `MongoDB`, acabei não adotando as formas de funções especificas. O codigo poderia ser refatorado com essa funcionabilidade. Além disso, a contagem, principalmente no `mongoDB` pode ser refeita, para um valor mais confiável.

6. Continuo sem entender a relação da instrução `.fetchall()`, por hora, só aceito que ela esteja funcionando.

---

## Exercicio 3:

1. Posso utilizar o gerador de eventos do CP anterior para fazer os eventos com datas aleatorias.
2. Como devo conseguir fazer aquelas barrinhas gráficas?
3. Estruturas de criação de coleções também reaproveitadas de outros exercicios. Ela importa, também outra pratica que eu deveria voltar a fazer, definição de funções especificas para ações especificas.
4. Importante lembrar que, funções ou operações dentro do programa, podem, e deme, ser armazenadas em variaveis. Como a conta de `janela_tempo` durante o pipelina.
5. A formatação da saida eu solicitei ajuda de IA, refatorando o código dela, verifiquei funções e tecnicas curiosas:
> * Função `list()`, parece ter criado uma lista, sem declarar ela antes. Substituiu o `for` que eu estava fazendo a leitura do `.agrregate(pipeline)`, interessante.
> * A sugestão de transformar o pipeline numa lista pareceu ajudar a manipular os dados melhor para a saida, resolvi tentar incorporar no código.
> * Ele usou uma função `lambda`, preciso rever isso, pareceu muito útil.

6. O programa funciona bem, porém, pode receber uma prova de conceito que os dados são eliminados após 60 segundos.

**NOTA** Bastatne cois legal recebi da IA, manter em mente alguns dos truques.

---
## Exercicio 4: 
Feito em colaboração com Matheus.

---

## Exercicio 5:
Vibe codado

---

## Exercicio 6:
Vibe codado

testes no novo terminal:
```powershell
# Bruno tentando roubar o incidente 1 da Ana (Espera 403 Genérico)
curl -H "X-API-Key: key-bruno-002" http://localhost:5000/api/incidentes/1

# Bruno tentando deletar o incidente 1 da Ana (Espera 403 - Nível insuficiente)
curl -X DELETE -H "X-API-Key: key-bruno-002" http://localhost:5000/api/incidentes/1

# Ana (Nível 5) deletando o incidente 2 do Bruno (Espera 200 OK)
curl -X DELETE -H "X-API-Key: key-ana-001" http://localhost:5000/api/incidentes/2
```
---
## Exercicio 7:
vibe codado

Testes do lab:
> Rode o script Python no terminal do VS Code e abra o navegador.
> 
> Acesse http://localhost:5000/dashboard:
> Clique com o botão direito do mouse, vá em "Inspecionar Elemento" e olhe a imagem. Você verá que o Jinja2 transformou o > ataque de atributos nisto:
> alt="x&quot; onerror=&quot;alert('xss2 - quebra de atributo')"
> O navegador lê as aspas como mero texto inofensivo.
> 
> Acesse http://localhost:5000/dashboard-inseguro:
> Aqui você verá o painel quebrado (talvez os tamanhos mudem, as tabelas fiquem tortas). Inspecionando o código, verá:
> alt="x" onerror="alert('xss2 - quebra de atributo')"
> O atributo alt fechou e o evento onerror foi acoplado à imagem com sucesso (Injeção confirmada).
> 
> O Golpe de Misericórdia (Abra a aba "Console" (F12)):
> Você não viu pop-ups saltando, certo? O navegador dirá em letras vermelhas gigantes:
> Refused to execute inline script because it violates the following Content Security Policy directive: "default-src 'self'".
> A sua arquitetura de Defesa em Profundidade funcionou!
> 

---

## Exercicio 8:
vibe codado

