## Flask Spatial API
#### Daniel Bowen
#### Project Description: 
When you navigate to the Assignment 3 link, a file called countries.geo.json on the backend is queried and stored within a KD Tree. Once the desired values are set on the left and you click anywhere on the map, a query is run on that kd tree for the nearest neighbors given the desired parameters in a modal display.
| File | Folder | Link |
| --- | --- | --- |
| assignment3.py | root | https://github.com/Kanrail/5443-Spatial-DS-Bowen/blob/master/Assignments/Assignment%203/assignment3.py |
| home.html | templates | https://github.com/Kanrail/5443-Spatial-DS-Bowen/blob/master/Assignments/Assignment%203/templates/home.html |
| assignment3.html | templates | https://github.com/Kanrail/5443-Spatial-DS-Bowen/blob/master/Assignments/Assignment%203/templates/assignment3.html |
| countries.geo.json | data | https://github.com/Kanrail/5443-Spatial-DS-Bowen/blob/master/Assignments/Assignment%203/data/countries.geo.json |

#### Instructions: 
Start the project from the assignment.py and go to http://localhost:8888. From the landing page, click the Assignment 3 link at the top right. Once on the page, you can set the values for how many surrounding neighbors and the distance at which they can be retrieved for the next time you click on the map. When you click on the map, a modal is generated with the nearest neighbor geojson data. This process can be repeated as many times as desired. 
|Dependency | Type | Link |
| --- | --- | --- |
| geojson | python library | https://pypi.org/project/geojson/ |
| KDTree from scipy.spatial | python library | https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.KDTree.html |
