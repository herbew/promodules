from setuptools import setup, find_packages

setup(
    name='promodules',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'django>=3.2',
        'django-formtools>=2.2',
    ],
    author='Heribertus Rustyawan',
    author_email='herbew@gmail.com',
    description='Django Project Management Modules',
    url='https://github.com/herbew/promodules.git',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)