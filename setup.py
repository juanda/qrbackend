from setuptools import setup

setup(
    name='qrbackend',
    packages=['qrbackend'],
    version='0.1.0',
    author='Juan David Rodríguez García',
    description='API para aplicación demo para openwebminars',
    license='MIT',
    author_email='juanda@juandarodriguez.es',
    include_package_data=True,
    install_requires=[
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    scripts=['bin/run.py']
)
