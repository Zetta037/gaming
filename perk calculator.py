
import math

current_level = int(input(f'Current level is: '))
level_goal = int(input(f'Desired level is: '))

# equation calculating xp required to go from level 1 to level x
# 12.5 * x**2 + 62.5 * x - 75

print('\n')
# current level calculations
current_level_xp = 12.5 * int(current_level**2) + 62.5 * current_level - 75
print(f'cumulative xp for current level: {current_level_xp}')

# desired level calculations
level_goal_xp = 12.5 * int(level_goal**2) + 62.5 * level_goal - 75
print(f'cumulative xp for level goal: {level_goal_xp}')

# sum of required character xp points needed to advance from current level to desired level
print(f'xp required to advance from {current_level} to {level_goal}: {level_goal_xp - current_level_xp}.')
print('\n')

# character xp is obtained by advancing skills.  the higher the skill level the greater the character xp that is granted upon skill advancement.  
# used a loop to calculate total character xp gained from advancing starting skill level to desired skill level

#  light_armor
light_armor = int(input(f'Starting light_armor level: ')) + 1
desired_light_armor = int(input(f'Desired light_armor level: '))
light_armor_xp = 0

while light_armor <= desired_light_armor:
    light_armor_xp = light_armor_xp + light_armor
    light_armor = light_armor +1

print(f'Character xp gained by advancing  light_armor: {light_armor_xp}')
print('\n')

#  sneak
sneak = int(input(f'Starting sneak level: ')) + 1
desired_sneak = int(input(f'Desired sneak level: '))
sneak_xp = 0

while sneak <= desired_sneak:
    sneak_xp = sneak_xp + sneak
    sneak = sneak +1

print(f'Character xp gained by advancing  sneak: {sneak_xp}')
print('\n')

#  lockpicking
lockpicking = int(input(f'Starting lockpicking level: ')) + 1
desired_lockpicking = int(input(f'Desired lockpicking level: '))
lockpicking_xp = 0

while lockpicking <= desired_lockpicking:
    lockpicking_xp = lockpicking_xp + lockpicking
    lockpicking = lockpicking +1

print(f'Character xp gained by advancing  lockpicking: {lockpicking_xp}')
print('\n')

#  pickpocket
pickpocket = int(input(f'Starting pickpocket level: ')) + 1
desired_pickpocket = int(input(f'Desired pickpocket level: '))
pickpocket_xp = 0

while pickpocket <= desired_pickpocket:
    pickpocket_xp = pickpocket_xp + pickpocket
    pickpocket = pickpocket +1

print(f'Character xp gained by advancing  pickpocket: {pickpocket_xp}')
print('\n')

#  speech
speech = int(input(f'Starting speech level: ')) + 1
desired_speech = int(input(f'Desired speech level: '))
speech_xp = 0

while speech <= desired_speech:
    speech_xp = speech_xp + speech
    speech = speech +1

print(f'Character xp gained by advancing  speech: {speech_xp}')
print('\n')

#  alchemy
alchemy = int(input(f'Starting alchemy level: ')) + 1
desired_alchemy = int(input(f'Desired alchemy level: '))
alchemy_xp = 0

while alchemy <= desired_alchemy:
    alchemy_xp = alchemy_xp + alchemy
    alchemy = alchemy +1

print(f'Character xp gained by advancing  alchemy: {alchemy_xp}')
print('\n')

#  illusion
illusion = int(input(f'Starting illusion level: ')) + 1
desired_illusion = int(input(f'Desired illusion level: '))
illusion_xp = 0

while illusion <= desired_illusion:
    illusion_xp = illusion_xp + illusion
    illusion = illusion +1

print(f'Character xp gained by advancing  illusion: {illusion_xp}')
print('\n')

#  conjuration
conjuration = int(input(f'Starting conjuration level: ')) + 1
desired_conjuration = int(input(f'Desired conjuration level: '))
conjuration_xp = 0

while conjuration <= desired_conjuration:
    conjuration_xp = conjuration_xp + conjuration
    conjuration = conjuration +1

print(f'Character xp gained by advancing  conjuration: {conjuration_xp}')
print('\n')

#  destruction
destruction = int(input(f'Starting destruction level: ')) + 1
desired_destruction = int(input(f'Desired destruction level: '))
destruction_xp = 0

while destruction <= desired_destruction:
    destruction_xp = destruction_xp + destruction
    destruction = destruction +1

print(f'Character xp gained by advancing  destruction: {destruction_xp}')
print('\n')

