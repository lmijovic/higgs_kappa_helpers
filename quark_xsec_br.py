import utils as utils 

# ======================================================================
# main
# ======================================================================

# from Run2 x-section paper 
# x_bbH_13 = 0.53 # pb
x_ccH_13 = 1.64 # pb ; @ kappabar_c =1
x_ccH = x_ccH_13 * utils.x_sf_13p6_13

# factor from MadGraph , @ NLO 
#Total cross-section: 7.534e+05 +- 1.6e+03 pb uudd (kappa_bar = 100)
#Total cross-section:      5.976e+04 +- 1.6e+02 pb cc (kappa_bar = 100)
x_sf_uudd_cc = 7.534e+05/5.976e+04 # u and d couplings varied simultaneously 

x_uuddH = x_ccH * x_sf_uudd_cc

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
