

'''IMPORTATED MODULES AND STATIC VARIABLES'''

import re
import math


'''ALL FUNCTIONS USED'''

#putting integers from string into lists within a list
def pulling_progression_integers(list):
    num = []
    for i in range(len(list)):
        temp = [int(s) for s in re.findall(r'\d+',(str(list[i])))]
        num += [temp]
    return num

#seperating character level and skill levels
def sep_char_and_skill(list):
    char_list = list[0]
    list.remove(list[0])
    skill_list = list
    return char_list,skill_list

#character level calculator
def char_xp_calc(num):
    xp = 12.5 * num**2 + 62.5 * num - 75
    return xp

#loop for chacracter level claculator
def char_xp_calc_loop():
    xp_list = []
    for i in range(len(char_lvl_input)):
        temp = char_xp_calc(char_lvl_input[i])
        xp_list.append(temp)
    current_char_xp = xp_list[0]
    desired_char_xp = xp_list[1]
    char_xp_gap = desired_char_xp - current_char_xp
    return current_char_xp,desired_char_xp,char_xp_gap

#calculating skill xp gained by advancing to desired level
def lvls_to_desired_lvl(list):
    xp = 0-(list[0])
    while list[0] <= list[1]:
        xp += list[0]
        list[0] += 1
    return xp

#loop for skill xp 
def lvls_to_desired_lvl_loop(list):
    for i in range(len(list)):
        list[i] = lvls_to_desired_lvl(list[i])
    return list

#XP gained from theoretical skill advancement
def xp_skill_gain(list):
    xp = 0
    i = len(list)-1
    while i >= 0:
        xp += list[i]
        i -= 1
    return xp

#
def theo_char_lvl():
    lvl = ((-25 + math.sqrt((8 * (cumulative_skill_advancement_xp + current_char_xp)) + 1225))/10)
    lvl = '{:.2f}'.format(lvl)
    return lvl

#
def experience_calculations():
    if char_xp_gap > cumulative_skill_advancement_xp:
        string = (f'You require {char_xp_gap - cumulative_skill_advancement_xp} more experience points to advance to character level {char_lvl_input[1]}.  You have only reached character level {theoretical_char_lvl}.')
    if cumulative_skill_advancement_xp > char_xp_gap:
        string = (f'You will gain {cumulative_skill_advancement_xp - char_xp_gap} more experience points than what is required to reach level {char_lvl_input[1]}.  In doing so, you have reached character level {theoretical_char_lvl}, congratulations!')
    if char_xp_gap == cumulative_skill_advancement_xp:
        string = (f'The experience gained is precisely enough to reach {theoretical_char_lvl}, wow!')
    return string


'''COMMANDS TO EXECUTE FUNCTIONS'''

#reading current/desired inputs into variable
with open('H:\shumi\coding environments\skyrim perk calc\current and desired level inputs','r') as f:
    input_list = f.read().splitlines()

#sifting for current/desired integers
input_num = pulling_progression_integers(input_list)

#seperating character level from skill level inputs
char_lvl_input,skill_lvl_input = sep_char_and_skill(input_num)

#calculating skill xp for current and desired character level and the gap inbetween
current_char_xp,desired_char_xp,char_xp_gap = char_xp_calc_loop()

#calculating skill xp gained by advancing to desired level
skill_xp_list = lvls_to_desired_lvl_loop(skill_lvl_input)

#XP gained from theoretical skill advancement
cumulative_skill_advancement_xp = xp_skill_gain(skill_lvl_input)

#theoretical character level reached from theoretical xp gained
theoretical_char_lvl = theo_char_lvl()

#calculating xp needed or plethora of xp gained to reach desired character/skill levels.
xp_outcome = experience_calculations()

#compiling calculated variables into an output list
current_character_level = (f'Current character level: {char_lvl_input[0]}  Experience currently accumulated by character: {current_char_xp:.2f}')
desired_character_level = (f'Desired character level: {char_lvl_input[1]}  Experience required to achieve desired character level: {desired_char_xp:.2f}')


skill_xp_header = ('Theoretical experience gained from each individual skill, if advanced to the desired level.')
LA_xp = (f'LIGHT ARMOR:     {skill_xp_list[0]}')
SN_xp = (f'SNEAK:           {skill_xp_list[1]}')
LP_xp = (f'LOCK PICKING:    {skill_xp_list[2]}')
PI_xp = (f'PICKPOCKET:      {skill_xp_list[3]}')
SP_xp = (f'SPEACH:          {skill_xp_list[4]}')
AL_xp = (f'ALCHEMY:         {skill_xp_list[5]}')
IL_xp = (f'ILLUSION:        {skill_xp_list[6]}')
CO_xp = (f'CONJURATION:     {skill_xp_list[7]}')
DE_xp = (f'DESTRUCTION:     {skill_xp_list[8]}')
RE_xp = (f'RESTORATION:     {skill_xp_list[9]}')
AL_xp = (f'ALTERATION:      {skill_xp_list[10]}')
EN_xp = (f'ENCHANTING:      {skill_xp_list[11]}')
SM_xp = (f'SMITHING:        {skill_xp_list[12]}')
HA_xp = (f'HEAVY ARMOR:     {skill_xp_list[13]}')
BL_xp = (f'Block:           {skill_xp_list[14]}')
TH_xp = (f'TWO HANDED:      {skill_xp_list[15]}')
OH_xp = (f'ONE HANDED:      {skill_xp_list[16]}')
AR_xp = (f'ARCHERY:         {skill_xp_list[17]}')

calc_header = ('The following are the calculations indicating the dynamics of character/skill leveling based off current/desired level inputs.')
char_lvl_gap = (f'Experienced required to advance character level from {char_lvl_input[0]} to {char_lvl_input[1]} is: {int(char_xp_gap)} experience points.')
skill_xp_gain = (f'Cumulative experienced gained from theoretical skill advancement is: {cumulative_skill_advancement_xp} experience points.')
xp_outcome

output = (str(current_character_level))
with open('H:\shumi\coding environments\skyrim perk calc\leveling calculations','w') as f:
    f.write(current_character_level + '\n' + desired_character_level + '\n' + '\n' + skill_xp_header + '\n' + LA_xp + '\n' + SN_xp + '\n' + LP_xp + '\n' + PI_xp + '\n' + SP_xp + '\n' + AL_xp + '\n' + IL_xp + '\n' + CO_xp + '\n' + DE_xp + '\n' + RE_xp + '\n' + AL_xp + '\n' + EN_xp + '\n' + SM_xp + '\n' + HA_xp + '\n' + BL_xp + '\n' + TH_xp + '\n' + OH_xp + '\n' + AR_xp + '\n' + '\n' + calc_header + '\n' + char_lvl_gap + '\n' + skill_xp_gain + '\n' + xp_outcome)

