# Install Node JS

**Create `bin` direcotry**

```bash
$ mkdir -p ~/bin && cd $_
```

**Download and install node js**

```bash
$ wget https://nodejs.org/dist/v16.13.2/node-v16.13.2-linux-x64.tar.xz;

$ tar xf node-v16.13.2-linux-x64.tar.xz;

$ ln -s ~/bin/node-v16.13.2-linux-x64 ~/bin/node;
```

**Add node js to PATH**

```bash
$ vi  ~/.bashrc

# Add below 3 lines into bashrc file.

# NodeJS
export NODEJS_HOME=~/bin/node/bin
export PATH=$NODEJS_HOME:$PATH

$ . ~/.bashrc
```

**Verify the node js version**

```bash
$ node -v
$ npm -v
```
