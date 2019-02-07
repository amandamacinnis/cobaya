# Tries to evaluate the BK15 likelihood at a reference point

from __future__ import absolute_import
from copy import deepcopy
from .common_cosmo import body_of_test
from cobaya.cosmo_input import cmb_precision


def test_bicep_keck_2015_camb(modules):
    info_theory = {"camb": {"extra_args": cmb_precision["camb"]}}
    body_of_test(modules, test_point, lik_info, info_theory, chi2,
                 extra_model={"primordial": "SFSR_t"})


def test_bicep_keck_2015_classy(modules):
    info_theory = {"classy": {"extra_args": cmb_precision["classy"]}}
    # extra tolerance for CLASS
    chi2_classy = deepcopy(chi2)
    chi2_classy["tolerance"] *= 2
    body_of_test(modules, test_point, lik_info, info_theory, chi2_classy,
                 extra_model={"primordial": "SFSR_t"})


lik_info = {"bicep_keck_2015": {}}

# NB: chi2 obtained using CAMB w HMcode
chi2 = {"bicep_keck_2015": 735.187, "tolerance": 0.16}

test_point = {
    "omegabh2": 0.2235620E-01,
    "omegach2": 0.1204042E+00,
    "theta": 0.1040871E+01,  # for CAMB
    "H0": 0.6718506E+02,  # for CLASS
    "tau": 0.5454114E-01,
    "logA": 0.3046322E+01,
    "ns": 0.9654113E+00,
    "r": 0.1451578E-01,
    "calPlanck": 0.1000689E+01,
    "BBdust": 0.4648994E+01,
    "BBsync": 0.1542620E+01,
    "BBalphadust": -0.5338430E+00,
    "BBbetadust": 0.1576173E+01,
    "BBalphasync": -0.1915241E+00,
    "BBbetasync": -0.3040606E+01,
    "BBdustsynccorr": -0.3441905E+00
}
