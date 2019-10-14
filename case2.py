import local as lc
"""Case-study #2 
Developers: Nikitina. A (55%)
            Revtova. L (55%)
            Arkhipova A. (60%)"""

name_month = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май',
              'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь',
              'Ноябрь', 'Декабрь']
QUESTION = lc.TXT_ANNUAL_MONTHS
annual_income = 0
for month in range(12):
    print('{} {}:'.format(QUESTION, name_month[month], end =''))
    income = float(input())
    annual_income += income
print(lc.TXT_ANNUAL_INCOME, annual_income)

S1 = 0.1
S2 = 0.15
S3 = 0.25
S4 = 0.28
S5 = 0.34
S6 = 0.35
S7 = 0.396

print (lc.TXT_SOCIAL_GROUP)
social_status = input()
D = annual_income

if social_status == '1':
    D1 = 0
    D2 = 9076
    D3 = 36901
    D4 = 89351
    D5 = 186351
    D6 = 405101
    D7 = 406751
    if D >= 406_751:
        N7 = S1 * (D2 - D1) + S2 * (D3 - D2) + S3 * (D4 - D3) +\
             S4 * (D5 - D6) + S5 * (D6 - D5) + S6 * (D7 - D6) + S7 * (D - D7)
        print (lc.TXT_TAX, N7, lc.TXT_TAX1)
    elif D >= 405_101:
        N6 = S1 * (D2 - D1) + S2 * (D3 - D2) + S3 * (D4 - D3) +\
             S4 * (D5 - D6) + S5 * (D6 - D5) + S6 * (D - D6)
        print(lc.TXT_TAX, N6, lc.TXT_TAX1)
    elif D >= 186_351:
        N5 = S1 * (D2 - D1) + S2 * (D3 - D2) + S3 * (D4 - D3) +\
             S4 * (D5 - D6) + S5 * (D - D5)
        print(lc.TXT_TAX, N5, lc.TXT_TAX1)
    elif D >= 89_351:
        N4 = S1 * (D2 - D1) + S2 * (D3 - D2) + S3 * (D4 - D3) +\
             S4 * (D - D4)
        print(lc.TXT_TAX, N4, lc.TXT_TAX1)
    elif D >= 36_901:
        N3 = S1 * (D2 - D1) + S2 * (D3 - D2) + S3 * (D - D3)
        print(lc.TXT_TAX, N3, lc.TXT_TAX1)
    elif D >= 9076:
        N2 = S1 * (D2 - D1) + S2 * (D - D2)
        print(lc.TXT_TAX, N2, lc.TXT_TAX1)
    elif D >= 0:
        N1 = S1 * (D - D1)
        print(lc.TXT_TAX, N1, lc.TXT_TAX1)

elif social_status == '2':
    D1 = 0
    D2 = 18_151
    D3 = 73_800
    D4 = 148_850
    D5 = 226_851
    D6 = 405_101
    D7 = 457_601
    if D >= 457_601:
        N7 = S1 * (D2 - D1) + S2 * (D3 - D2) + S3 * (D4 - D3) + \
             S4 * (D5 - D6) + S5 * (D6 - D5) + S6 * (D7 - D6) + S7 * (D - D7)
        print(lc.TXT_TAX, N7, lc.TXT_TAX1)
    elif D >= 405_101:
        N6 = S1 * (D2 - D1) + S2 * (D3 - D2) + S3 * (D4 - D3) + \
         S4 * (D5 - D6) + S5 * (D6 - D5) + S6 * (D - D6)
        print(lc.TXT_TAX, N6, lc.TXT_TAX1)
    elif D >= 226_851:
        N5 = S1 * (D2 - D1) + S2 * (D3 - D2) + S3 * (D4 - D3) + \
         S4 * (D5 - D6) + S5 * (D - D5)
        print(lc.TXT_TAX, N5, lc.TXT_TAX1)
    elif D >= 148_850:
        N4 = S1 * (D2 - D1) + S2 * (D3 - D2) + S3 * (D4 - D3) + \
         S4 * (D - D4)
        print(lc.TXT_TAX, N4, lc.TXT_TAX1)
    elif D >= 73_800:
        N3 = S1 * (D2 - D1) + S2 * (D3 - D2) + S3 * (D - D3)
        print(lc.TXT_TAX, N3, lc.TXT_TAX1)
    elif D >= 18_151:
        N2 = S1 * (D2 - D1) + S2 * (D - D2)
        print(lc.TXT_TAX, N2, lc.TXT_TAX1)
    elif D >= 0:
        N1 = S1 * (D - D1)
        print(lc.TXT_TAX, N1, lc.TXT_TAX1)
elif social_status == '3':
    D1 = 0
    D2 = 12_951
    D3 = 49_401
    D4 = 127_551
    D5 = 206_601
    D6 = 405_101
    D7 = 432_201
    if D >= 432_201:
        N7 = S1 * (D2 - D1) + S2 * (D3 - D2) + S3 * (D4 - D3) + \
             S4 * (D5 - D6) + S5 * (D6 - D5) + S6 * (D7 - D6) + S7 * (D - D7)
        print(lc.TXT_TAX, N7, lc.TXT_TAX1)
    elif D >= 405_101:
        N6 = S1 * (D2 - D1) + S2 * (D3 - D2) + S3 * (D4 - D3) + \
         S4 * (D5 - D6) + S5 * (D6 - D5) + S6 * (D - D6)
        print(lc.TXT_TAX, N6, lc.TXT_TAX1)
    elif D >= 206_601:
        N5 = S1 * (D2 - D1) + S2 * (D3 - D2) + S3 * (D4 - D3) + \
         S4 * (D5 - D6) + S5 * (D - D5)
        print(lc.TXT_TAX, N5, lc.TXT_TAX1)
    elif D >= 127_551:
        N4 = S1 * (D2 - D1) + S2 * (D3 - D2) + S3 * (D4 - D3) + \
         S4 * (D - D4)
        print(lc.TXT_TAX, N4, lc.TXT_TAX1)
    elif D >= 49_401:
        N3 = S1 * (D2 - D1) + S2 * (D3 - D2) + S3 * (D - D3)
        print(lc.TXT_TAX, N3, lc.TXT_TAX1)
    elif D >= 12_951:
        N2 = S1 * (D2 - D1) + S2 * (D - D2)
        print(lc.TXT_TAX, N2, lc.TXT_TAX1)
    elif D >= 0:
        N1 = S1 * (D - D1)
        print(lc.TXT_TAX, N1, lc.TXT_TAX1)
