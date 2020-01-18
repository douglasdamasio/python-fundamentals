# Lista de comandos

Lista de comandos do git

### Verifica nome configurado no git
git config user.name

### Set o nome para o qual você deseja
git config user.name "Douglas Damasio"

### Inicializa o Git
git init

### Verifica configuração do nome global no git
git config --global user.name

### Set o nome para o qual você deseja (Global)
git config --global user.name "Douglas Damasio"

### Verifica e-mail configurado (Global)
git config --global user.email

### Set o email para o qual você deseja (Global)
git config --global user.email "douglasdamasio18@gmail.com"

### Comando para criação das chaves publica e privada
ssh-keygen
-- As chaves ficam armazenadas na pasta oculta .ssh dentro da pasta do usuário

### Verifica conteudo da chave publica
cat id_rsa.pub

### Escreve o conteudo do README.md
echo "# Curso Python Fundamentals" >> README.md

### Verificar status do git
git status

### Adicionar todos arquivos ao git
git add .

### Adicionar apenas um arquivo ao git
git add README.md

### Adicionar repositório remoto
git remote add origin git@github.com:douglasdamasio/python-fundamentals.git

### Forçar a remoção de uma pasta de arquivos
rm -rf python-fundamentals/

### Clonagem de repositório
git clone git@github.com:douglasdamasio/python-fundamentals.git

### Commit, deve ser feito antes do push com um "comentario"
git commit -m "Inicial"

### Envia alterações para o seu github
git push -u origin master