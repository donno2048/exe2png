from setuptools import setup, find_packages
setup(
    name='exe2png',
    version='1.0.0',
    license='MIT',
    author='Elisha Hollander',
    author_email='just4now666666@gmail.com',
    description="Convert executables (or any other file) into an image",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url='https://github.com/donno2048/exe2png',
    project_urls={
        'Documentation': 'https://github.com/donno2048/exe2png#readme',
        'Bug Reports': 'https://github.com/donno2048/exe2png/issues',
        'Source Code': 'https://github.com/donno2048/exe2png',
    },
    python_requires='>=3.0',
    packages=find_packages(),
    install_requires=["pillow", "numpy"],
    classifiers=['Programming Language :: Python :: 3'],
    entry_points={ 'console_scripts': [ 'exe2png=exe2png.__main__:main' ] }
)
