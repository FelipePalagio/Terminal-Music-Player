
#!/bin/bash
# Monta automaticamente a memoria externa no caminho DEVICE
eval "$(luajit config.lua bash)"

DEVICE="$DVC"
MOUNTPOINT="$1"

OK="✔"; ERR="✘"; INFO="➜"
GREEN="\e[32m"; RED="\e[31m"; YELLOW="\e[33m"; RESET="\e[0m"

if [ -z "$MOUNTPOINT" ]; then
    echo -e "${RED}${ERR} NENHUM DISPOSITIVO FISICO ENCRONTRADO.${RESET}"
    echo -e "${INFO} : $0 /media/\$USER/LABEL"
    exit 1
fi

OUT=$(udisksctl mount -b "$DEVICE" 2>&1)

if [ $? -eq 0 ]; then
    echo -e "${GREEN}${OK} FEITO O MOUNT${RESET}"
    echo -e "${INFO} ${OUT}"
else
    echo -e "${RED}${ERR} ERRO NO MOUNT${RESET}"
    echo "$OUT"
fi
