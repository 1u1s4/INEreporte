from setuptools import setup, find_packages

setup(
    name='reporteine',
    version='0.2',
    author='Luis Alfredo Alvarado Rodríguez',
    description='Creador de reportes estilo INE.',
    long_description='',
    url='https://github.com/1u1s4/INE_LaTeX',
    keywords='development, setup, setuptools',
    python_requires='>=3',
    packages=find_packages(),
    py_modules=['funcionesINE', 'reporteine', 'WS_orga_INE'],
    install_requires=[
        'pandas',
        'rpy2'
    ],
    package_data={
        'reporteine': ['Fuentes/*', 'Plantilla/*', 'Direcciones/DCE/*', 'Direcciones/DIEC/*', 'Direcciones/DPIR/*'],
    },
    include_package_data=True,
)
