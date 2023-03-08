#pip install pygal_maps_world
import pygal
worldmap_chart = pygal.maps.world.World()
worldmap_chart.title = 'Worlds map'
worldmap_chart.add('Visited countries', ['ir','th','de','fr','fi','no','at','au','ee','it','nl','tr','my','ca','pl'])
worldmap_chart.add('The bucket list', ['us','in','cn','jp','nz','za'])
worldmap_chart.render()
worldmap_chart.render_to_file('Countries.svg')
