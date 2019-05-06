#!/bin/env python
from setuptools import setup

install_requires = []

setup_kwargs = dict(
    name="nexxera.nix",
    url="https://github.com/nexxera/nix",
    description=".",
    long_description=""".""",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    keywords=[],
)

# Versioning
setup_kwargs["use_scm_version"] = {"root": "..", "relative_to": __file__}

# Packages (using namespace)
setup_kwargs["include_package_data"] = True
setup_kwargs["packages"] = ["nexxera", "nexxera.nix"]
setup_kwargs["namespace_packages"] = ["nexxera"]

# Dependencies
setup_kwargs["install_requires"] = install_requires
setup_kwargs["dependency_links"] = []
setup_kwargs["setup_requires"] = ["setuptools_scm"]
setup_kwargs["tests_require"] = []

# Zops commands
setup_kwargs[
    "entry_points"
] = """
[zops.plugins]
nix=nexxera.nix.zops:main
"""

setup(**setup_kwargs)
