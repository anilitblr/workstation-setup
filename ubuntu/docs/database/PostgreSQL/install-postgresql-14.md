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

### Create a role

```bash
sudo -i;

su - postgres;

psql;

CREATE ROLE test WITH PASSWORD 'pass.word';

ALTER ROLE test NOSUPERUSER INHERIT NOCREATEDB NOCREATEROLE NOREPLICATION LOGIN;
```

### Create testdb database

```bash
CREATE DATABASE testdb WITH OWNER=test;
```

### Grant role permissions

```bash
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO test;

GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public to test;

GRANT USAGE ON SCHEMA public TO test;
```

### Drop testdb database

```bash
-- Drop the database
-- The multiple lines below are necessary b/c the Postgresql server has a safety
-- check where it won't drop a DB if there are any existing connections. The
-- error message will look like:
-- ERROR:  database "ss" is being accessed by other users
-- DETAIL:  There are 10 other sessions using the database.
SELECT 
   pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE
   pg_stat_activity.datname = 'testdb'
AND pid <> pg_backend_pid();

DROP DATABASE IF EXISTS testdb;
```

### Restore database

```bash
# Note: This is a example to create a shell script to restore database, it can be improved further to CREATE/RESTORE/DROP

vi restore-database.sh

# Variables
# ----------------------------------------------------------------------
SERVER=localhost
DATABASE=testdb
PORT=5432
USERNAME=test

echo "- Restore database"
psql -h ${SERVER} -p ${PORT} -U ${USERNAME} -d ${DATABASE} -w < testdb.sql

chmod +x restore-database.sh

sh restore-database.sh
```
