# coding:utf-8

import pymel.all as pm
import maya.cmds as cmds
import json

def loadeRenderGlobal():
    if not pm.objExists('renderInfoNode'):
        print u'lightInfoNode 가 존재 하지 않습니다.'
        return
    
    if( pm.getAttr( 'defaultRenderGlobals.currentRenderer' ) != 'arnold' ):
        pm.setAttr('defaultRenderGlobals.currentRenderer', 'arnold')

    renderInfoNode = pm.PyNode('renderInfoNode')
    renderInfo = json.loads(renderInfoNode.renderInfo.get())
    
    for attr, value in renderInfo.items():
        try:
            attrNode = pm.PyNode(attr)
            attrNode.set(value)
        except:
            pass
            #print '{} failed set value {}.'.format(attr, value)
            
    renderInfoNode.unlock()
    pm.delete(renderInfoNode)
    
    print u'렌더 셋팅을 성공 적으로 로드 하였습니다.'
    
def saveRenderGlobal():

    rgArnold   = pm.PyNode('defaultArnoldDriver')
    rgArnoldRO = pm.PyNode('defaultArnoldRenderOptions')
    rgCommon   = pm.PyNode('defaultRenderGlobals')
    rgRes      = pm.PyNode('defaultResolution')
    
    # get
    renderInfo = {}
    
    for attr in rgArnold.listAttr():
        try:
            renderInfo[attr.name()] = cmds.getAttr(attr.name())
        except:
            pass
    
    for attr in rgCommon.listAttr():
        try:
            renderInfo[attr.name()] = cmds.getAttr(attr.name())
        except:
            pass
        
    for attr in rgRes.listAttr():
        try:
            renderInfo[attr.name()] = cmds.getAttr(attr.name())
        except:
            pass
        
    for attr in rgArnoldRO.listAttr():
        try:
            renderInfo[attr.name()] = cmds.getAttr(attr.name())
        except:
            pass
        
    # add data
    if pm.objExists('renderInfoNode'):
        lightInfoNode = pm.PyNode('renderInfoNode')
        lightInfoNode.unlock()
        pm.delete(lightInfoNode)
    lightInfoNode = pm.createNode('network', n='renderInfoNode')
    lightInfoNode.addAttr('renderInfo', dt='string')
    
    jsonHandl = json.dumps(renderInfo)
    lightInfoNode.attr('renderInfo').set(jsonHandl)
    lightInfoNode.attr('renderInfo').lock()
    

    print u'렌더 셋팅을 성공 적으로 저장 했습니다.'
