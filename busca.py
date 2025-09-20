import pathlib
import time
import random
import time
import re
import argparse
from lupa import LuaRuntime
from multiprocessing import Pool, cpu_count
from functools import partial

formatos_autenticos = {'.mp3', '.flac', '.ogg', '.wav', '.aac', '.m4a', '.wma', '.opus'}

def verificar_audio(verificar):
    return verificar.is_file() and verificar.suffix.lower() in formatos_autenticos


def escanear_pasta(pasta):
    try:
        return [str(p) for p in pathlib.Path(pasta).iterdir() if verificar_audio(p)]
    except (PermissionError, OSError):
        return []


def executar(caminho,termo):
    temporizar = time.time()

    destino = pathlib.Path(caminho)
    
    todos = [str(d) for d in destino.rglob('*') if d.is_dir()]
    todos.append(str(destino))  
    
    nucleo_CPU = cpu_count()
    
    escanear = partial(escanear_pasta)
    
    with Pool(nucleo_CPU) as pool:
        resultados = pool.map(escanear, todos)
    
    audio = sorted([arqv for sub in resultados for arqv in sub])
    
    #print(f"{len(audio)} Arquivos Encontrados em {time.time() - temporizar:.2f} Segundos")
    search_term = termo
    pattern = r"(?i)" + ".*".join(re.escape(word) for word in search_term.split())
    #[print(i) for i in audio if re.search(pattern, i)]
       


    return [i for i in audio if re.search(pattern, i)]


    
def aleatoria(x):
    return random.choice(x)


lua = LuaRuntime()

lua = LuaRuntime()
configs = lua.execute(open("config.lua").read())

parser = argparse.ArgumentParser()
parser.add_argument("-search",  help="String to search")
args = parser.parse_args()

local_de_arquivos = configs["LED"]
tar = executar(local_de_arquivos,args.search)
for i in tar:
    print(i)
