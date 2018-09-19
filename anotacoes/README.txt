Anotações

Estrutura de arquivos:

Após ser criado, index.html conterá links para "Tutoriais".

Um tutorial é um arquivo de texto na pasta "tutoriais/" representando
uma sequencia plana de Paginas.

Cada arquivo em "tutoriais/" deve ter uma descrição curta na primeira
linha e nomes de arquivos nas seguintes linhas, na ordem desejada.
Estes nomes devem ser relativas à pasta "paginas/"

Cada Pagina na pasta "paginas/" deve ser um arquivo Markdown (.md) e
deve ter uma descrição na primeira linha. Esta descrição é usada no
índice de cada Tutorial.

Numa Pagina, </textarea> não deve ser escrito. Use &lt;/textarea> no
seu lugar.

Para criar os HTML, rode 'python build.py' (Python 3). Ele lerá todo
arquivo na pasta "tutoriais/". Tutoriais que não devem ser convertidos
podem ser movidas à pasta "arquivados/".

Arquivos HTML serão criados na pasta "html/". 

Publique a pasta "html/".
