import sys
from cx_Freeze import setup, Executable


base = None
# if sys.platform == "win32":
#     base = "Win32GUI"


executables = [
    Executable("AnaliseDados/janela.py", base=base)
]

buildOptions = dict(
    packages=[],
    includes=["pandas", "pyqt5"],
    include_files=[],
    excludes=[]
)

setup(
    name="Análise Automática de Dados",
    description="Análise Automática de Dados",
    options=dict(build_exe=buildOptions),
    executables=executables
)