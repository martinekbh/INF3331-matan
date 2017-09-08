#!/bin/bash

#ADD A BOOKMARK TO THE ~/.bookmarks FILE
if [ "$1" = "-a" ]; then
  if [ $# -eq 2 ]; then
    bookmarkname=$2
    bookmarklocation=$(pwd)     #Address of current directory
    echo "$bookmarkname|$bookmarklocation" >> $HOME/.bookmarks  #Add bookmark to the .bookmarks file
    declare "${bookmarkname}"=$bookmarklocation        #Declare bookmark variable
    echo "Successfully added bookmark to the ~/.bookmarks file."
    echo "Name of bookmark: $bookmarkname"
    echo "Bookmark locaktion: $bookmarklocation"
  else
    echo "You need to give one, and only one, name for the bookmark after '-a'"
  fi

#REMOVE A BOOKMARK FROM THE ~/.bookmarks file
elif [ "$1" = "-r" ]; then
  if [ $# -eq 1 ]; then
    echo "You need to give the name of the bookmark you want removed."
  else
    shift
    file=~/.bookmarks        #Address to the bookmarks-file
    if [ -f $file ]; then   #Check if file exists
      while read -r line
      do
        bookmark=$(echo $line| cut -d'|' -f 1) #Find name of bookmark
        if [ $bookmark = $1 ]; then           #If bookmark is the one to be deleted...
          echo "Found bookmark to be removed from the .bookmarks file: $bookmark"
          sed -i "/$1/d" $file    #Delete bookmark
          unset $bookmark
          exit 
        fi
      done<$file
      echo "The bookmark $2 was not found in the .bookmarks file" #The script exits before this if it found the bookmark
    else
      echo "The .bookmarks file count not be found in the home directory"
    fi
  fi

#RUN SCRIPT
elif [ $# -eq 0 ]; then
  file=~/.bookmarks        #Addess to the bookmarks-file
  if [ -f $file ]; then    #Check if file exists
    while read -r line
    do
      substring=$(echo $line| cut -d'|' -f 1) #Find name of bookmark
      declare "${substring}"=$(echo $line| cut -d'|' -f 2) #Save location of bookmark to the given name
    done <$file
  else
    echo "The .bookmarks file could not be found in the home directory"
  fi

else
  echo "No valid arguments were given. Use -a <bookmarkname> to add current directory to the list of bookmarks."
  echo "Use -r <bookmarkname> to remove a bookmark from the list of bookmarks."
fi
