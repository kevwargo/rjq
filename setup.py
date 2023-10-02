from setuptools import find_packages, setup

setup(
    name="rjq",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "rjq = rjq:run",
        ]
    },
)
