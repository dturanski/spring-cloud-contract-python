from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='spring-cloud-contract',

    version='0.1.0',
    description='Python support for Spring Cloud Contract',
    long_description=readme,
    author='David Turanski',
    author_email='dturanski@gmail.com',
    url='https://github.com/dturanski/springcloudcontract',
    license=license,
    packages=("spring", "spring.cloud", "spring.cloud.contract")
)
