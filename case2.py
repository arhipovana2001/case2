if social_status == '2':
    D1 = 0
    D2 = 18_151
    D3 = 73_800
    D4 = 148_850
    D5 = 226_851
    D6 = 405_101
    D7 = 457_601
if D >= 457_601:
N7 = S1 * (D2 - D1) + S2 * (D3 - D2) + S3 * (D4 - D3) +\
S4 * (D5 - D6) + S5 * (D6 - D5) + S6 * (D7 - D6) + S7 * (D - D7)
print(N7)
elif D >= 405_101:
N6 = S1 * (D2 - D1) + S2 * (D3 - D2) + S3 * (D4 - D3) +\
S4 * (D5 - D6) + S5 * (D6 - D5) + S6 * (D - D6)
print(N6)
elif D >= 226_851:
N5 = S1 * (D2 - D1) + S2 * (D3 - D2) + S3 * (D4 - D3) +\
S4 * (D5 - D6) + S5 * (D - D5)
print(N5)
elif D >= 148_850:
N4 = S1 * (D2 - D1) + S2 * (D3 - D2) + S3 * (D4 - D3) +\
S4 * (D - D4)
print(N4)
elif D >= 73_800:
N3 = S1 * (D2 - D1) + S2 * (D3 - D2) + S3 * (D - D3)
print(N3)
elif D >= 18_151:
N2 = S1 * (D2 - D1) + S2 * (D - D2)
print(N2)
elif D >= 0:
N1 = S1 * (D - D1)
print(N1)
