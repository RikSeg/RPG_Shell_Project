# Terminal Shell Temático:

- O programa é apenas uma interface de terminal simples que permite abrir arquivos na tela e simular entrada de credenciais para acesso a alguns arquivos. (ainda não implementado).
- O objetivo do programa era para ser usado como base de dados para um RPG de mesa, portanto tem a temática de uma fundação fictícia usada no RPG. Talvez futuramente posso fazer ele um sistema com arquitetura Cliente-Servidor verdadeira.

- Organização dos Arquivos:

Os arquivos são organizados em Tiers (.t1, .t2, .t3,etc.) dentro da pasta files/ sendo que cada tier um teria uma senha.

- t1- acesso irrestrito

- tn- precisará de uma senha.

Arquivo de ajuda para listar comandos está na pasta help_file/

## Para Executar:
- Pelo terminal/cmd:
~~~
python Terminal_shell.py
~~~
- Executável:

Acessando a pasta dist/ desse repositório há o .zip da pasta com um executável do programa e as pastas necessárias para ele funcionar. (Demo)
