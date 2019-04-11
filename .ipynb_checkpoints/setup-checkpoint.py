from setuptools import setup,find_packages

setup(
   name='hohi',
   version='0.1(dev)',
   description='Track the evolution of adiabatic eigenstates against an interaction parameter.',
   author='J.D.R Tommey',
   author_email='ucapdrt[at]ucl[dot]ac[dot]uk',
   url="https://github.com/jdrtommey/adiabatic_evolution",
   packages=find_packages(),  #same as name
   install_requires=['numpy','scipy','numba','tqdm'], #external packages as dependencies
)