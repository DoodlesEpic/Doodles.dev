#!/bin/bash

cd $1
git add -A
git commit -m "Website atualizado"
git push origin main