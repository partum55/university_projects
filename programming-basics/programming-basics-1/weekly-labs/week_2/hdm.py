import math

# input
# country, act_leb, act_eys, act_mys, act_gni = (str(input()), float(input()), float(input()), float(input()), float(input())) #country, life expectancy at birth, expected years of schooling, mean years of schooling, gross national income (GNI) per capita)

# test
country = "Ukraine"
act_leb, act_eys, act_mys, act_gni = 71.6, 15.0, 11.1, 13256

#constant
MIN_LEB = 20
MAX_LEB = 85

MIN_EYS = 0
MAX_EYS = 18

MIN_MYS = 0
MAX_MYS = 15

MIN_GNI = 100
MAX_GNI = 75000

# main
eys_index = (act_eys - MIN_EYS) / (MAX_EYS - MIN_EYS)
mys_index = (act_mys - MIN_MYS) / (MAX_MYS - MIN_MYS)

leb = (act_leb - MIN_LEB) / (MAX_LEB - MIN_LEB)
gni = (math.log(act_gni) - math.log(MIN_GNI)) / (math.log(MAX_GNI) - math.log(MIN_GNI))
ei = (eys_index + mys_index) / 2

hdi = math.cbrt((leb * ei * gni))

hdi_max = hdi > 0.7
bad_index =  [leb, ei, gni]
min_index = min(bad_index)
index4 = bad_index.index(min(bad_index))

bad = ["Life expectancy index", "Education index", "GNI"]

# output
print(f"Life expectancy index for {country} is {leb:.4f}. \n"
        f"Education index for {country} is {ei:.4f}. \n"
        f"GNI index for {country} is {gni:.4f}. \n"
        f"HDI for {country} is {hdi:.3f}. \n"
        f"HDI for {country} is high: {hdi_max}. \n"
        f"The worst index for {country} is {min_index:.4f}. \n")
print(bad[index4])