#  restoration
restoration = int(input(f'Starting restoration level: ')) + 1
desired_restoration = int(input(f'Desired restoration level: '))
restoration_xp = 0

while restoration <= desired_restoration:
    restoration_xp = restoration_xp + restoration
    restoration = restoration +1

print(f'Character xp gained by advancing  restoration: {restoration_xp}')
print('\n')

#  alteration
alteration = int(input(f'Starting alteration level: ')) + 1
desired_alteration = int(input(f'Desired alteration level: '))
alteration_xp = 0

while alteration <= desired_alteration:
    alteration_xp = alteration_xp + alteration
    alteration = alteration +1

print(f'Character xp gained by advancing  alteration: {alteration_xp}')
print('\n')

#  enchanting
enchanting = int(input(f'Starting enchanting level: ')) + 1
desired_enchanting = int(input(f'Desired enchanting level: '))
enchanting_xp = 0

while enchanting <= desired_enchanting:
    enchanting_xp = enchanting_xp + enchanting
    enchanting = enchanting +1

print(f'Character xp gained by advancing  enchanting: {enchanting_xp}')
print('\n')

#  smithing
smithing = int(input(f'Starting smithing level: ')) + 1
desired_smithing = int(input(f'Desired smithing level: '))
smithing_xp = 0

while smithing <= desired_smithing:
    smithing_xp = smithing_xp + smithing
    smithing = smithing +1

print(f'Character xp gained by advancing  smithing: {smithing_xp}')
print('\n')

#  heavy_armor
heavy_armor = int(input(f'Starting heavy_armor level: ')) + 1
desired_heavy_armor = int(input(f'Desired heavy_armor level: '))
heavy_armor_xp = 0

while heavy_armor <= desired_heavy_armor:
    heavy_armor_xp = heavy_armor_xp + heavy_armor
    heavy_armor = heavy_armor +1

print(f'Character xp gained by advancing  heavy_armor: {heavy_armor_xp}')
print('\n')

#  block
block = int(input(f'Starting block level: ')) + 1
desired_block = int(input(f'Desired block level: '))
block_xp = 0

while block <= desired_block:
    block_xp = block_xp + block
    block = block +1

print(f'Character xp gained by advancing  block: {block_xp}')
print('\n')

#  two_handed
two_handed = int(input(f'Starting two_handed level: ')) + 1
desired_two_handed = int(input(f'Desired two_handed level: '))
two_handed_xp = 0

while two_handed <= desired_two_handed:
    two_handed_xp = two_handed_xp + two_handed
    two_handed = two_handed +1

print(f'Character xp gained by advancing  two_handed: {two_handed_xp}')
print('\n')

#  one_handed
one_handed = int(input(f'Starting one_handed level: ')) + 1
desired_one_handed = int(input(f'Desired one_handed level: '))
one_handed_xp = 0

while one_handed <= desired_one_handed:
    one_handed_xp = one_handed_xp + one_handed
    one_handed = one_handed +1

print(f'Character xp gained by advancing  one_handed: {one_handed_xp}')
print('\n')

#  archery
archery = int(input(f'Starting archery level: ')) + 1
desired_archery = int(input(f'Desired archery level: '))
archery_xp = 0

while archery <= desired_archery:
    archery_xp = archery_xp + archery
    archery = archery +1

print(f'Character xp gained by advancing  archery: {archery_xp}')
print('\n')

# current level calculations
print(f'cumulative xp for current level: {current_level_xp}')

# desired level calculations
print(f'cumulative xp for level goal: {level_goal_xp}')

# sum of required character xp points needed to advance from current level to desired level
print(f'xp required to advance from {current_level} to {level_goal}: {level_goal_xp - current_level_xp}.')
print('\n')

#adding all theoretical xp gained together
xp_gained = light_armor_xp + sneak_xp + lockpicking_xp + pickpocket_xp + speech_xp + alchemy_xp + illusion_xp + conjuration_xp + destruction_xp + restoration_xp + alteration_xp + enchanting_xp + smithing_xp + heavy_armor_xp + block_xp + two_handed_xp + one_handed_xp + archery_xp

#printing theoretical xp gained
print(f'Total theoretical XP gained from theoretical skill advancement: {xp_gained}.')

#calculating and printing character level achieved
theoretical_level_reached = ((-25 + math.sqrt((8*xp_gained)+1225))/10)
print(f'character level achieved based off theoretical xp gained: {theoretical_level_reached:,.2}')

#calculating and printing xp needed beyond theoretical xp gained to reach desired character level.
print(f'XP required beyond theoretical XP gained to reach desired level: {level_goal_xp - xp_gained}')
