
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mOps-thezaza101",
    version="0.0.1",
    author="thezaza101",
    author_email="test@test.com",
    description="Mathematical operations using base python",
    long_description="Mathematical operations using base python...",
    long_description_content_type="text/markdown",
    url="https://github.com/verbaros/mOps",
    project_urls={
        "Bug Tracker": "https://github.com/verbaros/mOps/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD 3-Clause License",
        "Operating System :: OS Independent"
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
