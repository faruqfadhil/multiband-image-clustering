from PIL import Image
import numpy as np
from numpy import zeros
from clusterProses import Cluster  
import random
# initial loop from index 0
numb_of_data = 6
index = 0
ncluster=3
# initial variabel
image_temp = Image.open("/media/faruq/FARUQ/PENS/semester6/datamining/program/multiband_image/multiband_data/gb0.GIF")
final_data = zeros([image_temp.size[0]*image_temp.size[1],numb_of_data])
im = {}
while index < numb_of_data:
    name =str(index)
    im[index] = Image.open("/media/faruq/FARUQ/PENS/semester6/datamining/program/multiband_image/multiband_data/gb"+name+".GIF")
    i = 0
    for x in range(0, im[index].size[0]):
        for y in range(0, im[index].size[1]):
            pix_val = im[index].getpixel((x, y))
            final_data[i][index] = pix_val
            i+=1
    index+=1
# print(final_data)
# call clustering proses
k = Cluster.hierarcial(final_data,ncluster)
cluster_uniq = np.unique(k)
# data after cluster proses
data_with_cluster = np.insert(final_data, 6, k,axis=1)
# print(cluster_uniq)
# np.savetxt('data_cluster.csv',data_with_cluster, delimiter=' ') 

# create image
# create n-random rgb color by n-cluster
def colors(n):
  ret = []
  r = int(random.random() * 256)
  g = int(random.random() * 256)
  b = int(random.random() * 256)
  step = 256 / n
  for i in range(n):
    r += step
    g += step
    b += step
    r = int(r) % 256
    g = int(g) % 256
    b = int(b) % 256
    ret.append((r,g,b)) 
  return ret
warna = colors(ncluster)

im2 = Image.new("RGB", (image_temp.size[0], image_temp.size[1]))
pixels = im2.load()
i=0
for x in range(0, image_temp.size[0]):
    for y in range(0, image_temp.size[1]):
        for z in range(0,ncluster):
            if data_with_cluster[i][6] == cluster_uniq[z]:
                pixels[x,y] = warna[z]
        # if data_with_cluster[i][6] == 0:
        #     pixels[x,y] = warna[0]
        # elif data_with_cluster[i][6] == 1:
        #     pixels[x,y] = warna[1]
        # else:
        #     pixels[x,y] = warna[2]
        # print(x,y,i)
        i+=1
        # pixels[x, y] = warna1
# print(pixels)
im2.show()
