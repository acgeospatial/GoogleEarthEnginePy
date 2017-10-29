import ee
from ee import batch

## Initialize (a ee python thing)
ee.Initialize()

## define your collection
collection = ee.ImageCollection('LANDSAT/LC8_L1T_TOA')

#Dubai Path and Row
##path = collection.filter(ee.Filter.eq('WRS_PATH', 160))
##pathrow = path.filter(ee.Filter.eq('WRS_ROW', 43))

## Above commented out as you might not know the path and row this allows you to pass a coordinate
pointUAE = ee.Geometry.Point(55, 25)
pathrow = collection.filterBounds(pointUAE)
 
##Filter cloudy scenes.
clouds = pathrow.filter(ee.Filter.lt('CLOUD_COVER', 5))

## select the bands, we are going for true colour... but could be any!
bands = clouds.select(['B4', 'B3', 'B2'])

##make the data 8-bit.
def convertBit(image):
    return image.multiply(512).uint8()  

## call the conversion    
outputVideo = bands.map(convertBit)

print "about to build video"

#Export to video.
# Dubai
out = batch.Export.video.toDrive(outputVideo, description='dubai_video', dimensions = 720, framesPerSecond = 2, region=([55.6458,25.3540], [54.8135,25.3540],[54.8135,24.8042],[55.6458,24.8042]), maxFrames=10000)

## process the image
process = batch.Task.start(out)

print "process sent to cloud"
