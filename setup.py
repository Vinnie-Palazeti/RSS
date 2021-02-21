import setuptools

setuptools.setup(
    name="RSS",  # Replace with your own username
    version="0.0.1",
    author="Vinnie Palazeti",
    author_email="vinnie.palazeti@gmail.com",
    description="cmd line RSS",
    packages=setuptools.find_packages(),
    install_requires=[
        'datetime',
        'requests',
        'bs4',
        'argparse'
    ],
    python_requires='>=3.6',
)
