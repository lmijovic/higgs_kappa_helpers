import sys
sys.path.append('../')
import utils as utils

import unittest
import math

# kappa framework uses rather rough rounding,
# => expect results to be accurate within tolerance 
tolerance = 0.01

class utils_test(unittest.TestCase):

    #===================================================================
    # test the Standard Model scenario
    #===================================================================
    # branching ratios: 
    def test_get_width_sf_Hyy_kappa(self):
        sf = utils.get_width_sf_Hyy_kappa(utils.kappabar_c_sm, utils.kappabar_ud_sm)
        print("test_get_width_sf_Hyy_kappa: SM scale-factor", sf)
        self.assertTrue(math.fabs(sf - 1)< tolerance)

    def test_get_width_sf_Hgg_kappa(self):
        # kappa framework H->gg expression is lacking substantial SM charm term,
        # so SM sf will differ from 1 when we start accounting for charm 
        tolerance_hgg = tolerance + 0.123/utils.kappabar_c_sm
        sf = utils.get_width_sf_Hgg_kappa(utils.kappabar_c_sm, utils.kappabar_ud_sm)
        print("test_get_width_sf_Hgg_kappa: SM scale-factor", sf)
        # NB: crancked up tolerance 
        self.assertTrue(math.fabs(sf - 1)< tolerance_hgg)

    def test_get_width_sf_H_kappa(self):
        sf = utils.get_width_sf_H_kappa(utils.kappabar_c_sm, utils.kappabar_ud_sm)
        print("test_get_width_sf_H_kappa: SM scale-factor", sf)
        self.assertTrue(math.fabs(sf - 1)< tolerance)

    def test_get_br_Hyy_kappa(self):
        br = utils.get_br_Hyy_kappa(utils.kappabar_c_sm, utils.kappabar_ud_sm)
        print("test_get_br_Hyy_kappa: SM H->yy branching ratio", br)
        br_ref = utils.br_Hyy_sm
        self.assertTrue(math.fabs(br - br_ref)/br_ref< tolerance)

    # x-sections 
    def test_get_x_sf_ggH_kappa(self):
        sf = utils.get_x_sf_ggH_kappa(utils.kappabar_c_sm, utils.kappabar_ud_sm)
        print("test_get_x_sf_ggH_kappa: x-section SM scale-factor", sf)
        self.assertTrue(math.fabs(sf - 1)< tolerance)      

if __name__ == '__main__':
    unittest.main()
