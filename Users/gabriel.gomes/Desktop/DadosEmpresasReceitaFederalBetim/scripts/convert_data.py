import geopandas
import matplotlib.pyplot as plt
import pandas as pd
from pyproj import Proj, Transformer
from haversine import haversine

# inProj = Proj(init='epsg:4326')
# outProj = Proj(init='epsg:31983')
x1,y1 = -44.15582528,-19.86338126
x, y = -44.194697, -19.947591
# x2,y2 = transform(inProj,outProj,x1,y1)
# print (x2,y2)

lat1, log1 = -19.93991, -44.19137
lat2, log2 = -19.94006, -44.1945

pt1 = y1,x1
pt2 = y, x
transformer = Transformer.from_crs("epsg:4326", "epsg:31983")




p1 = transformer.transform(lat1, log1)
p2 = transformer.transform(lat2, log2)
# 2510101.4849381056, 4793263.186719755


print(p1)
print(p2)
print(haversine(pt1, pt2))
# lat sis -19,86338126    pelias  -19.947591
# log sis -44,15582528    pelias  -44.194697 



#dataFrame = pd.read_csv("../dados/afterDAdos_oti_back.csv")

