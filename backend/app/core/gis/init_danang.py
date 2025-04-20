# backend/app/core/gis/init_danang.py
import geopandas as gpd
from sqlalchemy import create_engine

def init_gis_data():
    engine = create_engine(os.getenv('DATABASE_URL'))
    
    # Load Đà Nẵng GIS data
    districts = gpd.read_file('/data/gis/danang_districts.geojson')
    flood_zones = gpd.read_file('/data/gis/danang_flood_zones.geojson')
    
    # Save to PostGIS
    districts.to_postgis('danang_districts', engine, if_exists='replace')
    flood_zones.to_postgis('danang_flood_zones', engine, if_exists='replace')
