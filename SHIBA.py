import pathlib
import time
import random
import shlex
import subprocess
from multiprocessing import Pool, cpu_count
from functools import partial
from pathlib import Path



formatos_autenticos = {'.mp3', '.flac', '.ogg', '.wav', '.aac', '.m4a', '.wma', '.opus'}

def verificar_audio(x):
    return x.is_file() and x.suffix.lower() in formatos_autenticos

def escanear_pasta(dir_path):
    audio_files = []
    try:
        for path in pathlib.Path(dir_path).iterdir():
            if verificar_audio(path):
                audio_files.append(str(path))
    except (PermissionError, OSError):
        pass  
    return audio_files

def execute(root_folder):
    start_time = time.time()
    
    
    root_path = pathlib.Path(root_folder)
    
    all_dirs = [str(d) for d in root_path.rglob('*') if d.is_dir()]
    all_dirs.append(str(root_path))  # Include root folder
    
    num_workers = cpu_count()
    
    scan_func = partial(escanear_pasta)
    
    with Pool(num_workers) as pool:
        results = pool.map(scan_func, all_dirs)
    
    audio = sorted([file for sublist in results for file in sublist])
    
    print(f"Found {len(audio)} audio files in {time.time() - start_time:.2f} seconds:")
    

    return audio



    
def aleatoria(x):
    return random.choice(x)





folder_to_scan = '/media/felipe_palagio/BAKITUP/felipe'
files = execute(folder_to_scan)
subprocess.run(['ffplay', aleatoria(files)], check=True)
