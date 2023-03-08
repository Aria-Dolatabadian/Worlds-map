#pip install pygal_maps_world
import pygal
worldmap_chart = pygal.maps.world.World()
worldmap_chart.title = 'Worlds map'
worldmap_chart.add('Visited countries', ['ir','th','de','fr','fi','no','at','au','ee','it','nl','tr','my','ca','pl'])
worldmap_chart.add('The bucket list', ['us','in','cn','jp','nz','za'])
worldmap_chart.render()
worldmap_chart.render_to_file('Countries.svg')





import pygal
supra = pygal.maps.world.SupranationalWorld()
supra.add('Asia', [('asia', 1)])
supra.add('Europe', [('europe', 1)])
supra.add('Africa', [('africa', 1)])
supra.add('North america', [('north_america', 1)])
supra.add('South america', [('south_america', 1)])
supra.add('Oceania', [('oceania', 1)])
supra.add('Antartica', [('antartica', 1)])
supra.render()
supra.render_to_file('Continents.svg')
