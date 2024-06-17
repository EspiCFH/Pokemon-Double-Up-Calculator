import re

print('What is the range of the first attack? (paste from the calc)')
print('ex. (67, 69, 69, 70, 72, 72, 73, 73, 75, 75, 76, 76, 78, 78, 79, 81)')
range1 = input('')
print('')
print('What is the range of the second attack?')
range2 = input('')
print('')
print('What is the Max HP of the target?')
hp = int(input(''))

r1d = re.findall('\d+',range1)
r2d = re.findall('\d+',range2)

odds = 0

for roll1 in r1d:
    viable = 0
    for roll2 in r2d:
        if hp - int(roll1) - int(roll2) <= 0:
            odds += 0.00390625

print('')
print('Odds of the Double-Up killing: '+str(100*round(odds,3))+'%')
