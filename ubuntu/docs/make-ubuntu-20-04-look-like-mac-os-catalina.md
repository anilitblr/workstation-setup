# Make Ubuntu 20.04 look like Mac OS Catalina

- [Make Ubuntu 20.04 look like Mac OS Catalina](#make-ubuntu-2004-look-like-mac-os-catalina)
  - [Install `universe` repository](#install-universe-repository)
  - [Install gnome tweak tool](#install-gnome-tweak-tool)
  - [Install gnome shell extensions](#install-gnome-shell-extensions)
  - [Install dconf editor](#install-dconf-editor)
  - [Download and extract GTK3 Themes](#download-and-extract-gtk3-themes)
  - [Download and extract icon themes](#download-and-extract-icon-themes)
  - [Download and extract shell themes](#download-and-extract-shell-themes)
  - [Download wallpaper](#download-wallpaper)
  - [Install plank - MacOS dock](#install-plank---macos-dock)
  - [Setup theme](#setup-theme)
  - [Disable dash-to-dock](#disable-dash-to-dock)

## Install `universe` repository

```bash
sudo apt-add-repository universe
```

## Install gnome tweak tool

```bash
sudo apt install gnome-tweak-tool
```

## Install gnome shell extensions

```bash
sudo apt install gnome-shell-extensions
```

## Install dconf editor

```bash
sudo apt install dconf-editor
```

## Download and extract GTK3 Themes

- Navigage to **https://www.gnome-look.org/p/1241688/**
- Click on **Files (31)** and download below 2 files.
  - Click on **Mc-OS-CTLina-Gnome-Dark-1.3.2.tar.xz** file to download
  - Click on **McOS-CTLina-Gnome-1.3.2.tar.xz** file to download
- Open terminal and execute below commands.
    ```bash
    cd ~/Downloads;
    sudo tar -xJf Mc-OS-CTLina-Gnome-Dark-1.3.2.tar.xz -C /usr/share/themes;
    sudo tar -xJf McOS-CTLina-Gnome-1.3.2.tar.xz -C /usr/share/themes;
    ```

## Download and extract icon themes

- Navigage to **https://www.gnome-look.org/p/1102582/**
- Choose **Download** and click on **Cupertino-Catalina.tar.xz**
- Open terminal and execute below commands.
    ```bash
    cd ~/Downloads;
    sudo tar -xJf Cupertino-Catalina.tar.xz -C /usr/share/icons;
    ```

## Download and extract shell themes

- Navigage to **https://www.gnome-look.org/p/1220826/**
- Click on **Files (4)** and download below 3 files.
  - Click on **mcOS11-Shell.zip** file to download
  - Click on **mcOS11-Shell-Dark.zip** file to download
  - Click on **mcOS11-GTK.zip** file to download
- Open terminal and execute below commands one by one.
    ```bash
    mkdir -p ~/.themes;
    cd ~/Downloads;
    unzip mcOS11-Shell.zip -d ~/.themes;
    unzip mcOS11-Shell-Dark.zip -d ~/.themes;
    unzip mcOS11-GTK.zip -d ~/.themes;
    ```

## Download wallpaper

- Navigage to **https://www.reddit.com/r/osx/comments**

## Install plank - MacOS dock

```bash
sudo apt-get install plank
```

## Setup theme

- Appearance 
  - Open **Tweaks** tool from applications
  - Applications: **McOS-CTLina-Gnome-1.3.2**
  - Icon: **Cupertino-Catalina**
  - Shell: **McOS11-Shell-Dark**
  - Background
    - Image: Choose **catalina.jpg** image
  - Lock Screen:
    - Image: Choose **catalina.jpg** image
  - Click on **<** at the top of the window, to go back to the main menu
- Extensions - Turn om only followings.
  - Applicatiion menu
  - Lock screen background
  - User themes
- Startup Applications
  - Add Plank
- Window Titlebars
  - Placement: **Left**  

## Disable dash-to-dock

- Choose **org** --> **gnome** --> **shell** --> **extensions** --> **dash-to-desk**
  - dash-max-icon-size: **25**
  - autohide (Dock shown on mouse over): **off**
  - autohide-in-fullscreen: **off**
  - dock-position:
    - Custom value: 'BOTTOM' 
