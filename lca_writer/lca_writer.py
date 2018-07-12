import os
import shutil
import pandas as pd


class LCAWriter():
    """
    A class capable of loading form data and writing and LCA file.

    Parameters:
        path : str
            Path to the form.
    """
    def __init__(self, path):
        self.path = path
        self.load_data(path)

    @staticmethod
    def load_case_converters():
        """Returns a list of value conversion functions for load case data."""
        wind_ice_model = {
            'Wind on All' : 0,
            'Wind on Face' : 2
        }

        pole_defl_check = {
            'No Limit' : 0
        }

        converters = {
            'wind_ice_model' : lambda x: wind_ice_model[x],
            'pole_defl_check' : lambda x: pole_defl_check[x]
        }

        return converters

    @staticmethod
    def save_template(path):
        """
        Saves a copy of the Excel template form to the specified path.

        Parameters:
            path : str
                Path to which form will be saved.
        """
        from . import data
        p = os.path.join(data.DATA_FOLDER, 'lca_form.xlsx')
        shutil.copy(p, path)

    def load_data(self, path):
        """
        Loads the data at the specified path and assigns it to the object.

        Parameters:
            path : str
                The location of the form.
        """
        # Load sheets
        load_cases = pd.read_excel(path, sheet_name = 'Load Cases',
                                   header = 1, converters = self.load_case_converters(),
                                   dtype = {'point_loads' : object, 'joint_displs' : object})
        point_loads = pd.read_excel(path, sheet_name = 'Point Loads', header = 1)
        joint_displs = pd.read_excel(path, sheet_name = 'Joint Displacements', header = 1)

        # Fill in blank data
        x = 'comment'
        point_loads[x] = point_loads[x].fillna('')
        joint_displs[x] = joint_displs[x].fillna('')

        x = ['trans_force', 'long_force', 'vert_force']
        point_loads[x] = point_loads[x].fillna(0)

        x = ['x_displ', 'y_displ', 'z_displ', 'x_rot', 'y_rot', 'z_rot']
        joint_displs[x] = joint_displs[x].fillna(0)

        # Filter point load and joint displacements
        for i, lc in load_cases.iterrows():
            load_cases.at[i, 'point_loads'] = point_loads[(point_loads['point_label'] != '')
                                                          & point_loads['load_case'].isin(['', lc['name']])]
            load_cases.at[i, 'joint_displs'] = joint_displs[(joint_displs['point_label'] != '')
                                                            & joint_displs['load_case'].isin(['', lc['name']])]
        self.load_cases = load_cases

    def lca_12_2(self):
        """Returns an LCA file version 12.2 string."""
        num_load_points = max(lc.point_loads.shape[0] for _, lc in self.load_cases.iterrows())

        s = ["TYPE='LCA FILE' VERSION='12.2' UNITS='US' SOURCE='Tower Version 14.40' USER='' FILENAME=''",
             '{} ; num_load_cases'.format(self.load_cases.shape[0]),
             '{} ; num_load_points'.format(num_load_points),
             '1 1 1 1 1 32.8084 0 0.000000 1 0 1 1 0 0 1 0 0 1.600000 0 0 1 0.000000 32808.398950']

        for _, lc in self.load_cases.iterrows():
            s += ['{name}'.format(**lc),
                  '0 ; include insulator wind/weight',
                  '{steel_sf} {wood_sf} {conc_ult_sf} {conc_first_crack_sf} {conc_zero_tens_sf} {guy_sf} {arm_sf} {brace_sf} {insl_sf} {found_sf} ; Strength factors: steel, wood, ult. conc, first conc, zero conc, guy, arm, brace, insulator, foundation'.format(**lc),
                  '{dead_load_factor} ; Structure weight load factor'.format(**lc),
                  '{trans_wind_pressure} {long_wind_pressure} {wind_ice_model} ; Factored structure transverse and longitudinal wind pressures'.format(**lc),
                  '{wind_area_factor} {ice_thickness} {ice_density} {pole_defl_check} {temperature} {pole_defl_limit}'.format(**lc)]

            i = 0
            for _, p in lc['point_loads'].iterrows():
                s += ["{point_label}".format(**p),
                      "{vert_force} {trans_force} {long_force} '{comment}' ; V T and L loads including insul weight".format(**p)]
                i += 1

            while i < num_load_points:
                s += ["''",
                      "0 0 0 '' ; V T and L loads including insul weight"]
                i += 1

            s += ['{}'.format(lc['joint_displs'].shape[0])]

            for _, d in lc['joint_displs'].iterrows():
                s += ["'{point_label}' {x_displ} {y_displ} {z_displ} {x_rot} {y_rot} {z_rot} '{comment}'".format(**d)]

        return '\r\n'.join(s)

    def write_lca(self, path = None, version = '12.2'):
        """
        Writes and LCA file of the specified version to the path.

        Parameters:
            path : str
                Path to the form.
            version : str
                The version of the LCA file to be written.
        """
        if path == None:
            path = self.path[:-5] + '.lca'

        method = getattr(self, 'lca_' + version.replace('.', '_'))
        s = method()

        with open(path, 'wt') as file:
            file.truncate()
            file.write(s)
