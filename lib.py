import osmium
import shapely.wkb
from shapely import wkt
import pandas as pd
import geopandas as gpd
from tqdm import tqdm
import os 
import numpy as np 

#utils 
def merge_two_dicts(x, y):
    z = x.copy()   # start with keys and values of x
    z.update(y)    # modifies z with keys and values of y
    return z

class AdminAreaHandler(osmium.SimpleHandler):
    def __init__(self):
        osmium.SimpleHandler.__init__(self)

        self.areas = []
        self.wkbfab = osmium.geom.WKBFactory()

    def area(self, a):            
        if  "admin_level" in a.tags:
            try:
                wkbshape = self.wkbfab.create_multipolygon(a)
                shapely_obj = shapely.wkb.loads(wkbshape, hex=True)
                
                area = { "id": a.id, "geo": shapely_obj }
                area = merge_two_dicts(area, a.tags)
                
                self.areas.append(area)
            except: 
                pass

#lib

def create_country_df(osm_file, output_path = '', save = True): 
    handler = AdminAreaHandler() 
    handler.apply_file(osm_file, locations = True, idx = 'flex_mem') 
    df = pd.DataFrame(handler.areas) 
    if save: 
        df.to_csv(output_path) 
    return df

def create_osm_codebook(country_df, region_admin_level, country_name = '', use_country_index = False, country_index = None, name_columns = None, convert = False): 
    if convert:
        country_df['geometry'] = country_df['geo'].apply(wkt.loads) 
    else: 
        country_df['geometry'] = country_df['geo']

    country_gdf = gpd.GeoDataFrame(country_df, crs='epsg:4326')
    if use_country_index: 
        country_geometry = country_gdf.loc[country_index, 'geometry']
    else: 
        countries = country_gdf[country_gdf['admin_level'] =='2']
        matching_countries = countries[countries['name'] == country_name]
        if len(matching_countries) != 1:
            print("Number of country rows matching name {}".format(len(matching_countries)))
            return ''
    

    country_indicies = [] 
    for i in country_gdf.index: 
        geometry = country_gdf.loc[i, 'geometry'] 
        if geometry.within(country_geometry): 
            country_indicies.append(i) 

    in_country_gdf = country_gdf.loc[country_indicies, :]

    if name_columns != None: 
        pass 
    else: 
        name_columns = ['ISO3166-1','ISO3166-1:alpha2', 'ISO3166-1:alpha3', 'ISO3166-1:numeric', 'ISO3166-2'] + [i for i in country_gdf.columns if ('name' in i) and (i != 'Unnamed: 0')]
    
    regions_ = in_country_gdf[in_country_gdf['admin_level'] == region_admin_level]
    regions = regions_.dropna(subset = ['ISO3166-2'])

    output = [{'index':i, 'code': regions.loc[i, 'ISO3166-2'], 'geometry': regions.loc[i, 'geometry'], 'contains': [], 'region_names': regions.loc[i, name_columns].dropna().tolist()}  for i in regions.index]

    for region in tqdm(output): 
        region_geometry = region['geometry']
        for j in in_country_gdf.index: 
            geometry = in_country_gdf.loc[j, 'geometry'] 
            if geometry.within(region_geometry): 
                subregion_names =[str(i) for i in in_country_gdf.loc[j, name_columns].dropna().tolist()]
                region['contains'].append({'names': subregion_names, 'geometry': geometry})
                region['region_names'] += subregion_names

    codebook = []

    for region in tqdm(output): 
        for name in region['region_names']:
            codebook.append({"Phrase": name, 
                                "Salience" : 1, 
                                'Sal2Dash': 1, 
                                'Topic/Type': 'Location', 
                                'Named Entity': '', 
                                'Sentiment': 0, 
                                'Source': '',
                                'Locality': 2, 
                                'Meta': '', 
                                'narrative_region': region['code']})

    codebook = pd.DataFrame(codebook) 
    codebook = codebook.drop_duplicates(subset = ['Phrase'])
    return codebook 

    


    


