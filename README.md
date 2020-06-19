![PyTesting](https://github.com/FunkeMT/nl.vu.st/workflows/pytesting/badge.svg)
![PyInstaller](https://github.com/FunkeMT/nl.vu.st/workflows/PyInstaller/badge.svg)

# nl.vu.st
VU Amsterdam - Computer Science - Software Testing

## Setup

Create a new python ```virtualenv``` and execute the following steps:

Run pip:

```pip install -r requirements_dev.txt```

Install git pre-commit hook for *black*:

```pre-commit install```

## GitHub Actions
### PyTesting
Will be triggered after push into the _master_ branch and executes the following tasks:

-  Lint with flake8
-  Test with pytest
-  Generate test coverage report

See [Workflow](https://github.com/FunkeMT/nl.vu.st/blob/master/.github/workflows/pytesting.yml) for more information.

### PyInstaller
Will be triggered after _tag_ creation (`v*`) and builds Python standalone packages/executables:

- build Unix (latest) executable
- build Windows (latest) executable
- build MacOS (latest) executable

Every build is packed into a ZIP container and includes a test file named _simulation.csv_.

See [Workflow](https://github.com/FunkeMT/nl.vu.st/blob/master/.github/workflows/pyinstaller.yml) for more information.

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
