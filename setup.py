from setuptools import setup, find_packages

setup(
    name='template', #change project name
    version='0.1.0',
    description='A short description of your project',
    author='Tomas Zinkevic',
    author_email='tom.zinkevic@gmail.com',
    url='https://github.com/Tom-Znk/template', #change project name
    packages=find_packages(),
    install_requires=[
        'numpy',             
        'scikit-learn',
        'torch',
        'matplotlib',
        'tqdm',
        # Add more dependencies as needed
    ],
    extras_require={
        'dev': [  # Development dependencies (e.g., for testing and linting)
            'pytest',
            'flake8',
            'mypy',
            # Add more development dependencies as needed
        ]
    },
    python_requires='>=3.11',  # Specify the minimum Python version required
)