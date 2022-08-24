# Add pre-commit hooks for flask app

## install pre-commit 
```bash
pip install pre-commit;
pre-commit --version
pre-commit install-hooks
```


## Add a pre-commit configuration
```bash

# Create file in the root dir of the project.
touch .pre-commit-config.yaml

# Update the file with the below content.
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v2.3.0
    hooks:
    -   id: trailing-whitespace
    -   id: end-of-file-fixer
    -   id: check-yaml
    -   id: debug-statements
    -   id: double-quote-string-fixer
    -   id: name-tests-test
    -   id: requirements-txt-fixer
-   repo: https://github.com/psf/black
    rev: stable
    hooks:
    - id: black
      language_version: python3.10
-   repo: https://gitlab.com/pycqa/flake8
    rev: 3.7.9
    hooks:
    - id: flake8

```

# References
ref: https://pre-commit.com/
ref: 


