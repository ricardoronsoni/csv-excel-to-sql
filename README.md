# csv-excel-to-sql
Programa Python que permite realizar consultas SQL em arquivos CSV e de excel.

## Funcionamento
- O programa irá importar o(s) arquivo(s) CSV, XLS ou XLSX para um banco de dados sqlite;   
- Os arquivos devem estar na pasta './dados';   
- Será criada uma tabela para cada arquivo localizado. A tabela terá o nome do arquivo, sem a sua extensão;   
- Para iniciar o programa é necessário digitar: 
```
python app.py
```
- O programa será iniciado no modo interativo no terminal, onde o usuário deverá digitar no terminal a instrução SQL.