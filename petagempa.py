import requests
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

url = 'https://data.bmkg.go.id/DataMKG/TEWS/gempaterkini.json'
response = requests.get(url)
data = response.json()

# Mengumpulkan informasi Lintang dan Bujur setiap gempa.
list_lat = []
list_lon = []

for info in data['Infogempa']['gempa']:
    list_lat.append(float(info['Lintang'][0:-3]))
    list_lon.append(float(info['Bujur'][0:-3]))

# Membuat peta Basemap dengan tingkat zoom dan ukuran peta yang sesuai.
map = Basemap(llcrnrlon=min(list_lon)-1, llcrnrlat=min(list_lat)-1, urcrnrlon=max(list_lon)+1, urcrnrlat=max(list_lat)+1,
              resolution='i', projection='merc', lat_0=sum(list_lat)/len(list_lat), lon_0=sum(list_lon)/len(list_lon))
map.drawcoastlines()
map.drawcountries()
map.fillcontinents(color='gray', lake_color='blue')
map.drawmapboundary(fill_color='white')

# Menambahkan titik-titik lokasi gempa ke dalam peta dengan ukuran marker yang disesuaikan.
for idx, lat in enumerate(list_lat):
    lon = list_lon[idx]
    x, y = map(lon, lat)
    mag = float(data['Infogempa']['gempa'][idx]['Magnitude'])
    map.plot(x, y, 'ro', markersize=mag**1, alpha=0.5)

# Menampilkan peta
plt.title('Lokasi Gempa Bumi Terkini BMKG')
plt.show()
