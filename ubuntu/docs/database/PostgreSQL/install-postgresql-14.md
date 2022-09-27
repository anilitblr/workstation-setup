# install PostgreSQL on Ubuntu

### Create the file repository configuration

```bash
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
```

### Import the repository signing key

```bash
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
```

### Update the package lists

```bash
sudo apt-get update
```

### Install the latest version of PostgreSQL.
### If you want a specific version, use 'postgresql-14'

```bash
sudo apt-get -y install postgresql # install latest version
sudo apt-get -y install postgresql-14 # install postgresql-14
```

### Create .pgpass file for passwordless connection

```bash
echo "
#hostname:port:database:username:password
localhost:5432:testdb:test:pass.word" | tee ~/.pgpass
```

### Change .pgpass file permission

```bash
chmod 600 ~/.pgpass
```

### Connect to testdb database

```bash
psql -h localhost -p 5432 -U test -d testdb -w;
```
