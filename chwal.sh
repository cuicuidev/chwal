#!/bin/bash

source ./dependencies.sh

if [ -z "$1" ]; then
	echo "Usage: $0 <wallpaper_path>"
fi

source ./config.sh

image_path="$1"

cp "$image_path" $HOME/.local/wallpaper.png
wal -i "$image_path"

lines_to_comment=(9 10 11 17)

for n in ${lines_to_comment[@]}; do
	sed -i "${n}s/^/\/\//" $HOME/.cache/wal/colors-wal-dwm.h
done

python $term.py

sudo make -C $st_path clean install
sudo make -C $dmenu_path clean install

