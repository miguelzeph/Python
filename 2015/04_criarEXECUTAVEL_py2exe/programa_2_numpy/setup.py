from distutils.core import setup
import py2exe

#setup(console=['programa_2.py'])

setup(
    options = {
            "py2exe":{
            #esse e o comando para bug do error faltando MSVCP90.dll
            "dll_excludes": ["MSVCP90.dll", "HID.DLL", "w9xpopen.exe"],
            
        }
    },
    console = [{'script': 'programa_2.py'}]
)