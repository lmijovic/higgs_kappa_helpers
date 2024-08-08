'''
calculate xsec and BR for modified charm and u/d quark couplings
'''

import utils as utils


print("\n\n----------------------------------------------------------\n")
print("Standard Model:")
kappabar_c = utils.kappabar_c_sm
kappabar_ud = 0
print("\nInclusive x-sections [pb]")
print("ggH: ",utils.get_x_ggH_kappa(kappabar_c, kappabar_ud))
print("ccH: ",utils.get_x_ccH_kappa(kappabar_c))
print("uuH and ddH: ",utils.get_x_uuddH_kappa(kappabar_ud))
print("\nH->yy branching ratio: [%]",
      100.*utils.get_br_Hyy_kappa(kappabar_c, kappabar_ud))

print("\n\n----------------------------------------------------------\n")
print("Standard Model + Yukawa couplings: y_u = y_d = y_b")
kappabar_c = utils.kappabar_c_sm
kappabar_ud = 1
print("\nInclusive x-sections [pb]")
print("ggH: ",utils.get_x_ggH_kappa(kappabar_c, kappabar_ud))
print("ccH: ",utils.get_x_ccH_kappa(kappabar_c))
print("uuH and ddH: ",utils.get_x_uuddH_kappa(kappabar_ud))
print("\nH->yy branching ratio: [%]",
      100.*utils.get_br_Hyy_kappa(kappabar_c, kappabar_ud))


print("\n\n----------------------------------------------------------\n")
print("Standard Model + Yukawa couplings: y_u = y_d = y_c")
kappabar_c = utils.kappabar_c_sm
kappabar_ud = utils.kappabar_c_sm
print("\nInclusive x-sections [pb]")
print("ggH: ",utils.get_x_ggH_kappa(kappabar_c, kappabar_ud))
print("ccH: ",utils.get_x_ccH_kappa(kappabar_c))
print("uuH and ddH: ",utils.get_x_uuddH_kappa(kappabar_ud))
print("\nH->yy branching ratio: [%]",
      100.*utils.get_br_Hyy_kappa(kappabar_c, kappabar_ud))

# all done 
print("\n\n")
