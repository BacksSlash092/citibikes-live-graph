import requests
import json
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation 
from matplotlib import style 


style.use('dark_background')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def connect_to_api():
    """Returns a dictionary, with the live feed data"""
    url = 'https://feeds.citibikenyc.com/stations/stations.json'
    r = requests.get(url)
    print('Status Code: ', r.status_code)
    response_dict = r.json()
    return response_dict 
    

def animate(i):
    response_dict = connect_to_api()
    r_dict = {}
    address_list = []
    bike_list=[]
    dock_list=[] 
    #print( print( response_dict['stationBeanList'][0]))
    for key in range(0,len(response_dict['stationBeanList'])):
        address, bikes = response_dict['stationBeanList'][key]['stAddress1'],response_dict['stationBeanList'][key]['availableBikes']
        dock = response_dict['stationBeanList'][key]['availableDocks']
      

        dock_list.append(dock)
        address_list.append(address)
        bike_list.append(bikes)

        r_dict[key] = bikes

        
        if r_dict[key] > bikes: 
            color ='red'

        if r_dict[key] < bikes: 
            color = 'green'
           
        else:
            color = 'blue'
        
        
    for key in range(0, 100):     
        plt.bar(key, bike_list[key],color=color, alpha=0.3, label='Bikes')
        plt.bar(key,dock_list[key], color='c',alpha=0.3,label='Docks')

plt.legend()
plt.title('Citibikes Availible by Station')
plt.xlabel('Station')
plt.ylabel('Bikes Availible')
ax1.legend()
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.grid(color='c')   
style.use('dark_background')
plt.show()
