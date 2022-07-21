# GitHub SSH setup on Ubuntu


- [GitHub SSH setup on Ubuntu](#github-ssh-setup-on-ubuntu)
  - [Set your Github username](#set-your-github-username)
  - [Set your email](#set-your-email)
  - [Generate your SSH key](#generate-your-ssh-key)
  - [Add your new SSH to the SSH config file](#add-your-new-ssh-to-the-ssh-config-file)
  - [Add your SSH private key to the ssh-agent](#add-your-ssh-private-key-to-the-ssh-agent)
  - [Add your SSH key to GitHub](#add-your-ssh-key-to-github)
  - [Verify that everything is setup correctly](#verify-that-everything-is-setup-correctly)

## Set your Github username

```
# Example: 
# git config user.name "github-username"
# git config --global user.name "github-username"

git config user.name "github-username"
git config --global user.name "github-username"
```

## Set your email

```
# Example: 
# git config --global user.email "your_email@youremail.com"
# git config user.email "your_email@youremail.com"

git config --global user.email "your-github-email-address"
git config user.email "your-github-email-address"
```

## Generate your SSH key

```
# Example: 
# ssh-keygen -t ed25519 -C "your_email@youremail.com" -f ~/.ssh/filename

ssh-keygen -t rsa -b 4096 -C "your_email@example.com" -f ~/.ssh/your-github-username

# Enter a passphrase when prompted.
```

## Add your new SSH to the SSH config file

```
vi ~/.ssh/config
```

Paste the following in the bottom of ~/.ssh/config.

```
Host github.com-your-github-username
    HostName github.com
    User git
    AddKeysToAgent yes
    UseKeychain yes
    IdentityFile ~/.ssh/your-github-username
```

## Add your SSH private key to the ssh-agent

```
# Example:
# ssh-add -K ~/.ssh/your-github-username

ssh-add -K ~/.ssh/your-github-username
```

## Add your SSH key to GitHub

```
# Example:
# cat ~/.ssh/your-github-username.pub

cat ~/.ssh/your-github-username.pub
```

Copy the output from the `cat` command and paste into GitHub based on the instructions below.

Open a browser to www.github.com and perform the following actions after logging
in.

- Click **Settings**.
- Click **SSH and GPG keys** in the left pane.
- Click **New SSH key**.
- Enter the following in **Title**: your-github-username.
- Paste your key into **Key**.
- Click **Add SSH key**.

## Verify that everything is setup correctly

```bash
ssh -p 22 -T git@github.com
```

The output should look like:

```bash
The authenticity of host 'github.com (IP Address)' can't be established.
RSA key fingerprint is XX:XX:XX:XX:XX:XX:XX:XX.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'github.com,IP Address' (RSA) to the list of known hosts.
Hi your-github-username! You've successfully authenticated, but GitHub does not provide shell access.
```
