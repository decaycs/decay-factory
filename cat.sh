#!/bin/bash

if [[ -d /home/$USER/Pictures/cat ]]; then
  echo "AWESOME! dir [~/Pictures/cat/] already exists."
else
  mkdir /home/$USER/Pictures/cat
  echo "dir [~/Pictures/cat/] has been created successfully!"
fi

if [[ -z $1 ]]; then
  catFactorypy
else
  catFactorypy $1
fi
