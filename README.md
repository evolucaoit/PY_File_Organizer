# 📂 PY_File_Organizer

## 📝 Descrição

**PY_File_Organizer** é um script em Python desenvolvido para organizar automaticamente arquivos em pastas separadas com base em suas extensões. Ele facilita o gerenciamento de arquivos ao categorizar diferentes tipos de mídia, documentos e outros formatos de arquivos, movendo-os para pastas específicas. 🚀

## 📂 Diagrama de Lógica do PY_File_Organizer

```mermaid
graph TD
    A[Iniciar Script] --> B[Listar arquivos no diretório atual]
    B --> C{É um arquivo?}
    C -- Sim --> D[Obter extensão do arquivo]
    C -- Não --> B
    D --> E{Extensão está na lista?}
    E -- Sim --> F[Verificar se pasta de destino existe]
    E -- Não --> B
    F -- Não --> G[Criar pasta de destino]
    F -- Sim --> H[Verificar se o arquivo já existe na pasta de destino]
    G --> H
    H -- Não --> I[Mover arquivo para a pasta de destino]
    H -- Sim --> J[Ignorar o arquivo]
    I --> B
    J --> B
    B --> K[Verificar arquivos não movidos]
    K --> L{É um arquivo não movido?}
    L -- Sim --> M[Obter extensão do arquivo]
    L -- Não --> B
    M --> N{Extensão está na lista?}
    N -- Sim --> O[Verificar se pasta de duplicados existe]
    N -- Não --> B
    O -- Não --> P[Criar pasta de duplicados]
    O -- Sim --> Q[Mover arquivo para a pasta de duplicados]
    P --> Q
    Q --> B


## 🌟 Motivações para Criar o Projeto PY_File_Organizer

Eu criei o **PY_File_Organizer** por algumas razões principais:

1. **Manutenção de Ordem e Organização** 📁: Com o tempo, meu computador acumulou muitos arquivos de diferentes tipos e extensões, espalhados em várias pastas. Manter tudo organizado manualmente tornou-se uma tarefa demorada e frustrante. Eu queria uma solução automatizada que me ajudasse a organizar meus arquivos de forma rápida e eficiente.

2. **Facilitar o Acesso a Arquivos** 🔍: Encontrar arquivos específicos pode ser desafiador quando eles estão perdidos em pastas desorganizadas. Ao criar pastas baseadas nas extensões dos arquivos, o **PY_File_Organizer** facilita o acesso a documentos, imagens, vídeos e outros arquivos, melhorando a produtividade e reduzindo o tempo gasto na busca por arquivos.

3. **Praticidade e Automação** 🤖: A automação de tarefas repetitivas é uma das vantagens de usar a programação. Eu queria criar uma ferramenta que pudesse rodar periodicamente, ou sempre que necessário, para organizar meus arquivos sem precisar de intervenção manual constante.

4. **Aprendizado e Experimentação** 🧑‍💻: Como desenvolvedor, gosto de criar projetos que me desafiem a aprender novas habilidades e melhorar minhas capacidades de codificação. Este projeto me proporcionou uma ótima oportunidade para trabalhar com módulos do Python como `os` e `shutil`, explorando práticas de automação de arquivos e manipulação de diretórios.

5. **Compartilhar uma Solução Útil** 🤝: Ao disponibilizar o **PY_File_Organizer** no GitHub, espero ajudar outras pessoas que enfrentam problemas semelhantes de organização de arquivos. Compartilhar o script permite que outros o utilizem e o modifiquem conforme suas necessidades, promovendo uma comunidade colaborativa.

Em resumo, o **PY_File_Organizer** nasceu da necessidade de organização, da busca por praticidade e da vontade de aprender e compartilhar conhecimento. Espero que este projeto seja útil para muitos! 🌟


---

## 🔍 Funcionalidades

- **Organização Automática:** O script varre o diretório atual e organiza os arquivos em pastas baseadas em suas extensões conhecidas. 📁
- **Suporte a Múltiplos Tipos de Arquivo:** Suporta uma ampla variedade de extensões de arquivos como `.jpeg`, `.png`, `.pdf`, `.mp4`, `.zip`, entre outros. 🎨🎵📚📦
- **Gestão de Duplicados:** Arquivos com o mesmo nome que já existem no destino são tratados de forma especial para evitar sobrescritas acidentais. ✋
- **Pasta de Duplicados:** Arquivos duplicados ou que não puderam ser movidos são armazenados em uma pasta específica chamada `possiveis-duplicados-validar` para revisão posterior. 🔄

---

## 🚀 Como Usar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/evolucaoit/PY_File_Organizer.git


📚 Extensões Suportadas
O script atualmente suporta as seguintes extensões de arquivo:

🛠️ Tecnologias Utilizadas

Python 🐍: A linguagem de programação utilizada para desenvolver o script.
OS Module 📂: Utilizado para interagir com o sistema operacional.
Shutil Module 🛠️: Utilizado para operações de arquivo e diretório.

## 🗂️ Organização de Arquivos com PY_File_Organizer

Aqui está como o **PY_File_Organizer** estrutura os arquivos de acordo com suas extensões:

| 📁 **Extensão** | 📂 **Pasta Destino** |
|-----------------|----------------------|
| 🖼️ `.jpeg`     | **jpeg**             |
| 🖼️ `.jpg`      | **jpg**              |
| 🖼️ `.png`      | **png**              |
| 📄 `.pdf`      | **pdf**              |
| 🎥 `.mp4`      | **mp4**              |
| 🎥 `.mkv`      | **mkv**              |
| ⚙️ `.exe`      | **exe**              |
| ⚙️ `.msi`      | **msi**              |
| 📦 `.rar`      | **rar**              |
| 📖 `.epub`     | **epub**             |
| 📦 `.zip`      | **zip**              |
| 📦 `.7z`       | **7z**               |
| 💿 `.iso`      | **iso**              |
| 🎥 `.webm`     | **webm**             |
| 🎵 `.m4a`      | **m4a**              |
| 🎵 `.mp3`      | **mp3**              |
| 🎥 `.wmv`      | **wmv**              |
| 🎥 `.avi`      | **avi**              |
| 📝 `.txt`      | **txt**              |
| 📝 `.efu`      | **efu**              |
| 🌐 `.torrent`  | **torrent**          |
| 📊 `.xls`      | **xls**              |
| 📊 `.ods`      | **ods**              |
| 📝 `.odt`      | **odt**              |
| 📝 `.doc`      | **doc**              |
| 📝 `.docx`     | **docx**             |
| 🐍 `.py`       | **py**               |
| 🌐 `.html`     | **html**             |
| 📄 `.md`       | **md**               |
| 📄 `.json`     | **json**             |
| 🗒️ `.yaml`     | **yaml**             |
| 📊 `.csv`      | **csv**              |

Essas pastas são automaticamente criadas e os arquivos são movidos para elas conforme suas extensões, garantindo uma organização impecável e eficiente! 🚀


