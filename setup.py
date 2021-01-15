import setuptools
import sys


setuptools.setup(
    name="benepar",
    version="0.2.0a0",
    author="Nikita Kitaev",
    author_email="kitaev@cs.berkeley.edu",
    description="Berkeley Neural Parser",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/nikitakit/self-attentive-parser",
    package_dir={"": "src"},
    packages=setuptools.find_packages("src"),
    python_requires=">=3.6",
    classifiers=(
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Text Processing :: Linguistic",
    ),
    install_requires=[
        "nltk>=3.2",
        "spacy>=2.0.9,<3.0.0",
        "torch>=1.6.0",
        "torch-struct @ git+https://github.com/harvardnlp/pytorch-struct@v0.4",
        "genbmm @ git+https://github.com/harvardnlp/genbmm@9a512865c7c18eed392ec490d0549933ab433f54",
        "tokenizers>=0.9.4",
        "transformers[torch,tokenizers]>=4.2.2",
        "protobuf",
        "sentencepiece>=0.1.91",
        "dataclasses;python_version<'3.7'",
    ],
)
