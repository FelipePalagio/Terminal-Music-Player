import time
import subprocess
import subprocess
import time
import shutil
import os
import sys 
from multiprocessing import Pool, cpu_count
from functools import partial


def fmt_time(seconds):
    minutes = int(seconds // 60)
    sec = int(seconds % 60)
    return f"{minutes:02d}:{sec:02d}"

def get_duration(file_path):
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

    print(f"\033[1;36m♪ :::\033[0m {os.path.basename(track)}\n")

    player = subprocess.Popen(
        ['ffplay', '-nodisp', '-autoexit', '-hide_banner', '-loglevel', 'error', track],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )

    terminal_width = shutil.get_terminal_size((80, 20)).columns
    bar_length = terminal_width - 20  
    anim_index = 0
    start = time.time()

    while player.poll() is None:
        elapsed = time.time() - start
        if duration:
            progress_ratio = min(elapsed / duration, 1.0)
            filled_len = int(bar_length * progress_ratio)
            time_str = f"{fmt_time(elapsed)}/{fmt_time(duration)}"
        else:
            time_str = fmt_time(elapsed)

        print(f"\r {time_str}", end='', flush=True)
        anim_index += 1
        time.sleep(0.15)

    print("\n\033[1;32mMONA LISA OVERDRIVE!\033[0m")

if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "play_with_ui":
        play_with_ui(sys.argv[2])

