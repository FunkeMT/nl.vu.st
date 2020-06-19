![PyTesting](https://github.com/FunkeMT/nl.vu.st/workflows/pytesting/badge.svg)
![PyInstaller](https://github.com/FunkeMT/nl.vu.st/workflows/PyInstaller/badge.svg)

# HB-Sim2020
The Heart Beat Monitor Simulation Software (HB-Sim2020) is to be developed as part of the PROJECT assignment of the Software Testing course at the Vrije Universiteit Amsterdam.  The main purpose of the software is to be tested during as well as after development to discuss the possible bugs for educational purposes. The software will run a simulation of a generic heartbeat monitor used in a medical facility. The heartbeat monitor should be able to notify the medical team of any anomalies in the oxygen levels, heart beat and blood pressure as well as give a constant update on these current values via a command line interface. Since this software should simulate a heartbeat monitor, it is not connected to any actual sensors and thus will receive it’sinput through a test file.

The main purpose and focus of this project is the investigation and development of software testing techniques based on a simple program implementation. The project starts with the formulation of the Software Requirements Specification (SRS) according to IEEE Std 830-1998. After the SRS is accepted, a software test plan is developed according to ANSI/IEEE Standard 829-1983. The actual implementation follows the developed guidelines from both the SRS and the test plan.

## Software Requirements Specification (SRS)
The SRS follows the IEEE Std 830-1989 guideline.

[Software Requirements Specification](https://github.com/FunkeMT/nl.vu.st/blob/master/docs/srs/main.pdf)

## Testing
The test phase is divided into two phases, namely (a) black box tests and (b) white box tests. The black-box tests are carried out by another study group in order to achieve an actual black-box test. However, the two phases consist of:

### Black-Box Testing
- Requirements Verification full SRS
- Individual Requirements Verification
- Requirements Validation
- Domain testing
- Boundary values analysis
- Equivalence  partitioning 
- Decision Table Testing

### White-Box Testing
[Test Plan](https://github.com/FunkeMT/nl.vu.st/blob/master/docs/test-plan/main.pdf)

- Test-Driven Development
- Code Review
- Static Code Analysis - linting
- Unit Testing (PyTest and PyCoverage)
- Mutation Testing
- Data Flow Diagram
- Integration Test
- User Acceptance Test

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
