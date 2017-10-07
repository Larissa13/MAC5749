"""
This script provides a function for returning the proper target string, given a dataset and class.
"""
import sys
sys.path.append('../')
from sarpy.datasets import load_mpeg7, load_leaf, load_nist, load_fashion_mnist

def get_class_name(dataset, target):
    if dataset == "mpeg7":
        if target == 0: return "Bone"
        if target == 1: return "Comma"
        if target == 2: return "Glas"
        if target == 3: return "HCircle"
        if target == 4: return "Heart"
        if target == 5: return "Misk"
        if target == 6: return "apple"
        if target == 7: return "bat"
        if target == 8: return "beetle"
        if target == 9: return "bell"
        if target == 10: return "bird"
        if target == 11: return "bottle"
        if target == 12: return "brick"
        if target == 13: return "butterfly"
        if target == 14: return "camel"
        if target == 15: return "car"
        if target == 16: return "carriage"
        if target == 17: return "cattle"
        if target == 18: return "cellular_phone"
        if target == 19: return "chicken"
        if target == 20: return "children"
        if target == 21: return "chopper"
        if target == 22: return "classic"
        if target == 23: return "crown"
        if target == 24: return "cup"
        if target == 25: return "deer"
        if target == 26: return "device0"
        if target == 27: return "device1"
        if target == 28: return "device2"
        if target == 29: return "device3"
        if target == 30: return "device4"
        if target == 31: return "device5"
        if target == 32: return "device6"
        if target == 33: return "device7"
        if target == 34: return "device8"
        if target == 35: return "device9"
        if target == 36: return "dog"
        if target == 37: return "elephant"
        if target == 38: return "face"
        if target == 39: return "fish"
        if target == 40: return "flatfish"
        if target == 41: return "fly"
        if target == 42: return "fork"
        if target == 43: return "fountain"
        if target == 44: return "frog"
        if target == 45: return "guitar"
        if target == 46: return "hammer"
        if target == 47: return "hat"
        if target == 48: return "horse"
        if target == 49: return "horseshoe"
        if target == 50: return "jar"
        if target == 51: return "key"
        if target == 52: return "lizzard"
        if target == 53: return "lmfish"
        if target == 54: return "octopus"
        if target == 55: return "pencil"
        if target == 56: return "personal_car"
        if target == 57: return "pocket"
        if target == 58: return "rat"
        if target == 59: return "ray"
        if target == 60: return "sea_snake"
        if target == 61: return "shoe"
        if target == 62: return "spoon"
        if target == 63: return "spring"
        if target == 64: return "stef"
        if target == 65: return "teddy"
        if target == 66: return "tree"
        if target == 67: return "truck"
        if target == 68: return "turtle"
        if target == 69: return "watch"

    if dataset == "leaf":
        if target == 0: return "Acer_Capillipes"
        if target == 1: return "Betula_Austrosinensis"
        if target == 2: return "Castanea_Sativa"
        if target == 3: return "Eucalyptus_Glaucescens"
        if target == 4: return "Fagus_Sylvatica"
        if target == 5: return "Ginkgo_Biloba"
        if target == 6: return "Ilex_Aquifolium"
        if target == 7: return "Liquidambar_Styraciflua"
        if target == 8: return "Magnolia_Heptapeta"
        if target == 9: return "Olea_Europaea"
        if target == 10: return "Populus_Adenopoda"
        if target == 11: return "Quercus_Afares"
        if target == 12: return "Rhododendron_x_Russellianum"
        if target == 13: return "Salix_Fragilis"
        if target == 14: return "Tilia_Oliveri"
        if target == 15: return "Ulmus_Bergmanniana"
        if target == 16: return "Viburnum_x_Rhytidophylloides"
        if target == 17: return "Zelkova_Serrata"
    
    if dataset == "fashion_mnist":
        if target == 0: return "Ankle_boot"
        if target == 1: return "Bag"
        if target == 2: return "Coat"
        if target == 3: return "Dress"
        if target == 4: return "Pullover"
        if target == 5: return "Sandal"
        if target == 6: return "Shirt"
        if target == 7: return "Sneaker"
        if target == 8: return "T_shirt"
        if target == 9: return "Trouser"

    if dataset == "nist":
        if target == 0: return "0"
        if target == 1: return "1"
        if target == 2: return "2"
        if target == 3: return "3"
        if target == 4: return "4"
        if target == 5: return "5"
        if target == 6: return "6"
        if target == 7: return "7"
        if target == 8: return "8"
        if target == 9: return "9"
        if target == 10: return "A"
        if target == 11: return "B"
        if target == 12: return "C"
        if target == 13: return "D"
        if target == 14: return "E"
        if target == 15: return "F"
        if target == 16: return "G"
        if target == 17: return "H"
        if target == 18: return "I"
        if target == 19: return "J"
        if target == 20: return "K"
        if target == 21: return "L"
        if target == 22: return "M"
        if target == 23: return "N"
        if target == 24: return "O"
        if target == 25: return "P"
        if target == 26: return "Q"
        if target == 27: return "R"
        if target == 28: return "S"
        if target == 29: return "T"
        if target == 30: return "U"
        if target == 31: return "V"
        if target == 32: return "W"
        if target == 33: return "X"
        if target == 34: return "Y"
        if target == 35: return "Z"
        if target == 36: return "a"
        if target == 37: return "b"
        if target == 38: return "c"
        if target == 39: return "d"
        if target == 40: return "e"
        if target == 41: return "f"
        if target == 42: return "g"
        if target == 43: return "h"
        if target == 44: return "i"
        if target == 45: return "j"
        if target == 46: return "k"
        if target == 47: return "l"
        if target == 48: return "m"
        if target == 49: return "n"
        if target == 50: return "o"
        if target == 51: return "p"
        if target == 52: return "q"
        if target == 53: return "r"
        if target == 54: return "s"
        if target == 55: return "t"
        if target == 56: return "u"
        if target == 57: return "v"
        if target == 58: return "w"
        if target == 59: return "x"
        if target == 60: return "y"
        if target == 61: return "z"






































































