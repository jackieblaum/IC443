import os
import gt_apps as my_apps
from BinnedAnalysis import *

def get_sourcemap(analysisPath,prefix,suffix,sources):

    fullDataDir = analysisPath + '/data/'
    dataDir = analysisPath + '/data/'
    responseDir = analysisPath + '/' + prefix + '_responses/'
    sourcemapsDir = analysisPath + '/' + prefix + '_sourceMaps/'
    generatedModelDir = analysisPath + '/' + prefix + '_generatedModels/'

    result = os.system('ls -1 ' + dataDir + '*PH*.fits > ' + dataDir + 'events.list')
    if result != 0:
        print('FAILED TO CONCATENATE DATA FILE NAMES.')

    concatScFileName = fullDataDir + prefix + '_spacecraft.list'
    result = os.system('ls -1 ' + fullDataDir + '*SC*.fits > ' + concatScFileName)
    if result != 0:
        print('FAILED TO CONCATENATE SPACECRAFT FILE NAMES.')

    my_apps.srcMaps['scfile'] = '@' + dataDir + prefix + 'spacecraft.list'
    my_apps.srcMaps['expcube'] = responseDir + prefix + 'ltCube' + suffix + '.fits'
    my_apps.srcMaps['cmap'] = dataDir + prefix + '_ccube' + suffix + '.fits'
    my_apps.srcMaps['srcmdl'] = generatedModelDir + prefix + 'model' + sources + '.xml'
    my_apps.srcMaps['irfs'] = 'P8R2_SOURCE_V6'
    my_apps.srcMaps['bexpmap'] = responseDir + prefix + 'allsky_expcube' + suffix + '.fits'
    my_apps.srcMaps['outfile'] = sourcemapsDir + prefix + 'srcmap' + sources + '.fits'
    my_apps.srcMaps['rfactor'] = 4
    my_apps.srcMaps['emapbnds'] = 'no'
    my_apps.srcMaps['clobber'] = 'yes'
    my_apps.srcMaps.run()

