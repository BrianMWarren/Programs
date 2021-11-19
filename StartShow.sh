# !/bin/bash 
python3 /media/pi/PhotoBackup/Music/Programs/LEDFXPreset_haloweenscroll.py
DISPLAY=:0.0 /usr/bin/vlc --playlist-autostart --play-and-exit --no-loop "/media/pi/PhotoBackup/Music"
wait
echo "done playing! Setting off preset"
python3 /media/pi/PhotoBackup/Music/Programs/LEDFXPreset_off.py