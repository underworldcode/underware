# -*- coding: utf-8 -*-

import pytest

# ==========================

def test_numpy_import():
    import numpy
    return

def test_scipy_import():
    import scipy
    print("\t\t You have scipy version {}".format(scipy.__version__))
    return

def test_sympy_import():
    import sympy
    print("\t\t You have sympy version {}".format(sympy.__version__))
    return

def test_pint_import():
    import pint
    return

def test_underware_import():
    import underware
    from underware import function 
    return

def test_jupyter_available():
    from subprocess import check_output
    try:
        result = str(check_output(['which', 'jupyter']))[2:-3]
    except:
        print( "jupyter notebook system is not installed" )
        print( "  - This is needed for notebook examples")
