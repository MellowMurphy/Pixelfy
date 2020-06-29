# Pixelfy

1. Put your *.jpg* or *.png* images into the `inputs\` folder and run `Pixelfy.py`
2. Multiple different resolution pixelized images will be in their own folders in `outputs\` 

## Input Image
<img src="examples/inputs/jugg.png?raw=true" width="400">

## Output Images
<img src="examples/outputs/jugg/jugg_128.png?raw=true" width="200">  <img src="examples/outputs/jugg/jugg_64.png?raw=true" width="150"> <img src="examples/outputs/jugg/jugg_32.png?raw=true" width="100"> <img src="examples/outputs/jugg/jugg_16.png?raw=true" width="50">

***The images are automatically cropped by default by finding the extents of the colored parts of the image using a combination of the transparency layer and solid white backgrounds.***
***If your image has no transparency layer, then one will be added.***

*Next to be done is a more general background removal technique.*
