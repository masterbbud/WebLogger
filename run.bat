@echo off
python main.py
git add logs/*
git commit -m "Added new backup" -a
git push