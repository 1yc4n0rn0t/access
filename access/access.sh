#!/bin/bash

# Ensure figlet, lolcat, cowsay are installed
# Uncomment the following lines to install dependencies (if not installed)

# sudo apt-get install figlet lolcat cowsay

# Display ASCII Art with lolcat and figlet
figlet -f slant "Access" | lolcat

cowsay -f kosh "GRANTED" | lolcat

echo ""  # Empty line

# Display some informational text with lolcat
echo "Access is a bash script written in Python" | lolcat
echo ""
echo "It can be used to gather intelligence on websites and web servers." | lolcat
echo ""
echo ""

# List available functions
echo "Functions:" | lolcat
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
echo ""  # Empty line

# Execute Python scripts to perform various tasks

echo "Running Domain to IP script..." 
python3 domain.py
echo ""

echo "Running Open Ports script..."
python3 ports.py
echo ""

echo "Running Passwords script..."
python3 passwords.py
echo ""

echo "Running Language/Framework detection script..."
python3 frame.py
echo ""

echo "Running Hidden Pages script..."
python3 hide.py
echo ""

echo "Running Open in Browser script..."
python3 browse.py
echo ""

echo "All tasks complete!"
