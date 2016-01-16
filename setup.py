from setuptools import setup, find_packages

setup( name='kopytka',
    version = '1.0',
    description = 'A simple CMS for Django',
    author = 'Curtis Maloney',
    author_email = 'curtis@tinbrain.net',
    url = 'http://github.com/funkybob/kopytka/',
    keywords = ['django', 'cms',],
    packages = find_packages(),
    include_package_data=True,
    zip_safe = False,
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    install_requires = [
        'Django>=1.9',
        'PyScss>=1.3.4',
    ]
)

