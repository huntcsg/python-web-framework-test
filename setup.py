from setuptools import setup, find_packages


setup(
    name='web-framework-comparison',
    packages=find_packages('src'),
    package_dir={
        '': 'src',
    },
    install_requires=[
        'requests',
    ],
    extras_require={
        'flask': [
            'flask',
            'gunicorn',
        ],
        'pyramid': [
            'pyramid',
            'gunicorn',
        ],
        'tornador': [
            'tornado',
        ],
        'locust': [
            'locust',
        ],
        "quart": [
            "quart",
            "hypercorn"
        ],
    }
)
