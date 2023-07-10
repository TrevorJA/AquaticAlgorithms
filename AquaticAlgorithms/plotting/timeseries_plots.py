"""
Contains functions used to make different plots for timeseries data.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cm as cm
import numpy as np

def plot_streamflow_by_year(df, log_scale=False, 
                            save_fig=False, save_name='streamflow_by_year.png'):
    
    # Create a new column for the year
    df['Year'] = df.index.year
    
    # Calculate the total streamflow for each year
    df['Total_Streamflow'] = df.groupby('Year')['streamflow'].transform('sum')

    # Sort the dataframe by the total streamflow
    df.sort_values('Total_Streamflow', inplace=True)

    # Create a colormap to map each year to a color based on its total streamflow
    colormap = cm.get_cmap('viridis')
    colors = colormap(np.linspace(0, 1, df['Year'].nunique()))

    # Create a new figure
    fig, ax = plt.subplots()

    # Plot the streamflow for each year
    for i, year in enumerate(df['Year'].unique()):
        df_year = df[df['Year'] == year]
        ax.plot(df_year.index.dayofyear, df_year['streamflow'], color=colors[i], label=year)

    # Set the y-axis to a log scale if specified
    if log_scale:
        ax.set_yscale('log')

    # Set the x-axis to show only the month
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))

    # Add a legend
    ax.legend()

    # Save the figure if specified
    if save_fig:
        plt.savefig(save_name)

    # Show the plot
    plt.show()
    return
