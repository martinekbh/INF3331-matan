#!/bin/bash
if [ "$#" = "0" ]; then
  echo "You forgot to write some arguments"
  exit
fi

if [ "$1" = "S" ]; then       #Summation
  echo "Finding sum..."
  sum=0
  shift #skip first argument
  while [ $# -gt 0 ]
  do
    if [ "$1" -eq "$1" ] 2>/dev/null #Make sure argument is an integer
    then
      let "sum+=$1"
      shift
    else
      echo "$1 is not an integer"
      exit
    fi
  done
  echo "Sum: ${sum}"
  exit

elif [ "$1" = "P" ]; then   #Finding the product
  echo "Finding product..."
  prod=1
  shift
  for number in "$@"
  do
    if [ "$number" -eq "$number" ] 2>/dev/null #Is argument an integer?
    then
      let "prod=prod * number"
    else
      echo "$number is not an integer"
      exit
    fi
  done
  echo "Product: ${prod}"
  exit

elif [ "$1" = "M" ]; then     #Maximum
  echo "Finding maximum..."
  max=0
  shift
  while [ $# -gt 0 ]
  do
    if [ "$1" -eq "$1" ] 2>/dev/null
    then
      if [ $1 -gt $max ]; then
        max=$1
      fi
      shift
    else
      echo "$1 is not an integer"
      exit
    fi
  done
  echo "Maximum: ${max}"
  exit

elif [ "$1" = "m" ]; then     #Minimum
  echo "Finding minimum..."
  shift
  min=$1
  shift
  while [ $# -gt 0 ]
  do
   if [ "$1" -eq "$1" ] 2>/dev/null
   then
     if [ $1 -lt $min ]; then
        min=$1
      fi
      shift
    else
      echo "$1 is not an integer"
      exit
    fi
  done
  echo "Minimum: ${min}"
  exit

else
  echo "The first argument written has to be one of the following:"
  echo "S (sum), P (product), M (maximum), or m (minimum)"
  echo "The following arguments have to be whole numbers"

fi
