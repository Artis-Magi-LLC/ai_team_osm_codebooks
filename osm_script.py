import lib as l 
from tqdm import tqdm

country_data_folder = '/home/dylan/open_st_map/country_data/'
country_df_folder = '/home/dylan/open_st_map/country_dfs/'
codebook_folder = '/home/dylan/open_st_map/country_codebooks/' 

# {'country_name':'Belarus',
#           'region_admin_level':'4', 
#           'filename': 'belarus-latest.osm.pbf'},
# {'country_name':'Bosnia and Herzegovina',
#           'region_admin_level' : '4',
#           'filename': 'bosnia-herzegovina-latest.osm.pbf'}
# {'country_name' : 'Bulgaria',
#           'region_admin_level': '6',
#           'filename': 'bulgaria-latest.osm.pbf'}

#        {'country_name' : 'Burkina Faso',
#         'region_admin_level': '4',
#        'filename': 'burkina-faso-latest.osm.pbf'}
#
# {'country_name' : 'Democratic Republic of the Congo',
#           'region_admin_level': '4',
#           'filename': 'congo-democratic-republic-latest.osm.pbf'},
# {'country_name' : 'Egypt',
#           'region_admin_level': '4',
#           'filename': 'egypt-latest.osm.pbf'},
# {'country_name' : 'Georgia',
#           'region_admin_level': '4',
#           'filename': 'georgia-latest.osm.pbf'},
# {'country_name' : 'Ghana',
#           'region_admin_level': '4',
#           'filename': 'ghana-latest.osm.pbf'},
# {'country_name' : 'Kenya',
#           'region_admin_level': '4',
#           'filename': 'kenya-latest.osm.pbf'},
# {'country_name' : 'Libya',
#           'region_admin_level': '4',
#           'filename': 'libya-latest.osm.pbf'},
# {'country_name' : 'Moldova',
#           'region_admin_level': '4',
#           'filename': 'moldova-latest.osm.pbf'},
# {'country_name' : 'Somalia',
#           'region_admin_level': '5',
#           'filename': 'somalia-latest.osm.pbf'}

# {'country_name' : 'Romania',
#          'region_admin_level': '6',
#          'filename': 'romania-latest.osm.pbf'}
    # {'country_name' : 'Poland',
    #      'region_admin_level': '4',
    #      'filename': 'poland-latest.osm.pbf'},
input = [
    {'country_name' : 'Central African Republic',
         'region_admin_level': '4',
         'filename': 'central-african-republic-latest.osm.pbf'},
    {'country_name' : 'Chile',
         'region_admin_level': '4',
         'filename': 'chile-latest.osm.pbf'},
    {'country_name' : 'Colombia',
         'region_admin_level': '4',
         'filename': 'colombia-latest.osm.pbf'},
    {'country_name' : 'Czech Republic',
         'region_admin_level': '4',
         'filename': 'czech-republic-latest.osm.pbf'},
    {'country_name' : 'Djibouti',
         'region_admin_level': '4',
         'filename': 'djibouti-latest.osm.pbf'},
    {'country_name' : 'Ecuador',
         'region_admin_level': '4',
         'filename': 'ecuador-latest.osm.pbf'},
    {'country_name' : 'Gabon',
         'region_admin_level': '4',
         'filename': 'gabon-latest.osm.pbf'},
    {'country_name' : 'Guatemala',
         'region_admin_level': '4',
         'filename': 'guatemala-latest.osm.pbf'},
    {'country_name' : 'Honduras',
         'region_admin_level': '4',
         'filename': 'colombia-latest.osm.pbf'},
    {'country_name' : 'Hungary',
         'region_admin_level': '6',
         'filename': 'hungary-latest.osm.pbf'},
    {'country_name' : 'Iran',
         'region_admin_level': '4',
         'filename': 'iran-latest.osm.pbf'},
    {'country_name' : 'Kazakhstan',
         'region_admin_level': '4',
         'filename': 'kazakhstan-latest.osm.pbf'},
    {'country_name' : 'Mexico',
         'region_admin_level': '4',
         'filename': 'mexico-latest.osm.pbf'},
    {'country_name' : 'Nigeria',
         'region_admin_level': '4',
         'filename': 'nigeria-latest.osm.pbf'},
    {'country_name' : 'Niger',
         'region_admin_level': '6',
         'filename': 'niger-latest.osm.pbf'},
    {'country_name' : 'Panama',
         'region_admin_level': '4',
         'filename': 'panama-latest.osm.pbf'},
    {'country_name' : 'Philippines',
         'region_admin_level': '3',
         'filename': 'philippines-latest.osm.pbf'},
    {'country_name' : 'Sierra Leone',
         'region_admin_level': '4',
         'filename': 'sierra-leone-latest.osm.pbf'},
    {'country_name' : 'Sudan',
         'region_admin_level': '4',
         'filename': 'sudan-latest.osm.pbf'},
    {'country_name' : 'Syria',
         'region_admin_level': '4',
         'filename': 'syria-latest.osm.pbf'},
    {'country_name' : 'Tajikistan',
         'region_admin_level': '4',
         'filename': 'tajikistan-latest.osm.pbf'},
    {'country_name' : 'Tunisia',
         'region_admin_level': '4',
         'filename': 'tunisia-latest.osm.pbf'},
    {'country_name' : 'Venezuela',
         'region_admin_level': '4',
         'filename': 'venezuela-latest.osm.pbf'}
         ]

for country in input: 

    country_name = country['country_name']
    filename = country['filename']
    print("processing {}".format(country_name))
    country_df = l.create_country_df(country_data_folder+filename, country_df_folder+country_name.lower()+'country_df.csv')
    codebook = l.create_osm_codebook(country_df, country['region_admin_level'], country_name = country_name)
    
    if len(codebook) == 0: 
        print("no rows in codebook for country {}".format(country_name)) 

    
    else: 
        print("number of phrases in codebook for {}:{}".format(country_name, len(codebook)))
        codebook.to_csv(codebook_folder + 'osm_codebook_{}.csv'.format(country_name))


