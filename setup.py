from setuptools import setup

setup(
    name="aws-snapshots-automation",
    version='0.1',
    author="Sathish Sandu",
    author_email="sathish.sandu@gmail.com",
    description="This is a tool to manage AWS EC2 Snapshots",
    license="GPLv3+",
    packages=['shotty'],
    url='https://github.com/sathishsandu/aws-snapshots-automation',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)
