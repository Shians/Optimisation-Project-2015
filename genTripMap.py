from PIL import Image, ImageDraw
im = Image.open("Europe.png")
draw = ImageDraw.Draw(im)

def drawline( orig, dest, airfares = [] ):
    # colour defined by travel cost
    if not airfares:
        draw.line(location[orig] + location[dest], fill="hsl(0,100%,0%)", width=7)
        colour = 120-120*(travel[orig][dest]-minTravel)/(maxTravel-minTravel)
        draw.line(location[orig] + location[dest], fill="hsl(%d,100%%,50%%)" % (colour), width=4)
    else:
        draw.line(location[orig] + location[dest], fill="hsl(0,100%,0%)", width=6)
        colour = 120-120*(airfares[dest]-min(airfares))/(max(airfares)-min(airfares))
        draw.line(location[orig] + location[dest], fill="hsl(%d,100%%,50%%)" % (colour), width=4)

def drawcircle( city, radius ):
    # colour defined by daily cost
    colour = 120-120*(dailyMid[city]-min(dailyMid))/(max(dailyMid)-min(dailyMid))
    draw.ellipse((location[city][0]-(radius+4), location[city][1]-(radius+4), location[city][0]+(radius+4), location[city][1]+(radius+4)), fill="hsl(0,100%,0%)")
    draw.ellipse((location[city][0]-(radius+2), location[city][1]-(radius+2), location[city][0]+(radius+2), location[city][1]+(radius+2)), "hsl(%d,100%%,50%%)" % (colour))

##### define the trip #####
trip = ["Venice","London","Madrid","Florence","Moscow","Crete","Prague","Barcelona","Istanbul"]
days = [ 3, 6, 2, 3, 5, 25, 2, 3, 1 ]
#####

names = ["Moscow","Paris","London","Madrid","Rome","Crete","Barcelona","Berlin","Budapest","Florence","Amsterdam","Prague","Istanbul","Vienna","Venice"]

travel = [
    [0,146,126,202,146,168,143,156,207,291,154,146,115,131,129],
    [227,0,60,143,93,123,139,110,162,85,52,165,150,140,68],
    [213,82,0,249,160,284,135,107,163,224,124,171,197,179,152],
    [188,86,136,0,144,188,69,70,96,138,103,124,180,143,119],
    [223,80,125,146,0,177,39,96,69,84,94,94,74,105,71],
    [233,81,223,188,58,0,131,123,58,241,200,114,120,164,169],
    [200,121,79,76,32,165,0,143,108,103,90,110,141,103,74],
    [130,53,81,97,83,153,110,0,83,214,92,123,99,176,104],
    [249,133,125,96,41,123,96,76,0,164,157,113,50,149,97],
    [309,246,162,172,86,301,90,186,204,0,227,155,279,229,150],
    [155,158,73,141,136,211,117,106,125,229,0,85,121,155,95],
    [112,122,100,112,48,193,116,108,138,144,97,0,85,152,65],
    [123,101,127,154,67,173,122,86,41,235,66,108,0,59,65],
    [145,162,122,202,90,75,145,117,175,171,90,181,121,0,194],
    [167,65,17,117,84,191,97,119,110,152,75,96,177,152,0]
]

fromMelb = [1390,1090,1007,1175,1082,1298,1101,1376,1399,1611,1376,1236,1140,1044,1362]
toMelb = [803,844,875,1061,934,922,983,921,1033,1186,622,1058,748,836,1076]
dailyMid = [92, 223, 298, 148, 169, 181, 126, 130, 145, 142, 165, 100, 85, 158, 134]

location = [(1173,104),(372,363),(314,269),(233,635),(600,588),(900,784),(366,604),(622,231),(750,409),(573,532),(430,237),(647,321),(978,617),(691,386),(598,477),(1140,759),(1155,742)]

minTravel = 17
maxTravel = 309

# draw line from melbourne to first city
dest = names.index(trip[0])
drawline( 15, dest, fromMelb )

for i in range(len(trip)-1):
    orig = names.index(trip[i])
    dest = names.index(trip[i+1])
    drawline( orig, dest )
    drawcircle( orig, days[i] )

# draw line from last city to melbourne
drawline( 16, dest, toMelb )

# draw a circle on the last city
drawcircle( dest, days[len(trip)-1] )


im.save("Trip.png")

