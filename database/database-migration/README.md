# database-migrations-scripts

## create environment
```bash
conda env create -f environment.yml
conda activate database-migration
```

## diretory structure
```bash
mkdir postgredb
cd postgredb
```

## alembic init
```bash
alembic init blockchainsentry
```

## create revision
```bash
alembic revision -m "create bcs data"
```



