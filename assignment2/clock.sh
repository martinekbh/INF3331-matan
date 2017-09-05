#!/bin/bash
if [ "$1" = "sk" ]; then
  while [ 0 ]; do #Infinite loop
    clear
    TZ=Asia/Seoul date +%H:%M:%S
    sleep 1 #Lazy way to count seconds...
  done

elif [ "$1" = "no" ]; then
  while [ 0 ]; do #Infinite loop
    clear
    TZ=Europe/Oslo date +%H:%M:%S
    sleep 1
  done

elif [ "$1" = "us" ]; then
  while [ 0 ]; do #Infinite loop
    clear
    TZ=America/New_York date +%H:%M:%S
    sleep 1
  done

else
  while [ 0 ]; do #Infinite loop
    clear
    date +%H:%M:%S
    sleep 1
  done
fi
