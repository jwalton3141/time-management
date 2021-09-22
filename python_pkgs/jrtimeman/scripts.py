import subprocess


def test():
    """Run all unittests."""
    result = subprocess.run(
      ["python", "-u", "-m", "unittest", "discover"],
      capture_output=True
    )
    print(result.stdout.decode("utf8"), end="")
    print(result.stderr.decode("utf8"), end="")
    # helpful in a CI pipeline
    if result.returncode:
        exit(code=result.returncode)
