# Install maven v3.8.6 on Ubuntu

**Create `bin` directory and `change directory` into it**

```bash
mkdir -p ~/bin && cd $_;
```

**Download maven v3.8.6**

```bash
wget https://dlcdn.apache.org/maven/maven-3/3.8.6/binaries/apache-maven-3.8.6-bin.zip;
```

**Extract downloaded maven v3.8.6**

```bash
unzip apache-maven-3.8.6-bin.zip;
```

**Update the profile file**

```bash
cat << 'EOT' >> ~/.profile
# maven v3.8.6
export PATH=~/bin/apache-maven-3.8.6/bin:$PATH
EOT
```

**Update maven to PATH**

```bash
source ~/.profile;
```

**Check the installed version of maven**

```bash
mvn -v; # Output looks like below.
```

- OUTPUT: `Apache Maven 3.8.6 (84538c9988a25aec085021c365c560670ad80f63)
Maven home: /home/<your username>/bin/apache-maven-3.8.6
Java version: 1.8.0_312, vendor: Private Build, runtime: /usr/lib/jvm/java-8-openjdk-amd64/jre
Default locale: en_IN, platform encoding: UTF-8
OS name: "linux", version: "5.13.0-52-generic", arch: "amd64", family: "unix`
