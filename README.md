# CHWAL

Change your wallpaper with pywal, automatically recompile Suckless' software, and update the terminal.

### Usage
`config.sh` file:
```sh
dwm_path=<path_to_dwm_source>
st_path=<path_to_st_source>
dmenu_path=<path_to_dmenu_source>

term=<terminal you are using>
```

call chwal.sh followed by a path to the image you want to set as a new background:
```sh
source chwal.sh path/to/image.png
```

Issue: dwm restart needed for dmenu to update itself

Supported terminals:

- Alacritty
- Suckless' ST
