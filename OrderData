# Import the Earth Engine Python Package
import ee
from ee import batch ### I found this to work for me.

# Initialize the Earth Engine object, using the authentication credentials.
ee.Initialize()

# Get the panchromatic band of a landsat 8 tile - this is tile that cover San Francisco USA
image = ee.Image('LANDSAT/LC8_L1T/LC80440342014077LGN00').select('B8')

# get a landsat scene, band RGB 432 (true colour) - Bejing China
landsat = ee.Image('LANDSAT/LC8_L1T_TOA/LC81230322014135LGN00').select(['B4', 'B3', 'B2'])

#output the landsat true colour RGB, region defined - Region has to be a nested loop
out1 = batch.Export.image.toDrive(landsat, description='out1', region=([116.2621, 39.8412], [116.2621, 40.01236],[116.4849, 40.01236],[116.4849, 39.8412]))

# Canny edge detect on san francisco image
canny =  ee.Algorithms.CannyEdgeDetector(image,10,1)

# Output the edge detect
out2 = batch.Export.image.toDrive(canny, description='out2', maxPixels=238523062)

#run the processes on Google Earth Engine
process = batch.Task.start(out1)
process = batch.Task.start(out2)
