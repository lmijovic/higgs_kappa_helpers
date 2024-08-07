import sys
sys.path.append('../')
import utils as utils

import unittest
import math

# kappa framework uses rather rough rounding,
# => expect results to be accurate within tolerance 
tolerance = 0.01

class utils_test(unittest.TestCase):

    def test_get_width_sf_Hyy_kappa(self):
        sf = utils.get_width_sf_Hyy_kappa(utils.kappabar_c_sm, utils.kappabar_ud_sm)
        print("test_get_width_sf_Hyy_kappa: SM scale-factor", sf)
        self.assertTrue(math.fabs(sf - 1)< tolerance)



if __name__ == '__main__':
    unittest.main()
