# setup.py
from cx_Freeze import setup, Executable

# Dependências adicionais podem ser listadas aqui
build_exe_options = {"packages": ["include"], "excludes": []}

# Defina o executável
setup(
    name="meu_projeto",
    version="1.0",
    description="Descrição do meu projeto",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=None)]
)
