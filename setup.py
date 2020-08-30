import pathlib

from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()


def get_version(root, rel_path):
    for line in (root / rel_path).read_text().splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find the version string (`__version__`).")


setup(
    name="mahou",
    version=get_version(HERE, "mahou/__init__.py"),
    description="A package full of tricks... sorry, full of IPython magic commands.",
    long_description=README,
    long_description_content_type="text/markdown",
    author="João Palmeiro",
    author_email="jm.palmeiro@campus.fct.unl.pt",
    url="https://github.com/joaopalmeiro/mahou",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: IPython",
        "Framework :: Jupyter",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
    license="MIT",
    keywords="formatter, ipython, black, jupyter, notebook, magic",
    include_package_data=True,
    install_requires=["black", "ipython"],
    python_requires=">=3.6, <=3.8",
    project_urls={
        "Bug Reports": "https://github.com/joaopalmeiro/mahou/issues",
        "Source": "https://github.com/joaopalmeiro/mahou",
    },
)
