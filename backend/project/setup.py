from setuptools import setup, find_packages
setup_requires = [
    ]
install_requires = [
    'django==3.2.4',
    'html5lib==1.1',
    'wheel==0.36.2',
    'JPype1==1.1.2',
    'konply==0.5.2',
    'wordcloud==1.8.1'
    ]
dependency_links = [
    'git+https://github.com/django/django.git@stable/1.6.x#egg=Django-1.6b4',
    ]
setup(
    name='Root App',
    version='0.1',
    description='Root App',
    author='root',
    author_email='root@root.com',
    packages=find_packages(),
    install_requires=install_requires,
    setup_requires=setup_requires,
    dependency_links=dependency_links,
    scripts=['manage.py'],
    entry_points={
        'console_scripts': [
            'publish = project.common.script:main',
            'scan = project.crime.script:main',
            'update = project.gas_station.script:main',
            ],
        },
    )