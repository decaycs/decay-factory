#!/bin/bash

PICTURES_PATH=$HOME/Pictures/decay

if ! test -d $PICTURES_PATH; then
  mkdir $PICTURES_PATH
  echo "dir [~/Pictures/decay] has been created successfully!"
fi

decayFactorypy ${@}
