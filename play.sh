
#!/bin/bash

MOUNTPOINT="/media/felipe_palagio/BAKITUP"

if mountpoint -q "$MOUNTPOINT"; then
    true
else
    echo "Mounting $MOUNTPOINT..."
    ./mounter.sh
fi

python3 SHIBA.py
