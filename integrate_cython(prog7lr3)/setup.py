from distutils.core import setup, Extension
from Cython.Build import cythonize

ext_modules = [
    Extension(
        "integrate",
        ["integrate.pyx"],
        extra_compile_args=['/fopenmp']
    )
]

setup(
    ext_modules=cythonize(ext_modules),
)