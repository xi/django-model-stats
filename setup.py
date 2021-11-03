from setuptools import find_packages, setup


setup(
    name='django-model-stats',
    description='Display how often models and model fields are used in the database',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/xi/django-model-stats',
    author='Tobias Bengfort',
    author_email='tobias.bengfort@posteo.de',
    version='0.0.0',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)
