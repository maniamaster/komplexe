date=$(date +"%y%m%d_%H%M")
ls -vr *.png > stills.txt
mencoder -nosound -ovc lavc -lavcopts vcodec=mpeg4:aspect=16/9:vbitrate=8000000 -vf scale=1920:1080 -o $date.avi -mf type=png:fps=20 mf://@stills.txt
rm -f stills.txt
