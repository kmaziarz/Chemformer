from setuptools import setup

setup(
    name="syntheseus-chemformer",
    version="0.2.0",
    description="Fork of Chemformer for use in the syntheseus library",
    package_dir={
        "chemformer": ".",
        "chemformer.molbart": "molbart"
    },
    package_data={"": ["*.txt"]},
    install_requires=[
        "pytorch-lightning==1.9.4",
        "torchmetrics==1.5.1",
        "syntheseus-PySMILESutils"
    ],
    url="https://github.com/kmaziarz/Chemformer",
)
