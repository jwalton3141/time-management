import subprocess


def test():
    """Test

    Run all unittests. Equivalent to:
    `poetry run python -u -m unittest discover -s tests -v -p "*.py"`
    """
    subprocess.run(
        [
            'python', '-u', '-m', 'pytest',
            'tests'
        ]
    )

def _coverage():
    """Coverage

    Run a coverage report. Equivalent to:
    `poetry run coverage run -m unittest discover -s tests -p '*.py'`
    """
    subprocess.run(
        [
            'python', '-m',
            'coverage', 'run', '-m', 'pytest',
            'tests'
        ]
    )

def coverage_report():
    """Coverage report

    Report on coverage report
    Equivalent to:
    ```
    poetry run coverage run -m unittest discover -s tests -p '*.py'
    poetry run coverage report
    ```
    """
    _coverage()
    subprocess.run(
        ['python', '-m', 'coverage', 'report']
    )