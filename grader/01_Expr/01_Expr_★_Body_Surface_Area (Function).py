# Please apply your effort before copying, pasting, and converting to your own version.

import math

def mosteller(w, h):
    return math.sqrt(w*h) / 60

def du_bois(w, h):
    return 0.007184 * w**0.425 * h**0.725

def fujimoto(w, h):
    return 0.008883 * w**0.444 * h**0.663

def main():
    weight = float(input())
    height = float(input())
    m, d, f = mosteller(weight, height), du_bois(weight, height), fujimoto(weight, height)
    print("Mosteller =", round(m, 5))
    print("Du Bois =", round(d, 5))
    print("Fujimoto =", round(f,5))
    
exec(input()) 