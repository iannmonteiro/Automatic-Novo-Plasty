# Automatic-Novo-Plasty

Para gerar diversos arquivos "config.txt" que servem de input do NOVOPlasty, use o script em python para facilitar o processo quando se tem muitas amostras.

# Passo 1
Altere as configurações que serão comum a todos os arquivos

# Passo 2
Crie um arquivo input com as informações que serão alteradas, diferencie cada config com um separador "*" na linha entre as variáveis (ver arquivo exemplo)

# Passo 3
Execute utilizando o comando no linux "python3 novoplasticautomatic.py -i input.txt -o config.txt"

-i: coloque o nome do arquivo que está com as alterações
-o informe o nome dos arquivos configs que serão salvos
