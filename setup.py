from setuptools import setup, find_packages

def parse_requirements(filename):
    """Load requirements from a pip requirements file."""
    with open(filename, "r") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="your_project_name",
    version="0.1",
    packages=find_packages(where="python"),
    package_dir={"": "python"},
    install_requires=parse_requirements("python/requirements.txt"),  # Production dependencies
    extras_require={
        "dev": parse_requirements("python/requirements-dev.txt"),    # Development dependencies
    },
    test_suite="tests",
)
