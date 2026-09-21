# 🛠️ Padrão de Mensagens de Commit e Automação

Este repositório utiliza um padrão acadêmico personalizado de mensagens de commit baseado em prefixos e códigos de emojis (shortcodes). O objetivo é manter o histórico de evolução dos estudos limpo, visual e fácil de escanear diretamente na listagem do GitHub.

Para garantir compatibilidade e legibilidade total na interface principal do GitHub, os nomes de arquivos e diretórios são destacados utilizando **aspas simples (`'`)**.

---

## 📌 Guia de Bolso (Tabela de Referência)

| Prefixo | Código para o Terminal | Emoji no GitHub | Quando usar no dia a dia |
| :--- | :--- | :---: | :--- |
| `🆕 init:` | `:new: init:` | 🆕 | Começou um novo tópico de estudo ou arquivo do zero. |
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

## ⚙️ Scripts de Automação (Git Aliases)

Para evitar ter que digitar ou decorar os códigos de emojis toda vez, foram configurados **atalhos oficiais do Git (aliases)** que geram a estrutura da mensagem automaticamente.

### Comando Único de Configuração
Execute o bloco de código abaixo no seu terminal (apenas uma vez) para habilitar todas as automações:

```bash
git config --global alias.init-study '!f() { git commit -m ":new: init: cria '\''"\$"'\''"; }; f' && \
git config --global alias.wip '!f() { git commit -m ":gear: wip: '\''"\$"'\'' em andamento"; }; f' && \
git config --global alias.part '!f() { git commit -m ":hammer: part: '\''"\$"'\'' incompleto"; }; f' && \
git config --global alias.todo '!f() { git commit -m ":bulb: todo: '\''"\$"'\'' pode receber melhoria"; }; f' && \
git config --global alias.rm-file '!f() { git commit -m ":wastebasket: remove: deleta '\''"\$"'\''"; }; f' && \
git config --global alias.mv-file '!f() { git commit -m ":truck: move: move '\''"\$"'\''"; }; f' && \
git config --global alias.docs '!f() { git commit -m ":memo: docs: atualiza '\''"\$"'\''"; }; f' && \
git config --global alias.done '!f() { git commit -m ":white_check_mark: done: '\''"\$"'\'' finalizado"; }; f'
```

### 🚀 Exemplos Práticos de Uso no Dia a Dia

Após a configuração, o fluxo de comandos simplificados no terminal passa a ser:

```bash
# 1. Ao iniciar um novo script de exercício:
git add Exercicio_05.py
git init-study Exercicio_05.py
# Mensagem gerada: 🆕 init: cria 'Exercicio_05.py'

# 2. Se precisar interromper o desenvolvimento na metade:
git add Exercicio_05.py
git wip Exercicio_05.py
# Mensagem gerada: ⚙️ wip: 'Exercicio_05.py' em andamento

# 3. Se o código ficou incompleto ou travado em uma parte:
git add Exercicio_05.py
git part Exercicio_05.py
# Mensagem gerada: 🔨 part: 'Exercicio_05.py' incompleto

# 4. Ao registrar ou revisar anotações teóricas:
git add duvidas.md
git docs duvidas.md
# Mensagem gerada: 📝 docs: atualiza 'duvidas.md'

# 5. Ao mapear uma melhoria para o futuro:
git add Exercicio_05.py
git todo Exercicio_05.py
# Mensagem gerada: 💡 todo: 'Exercicio_05.py' pode receber melhoria

# 6. Ao finalizar e validar completamente o exercício:
git add Exercicio_05.py
git done Exercicio_05.py
# Mensagem gerada: ✅ done: 'Exercicio_05.py' finalizado
```
