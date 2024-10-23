machine="$(cat /etc/os-release | grep "ID_LIKE=")"
if [ $machine == "ID_LIKE=debian" ]
then
	sudo apt-get update -y && apt-get install nmap firefox-esr wireshark python3 python3-pip tcpdump tshark -y
elif [ $machine == "ID_LIKE=arch" ]
then
	sudo pacman -Syyu --noconfirm && pacman -S nmap firefox wireshark-qt python-pip python tcpdump termshark --noconfirm
fi
sudo mkdir /usr/share/mona/ && mkdir /usr/share/doc/project-monalisa/
sudo mv mona.py mona && chmod +x mona protocol.json project-monalisa.desktop
sudo mv mona /usr/bin && mv protocol.json /usr/share/mona && mv project_mona.png /usr/share/pixmaps && mv project-monalisa.desktop /usr/share/applications && mv README.md LICENSE /usr/share/doc/project-monalisa
sudo pip install -r requirements.txt --break

