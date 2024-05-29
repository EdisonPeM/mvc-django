#!/bin/bash

if docker ps | grep -q biblioteca_app
then
  docker exec server sh -c "$*"
else
  echo "Container is not running"
fi
