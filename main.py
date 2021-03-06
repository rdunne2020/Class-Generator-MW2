#!/usr/bin/env python3
'''This is a random class generator for modern warfare 2, maybe more games will be added eventually'''

from random import randint as rand

def single_attachment(attachment_list, attach_size = 1):
    if attach_size == 0: #For the machine pistols
        equip = rand(0, len(attachment_list)-1)
        attachment = attachment_list[equip]
        return attachment

    soa_index = rand(0, attach_size) #sets the index for sights or attachments
    soa = attachment_list[soa_index] #sight or attachment
    equip = rand(0, len(attachment_list[soa_index])-1) #gets the index for attachment in sights or attachments
    attachment = attachment_list[soa_index][equip] #pulls the string
    return attachment

def shotgun_attachments(attach_list):
    attach_index = rand(0, len(attach_list)-1)#generates random number to pull out of the array
    attachment = attach_list[attach_index]
    return attachment

def two_shotgun_attachments(attach_list):
    attach_index = rand(0, len(attach_list)-1)
    attachment = attach_list[attach_index]
    second_attach_index = rand(0, len(attach_list)-1)
    second_attachment = attach_list[second_attach_index]
    while attachment == second_attachment: #making sure the attachments arent the same
        second_attach_index = rand(0, len(attach_list)-1)
        second_attachment = attach_list[second_attach_index]
    attachment = attachment + ' & ' + second_attachment
    return attachment

def two_attachment(attachment_list, attach_size = 1):
    #first attachment generation
    soa_index = rand(0, attach_size)
    soa = attachment_list[soa_index] #sight or attachment
    equip = rand(0, len(attachment_list[soa_index])-1)#pulling the index of string literal of the attachment
    attachment = attachment_list[soa_index][equip]
    #second attachment generation
    soa_index2 = rand(0, 1)
    if soa_index == 0 and soa_index2 == 0: #making sure there arent two sights
        soa_index2 = 1
    soa = attachment_list[soa_index2] #sight or attachment
    equip2 = rand(0, len(attachment_list[soa_index2])-1) #pulling the index of string literal of the attachment
    while equip2 == equip:  #making sure there arent two of the same attachment
         equip2 = rand(0, len(attachment_list[soa_index2])-1)
    if soa_index == 1 and attachment_list[0] == 'M4A1': #making sure there arent glauncher and shotgun for ar's
        while (equip2 == 3 and equip == 0) or (equip2 == 0 and equip == 3):
            equip2 = rand(0, len(attachment_list[soa_index2])-1)
    second_attach = attachment_list[soa_index2][equip2]
    attachment = attachment + ' & ' + second_attach
    return attachment

def two_pistol_attach(attach_list):
    soa_index = rand(0, len(attach_list)-1)
    attachment = attach_list[soa_index]
    second_attachment = attach_list[rand(0, len(attach_list)-1)]
    while attachment == "Akimbo" and second_attachment == "Tactical Knife":
        second_attachment = attach_list[rand(0, len(attach_list)-1)]
        #print("2a test", second_attachment)
    while attachment == "Tactical Knife" and second_attachment == "Akimbo":
        second_attachment = attach_list[rand(0, len(attach_list)-1)]
        #print("2b test", second_attachment)
    while second_attachment == attachment:
        second_attachment = attach_list[rand(0, len(attach_list)-1)]
    attachment = attachment + ' & ' + second_attachment
    return attachment


rifles = ['M4A1', 'FAMAS', 'SCAR-H', 'TAR-21', 'FAL', 'M16A4', 'ACR', 'F2000', 'AK-47']#0
sights = ['Red Dot Sight', 'ACOG Scope', 'Holographic Sight', 'Thermal Sight']
rifles_attachments = ['Grenade Launcher', 'Silencer', 'FMJ', 'Shotgun Attachment', 'Heartbeat Sensor', 'Extended Mags']
r_attachments = [sights, rifles_attachments]

smg = ['MP5K', 'UMP45', 'VECTOR', 'P90', 'MINI-UZI']#1
smg_attachments = ['Rapid Fire', 'FMJ', 'Akimbo', 'Silencer', 'Extended Mags']
s_attachments = [sights, smg_attachments]

lmg = ['L86 LSW', 'RPD', 'MG4', 'AUG HBAR', 'M240']#2
lmg_attachments = ['Grip', 'FMJ', 'Silencer', 'Extended Mags', 'Heartbeat Sensor']
l_attachments = [sights, lmg_attachments]

snipers = ['INTERVENTION', 'BARRETT .50CAL', 'WA2000', 'M21 EBR']#3
snipers_sights = ['ACOG Scope', 'Thermal Sight']
snipers_attachments = ['Silencer', 'Heartbeat Sensor', 'FMJ', 'Extended Mags']
sr_attachments = [snipers_sights, snipers_attachments]

shield = ['RIOT SHIELD']#4

pistols = ['USP .45', '.44 Magnum', 'M9', 'DESERT EAGLE']#0
light_pistol_attachments = ['FMJ', 'Silencer', 'Akimbo', 'Extended Mags', 'Tactical Knife']
heavy_pistol_attachments = ['FMJ', 'Akimbo', 'Tactical Knife']
p_attachments = [light_pistol_attachments, heavy_pistol_attachments]

mp = ['PP2000', 'G18', 'M93 RAFFICA', 'TMP']#1
mp_attachments = ['Red Dot Sight', 'Holographic Sight', 'Silencer', 'FMJ', 'Extended Mags', 'Akimbo']#should be setup to avoid sights in akimbo

shotguns = ['SPAS-12', 'AA-12', 'STRIKER', 'M1014', 'RANGER', 'MODEL 1887']#2
modern_attachments = ['Silencer', 'Grip', 'FMJ', 'Extended Mags', 'Red Dot Sight', 'Holographic Sight']
old_attachments = ['Akimbo', 'FMJ']
shot_attachments = [modern_attachments, old_attachments]

