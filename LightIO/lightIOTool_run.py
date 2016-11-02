# coding:utf-8

import sys

def lightIOTool_run():
    try:
        filePath = __file__
        appPath = filePath.rpartition('\\')[0]
    except:
        print 'Environ Value {} not exist.'.format(appPath)
    
    else:
        path = appPath
        
        if not path in sys.path:
            sys.path.append(path)
        
        import lightUI
        reload(lightUI)
        lightUI.main()

if __name__ == 'lightIOTool_run':  
    lightIOTool_run()



