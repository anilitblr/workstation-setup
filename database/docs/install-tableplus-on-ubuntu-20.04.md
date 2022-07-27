# Install TablePlus on Ubuntu 20.04


## Add TablePlus gpg key
```bash
wget -qO - https://deb.tableplus.com/apt.tableplus.com.gpg.key | sudo apt-key add -
```
## Add TablePlus repo

```bash
sudo add-apt-repository "deb [arch=amd64] https://deb.tableplus.com/debian/20 tableplus main"
```

## Install

```bash
sudo apt update
sudo apt install tableplus
```

ref: https://tableplus.com/blog/2019/10/tableplus-linux-installation.html