import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    #import data as csv
    rawDF = pd.read_csv("./data/APP-103 SEDI Data.csv")

    #create a new empty dataframe with the same columns but no/empty rows
    sampledDF = rawDF.iloc[:0].copy()

    #loop for each column in the raw data
    for idx in range(len(rawDF.columns)):
        #read the current column into a series called "col"
        col = rawDF.iloc[:,idx]
        #create a new column by sampling "col" 100 times, with replacement
        newCol = col.sample(n=100, replace=True).reset_index(drop=True)
        #assign new column to the corresponding column in the new dataframe
        sampledDF.iloc[:,idx] = newCol

    #in the code below, section 1 will generate a graph of the averages of the sampled data, while
    #section 2 will generate a graph of ALL the sampled data points. comment out/uncomment whichever
    #section is needed before running

    #SECTION 1: plotting averages of sampled data

    avgDF = rawDF.iloc[:0].copy()

    listOfAvgs = []

    for idx in range(len(rawDF.columns)):
        col = rawDF.iloc[:,idx]
        avg = col.mean()
        listOfAvgs.append(avg)

    avgDF.loc[len(avgDF)] = listOfAvgs

    print(avgDF)

    finalDF = avgDF.transpose()

    finalDF.plot(legend=False, xlabel="Time (s)", ylim=[44,44.4], ylabel="Time of Flight (ToF) (μS)")
    plt.show()

    fig = finalDF.plot(legend=False, xlabel="Time (s)", ylim=[44,44.4], ylabel="Time of Flight (ToF) (μS)").get_figure()
    fig.savefig("avg_line_graph.png")

    #SECTION 2: plotting ALL sampled data

    #this line is included because my original data had the time intervals as the first row and all the values for
    #ToF as all the other rows. when using .plot, pandas automatically uses the first column as the x-axis, so
    #i transposed my data to take advantage of this. if the data is already organized such that the first column
    #is your x-values and the rest of the columns are your y-values, this line is not needed
    #finalDF = sampledDF.transpose()

    #plot the data
    #finalDF.plot(legend=False, title="Time of Flight (ToF) at 1.5cm Over Time: Randomly Sampled Data", xlabel="Time (s)", ylabel="Time of Flight (ToF) (μS)")
    #plt.show()

    #save the plot as a png
    #fig = finalDF.plot(legend=False, title="Time of Flight (ToF) at 1.5cm Over Time: Randomly Sampled Data", xlabel="Time (s)", ylabel="Time of Flight (ToF) (μS)").get_figure()
    #fig.savefig("sampled_line_graph.png")