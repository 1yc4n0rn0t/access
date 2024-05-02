#!/bin/bash

# Bash Commands

figlet -f slant Access | lolcat

cowsay -f kosh GRANTED | lolcat

echo ""

echo "Access is bash script written in python" | lolcat
echo ""
echo "It can be used to gather intelligence on websites and webservers." | lolcat
echo ""
echo ""

echo "Functions:" | lolcat
echo ""
echo ""

echo "1) Domain to IP" | lolcat 
echo "2) Open Ports" | lolcat
echo "3) Passwords" | lolcat
echo "4) Language/Framework" | lolcat
echo "5) Hidden Pages" | lolcat
echo "6) Open in browser" | lolcat
echo ""
echo "=====================================================================" | lolcat
echo "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++" | lolcat
echo "=====================================================================" | lolcat
echo ""

# Python Code

python domain.py

echo ""
python ports.py
echo ""
python passwords.py
echo ""
python frame.py
echo ""
python hide.py
echo ""
python browse.py

# End Python Code
