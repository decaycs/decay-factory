#!/bin/bash

if [[ -d /home/$USER/Pictures/odf ]]; then
  echo "AWESOME! dir [~/Pictures/odf/] already exists."
else
  mkdir /home/$USER/Pictures/odf
  echo "dir [~/Pictures/odf/] has been created successfully!"
fi

if [[ -z $1 ]]; then
  odfpy
else
  odfpy $1
fi
