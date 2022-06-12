#!/bin/bash

if [[ -d /home/$USER/Pictures/decay ]]; then
  echo "AWESOME! dir [~/Pictures/decay] already exists."
else
  mkdir /home/$USER/Pictures/decay
  echo "dir [~/Pictures/decay] has been created successfully!"
fi

if [[ -z $1 ]]; then
  decayFactorypy
else
  decayFactorypy $1
fi
