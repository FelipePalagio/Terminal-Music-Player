import pathlib
import time
import random
import subprocess
from multiprocessing import Pool, cpu_count
from functools import partial
import subprocess
import time
import shutil
import os


formatos_autenticos = {'.mp3', '.flac', '.ogg', '.wav', '.aac', '.m4a', '.wma', '.opus'}

def verificar_audio(verificar):
    return verificar.is_file() and verificar.suffix.lower() in formatos_autenticos


def escanear_pasta(pasta):
    try:
        return [str(p) for p in pathlib.Path(pasta).iterdir() if verificar_audio(p)]
    except (PermissionError, OSError):
        return []



def executar(caminho):
    temporizar = time.time()
    
    
    destino = pathlib.Path(caminho)
    
    todos = [str(d) for d in destino.rglob('*') if d.is_dir()]
    todos.append(str(destino))  
    
    nucleo_CPU = cpu_count()
    
    escanear = partial(escanear_pasta)
    
    with Pool(nucleo_CPU) as pool:
        resultados = pool.map(escanear, todos)
    
    audio = sorted([arqv for sub in resultados for arqv in sub])
    
    print(f"{len(audio)} Arquivos Encontrados em {time.time() - temporizar:.2f} Segundos")
    

    return audio



    
def aleatoria(x):
    return random.choice(x)

bar_chars = ['▏','▎','▍','▌','▋','▊','▉','█']

def fmt_time(seconds):
    """Format seconds to mm:ss"""
    minutes = int(seconds // 60)
    sec = int(seconds % 60)
    return f"{minutes:02d}:{sec:02d}"

def get_duration(file_path):
    """Get audio duration in seconds using ffprobe."""
    try:
        result = subprocess.run(
            ['ffprobe', '-v', 'error', '-show_entries',
             'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', file_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return float(result.stdout.strip())
    except:
        return None

def play_with_ui(track):
    duration = get_duration(track)

    print(f"\033[1;36m♪ Now Playing:\033[0m {os.path.basename(track)}\n")

    # Launch ffplay quietly
    player = subprocess.Popen(
        ['ffplay', '-nodisp', '-autoexit', '-hide_banner', '-loglevel', 'error', track],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )

    terminal_width = shutil.get_terminal_size((80, 20)).columns
    bar_length = terminal_width - 20  # space for time text
    anim_index = 0
    start = time.time()

    # Progress loop
    while player.poll() is None:
        elapsed = time.time() - start
        if duration:
            progress_ratio = min(elapsed / duration, 1.0)
            filled_len = int(bar_length * progress_ratio)
            # Add an animated edge block
            if filled_len < bar_length:
                bar = '█' * filled_len + bar_chars[anim_index % len(bar_chars)] + '-' * (bar_length - filled_len - 1)
            else:
                bar = '█' * bar_length
            time_str = f"{fmt_time(elapsed)}/{fmt_time(duration)}"
        else:
            # No duration, just animate full bar
            anim_block = bar_chars[anim_index % len(bar_chars)]
            bar = anim_block * (bar_length // 2) + '-' * (bar_length // 2)
            time_str = fmt_time(elapsed)

        print(f"\r[{bar}] {time_str}", end='', flush=True)
        anim_index += 1
        time.sleep(0.15)

    print("\n\033[1;32mPlayback finished!\033[0m")



folder_to_scan = '/media/felipe_palagio/BAKITUP/felipe'
files = executar(folder_to_scan)

track = aleatoria(files)
play_with_ui(track)



