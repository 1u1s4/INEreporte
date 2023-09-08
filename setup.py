from setuptools import setup, find_packages

setup(
    name='INEreporte',
    version='0.5.5',
    author='Luis Alfredo Alvarado Rodríguez',
    description='Creador de reportes estilo INE.',
    long_description='',
    url='https://github.com/1u1s4/INEreporte',
    keywords='development, setup, setuptools',
    python_requires='>=3.7',
    packages=find_packages(),
    py_modules=['Reporte'],
    install_requires=[
        'pandas',
        'rpy2',
        'requests',
        'bs4',
        'xlrd==2.0.1',
        'openpyxl',
        'html5lib',
        'utilsjo @ git+https://github.com/1u1s4/utilsjo.git',
        'colorimapgt @ git+https://github.com/1u1s4/colorimapgt.git'
    ],
    package_data={
        'INEreporte': ['Fuentes/*', 'Plantilla/*', 'Direcciones/DCE/*', 'Direcciones/DIEC/*', 'Direcciones/DPIR/*'],
    },
    include_package_data=True,
)
