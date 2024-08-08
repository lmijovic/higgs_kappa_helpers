# ======================================================================
# global constants:
# ======================================================================

width_Higgs_sm = 4.1 # Higgs width [MeV]
br_Hyy_sm = 2.3*0.01 #H->yy branching ratio (br) 2.3%
mb_mc = 4.5 # ratio of b and charm running masses arXiv:2201.11428

# cross-sections at Run3 ECM 13p6 TeV:
# https://twiki.cern.ch/twiki/bin/view/LHCPhysics/LHCHWG1#13_6_TeV_cross_section_updates
x_ggH_sm = 52.23 # pb 
# cross-section scale-factor between 13p6 and 13 TeV
x_sf_13p6_13 = x_ggH_sm/48.61 # pb 

# SM:
kappa_c_sm = 1
kappabar_c_sm = kappa_c_sm/mb_mc
# in SM, up and down are negligible 
kappabar_ud_sm = 0

# ======================================================================
# branching ratio helper functions
# ======================================================================

# https://cds.cern.ch/record/2789544 , Ch 6, Tab 6
# returns scale-factor of H->yy width wrt to the SM value  
def get_width_sf_Hyy_kappa(p_kappabar_c, p_kappabar_ud):
    # from https://cds.cern.ch/record/2789544 ,Ch6 Tab 6:
    b_t_interference = -0.002
    b_W_interference = 0.008
    width_sf_Hyy = 1.589 + 0.07 - 0.674 + \
        0.009 + b_W_interference + b_t_interference - 0.002 + \
        b_W_interference * p_kappabar_c + b_t_interference * p_kappabar_c + \
        2*(b_W_interference * p_kappabar_ud + b_t_interference * p_kappabar_ud)
    return(width_sf_Hyy)

# returns scale-factor of H->gg  (g = gluon) wrt to the SM value 
def get_width_sf_Hgg_kappa(p_kappabar_c, p_kappabar_ud):
    bquad = 0.012
    b_t_interference=-0.123
    width_sf_Hgg = 1.111 + bquad + b_t_interference + \
        bquad*p_kappabar_c*p_kappabar_c + b_t_interference * p_kappabar_c + \
        2*(bquad*p_kappabar_ud*p_kappabar_ud + b_t_interference * p_kappabar_ud) 
    return(width_sf_Hgg)

# returns scale-factor of Higgs total decay width, wrt to the SM value
def get_width_sf_H_kappa(p_kappabar_c, p_kappabar_ud):
    b_quad = 0.581
    width_sf_H = b_quad + 0.215 + 0.063 + 0.026 + 0.0015 + 0.0004 + 0.00022 + \
         0.082*get_width_sf_Hgg_kappa(p_kappabar_c, p_kappabar_ud) + \
         0.0023*get_width_sf_Hyy_kappa(p_kappabar_c, p_kappabar_ud) + \
         b_quad*p_kappabar_c*p_kappabar_c + 2*(b_quad*p_kappabar_ud*p_kappabar_ud)
    return(width_sf_H)


def get_br_Hyy_kappa(p_kappabar_c, p_kappabar_ud):
    width_Hyy_sm = width_Higgs_sm * br_Hyy_sm
    width_Hyy = width_Hyy_sm * get_width_sf_Hyy_kappa(p_kappabar_c, p_kappabar_ud)
    width_H = width_Higgs_sm * get_width_sf_H_kappa(p_kappabar_c, p_kappabar_ud)
    return(width_Hyy/width_H)


# ======================================================================
# cross-section helper functions
# ======================================================================

def get_x_sf_ggH_kappa(p_kappabar_c, p_kappabar_ud):
    b_quad = 0.002
    bint = -0.038
    sf = 1.04 + b_quad + bint- 0.005* p_kappabar_c*mb_mc + b_quad*p_kappabar_c*p_kappabar_c + \
        2*(bint*p_kappabar_ud +  b_quad*p_kappabar_ud*p_kappabar_ud)
    return(sf)
