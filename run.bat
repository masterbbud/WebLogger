@echo off
call genenv
call cd C:\Users\maste\Documents\Python\WebLogger
call python main.py
call git add logs/*
call git commit -m "Added new backup" -a
call git push