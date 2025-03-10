from setuptools import setup, find_packages


setup(
    name="cliname",
    version="0.1",
    packages=find_packages(),
    install_requires=["click"],
    entry_points={
        "console_scripts": [
            # 'prefix = package.module:func'
            "cliname=cli.script:cli"
        ],
    },
    author="Author Name",
    description="A simple CLI tool.",
)
