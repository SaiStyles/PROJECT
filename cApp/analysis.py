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
warnings.filterwarnings('ignore')

# Define the base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load shapefile using Geopandas
shp_gdf = gpd.read_file(f'{BASE_DIR}/dataset/INDIA/Indian_states.shp')

# List files in the dataset directory
for dirname, _, filenames in os.walk(f'{BASE_DIR}/dataset'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# Read the datasets
victims = pd.read_csv(f'{BASE_DIR}/dataset/20_Victims_of_rape.csv')
murder = pd.read_csv(f'{BASE_DIR}/dataset/32_Murder_victim_age_sex.csv')
police_hr = pd.read_csv(f'{BASE_DIR}/dataset/35_Human_rights_violation_by_police.csv')
auto_theft = pd.read_csv(f'{BASE_DIR}/dataset/30_Auto_theft.csv')
prop_theft = pd.read_csv(f'{BASE_DIR}/dataset/10_Property_stolen_and_recovered.csv')




def main_rape():
    rape_victims = victims[victims['Subgroup'] == 'Victims of Incest Rape']

    total_rape_cases = pd.DataFrame(rape_victims.groupby(['Year'])['Rape_Cases_Reported'].sum().reset_index())

    total_rape_cases_state = pd.DataFrame(rape_victims.groupby(['Area_Name'])['Rape_Cases_Reported'].sum().reset_index())

    fig = px.bar(total_rape_cases, x='Year', y='Rape_Cases_Reported', color_discrete_sequence=['blue'])
    fig.update_traces(text=total_rape_cases['Rape_Cases_Reported'], textposition='outside')

    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    fig1 = f"{BASE_DIR}/static/media/FILES/victims/bar{current_time}.png"
    fig.write_image(fig1)

    total_rape_cases_state.columns = ['State/UT', 'Cases Reported']
    merge = shp_gdf.set_index('st_nm').join(total_rape_cases_state.set_index('State/UT'))

    fig, ax = plt.subplots(1, figsize=(10, 10))
    ax.set_title('State-wise Rape-Cases Reported (2001-2010)', fontdict={'fontsize': 15, 'fontweight': '3'})
    merge.plot(column='Cases Reported', cmap='Reds', linewidth=0.5, ax=ax, edgecolor='0.2', legend=True)

    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    fig2 = f"{BASE_DIR}/static/media/FILES/victims/{current_time}.png"
    plt.savefig(fig2)

    above_50 = rape_victims['Victims_Above_50_Yrs'].sum()
    ten_to_14 = rape_victims['Victims_Between_10-14_Yrs'].sum()
    fourteen_to_18 = rape_victims['Victims_Between_14-18_Yrs'].sum()
    eighteen_to_30 = rape_victims['Victims_Between_18-30_Yrs'].sum()
    thirty_to_50 = rape_victims['Victims_Between_30-50_Yrs'].sum()
    upto_10 = rape_victims['Victims_Upto_10_Yrs'].sum()

    age_grp = ['Upto 10','10 to 14','14 to 18','18 to 30','30 to 50','Above 50']
    age_group_vals = [upto_10,ten_to_14,fourteen_to_18,eighteen_to_30,thirty_to_50,above_50]

    fig, ax = plt.subplots()
    ax.pie(age_group_vals, labels=age_grp, autopct='%1.1f%%')
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    fig3 = f"{BASE_DIR}/static/media/FILES/victims/pie{current_time}.png"
    plt.title("Age wise victims @ India")
    plt.savefig(fig3)
    return fig1, fig2, fig3




def for_state_rape(state = 'Kerala'):
    rape_victims = victims[victims['Subgroup'] == 'Victims of Incest Rape']
    rape_victims = rape_victims[victims['Area_Name'] == state]
    total_rape_cases = pd.DataFrame(rape_victims.groupby(['Year'])['Rape_Cases_Reported'].sum().reset_index())
    print(total_rape_cases)

    total_rape_cases.columns=['Year',f'Cases Reported @ {state}']
    fig = px.bar(total_rape_cases, x='Year', y=f'Cases Reported @ {state}', color_discrete_sequence=['blue'])
    fig.update_traces(text=total_rape_cases[f'Cases Reported @ {state}'], textposition='outside')
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    fig_state1 = f"{BASE_DIR}/static/media/FILES/victims/bar_single{current_time}.png"
    fig.write_image(fig_state1)

    above_50 = rape_victims['Victims_Above_50_Yrs'].sum()
    ten_to_14 = rape_victims['Victims_Between_10-14_Yrs'].sum()
    fourteen_to_18 = rape_victims['Victims_Between_14-18_Yrs'].sum()
    eighteen_to_30 = rape_victims['Victims_Between_18-30_Yrs'].sum()
    thirty_to_50 = rape_victims['Victims_Between_30-50_Yrs'].sum()
    upto_10 = rape_victims['Victims_Upto_10_Yrs'].sum()

    age_grp = ['Upto 10','10 to 14','14 to 18','18 to 30','30 to 50','Above 50']
    age_group_vals = [upto_10,ten_to_14,fourteen_to_18,eighteen_to_30,thirty_to_50,above_50]

    fig, ax = plt.subplots()
    ax.pie(age_group_vals, labels=age_grp, autopct='%1.1f%%')
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    fig_state2 = f"{BASE_DIR}/static/media/FILES/victims/pie_single{current_time}.png"
    plt.title(f"Age wise victims @ {state}")
    plt.savefig(fig_state2)
    return fig_state1, fig_state2


def main_murder():

    total_murder_cases = pd.DataFrame(murder.groupby(['Year'])['Victims_Total'].sum().reset_index())

    total_murder_cases_state = pd.DataFrame(murder.groupby(['Area_Name'])['Victims_Total'].sum().reset_index())

    fig = px.bar(total_murder_cases, x='Year', y='Victims_Total', color_discrete_sequence=['purple'])
    fig.update_traces(text=total_murder_cases['Victims_Total'], textposition='outside')

    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    fig1 = f"{BASE_DIR}/static/media/FILES/murder/bar{current_time}.png"
    fig.write_image(fig1)

    total_murder_cases_state.columns = ['State/UT', 'Cases Reported']
    merge = shp_gdf.set_index('st_nm').join(total_murder_cases_state.set_index('State/UT'))

    fig, ax = plt.subplots(1, figsize=(10, 10))
    ax.set_title('State-wise Murder-Cases Reported (2001-2010)', fontdict={'fontsize': 15, 'fontweight': '3'})
    merge.plot(column='Cases Reported', cmap='RdPu', linewidth=0.5, ax=ax, edgecolor='0.2', legend=True)
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    fig2 = f"{BASE_DIR}/static/media/FILES/murder/{current_time}.png"
    plt.savefig(fig2)

    above_50 = murder['Victims_Above_50_Yrs'].sum()
    ten_to_14 = murder['Victims_Upto_10_15_Yrs'].sum()
    fifteen_to_18 = murder['Victims_Upto_15_18_Yrs'].sum()
    eighteen_to_30 = murder['Victims_Upto_18_30_Yrs'].sum()
    thirty_to_50 = murder['Victims_Upto_30_50_Yrs'].sum()
    upto_10 = murder['Victims_Upto_10_Yrs'].sum()

    age_grp = ['Upto 10','10 to 15','15 to 18','18 to 30','30 to 50','Above 50']
    age_group_vals = [upto_10,ten_to_14,fifteen_to_18,eighteen_to_30,thirty_to_50,above_50]

    fig, ax = plt.subplots()
    ax.pie(age_group_vals, labels=age_grp, autopct='%1.1f%%')
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    fig3 = f"{BASE_DIR}/static/media/FILES/murder/pie{current_time}.png"
    plt.title("Age wise victims @ India")
    plt.savefig(fig3)

    total_murder_cases_male = pd.DataFrame(murder.groupby(['Sub_Group_Name'])['Victims_Total'].sum().reset_index())
    total_murder_cases_male.columns=['Genders','Victims_Total']
    fig = px.bar(total_murder_cases_male, x='Genders', y='Victims_Total', color_discrete_sequence=['purple'])
    fig.update_traces(text=total_murder_cases_male['Victims_Total'], textposition='outside')
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    fig4 = f"{BASE_DIR}/static/media/FILES/murder/bar_gender{current_time}.png"
    fig.write_image(fig4)
    print(total_murder_cases_male)
    return fig1, fig2, fig3, fig4




def for_state_murder(state = 'Kerala'):
    total_murder_cases = murder[murder['Area_Name'] == state]
    total_murder_cases = pd.DataFrame(total_murder_cases.groupby(['Year'])['Victims_Total'].sum().reset_index())
    print(total_murder_cases)

    total_murder_cases.columns=['Year',f'Cases Reported @ {state}']
    fig = px.bar(total_murder_cases, x='Year', y=f'Cases Reported @ {state}', color_discrete_sequence=['purple'])
    fig.update_traces(text=total_murder_cases[f'Cases Reported @ {state}'], textposition='outside')

    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    fig_state1 = f"{BASE_DIR}/static/media/FILES/murder/bar{current_time}.png"
    fig.write_image(fig_state1)

    total_murder_cases_new = murder[murder['Area_Name'] == state]
    above_50 = total_murder_cases_new['Victims_Above_50_Yrs'].sum()
    ten_to_14 = total_murder_cases_new['Victims_Upto_10_15_Yrs'].sum()
    fifteen_to_18 = total_murder_cases_new['Victims_Upto_15_18_Yrs'].sum()
    eighteen_to_30 = total_murder_cases_new['Victims_Upto_18_30_Yrs'].sum()
    thirty_to_50 = total_murder_cases_new['Victims_Upto_30_50_Yrs'].sum()
    upto_10 = total_murder_cases_new['Victims_Upto_10_Yrs'].sum()

    age_grp = ['Upto 10','10 to 15','15 to 18','18 to 30','30 to 50','Above 50']
    age_group_vals = [upto_10,ten_to_14,fifteen_to_18,eighteen_to_30,thirty_to_50,above_50]

    fig, ax = plt.subplots()
    ax.pie(age_group_vals, labels=age_grp, autopct='%1.1f%%')
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    fig_state2 = f"{BASE_DIR}/static/media/FILES/murder/pie{current_time}.png"
    plt.title(f"Age wise victims @ {state}")
    plt.savefig(fig_state2)

    total_murder_for_gender = murder[murder['Area_Name'] == state]
    total_murder_cases_male = pd.DataFrame(total_murder_for_gender.groupby(['Sub_Group_Name'])['Victims_Total'].sum().reset_index())
    total_murder_cases_male.columns=['Genders',f'Victims_Total @ {state}']
    fig = px.bar(total_murder_cases_male, x='Genders', y=f'Victims_Total @ {state}', color_discrete_sequence=['purple'])
    fig.update_traces(text=total_murder_cases_male[f'Victims_Total @ {state}'], textposition='outside')
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    fig_state3 = f"{BASE_DIR}/static/media/FILES/murder/bar_gender{current_time}.png"
    fig.write_image(fig_state3)
    print(total_murder_cases_male)
    return fig_state1, fig_state2, fig_state3


def main_police_hr():
    total_cases = pd.DataFrame(police_hr.groupby(['Year'])['Cases_Registered_under_Human_Rights_Violations'].sum().reset_index())
    total_cases_state = pd.DataFrame(police_hr.groupby(['Area_Name'])['Cases_Registered_under_Human_Rights_Violations'].sum().reset_index())
    print(total_cases)
    print(total_cases_state)
    fig = px.bar(total_cases, x='Year', y='Cases_Registered_under_Human_Rights_Violations', color_discrete_sequence=['green'])
    fig.update_traces(text=total_cases['Cases_Registered_under_Human_Rights_Violations'], textposition='outside')
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    fig1 = f"{BASE_DIR}/static/media/FILES/police_hr/bar{current_time}.png"
    fig.write_image(fig1)

    total_cases_state.columns = ['State/UT', 'Cases Reported']
    merge = shp_gdf.set_index('st_nm').join(total_cases_state.set_index('State/UT'))

    fig, ax = plt.subplots(1, figsize=(15, 15))
    ax.set_title('State-wise Human Rights Violations Reported (2001-2010)', fontdict={'fontsize': 15, 'fontweight': '3'})
    merge.plot(column='Cases Reported', cmap='Greens', linewidth=0.5, ax=ax, edgecolor='0.2', legend=True)
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    fig2 = f"{BASE_DIR}/static/media/FILES/police_hr/{current_time}.png"
    plt.savefig(fig2)

    new_police_hr = police_hr[police_hr['Sub_Group_Name'] != '12. Total (Sum of 1-11 Above)']
    total_cases_cat = pd.DataFrame(new_police_hr.groupby(['Sub_Group_Name'])['Cases_Registered_under_Human_Rights_Violations'].sum().reset_index())
    print(total_cases_cat)
    fig = px.bar(total_cases_cat, x='Sub_Group_Name', y='Cases_Registered_under_Human_Rights_Violations', color_discrete_sequence=['green'])
    fig.update_traces(text=total_cases_cat['Cases_Registered_under_Human_Rights_Violations'], textposition='outside')
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    fig3 = f"{BASE_DIR}/static/media/FILES/police_hr/bar_cat{current_time}.png"
    fig.write_image(fig3)
    return fig1, fig2, fig3

def for_state_police(state = 'Kerala'):
    total_cases = police_hr[police_hr['Area_Name'] == state]
    total_cases = pd.DataFrame(total_cases.groupby(['Year'])['Cases_Registered_under_Human_Rights_Violations'].sum().reset_index())
    print(total_cases)
    total_cases.columns=['Year',f'Cases Reported @ {state}']
    fig = px.bar(total_cases, x='Year', y=f'Cases Reported @ {state}', color_discrete_sequence=['green'])
    fig.update_traces(text=total_cases[f'Cases Reported @ {state}'], textposition='outside')
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    fig_state1 = f"{BASE_DIR}/static/media/FILES/police_hr/bar{current_time}.png"
    fig.write_image(fig_state1)

    total_cases_new = police_hr[police_hr['Area_Name'] == state]
    print(total_cases_new)
    total_cases_new = pd.DataFrame(total_cases_new.groupby(['Sub_Group_Name'])['Cases_Registered_under_Human_Rights_Violations'].sum().reset_index())
    new_police_hr = total_cases_new[total_cases_new['Sub_Group_Name'] != '12. Total (Sum of 1-11 Above)']
    new_police_hr.columns=['Sub_Group_Name',f'Cases Reported @ {state}']
    total_cases_cat = pd.DataFrame(new_police_hr.groupby(['Sub_Group_Name'])[f'Cases Reported @ {state}'].sum().reset_index())
    fig = px.bar(total_cases_cat, x='Sub_Group_Name', y=f'Cases Reported @ {state}', color_discrete_sequence=['green'])
    fig.update_traces(text=total_cases_cat[f'Cases Reported @ {state}'], textposition='outside')
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    fig_state2 = f"{BASE_DIR}/static/media/FILES/police_hr/bar_cat{current_time}.png"
    fig.write_image(fig_state2)
    return fig_state1, fig_state2

