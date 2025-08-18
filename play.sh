#!/bin/bash

MOUNTPOINT="/media/felipe_palagio/BAKITUP"

if mountpoint -q "$MOUNTPOINT"; then
    true
else
    echo "Mounting $MOUNTPOINT..."
    ./mounter.sh
fi


while [[ $# -gt 0 ]]; do
  case "$1" in
    -s)
      var="$2"
      shift 2
      ;;
    *)
      shift
      ;;
  esac
done



choice=$(python3 busca.py -s "$var" | fzf --prompt="Select item: ")
python3 runtime.py play_with_ui "$choice"
