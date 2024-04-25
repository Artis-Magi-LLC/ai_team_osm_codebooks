import lib as l 
from tqdm import tqdm

country_data_folder = '/home/dylan/open_st_map/country_data/'
country_df_folder = '/home/dylan/open_st_map/country_dfs/'
codebook_folder = '/home/dylan/open_st_map/country_codebooks/' 

input = [{'country_name':'Belarus',
          'region_admin_level':'4', 
          'filename': 'belarus-latest.osm.pbf'},
         {'country_name':'Bosnia and Herzegovina',
          'region_admin_level' : '4',
          'filename': 'bosnia-herzegovina-latest.osm.pbf'},
         {'country_name' : 'Bulgaria',
          'region_admin_level': '6',
          'filename': 'bulgaria-latest.osm.pbf'},
         {'country_name' : 'Burkina Faso',
          'region_admin_level': '4',
          'filename': 'burkina-faso-latest.osm.pbf'},
         {'country_name' : 'Democratic Republic of the Congo',
          'region_admin_level': '4',
          'filename': 'congo-democratic-republic-latest.osm.pbf'},
         {'country_name' : 'Egypt',
          'region_admin_level': '4',
          'filename': 'egypt-latest.osm.pbf'},
         {'country_name' : 'Georgia',
          'region_admin_level': '4',
          'filename': 'georgia-latest.osm.pbf'},
         {'country_name' : 'Ghana',
          'region_admin_level': '4',
          'filename': 'ghana-latest.osm.pbf'},
         {'country_name' : 'Iraq',
          'region_admin_level': '4',
          'filename': 'iraq-latest.osm.pbf'},
         {'country_name' : 'Kenya',
          'region_admin_level': 'kenya-latest.osm.pbf',
          'filename': '4'},
         {'country_name' : 'Libya',
          'region_admin_level': '4',
          'filename': 'libya-latest.osm.pbf'},
         {'country_name' : 'Moldova',
          'region_admin_level': '4',
          'filename': 'moldova-latest.osm.pbf'},
         {'country_name' : 'Romania',
          'region_admin_level': '6',
          'filename': 'romania-latest.osm.pbf'},
         {'country_name' : 'Somalia',
          'region_admin_level': '5',
          'filename': 'somalia-latest.osm.pbf'},
         {'country_name': 'Tanzania',
          'region_admin_level': '4',
          'filename':'tanzania-latest.osm.pbf'}]

for country in input: 

    country_name = country['country_name']
    filename = country['filename']
    print("processing {}".format(country_name))
    with open(country_data_folder+filename, 'rb') as f: 

        country_df = l.create_country_df(f, country_df_folder+country_name.lower()+'country_df.csv')
        codebook = l.create_osm_codebook(country_df, country['region_admin_level'], country_name = country_name)
    
    if len(codebook) == 0: 
        print("no rows in codebook for country {}".format(country_name)) 

    
    else: 
        print("number of phrases in codebook for {}:{}".format(country_name, len(codebook)))
        codebook.to_csv(codebook_folder + 'osm_codebook_{}'.format(country_name))


