#!/bin/bash
python virtualenv.py flask
flask/bin/pip install -r requirements.txt
mkdir tmp
