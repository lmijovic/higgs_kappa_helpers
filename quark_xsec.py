# https://cds.cern.ch/record/2789544 , Ch 6
# Tab 6:
def x_sfact_ggH_kappa(p_kappabar_c, p_kappabar_ud):
    bquad = 0.002
    bint = -0.038
    mb_mc = 4.5 # converting between happabar_c and kappa_c 
    sfact = 1.04 + bquad + bint- 0.005* p_kappabar_c*mb_mc + bquad*p_kappabar_c*p_kappabar_c + \
        2*(bint*p_kappabar_ud +  bquad*p_kappabar_ud*p_kappabar_ud)
    return(sfact)

# ======================================================================
# light quark production cross-sections:
# ======================================================================

# https://twiki.cern.ch/twiki/bin/view/LHCPhysics/LHCHWG1#13_6_TeV_cross_section_updates
x_ggH = 52.23 # pb , xsec @ 13.6

# scale-factor between 13p6 and 13
x_sfact_13p6_13 = x_ggH/48.61 # pb 

# from Run2 x-section paper 
x_bbH_13 = 0.53 # pb
x_ccH_13 = 1.64 # pb ; @ kappabar_c =1
x_ccH = x_ccH_13 * x_sfact_13p6_13

# factor from MadGraph , @ NLO 
#Total cross-section: 7.534e+05 +- 1.6e+03 pb uudd (kappa_bar = 100)
#Total cross-section:      5.976e+04 +- 1.6e+02 pb cc (kappa_bar = 100)
x_sfact_uudd_cc = 7.534e+05/5.976e+04 # u and d couplings varied simultaneously 

x_uuddH = x_ccH * x_sfact_uudd_cc

print("incusive x-sections at kappa_bar = 1: ")
print("x_uuddH: ", x_uuddH, " [pb]")
print("x_ccH: ", x_ccH, " [pb]")

# ======================================================================
# ggF cross-sections: affected by light quark loops
# ======================================================================
# let's leave everything to SM: 
kappabar_c = 1/4.5 # mb_mc = 4.5 
kappabar_ud = 0 
sf_ggH = x_sfact_ggH_kappa(kappabar_c, kappabar_ud)
print("inclusive standard model ggH x-section is: ", sf_ggH, x_ggH*sf_ggH, " pb")

# let's set ud coupling equal to b coupling:  
kappabar_c = 1/4.5 # mb_mc = 4.5 
kappabar_ud = 1 
sf_ggH = x_sfact_ggH_kappa(kappabar_c, kappabar_ud)
print("inclusive ggH x-section is for kappabar_c:", kappabar_c, ", kappabar_ud:", kappabar_ud,
      "is this time larger than SM:", sf_ggH, "and amounts to:", x_ggH*sf_ggH, " pb")
