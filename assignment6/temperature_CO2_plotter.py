import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['figure.figsize'] = (15, 5)

co2_stats = pd.read_csv('data/co2.csv', sep=',') # Read co2 data
temp_stats = pd.read_csv('data/temperature.csv', sep=',') # Read temperature data
co2_country_stats = pd.read_csv("data/CO2_by_country.csv", sep=',') # Read CO2 per country data

def plot_CO2(startyear=1751, endyear=2012, ymin=None, ymax=None, showplot=False):
    """Function that plots CO2-amount against time.

    The years to be plotted can be specified - if they are not the whole data-set
    will be plotted (1751-2012). The user can also put restrictions on the
    y-axis by specifying ymin and ymax, where ymin < ymax is required.
    Data is gathered from data/co2.csv

    Args:
        startyear (int): The year at which the plot starts, i.e. xmin. Defaults to 1751.
        endyear (int): The year at wchich the plot ends, i.e. xmax. Defaults to 2012.
        ymin (float): Lowest value of CO2 to be plotted. Defaults to None.
        ymax (float): Highest value of CO2 to be plotted. Defaults to None.
        showplot (bool): Decides whether plot will be shown before function returns.
            Defaults to False

    Returns:
        class 'matplotlib.axes._subplots.AxesSubplot': A matplotlib plot.
    """
    startindex = startyear - 1751 # First row from the table to be plotted
    endindex = endyear - 1751 # Last row from the table to be plotted

    plt.close("all") # Close all pre-existing open matplotlib.pyplot figures to avoid clutter.
    plot = co2_stats[startindex:endindex].plot(x='Year', y='Carbon') # Plotting co2 emissions from startyear to endyear
    plot.set_title("Amount of CO2 from " + str(startyear) + " to " + str(endyear)) # Make descriptive title
    plot.set_ylabel("CO2-emissions/million tons") # Set y-label

    if (ymin != None): # If user has specified y-axis restrictions, apply these to plot
        if ymin < ymax: 
            plt.axis([startyear, endyear, ymin, ymax]) # Specify axis restrictions
        else:
            print("\nERROR with input arguments:")
            print("When specifying y-axis restrictions, ymin has to be lower than ymax.")
            print("Your input was: ymin =", ymin, ", ymax =",ymax)
            return

    if showplot: plt.show() # Show plot
    return plot


def plot_temperature(months, startyear=1816, endyear=2012, ymin=None, ymax=None, showplot=False):
    """Function that plots temperature against time.

    Data is gathered from data/temperature.csv

    Args:
        months (str or list): Specific months can be specified so only data from the
            selected months will show. The argument can be either a string (for a single
            month) or a list of strings (for multiple months). The name of the months have
            to be written in full, with capital first letter. Ex: ['January', 'February'].
        startyear (int): The year at which the plot starts, i.e. xmin. Defaults to 1816.
        endyear (int): The year at which the plot ends, i.e. xmax. Defaults to 2012.
        ymin (float): Lowest value of CO2 to be plotted. Defaults to None.
        ymax (float): Highest value of CO2 to be plotted. Defaults to None.
        showplot (bool): Decides whether plot will be shown before function returns. Defaults to False.

    Returns:
        class 'matplotlib.axes._subplots.AxesSubplot': A matplotlib plot.
    """
    startindex = startyear-1816
    endindex = endyear-1816
    plt.close("all") # Close all pre-existing open matplotlib.pyplot figures to avoid clutter.

    if (startyear < endyear): 
        if isinstance(months, str) or isinstance(months, list): # Month(s) is specified
            plot = temp_stats[startindex:endindex].plot(x='Year', y=months) # Plot temperature for specified month(s) and years

            # Make meaningful title for the plot
            if isinstance(months, str):
                plot.set_title("Temperature in " + str(months) + " from " + str(startyear) + " to " + str(endyear))
            else:
                all_the_months = months[-2] + " and " + months[-1]
                i = len(months)-3 # Counter
                while (i >= 0):
                    all_the_months = months[i] + ", " + all_the_months # Add remaining months in list
                    i=i-1 # Count down
                title = "Temperatures in " + all_the_months + " from " + str(startyear) + " to " + str(endyear)
                plot.set_title(title)

            # If user has specified y-axis restrictions, apply these to plot
            if (ymin != None) and (ymax != None):
                if ymin < ymax: # This has to be true
                    plt.axis([startyear, endyear, ymin, ymax]) # Specify axis restrictions
                else:
                    print("\nERROR with input arguments:")
                    print("When specifying y-axis restrictions, ymin has to be lower than ymax.")
                    print("Your input was: ymin =", ymin, ", ymax =",ymax)
                    return

            plot.set_ylabel("Temperature/Degrees Celcius") # Label the y-axis

        else: #No month was specified. 
            # Idea: To show meaningful data plot average temp per year ?? 
            print("\nERROR with input arguments.")
            print("The month(s) to plot was not specified, or was not a string or a list of strings.")
            print("Include this as the first parameter when calling on the function.")
            print("Your input was: " + str(months) + ".\n")
            return

    else:
        # IDEA: Plot temperature for all months in specified year ??
        print("\nERROR with input arguments. Startyear cannot be less than or equal to endyear.\n")
        return

    if showplot: plt.show() # Show plot
    return plot



