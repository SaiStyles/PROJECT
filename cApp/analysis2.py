import numpy as np
import pandas as pd
import os
from pathlib import Path
import geopandas as gpd
import matplotlib.pyplot as plt
import warnings
from plotly.offline import plot, iplot
import plotly.express as px
from datetime import datetime
import random

warnings.filterwarnings('ignore')

# Define the base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load shapefile using Geopandas
shp_gdf = gpd.read_file(f'{BASE_DIR}/dataset/INDIA/Indian_states.shp')


# Read the datasets
crimes_file = pd.read_csv(f'{BASE_DIR}/dataset/Crimes.csv')

in_colors = ['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Grays', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_grey', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gist_yerg', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'grey', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 'winter_r']
bar_colors = ["aliceblue","antiquewhite","aqua","aquamarine","azure","beige","bisque","black","blanchedalmond","blue","blueviolet","brown","burlywood","cadetblue","chartreuse","chocolate","coral","cornflowerblue","cornsilk","crimson","cyan","darkblue","darkcyan","darkgoldenrod","darkgray","darkgrey","darkgreen","darkkhaki","darkmagenta","darkolivegreen","darkorange","darkorchid","darkred","darksalmon","darkseagreen","darkslateblue","darkslategray","darkslategrey","darkturquoise","darkviolet","deeppink","deepskyblue","dimgray","dimgrey","dodgerblue","firebrick","floralwhite","forestgreen","fuchsia","gainsboro","ghostwhite","gold","goldenrod","gray","grey","green","greenyellow","honeydew","hotpink","indianred","indigo","ivory","khaki","lavender","lavenderblush","lawngreen","lemonchiffon","lightblue","lightcoral","lightcyan","lightgoldenrodyellow","lightgray","lightgrey","lightgreen","lightpink","lightsalmon","lightseagreen","lightskyblue","lightslategray","lightslategrey","lightsteelblue","lightyellow","lime","limegreen","linen","magenta","maroon","mediumaquamarine","mediumblue","mediumorchid","mediumpurple","mediumseagreen","mediumslateblue","mediumspringgreen","mediumturquoise","mediumvioletred","midnightblue","mintcream","mistyrose","moccasin","navajowhite","navy","oldlace","olive","olivedrab","orange","orangered","orchid","palegoldenrod","palegreen","paleturquoise","palevioletred","papayawhip","peachpuff","peru","pink","plum","powderblue","purple","red","rosybrown","royalblue","rebeccapurple","saddlebrown","salmon","sandybrown","seagreen","seashell","sienna","silver","skyblue","slateblue","slategray","slategrey","snow","springgreen","steelblue","tan","teal","thistle","tomato","turquoise","violet","wheat","white","whitesmoke","yellow","yellowgreen"]

def main(crime_selected):
    crime = crimes_file[crimes_file['DISTRICT'] == 'TOTAL']
    print(crime)
    # crime.loc[crime.STATE.str.isupper(), 'STATE'] = crime.STATE.str.title()
    total_murder_cases = pd.DataFrame(crime.groupby(['YEAR'])[crime_selected].sum().reset_index())
    print(total_murder_cases)
    total_murder_cases_state = pd.DataFrame(crime.groupby(['STATE'])[crime_selected].sum().reset_index())
    print(total_murder_cases_state)

    col1 = random.choice(bar_colors)
    fig = px.bar(total_murder_cases, x='YEAR', y=crime_selected, color_discrete_sequence=[col1])
    fig.update_traces(text=total_murder_cases[crime_selected], textposition='outside')
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    fig1 = f"{BASE_DIR}/static/media/FILES/bar{current_time}.png"
    fig.write_image(fig1)

    total_murder_cases_state.columns = ['STATE', crime_selected]
    merge = shp_gdf.set_index('st_nm').join(total_murder_cases_state.set_index('STATE'))
    fig, ax = plt.subplots(1, figsize=(10, 10))
    ax.set_title(f'State-wise {crime_selected} Cases Reported (2001-2013)', fontdict={'fontsize': 15, 'fontweight': '3'})
    col2 = random.choice(in_colors)
    merge.plot(column=crime_selected, cmap=col2, linewidth=0.5, ax=ax, edgecolor='0.2', legend=True)
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    fig2 = f"{BASE_DIR}/static/media/FILES/{current_time}.png"
    plt.savefig(fig2)

    return fig1, fig2 

def state_main(crime_selected,state):
    crime = crimes_file[crimes_file['DISTRICT'] == 'TOTAL']
    print("==========================================================")
    print(crime)
    print("==========================================================")
    crime = crimes_file[crimes_file['STATE'] == state]
    print("==========================================================")
    print(crime)
    print("==========================================================")
    total_murder_cases = pd.DataFrame(crime.groupby(['YEAR'])[crime_selected].sum().reset_index())
    print(total_murder_cases)
    total_murder_cases_state = pd.DataFrame(crime.groupby(['STATE'])[crime_selected].sum().reset_index())
    print(total_murder_cases_state)

    col1 = random.choice(bar_colors)
    fig = px.bar(total_murder_cases, x='YEAR', y=crime_selected, color_discrete_sequence=[col1])
    fig.update_traces(text=total_murder_cases[crime_selected], textposition='outside')
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    fig1 = f"{BASE_DIR}/static/media/FILES/bar{current_time}.png"
    fig.write_image(fig1)

    return fig1



# main("KIDNAPPING & ABDUCTION")