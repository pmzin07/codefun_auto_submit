@echo off
title CodeFun AutoSubmit Script

echo --- Dang kiem tra va cap nhat pip ---
python -m pip install --upgrade pip

echo.
echo --- Dang cai dat Selenium ---
pip install selenium

echo.
echo --- (Tuy chon) Cai dat webdriver-manager ---
pip install webdriver-manager

echo.
echo --- Chay file Main.py ---
python Main.py

echo.
echo --- Hoan tat! Nhan phim bat ky de thoat ---
pause