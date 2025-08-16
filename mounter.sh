
#!/bin/bash

DEVICE="/dev/sda1"
MOUNT_LABEL="BAKITUP"
TARGET_DIR="/media/$USER/$MOUNT_LABEL"

udisksctl mount -b "$DEVICE"


sleep=2
