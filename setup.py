import sys
from cx_Freeze import setup, Executable

target = Executable(
    script="ordena_texto.py",
    base="Win32GUI",
    icon=u"D:\Repositorios_Separados_GITHUB\Ordena_Texto\icone_app.ico"
    )

setup(
    name = "Ordena Texto",
    version = "0.1",
    description = "Uma simples aplicação para ordenação de textos",
    author="Anderson Bragherolli",
    executables=[target]
    )