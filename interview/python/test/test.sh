#! /usr/bin/bash

test=("$@")
j=0
for i in "$@"
do
  echo $i
  j=($j+1)
  echo $j
done