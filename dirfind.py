#!/usr/bin/python
import requests

print("""
+++++++++++++++++++++++++++++
+ SCRIPT FEITO POR SR. ALTO +
+                           +
+    SALVE #HYS TEAM        +
+                           +
+      Versao 1.0           +
+                           +
+ https://github.com/SrAlto +
+++++++++++++++++++++++++++++
                                                                                                                                                                                           
""")
url = raw_input("Digite o site: ")
arquivo = open('wordlist.txt')

linhas = arquivo.readlines()

for linha in linhas:
    resposta = requests.get(url+linha)
    codigo = resposta.status_code
    if codigo == 200:
        print url+linha, codigo
        print 'OK!'

    