launchers = ['AT4-HS', 'THUMPER', 'STINGER', 'JAVELIN', 'RPG-7']#3

oma = ['One Man Army']#4
perk1 = ['Marathon', 'Sleight of Hand', 'Bling', 'Scavenger', 'One Man Army']#0
perk2 = ['Stopping Power', 'Lightweight', 'Hardline', 'Cold Blooded', 'Danger Close']#1
perk3 = ['Commando', 'Steady Aim', 'Ninja', 'Scrambler', 'Sitrep', 'Last Stand']#2
deathstreaks = ['Copycat', 'Painkiller', 'Final Stand', 'Martyrdom']#0
l_equipment = ['Frag Grenade', 'Semtex Grenade', 'Throwing Knife', 'Tactical Insertion', 'Blast Shield', 'C4']
t_equipment = ['Stun Grenade', 'Flashbang Grenade', 'Smoke Grenade']


primaries = [rifles, smg, lmg, snipers, shield]
secondaries = [pistols, mp, shotguns, launchers, oma]

#-------------------------------------------------------
#Weapons
#-------------------------------------------------------
prim_cat = rand(0,4) #primary weapon category index
#prim_cat = 1 #specific category test
prim_weap = rand(0, len(primaries[prim_cat])-1) #primary weapon index
sec_cat = rand(0,3) #secondary weapon category index
#sec_cat = 0 #specific category test
sec_weap = rand(0, len(secondaries[sec_cat])-1) #secondary weapon index

#--------------------------------------------------------
#Perks
#--------------------------------------------------------
perk1_ind = rand(0, 4)
#perk1_ind = 2 #bling test
if perk1[perk1_ind] == 'One Man Army':
    sec_cat = 4
    sec_weap = 0
perk2_ind = rand(0, 4)
perk3_ind = rand(0, 5)
#--------------------------------------------------------
#Primary Attachments
attachment = ''
if perk1[perk1_ind] != 'Bling': #without bling
    if prim_cat == 0:
        attachment = single_attachment(r_attachments)
    elif prim_cat == 1:
        attachment = single_attachment(s_attachments)
    elif prim_cat == 2:
        attachment = single_attachment(l_attachments)
    elif prim_cat == 3:
        attachment = single_attachment(sr_attachments)
    elif prim_cat == 4:
        pass
else:
    if prim_cat == 0: #with bling
        attachment = two_attachment(r_attachments)
    elif prim_cat == 1:
        attachment = two_attachment(s_attachments)
    elif prim_cat == 2:
        attachment = two_attachment(l_attachments)
    elif prim_cat == 3:
        attachment = two_attachment(sr_attachments)
    elif prim_cat == 4:
        pass
#--------------------------------------------------------
#Pistol Attachments
pistol_attachment = ''
if perk1[perk1_ind] != 'Bling': #without bling
    if sec_cat == 0:
        if sec_weap == 0 or sec_weap == 2:
            pistol_attachment = single_attachment(p_attachments, 1)
        else:
            pistol_attachment = single_attachment(p_attachments, 1)
            while pistol_attachment == 'Extended Mags' or pistol_attachment == 'Silencer': #disregarding the attachments
                pistol_attachment = single_attachment(p_attachments, 1)
#------------------------------------------------------------
    elif sec_cat == 1:
        pistol_attachment = single_attachment(mp_attachments, 0)
#------------------------------------------------------------
    elif sec_cat == 2:
        if sec_weap >= 0 and sec_weap < 4:
            pistol_attachment = shotgun_attachments(modern_attachments)
        else:
            pistol_attachment = shotgun_attachments(old_attachments)
#------------------------------------------------------------
    elif sec_cat == 3: #launcher
        pistol_attachment = 'N/A'
#------------------------------------------------------------
else:
    if sec_cat == 0: #with bling
        if sec_weap == 0 or sec_weap == 2:
            pistol_attachment = two_pistol_attach(light_pistol_attachments)
            while pistol_attachment == 'Tactical Knife & Akimbo' or pistol_attachment == 'Akimbo & Tactical Knife':
                pistol_attachment = two_pistol_attach(light_pistol_attachments)
        else:
            pistol_attachment = two_pistol_attach(heavy_pistol_attachments)
            while pistol_attachment == 'Tactical Knife & Akimbo' or pistol_attachment == 'Akimbo & Tactical Knife':
                pistol_attachment = two_pistol_attach(heavy_pistol_attachments)
#------------------------------------------------------------
    elif sec_cat == 1:
        pistol_attachment = two_pistol_attach(mp_attachments)
#------------------------------------------------------------
    elif sec_cat == 2:
        if sec_weap >= 0 and sec_weap < 4:
            pistol_attachment = two_shotgun_attachments(modern_attachments)
        else:
            pistol_attachment = two_shotgun_attachments(old_attachments)
#------------------------------------------------------------
    elif sec_cat == 3: #launcher
        pistol_attachment = 'N/A'
#---------------------------------------------------------------
#Equipment
lethal_equipment = l_equipment[rand(0,5)]
tactical_equipment = t_equipment[rand(0, 2)]
#---------------------------------------------------------------
cac = primaries[prim_cat][prim_weap] + ' w/ ' + attachment + '\n' + secondaries[sec_cat][sec_weap] + ' w/ ' + pistol_attachment
cac = cac + '\n' + lethal_equipment + ', ' + tactical_equipment
cac = cac + '\n' + perk1[perk1_ind] + ', ' + perk2[perk2_ind] + ', ' + perk3[perk3_ind]
cac = cac + '\n' + deathstreaks[rand(0,3)] + '\n'
print(cac)
