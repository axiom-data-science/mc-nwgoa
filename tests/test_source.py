
import model_catalogs as mc
import intake


def test_attrs():
    """Check that cf-xarray works with all axes/coords."""
    
    ds = mc.transform_source(intake.cat.nwgoa).to_dask()
    
    axes = {'X': ['xi_psi', 'xi_rho', 'xi_u', 'xi_v'],
            'Y': ['eta_psi', 'eta_rho', 'eta_u', 'eta_v'],
            'Z': ['s_rho', 's_w'],
            'T': ['ocean_time']}
    
    assert ds.cf.axes == axes
    
    coords = {'longitude': ['lon_rho'],
              'latitude': ['lat_rho'],
              'vertical': ['s_rho', 's_w'],
              'time': ['ocean_time']}

    assert ds.cf.coordinates == ds.cf.coordinates
    
    std_names = {'surface_eastward_sea_water_velocity': ['Uwind_eastward'],
                 'surface_northward_sea_water_velocity': ['Vwind_northward'],
                 'sea_ice_area_fraction': ['aice'],
                 'sea_ice_thickness': ['hice'],
                 'ocean_s_coordinate_g2': ['s_rho', 's_w'],
                 'sea_water_practical_salinity': ['salt'],
                 'surface_snow_thickness': ['snow_thick'],
                 'sea_water_potential_temperature': ['temp'],
                 'eastward_sea_ice_velocity': ['uice_eastward'],
                 'sea_water_x_velocity': ['u_eastward'],
                 'sea_water_y_velocity': ['v_northward'],
                 'northward_sea_ice_velocity': ['vice_northward'],
                 'upward_sea_water_velocity': ['w'],
                 'water_surface_height_above_reference_datum': ['zeta']}
    
    assert ds.cf.standard_names == std_names
    
    ds.close()