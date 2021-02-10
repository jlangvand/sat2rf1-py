import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sat2rf1-orbitntnu", # Replace with your own username
    version="0.0.1",
    author="Joakim Skogø Langvand @jlangvand",
    author_email="jlangvand@gmail.com",
    description="Tools for Nanoavionics Sat2RF1",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jlangvand/sat2rf1",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)
