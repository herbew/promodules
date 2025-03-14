from setuptools import setup, find_packages

setup(
    name='promodules',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'promodules': ['templates/modules/*.html',],
        'modules': ['fixtures/*.json'],
    },
    install_requires=[
        'django==5.1.7',
        'django-formtools==2.5.1',
        'django-environ',
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
