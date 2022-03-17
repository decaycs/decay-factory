#!/bin/bash

if [[ -d /home/$USER/Pictures/odf ]]; then
  echo "AWESOME! dir [~/Pictures/cat/] already exists."
else
  mkdir /home/$USER/Pictures/odf
  echo "dir [~/Pictures/cat/] has been created successfully!"
fi

if [[ -z $1 ]]; then
  catpy
else
  catpy $1
fi
