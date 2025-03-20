'''
Created on 24-04-2021

@author: Marcin Kutrzynski
'''

#this script should be run inside CityEngine enviroment, so 'scripting' will be recognized
from scripting import *

# get a CityEngine instance
ce = CE()

import sys
sys.path.append('generate_city')
from create_network import *
from create_photo_EQR import *


#TODO: dodac jako procedure
#wlaczenie nieba

panoramaSettings = ce.getPanorama()
panoramaSettings.setVisible(True)
ce.setPanorama(panoramaSettings)

    
create_random_city()
"""
create_photo_set()

#zmiana r�l
#niebieskie

#wylaczenie nieba
panoramaSettings = ce.getPanorama()
panoramaSettings.setVisible(False)
ce.setPanorama(panoramaSettings)

objects = ce.getObjectsFrom(ce.scene,  ce.withName('street'))
for o in objects:
    ce.setAttributeSource(o,'/ce/rule/Display_Textures',"USER")
    ce.setAttribute(o,'/ce/rule/Display_Textures',False)

objects = ce.getObjectsFrom(ce.scene,  ce.withName('lot'))
for buildings in objects:
    ce.setRuleFile(buildings, 'rules/dilatation_street.cga')
    
objects = ce.getObjectsFrom(ce.scene,  ce.withName('LotCorner'))
for o in objects:
    ce.setRuleFile(o, 'none')


#generowanie obrazow

print "czekanie na rendering 2"
ce.generateModels(ce.getObjectsFrom(ce.scene))
views = ce.getObjectsFrom(ce.get3DViews())
views[0].frame()
ce.waitForUIIdle()    
print "koniec 2"
"""
#create_photo_set(main_road = 'main_road', prefix = 'z')
"""
objects = ce.getObjectsFrom(ce.scene,  ce.withName('street'))
for o in objects:
    ce.setRuleFile(o, 'none')    
        
print "czekanie na rendering 3"     
ce.generateModels(ce.getObjectsFrom(ce.scene))
views = ce.getObjectsFrom(ce.get3DViews())
views[0].frame()
ce.waitForUIIdle()    
print "koniec 3"
"""
#create_photo_set(main_road = 'main_road', prefix = 'y')
"""
   
   
    
#    if ce.getStartRule(shape) == 'Default$Lot':
#        ce.setName(shape, 'lot')
#        ce.setRuleFile(shape, 'rules/paris.cga')  
#    elif ce.getStartRule(shape) == 'Lot':
#        ce.setName(shape, 'lot')
#        ce.setRuleFile(shape, 'rules/paris.cga')           
#    elif ce.getStartRule(shape) == 'Default$LotInner':
#        ce.setName(shape, 'lot')
#        ce.setRuleFile(shape, 'rules/paris.cga')   
#    else:
#        ce.setName(shape, 'street')
#        ce.setRuleFile(shape, 'rules/Streets_Advanced/Advanced_Street.cga')
"""

