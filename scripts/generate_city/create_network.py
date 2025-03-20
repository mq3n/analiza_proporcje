'''
Created on 24-04-2021

Author: Marcin Kutrzynski
'''
from scripting import *
import random

def clear_city():
    pass

def create_random_city():
    ce = CE()
    graphlayer = ce.addGraphLayer('streets')
    
    vertices = [0, 0, -1000, 0, 0, 1000]
    graph = ce.createGraphSegments(graphlayer, vertices)
    ce.setName(graph, 'main_road')
    
    vertices = [100, 0, -1000, 100, 0, 1000]
    graph = ce.createGraphSegments(graphlayer, vertices)
    ce.setName(graph, 'right_road')
    
    vertices = [-100, 0, -1000, -100, 0, 1000]
    graph = ce.createGraphSegments(graphlayer, vertices)
    ce.setName(graph, 'left_road')
    
    side = 1
    vertices = []
    for z in range(-1100, 1100, 200):
        side = side * -1
        vertices.extend([side * 200, 0, z + random.randint(0, 300)])
    
    graph = ce.createGraphSegments(graphlayer, vertices)
    ce.setName(graph, 'crossing1_road')
    
    side = -1
    vertices = []
    for z in range(-1100, 1100, 200):
        side = side * -1
        vertices.extend([side * 200, 0, z + random.randint(0, 300)])
    
    graph = ce.createGraphSegments(graphlayer, vertices)
    ce.setName(graph, 'crossing2_road')
    
    cleanupSettings = CleanupGraphSettings()
    cleanupSettings.setIntersectSegments(True)
    cleanupSettings.setMergeNodes(False)
    cleanupSettings.setMergingDist(10)
    cleanupSettings.setSnapNodesToSegments(True)
    cleanupSettings.setSnappingDist(10)
    cleanupSettings.setResolveConflictShapes(True)
    
    graphlayer = ce.getObjectsFrom(ce.scene, ce.isGraphLayer)
    ce.cleanupGraph(graphlayer, cleanupSettings)
    
    objects = ce.getObjectsFrom(ce.scene, ce.withName('main_road'))
    for o in objects:
        ce.setAttributeSource(o, '/ce/segment/streetWidth', "USER")
        ce.setAttribute(o, '/ce/segment/streetWidth', 50)

    # szerokosc ulic
    objects = ce.getObjectsFrom(ce.scene, ce.withName('main_road'))
    for o in objects:
        ce.setAttribute(o, '/ce/street/streetWidth', random.randint(8, 24))
        ce.setAttributeSource(o, '/ce/street/sidewalkWidthRight', "USER")
        ce.setAttribute(o, '/ce/street/sidewalkWidthRight', random.randint(2, 15))
        ce.setAttributeSource(o, '/ce/street/sidewalkWidthLeft', "USER")
        ce.setAttribute(o, '/ce/street/sidewalkWidthLeft', random.randint(2, 15))
    
    objects = ce.getObjectsFrom(ce.scene, ce.withName('Block'))
    for block in objects:
        ce.setAttributeSource(block, '/ce/block/shapeCreation', "USER")
        ce.setAttribute(block, '/ce/block/subdivisionRecursive', False)
        ce.setAttributeSource(block, '/ce/block/subdivisionRecursive', "USER")
        ce.setAttribute(block, '/ce/block/type', 'Offset Subdivision')
        ce.setAttributeSource(block, '/ce/block/cornerWidth', "USER")
        ce.setAttribute(block, '/ce/block/cornerWidth', random.randint(90, 200))
    
    objects = ce.getObjectsFrom(ce.scene, ce.withName('Shape'))
    for shape in objects:
        if ce.getStartRule(shape) == 'Default$Lot':
            ce.setName(shape, 'lot')
            ce.setRuleFile(shape, 'rules/paris.cga')  
        elif ce.getStartRule(shape) == 'Lot':
            ce.setName(shape, 'lot')
            ce.setRuleFile(shape, 'rules/paris.cga')           
        elif ce.getStartRule(shape) == 'Default$LotInner':
            ce.setName(shape, 'lot')
            ce.setRuleFile(shape, 'rules/paris.cga')
        elif ce.getStartRule(shape) == 'Default$LotCorner':
            ce.setName(shape, 'LotCorner')
            ce.setRuleFile(shape, 'rules/paris.cga')     
        else:
            ce.setName(shape, 'street')
            ce.setRuleFile(shape, 'rules/Streets_Advanced/Advanced_Street.cga')
        
    objects = ce.getObjectsFrom(ce.scene, ce.withName('street'))
    for street in objects:
        ce.setAttributeSource(street, '/ce/rule/Vehicles_per_km', "USER")
        ce.setAttribute(street, '/ce/rule/Vehicles_per_km', random.randint(20, 50))
    
    objects = ce.getObjectsFrom(ce.scene, ce.withName('lot'))
    for buildings in objects:
        ce.setAttributeSource(buildings, '/ce/rule/High_LoD', "USER")
        ce.setAttribute(buildings, '/ce/rule/High_LoD', True)
        
    objects = ce.getObjectsFrom(ce.scene, ce.withName('LotCorner'))
    for green in objects:
        ce.setAttributeSource(green, '/ce/rule/High_LoD', "USER")
        ce.setAttribute(green, '/ce/rule/High_LoD', True)
        ce.setAttributeSource(green, '/ce/rule/ShowTrees', "USER")
        ce.setAttribute(green, '/ce/rule/ShowTrees', "Realistic")       
    
    # chodnik     
    objects = ce.getObjectsFrom(ce.scene, ce.withName('street'))
    for street in objects:
        if ce.getStartRule(street) == 'Default$Sidewalk':
            ce.setAttributeSource(street, '/ce/rule/Plantings', "USER")
            ce.setAttribute(street, '/ce/rule/Plantings', True if random.randint(0, 10) > 5 else False)
            ce.setAttributeSource(street, '/ce/rule/Sidewalk_Texture', "USER")
            ce.setAttribute(street, '/ce/rule/Sidewalk_Texture', 'Cement Block Grey Running Bond')
            ce.setAttributeSource(street, '/ce/rule/Sidewalk_Texture_Scale', "USER")
            ce.setAttribute(street, '/ce/rule/Sidewalk_Texture_Scale', 5)
            ce.setAttributeSource(street, '/ce/rule/People_percentage', "USER")
            ce.setAttribute(street, '/ce/rule/People_percentage', random.randint(0, 35))
            ce.setAttributeSource(street, '/ce/rule/Tree.Name', "USER")
            ce.setAttribute(street, '/ce/rule/Tree.Name', 'Yew')         

    print("czekanie na rendering")     
    ce.generateModels(ce.getObjectsFrom(ce.scene))
    views = ce.getObjectsFrom(ce.get3DViews())
    views[0].frame()
    ce.waitForUIIdle()    
    print("koniec")