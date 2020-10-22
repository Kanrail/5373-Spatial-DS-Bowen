from flask import *
from flask_cors import CORS
from scipy.spatial import KDTree
import os,sys
import json
import geojson

app = Flask(__name__)
CORS(app)

geoDataList = []
neighborCoords = []

numNeighbors = 5
neighborsUpperBound = 5

def kdtree(data):
    tree = KDTree(data)
    return tree

def get_data_from_file():
    data_file = './data/countries.geo.json'
    if os.path.isfile(data_file):
        with open(data_file,'r') as f:
            data = f.read()
    else:
        return jsonify({"Error":"countries.geo.json not there!!"})

    return json.loads(data)

def load_datalist(data):
    global geoDataList
    geoDataList = []

    for country in data:
        coords = country['geometry']['coordinates']
        kind = country['geometry']["type"]
        for coord in coords:
            poly = coord
            while len(poly) == 1:
                poly = poly[0]
            for i in range(len(poly)):
                geoDataList.append(poly[i])

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/assignment3/',methods=['GET','POST'])
def assignment3():
    mapbox_token = 'pk.eyJ1Ijoia2FucmFpbCIsImEiOiJja2ZsaHVwaDcxNzF3MnBsM3E5ZWFpd25qIn0.iYAE4XAQ6nJ30Lg28ncXvg'
    
    return render_template('assignment3.html',mapbox_token=mapbox_token)

@app.route('/assignment3/neighbor_values',methods=['POST'])
def set_neighbor_values():
    global numNeighbors,neighborsUpperBound
    
    if request.json["numNeighbors"] != None:
        numNeighbors = int(request.json["numNeighbors"])
    else:
        numNeighbors = 5
    if request.json["neighborsUpperBound"] != None:
        neighborsUpperBound = int(request.json["neighborsUpperBound"])
    else:
        neighborsUpperBound = 5
    
    print('numNeighbors '+str(numNeighbors)+' '+'upperbound '+str(neighborsUpperBound))
    return jsonify({'success':True})

@app.route('/click/')
def click():
    global neighborCoords,geoDataList,numNeighbors,neighborsUpperBound
    neighborCoords = []
    lng,lat = request.args.get("lngLat",None).split(",")
    
    #Set the initial point based on click
    searchArea = []
    searchArea.append(float(lng))
    searchArea.append(float(lat))
    
    try:
        #Query the KDTree for the neighbors
        distanceList, neighborList = tree.query(searchArea, k = numNeighbors, distance_upper_bound = neighborsUpperBound)
        
        #Print each nearest neighbor and their distance from the point
        for i in range(len(distanceList)):
            print(f"Long: {lng} Lat: {lat}\nNearest Neighbor: {geoDataList[neighborList[i]]} at distance of {distanceList[i]}\n")
            
        #Store the nearest neighbor information
        for neighbor in neighborList:
            neighborCoords.append(geojson.Feature(geometry = geojson.Point(geoDataList[neighbor]), properties = {'title':'neighbor'}))
        neighborCoords = geojson.FeatureCollection(neighborCoords)
    except:
        print('No neighbors found')
    return jsonify({'success':True, 'neighbors':neighborCoords})


if __name__ == '__main__':
    load_datalist(get_data_from_file())
    tree = kdtree(geoDataList)
    
    app.run(host='0.0.0.0', port=8888)