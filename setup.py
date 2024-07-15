from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='TiLauncher',
    version='1.0',
    author='XTITAX',
    author_email='xtitax@yandex.ru',
    description='A short description of your package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/XTITAX/TiLauncher',
    packages=find_packages(include=['TiLauncher']),
    include_package_data=True,
    install_requires=[
        'minecraft_launcher_lib',
        'tkinter',
        'pillow',
        'subprocess',
        'os',
        'uuid',
        'json',
        'threading',
        'time',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)