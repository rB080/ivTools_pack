import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='ivTools',
    version='0.1.1',
    author='rB',
    author_email='rajbhothesecond@gmail.com',
    description='Initial Dev',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/rB080/ivTools.git',
    license='MIT',
    packages=['ivTools'],
    install_requires=[
        'opencv-python',

    ],
)
