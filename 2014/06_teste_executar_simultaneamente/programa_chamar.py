import subprocess
subprocess.Popen(["python27.exe","./programa1.py"])
subprocess.Popen(["python27.exe","./programa2.py"])

# As bibliotecas chamadas aqui, nao sao lidas pelos programas 1 e 2 

# E se der problema em um programa, ele n interfere o outro...


# O processo pode ocorrer simultaneamente, isto pode misturar algum print... por isso e bom usar a biblioteca "time".
