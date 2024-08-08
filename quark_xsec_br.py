'''
calculate xsec and BR for modified charm and u/d quark couplings
'''


import utils as utils

#=======================================================================
# 
#=======================================================================




print("incusive x-sections at kappa_bar = 1: ")
print("x_uuddH: ", x_uuddH, " [pb]")
print("x_ccH: ", x_ccH, " [pb]")

# ======================================================================
# ggF cross-sections: affected by light quark loops
# ======================================================================
# let's leave everything to SM: 
kappabar_c = 1/4.5 # mb_mc = 4.5 
kappabar_ud = 0 
sf_ggH = utils.get_x_sf_ggH_kappa(kappabar_c, kappabar_ud)
print("inclusive standard model ggH x-section is: ", sf_ggH, utils.x_ggH_sm*sf_ggH, " pb")

# let's set ud coupling equal to b coupling:  
kappabar_c = 1/4.5 # mb_mc = 4.5 
kappabar_ud = 1 
sf_ggH = utils.get_x_sf_ggH_kappa(kappabar_c, kappabar_ud)
print("inclusive ggH x-section is for kappabar_c:", kappabar_c, ", kappabar_ud:", kappabar_ud,
      "is this time larger than SM:", sf_ggH, "and amounts to:", utils.x_ggH_sm*sf_ggH, " pb")
