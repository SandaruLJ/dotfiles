#!/bin/bash

cuefile=$1
audiofile=$2

if [ -z "$cuefile" -o -z "$audiofile"  ]; then
    echo "Please specify a CUE file and an audio file"
    exit 1
fi

echo -e "Splitting audio file '$audiofile' using CUE file '$cuefile' ...\n" &&
shnsplit -f "$cuefile" -o flac -t "%n. %t" "$audiofile" &&
echo -e "\n...Done!" &&

echo -e "\nDeleting the original audio file '$audiofile' ..." &&
trash "$audiofile" &&
echo "...Done!" &&

echo -e "\nChecking if pregap exists.."
for file in *.flac; do
    if [[ $file == 00.* ]]; then
        trash "$file"
    fi
done

echo -e "\nConverting FLAC files to MP3 ...\n" &&
parallel ffmpeg -i {} -qscale:a 0 {.}.mp3 ::: ./*.flac &&
echo -e "\n...Done!" &&

echo -e "\nDeleting FLAC files" &&
trash *.flac &&
echo "...Done!" &&

echo -e "\nTagging MP3s with data from '$cuefile' ..." &&
cuetag.sh "$cuefile" *.mp3 &&
echo "...Done!" &&

echo -e "\nDeleting the CUE file: '$cuefile' ..." &&
trash "$cuefile" &&
echo "...Done!" &&
echo -e "\nOperation finished successfully!"
