@echo off
cd C:\Users\maste\Documents\Python\WebLogger
python main.py
git add logs/*
git commit -m "Added new backup" -a
git push