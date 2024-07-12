import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

import math

# 1
df = pd.read_csv('medical_examination.csv')
#print(df)

# 2
df['bmi'] = df['weight']/(df['height']/100)**2
df.loc[df['bmi'] >25, 'overweight'] = 1
df.loc[df['bmi'] <= 25, 'overweight'] = 0
#print(df.columns.values.tolist())

# 3
# Normalize
df.loc[df['cholesterol'] == 1, 'cholesterol'] = 0
df.loc[df['cholesterol'] > 1, 'cholesterol'] = 1

df.loc[df['gluc'] == 1, 'gluc'] = 0
df.loc[df['gluc'] > 1, 'gluc'] = 1
#print(df)

#print(df.columns)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars = ['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 6
    # should be summed by variables in catplot what, see above

    # 7
    # variable x axis, hue would be the count for variables, we are faceting with cardio with col
    fig = sns.catplot(data=df_cat, kind="count",  x="variable",hue="value", col="cardio").set_axis_labels("Variable", "Total")

    
    # 8
    #ig = fig.figure

    # 9
    fig.savefig('catplot.png')
    #print(df_cat)
    print(df)
    plt.show()
    return fig
draw_cat_plot()


# 10 
def draw_heat_map():
    # 11, Filter based on diastolic pressure being higher than systolic
    height_l = df['height'].quantile(0.025)
    height_h = df['height'].quantile(0.975)
    weight_l = df['weight'].quantile(0.025)
    weight_h = df['weight'].quantile(0.975)
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & 
                  (df['height'] >= height_l) & (df['height'] <= height_h) &
                  (df['weight'] >= weight_l) & (df['weight'] <= weight_h)]


    # 12
    corr = df_heat.corr()

    #13
    mask = np.triu(corr, k = 0)

    #14
    plt.figure(figsize =(15, 15))

    #15
    heat = sns.heatmap(corr, mask = mask, annot = True, cmap = sns.color_palette("viridis", as_cmap=True), center = 0)
    plt.yticks(rotation = 0)
    plt.title = ('Medical Data Correlation')
    plt.show()
    plt.savefig("heat.png")
    #print(df_heat)
    return heat
draw_heat_map()



