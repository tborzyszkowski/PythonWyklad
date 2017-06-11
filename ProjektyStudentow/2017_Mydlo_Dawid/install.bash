#!/usr/bin/env bash

if [ -z "$PET_FOLDER" ]; then
    PET_FOLDER="${HOME}/.pet"
else
    if [ "${PET_FOLDER:0:1}" == "~" ]; then
        PET_FOLDER="${HOME}${PET_FOLDER:1}"
    fi
    if [ "${PET_FOLDER: -1}" == "/" ]; then
        PET_FOLDER="${PET_FOLDER:0:${#PET_FOLDER}-1}"
    fi
fi
if [ -z "$install_dir" ]; then
    install_dir="."
else
    if [ "${install_dir:0:1}" == "~" ]; then
        install_dir="${HOME}${install_dir:1}"
    fi
    if [ "${install_dir: -1}" == "/" ]; then
        install_dir="${install_dir:0:${#install_dir}-1}"
    fi
fi

curl -fsSL https://github.com/limebrains/pet/archive/master.zip -o pet.zip
if [ ! -f pet.zip ]; then
    printf "\n\e[1;31mInstallation unsuccessful due to failed download\e[0m\n"
    exit
fi
unzip -o pet.zip -d "$install_dir"
rm -f pet.zip
if [ ! -d "$install_dir/pet-master" ]; then
    printf "\n\e[1;31mInstallation unsuccessful due to failed unzip\e[0m\n"
    exit
fi
pip install -e "$install_dir/pet-master/"
printf "\n------------------------\n-Installing rest of pet-\n------------------------\n"
if [ "$USER" == 'root' ]; then
    printf "\n\n\e[1;31mWarning (used as root): During first run use\npet recreate\e[0m\n"
else
    python "$install_dir/pet-master/pet/cli.py" 'recreate'
fi
printf "\n------------------------\n-auto-completion deploy-\n------------------------\n"
printf "\n\e[1;33mAuto-completion requires sudo\e[0m\n"
if [ "$USER" == 'root' ]; then
    if [ -z "$shell" ]; then
        sudo python 'pet-master/pet/cli.py' 'deploy'
    else
        sudo python 'pet-master/pet/cli.py' 'deploy' '-s' "$shell"
    fi
else
    printf "\n\e[1;33mNeeds sudo - use 'sudo pet deploy'\e[0m\n"
fi
printf "\n\e[1;32mInstallation completed\e[0m\n"
