# 🛠️ Padrão de Mensagens de Commit e Automação

Este repositório utiliza um padrão acadêmico personalizado de mensagens de commit baseado em prefixos e códigos de emojis (shortcodes). O objetivo é manter o histórico de evolução dos estudos limpo, visual e fácil de escanear diretamente na listagem do GitHub.

Para garantir compatibilidade e legibilidade total na interface principal do GitHub, os nomes de arquivos e diretórios são destacados utilizando **aspas simples (`'`)**.

---

## 📌 Guia de Bolso (Tabela de Referência)

| Prefixo | Código para o Terminal | Emoji no GitHub | Quando usar no dia a dia |
| :--- | :--- | :---: | :--- |
| `🎯 task:` | `:target: task:` | 🎯 | Iniciou uma nova tarefa, lista de exercícios ou meta de estudo. |
| `🆕 init:` | `:new: init:` | 🆕 | Começou um arquivo de código principal do zero (ex: `Exercicio_06.py`). |
| `📎 add:` | `:paperclip: add:` | 📎 | Adicionou um arquivo qualquer de suporte (dados, logs, imagens). |
| `⚙️ wip:` | `:gear: wip:` | ⚙️ | Atividade em andamento (salvando o código no meio do processo). |
| `🔨 part:` | `:hammer: part:` | 🔨 | Atividade incompleta / Feita apenas uma parte do exercício. |
| `💡 todo:` | `:bulb: todo:` | 💡 | Identificou um ponto que pode ser melhorado ou otimizado depois. |
| `🗑️ remove:` | `:wastebasket: remove:` | 🗑️ | Deletou um arquivo ou pasta do repositório. |
| `🚚 move:` | `:truck: move:` | 🚚 | Moveu um arquivo de pasta ou renomeou um diretório. |
| `✨ feat:` | `:sparkles: feat:` | ✨ | Desenvolveu uma nova lógica ou resolveu um novo exercício. |
| `🐛 fix:` | `:bug: fix:` | 🐛 | Corrigiu um erro de sintaxe ou lógica acadêmica. |
| `🔧 refactor:` | `:wrench: refactor:` | 🔧 | Deixou o código mais limpo e otimizado (boas práticas). |
| `📝 docs:` | `:memo: docs:` | 📝 | Atualizou conceitos teóricos e anotações no Markdown. |
| `✅ done:` | `:white_check_mark: done:` | ✅ | Exercício concluído, revisado e validado. |
| `🏆 done:` | `:trophy: done:` | 🏆 | Módulo, capítulo ou lista de exercícios finalizada com sucesso. |

---

## ⚙️ Configuração dos Atalhos (Git Aliases) no PowerShell

Como o Windows PowerShell possui regras estritas para aspas e caracteres de escape, a forma mais segura e à prova de falhas para configurar esses atalhos é editando o arquivo de configuração global do Git diretamente.

### Passo a Passo para Instalação:

1. Abra o terminal do **PowerShell** no VS Code e execute o comando abaixo:
   ```powershell
   git config --global --edit
   ```
2. Um arquivo de texto será aberto no seu editor padrão ou no Bloco de Notas.
3. Vá até o final do arquivo, pule uma linha e cole o bloco de configuração abaixo:

```ini
[alias]
	task = "!f() { git commit -m \":target: task: '\$1'\"; }; f"
	init-study = "!f() { git commit -m \":new: init: cria '\$1'\"; }; f"
	add-file = "!f() { git commit -m \":paperclip: add: adiciona '\$1'\"; }; f"
	wip = "!f() { git commit -m \":gear: wip: '\$1' em andamento\"; }; f"
	part = "!f() { git commit -m \":hammer: part: '\$1' incompleto\"; }; f"
	todo = "!f() { git commit -m \":bulb: todo: '\$1' pode receber melhoria\"; }; f"
	rm-file = "!f() { git commit -m \":wastebasket: remove: deleta '\$1'\"; }; f"
	mv-file = "!f() { git commit -m \":truck: move: move '\$1'\"; }; f"
	docs = "!f() { git commit -m \":memo: docs: atualiza '\$1'\"; }; f"
	done = "!f() { git commit -m \":white_check_mark: done: '\$1' finalizado\"; }; f"
```
4. Salve e feche o arquivo.

---

## 🚀 Exemplos Práticos de Uso no PowerShell

Após salvar as configurações, você pode gerenciar o fluxo de estudos executando comandos simples de uma palavra no PowerShell:

```powershell
# 1. Ao iniciar uma nova meta de estudos geral:
git task "estudos de machine learning e redes neurais"
# Mensagem no GitHub: 🎯 task: 'estudos de machine learning e redes neurais'

# 2. Ao criar o arquivo script de um exercício específico:
git add Exercicio_06.py
git init-study Exercicio_06.py
# Mensagem no GitHub: 🆕 init: cria 'Exercicio_06.py'

# 3. Ao anexar um arquivo qualquer que sirva de suporte:
git add auth.log
git add-file auth.log
# Mensagem no GitHub: 📎 add: adiciona 'auth.log'

# 4. Se precisar interromper o desenvolvimento na metade:
git add Exercicio_06.py
git wip Exercicio_06.py
# Mensagem no GitHub: ⚙️ wip: 'Exercicio_06.py' em andamento

# 5. Se o código ficou incompleto ou travado:
git add Exercicio_06.py
git part Exercicio_06.py
# Mensagem no GitHub: 🔨 part: 'Exercicio_06.py' incompleto

# 6. Ao registrar ou revisar anotações teóricas:
git add duvidas.md
git docs duvidas.md
# Mensagem no GitHub: 📝 docs: atualiza 'duvidas.md'

# 7. Ao mapear uma melhoria para o futuro:
git add Exercicio_06.py
git todo Exercicio_06.py
# Mensagem no GitHub: 💡 todo: 'Exercicio_06.py' pode receber melhoria

# 8. Ao finalizar e validar completamente o exercício:
git add Exercicio_06.py
git done Exercicio_06.py
# Mensagem no GitHub: ✅ done: 'Exercicio_06.py' finalizado
```
