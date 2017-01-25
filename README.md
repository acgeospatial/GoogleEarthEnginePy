# GoogleEarthEnginePy
Basic script to order data on Google Earth Engine using Python API

October 2016 brought the announcement from Google that it had all Landsat and Sentinel data on its cloud. Amazon are also hosting all this data, ESRI are using the Amazon cloud and so are Planet (both of these for over a year). Never before has so much Earth Observation data been available to everyone. I wrote last week about Google Earth Engine Timelapse – you can view anywhere on the planet, one image per year from 1984-2016 (and onwards you would think). Already, amazing changes are being shown; what a stunning tool for the teaching of Geography and Earth Science. It will surely set student’s minds alight.

For the last 10 years I have downloaded huge volumes of data, processed it locally, saved the output and archived the data. However, things are changing; traditional workflows are being replaced by server side processing. I am going to describe this in part below, but first this.

It’s all a bit like ordering a sandwich

Bear with me. America has a strong service culture. On my first visit to the US I wanted a sandwich. I went in with the best of intentions of ordering something like a chicken sandwich (I can’t remember exactly), but what ultimately I was faced with was a bewildering array of questions pertaining to my choice. What type of bread (after about 5 types I panic and just take the one I can remember being offered)…what filling…what spread…what salad…how much…sauces…pepper…extra cheese. I end up by just saying yes (I am British, I didn’t want to cause a fuss). Later on in the day I was in a bookshop and wanted a tea; after being offered small, medium, large, extra large – errr, just medium is fine. I am pretty sure I ended up with what can only be described as a pint of tea – how much would I have got with extra large?

Where am I going with this rather tenuous(?) analogy? Accessing imagery on the cloud through an API and processing it seems to me to be much like ordering a sandwich, only this time I am in control and I can always change my order if it doesn’t meet my needs/expectations.

Processing imagery with Google Earth Engine – basic

You can sign up / request access here https://earthengine.google.com/ as long as you are using this non-commercially then no problem. I am using it non-commercially. You will get an email giving you links to Earth Engine Code Editor which is a JavaScript development environment, and you can get information about this here.

I am mostly interested in using the other API which is a Python library this is a pretty comprehensive guide to setting up and getting ready to code in the Python API. If it’s working then this script:

# Import the Earth Engine Python Package
import ee

# Initialize the Earth Engine object, using the authentication credentials.
ee.Initialize()

# Print the information for an image asset.
image = ee.Image('srtm90_v4')
print(image.getInfo())

Will return
![alt tag](http://www.acgeospatial.co.uk/wp-content/uploads/2016/12/image1.png)

Get this far and you are ready to access and process all the data on Earth Engine. These are the datasets available, how many? 275! (NDVI, NSDI, Reflectance, NBRT etc etc).

Python API

There is not much information on the https://developers.google.com/earth-engine/ about Python, so GitHub is the place to now dive into.

So, just like ordering a sandwich, you can use the API to order whatever you want. Here I am asking for

    an edge detection on one tile of the panchromatic band of Landsat 8 and on a different Landsat 8 tile a true colour RGB (4,3,2) and then clipped to a region of my choice. 

No more downloading an image and then doing the processing; I am asking for exactly what I want.

![alt tag](http://www.acgeospatial.co.uk/wp-content/uploads/2016/12/image2-768x311.png)

Run the above script and go to the Earth Engine Code Editor (JavaScript) and you can see what is running and its status.

![alt tag](http://www.acgeospatial.co.uk/wp-content/uploads/2016/12/image3.png)

When its done

![alt tag](http://www.acgeospatial.co.uk/wp-content/uploads/2016/12/image4.png)

You’ll get a link as well to your google drive account

![alt tag](http://www.acgeospatial.co.uk/wp-content/uploads/2016/12/image5.png)

Click on the output link (I created a folder after running the script called imagery)

![alt tag](http://www.acgeospatial.co.uk/wp-content/uploads/2016/12/image6.png)

And here I go, out1.tif (its georeferenced aswell!)

![alt tag](http://www.acgeospatial.co.uk/wp-content/uploads/2016/12/image7-768x456.png)

And out 2

![alt tag](http://www.acgeospatial.co.uk/wp-content/uploads/2016/12/image8-768x456.png)
![alt tag](http://www.acgeospatial.co.uk/wp-content/uploads/2016/12/image9-768x456.png)

And to prove it is georeferenced, here is the OpenStreetMap data sitting behind it

![alt tag](http://www.acgeospatial.co.uk/wp-content/uploads/2016/12/image10-768x456.png)

So, using Google Earth Engine is just like ordering a sandwich, only if you get it wrong you can keep ordering again and again and again. Just don’t ask for a medium tea.

Do you want to find out about more of my work? http://www.acgeospatial.co.uk
