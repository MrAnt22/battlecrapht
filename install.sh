#!/bin/bash
detect_distro() {
    if [ -f /etc/os-release ]; then
        . /etc/os-release
        echo $ID
    else
        echo "unknown"
    fi
}

install_python() {
    DISTRO=$(detect_distro)

    case "$DISTRO" in
        "ubuntu" | "debian")
            echo "Detected Ubuntu/Debian-based system."
            sudo apt update
            sudo apt install -y software-properties-common
            sudo add-apt-repository -y ppa:deadsnakes/ppa
            sudo apt update
            sudo apt install -y python3.11
            ;;

        "fedora")
            echo "Detected Fedora-based system."
            sudo dnf update -y
            sudo dnf install -y python3.11
            ;;

        "arch" | "manjaro")
            echo "Detected Arch/Manjaro-based system."
            sudo pacman -Sy --needed --noconfirm python
            ;;

        *)
            echo "Unsupported or unknown distribution."
            exit 1
            ;;
    esac

    if command -v python3.11 >/dev/null 2>&1; then
        echo "Python 3.11 installed successfully!"
        python3.11 --version
    else
        echo "Failed to install Python 3.11."
        exit 1
    fi
}

install_python

echo "Installing other dependencies..."

pip install pygame

echo "Everything is now installed. Press anything to exit."

read -n 1 -s
