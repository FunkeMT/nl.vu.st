![pytesting](https://github.com/FunkeMT/nl.vu.st/workflows/pytesting/badge.svg)

# nl.vu.st
VU Amsterdam - Computer Science - Software Testing

## Setup

Create a new python ```virtualenv``` and execute the following steps:

Run pip:

```pip install -r requirements_dev.txt```

Install git pre-commit hook for *black*:

```pre-commit install```

## Tests

Create tests into the ```tests``` folder and execute tests via running ```pytest``` at the project root folder.

### Coverage

To create the test coverage report run

```pytest --cov=./ -v```

You can also find the current master coverage at the GitHub Actions build report at section *Generate coverage report*.

### Assignment

| Student | Gets Review From |
|---------|------------------|
| Sven    | Wouter           |
| Pjotr   | Markus           |
| Wouter  | Pjotr            |
| Markus  | Sven             |
