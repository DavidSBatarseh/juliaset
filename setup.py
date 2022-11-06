from setuptools import setup
from Cython.Build import cythonize
#cython: language_level=3
setup(
    name='juliaSetOptimization',
    ext_modules = cythonize('juliaFunction.pyx', compiler_directives={'language_level': 3}),
    zip_safe=False,
)