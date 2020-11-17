#!/usr/bin/env python3
'''
Install molehill.
'''
import setuptools

ver_globals = {}
with open("molehill/version.py") as fp:
    exec(fp.read(), ver_globals)
version = ver_globals["version"]

setuptools.setup(
    name="molehill",
    version=version,
    author="Brett Viren",
    author_email="brett.viren@gmail.com",
    description="Model oriented objects",
    url="https://brettviren.github.io/molehill",
    packages=setuptools.find_packages(),
    python_requires='>=3.5',    # use of typing probably drive this
    install_requires=[
        "click",
        "moo",
        "pyzmq",
        "pyre",
    ],
    entry_points=dict(
        console_scripts=[
            'mole = molehill.__main__:main',
        ]
    ),
    include_package_data=True,
)