def plot_CO2_by_country(startyear, endyear, lower=None, upper=None, showplot=False):
    """Function that generates a bar chart of the CO2 emissions of all countries within a set threshold.

    The function will make a bar-chart of the CO2-emissions of all countries with
    emissions within a user-specified interval (set by the parameters lower and upper).
    The user has to specify the time-period which is to be shown in the graph.
    This is done by specifying the startyear and endyear parameters. A time-period
    that extends over 16 years or more is not recommended, as the graph will not
    look nice.

    Args:
        startyear (int): The first year to be graphed in the bar chart.
        endyear (int): The last year to be graphed in the bar chart.
        lower: The lower theshold.
        upper: The upper theshold.
        showplot (bool): Decides if bar-chart will be shown before function returns.

    Returns:
        chart (class 'matplotlib.axes._subplots.AxesSubplot'): A bar chart.
    """
    plt.close("all") # Close all pre-existing open matplotlib.pyplot figures to avoid clutter.
    years = []
    for num in range(startyear, endyear+1): years.append(str(num)) # List of years to be plotted

    # Function to check whether emission values are within given theshold
    def find_correct_values(array):
        noval=0
        for x in array:
            if (x < lower) or (x > upper):
                return False
            elif np.isnan(x):
                noval+=1
        if noval >= len(array):
            return False
        return True # All values were within threshold

    #Return a boolean-array that tells which countries have emissions within given threshold
    valid_countries = np.apply_along_axis(find_correct_values, axis=1, arr=co2_country_stats.as_matrix(years))

    countries = np.where(valid_countries)[0] # Find the indices in the valid_countries that are True
    data = co2_country_stats[['Country Code']+years].iloc[countries] # This is the data we need to graph
    chart = data.plot(x='Country Code', kind='bar') # Make bar-chart
    title = "Countries emitting between " + str(lower) + " and " + str(upper) + " million tons CO2 from " + str(startyear) + " to " + str(endyear) # Make descriptice title
    chart.set_title(title)
    chart.set_ylabel("CO2 emissions per country") # Label the y-axis
    if showplot: plt.show() # Show graph
    return chart

    

    


#TESTING:
#plot_CO2()
#plot_CO2(1950, 2000, 0, 5000, showplot=True)
#plot_CO2(1950, 2000, 350, 350) #Returns error

#plot_temperature(['January', 'February', 'March', 'April'], 1950, 2000, showplot=True)
#plot_temperature('August', 1950, 2000, showplot=True)
#plot_temperature('May', 2000, 2000) #Returns error
#plot_temperature(12, 2000, 2001) #Returns error

#plot_CO2_by_country(2011, 2013, 22.8, 100, showplot=True)
