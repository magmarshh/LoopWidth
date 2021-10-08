#!/usr/local/bin/python3.9

"""
Executable python script that will take in however many loop files and plot them
onto a violin plot to be compared or just one.
"""

import pandas
import seaborn as sns
import argparse
from math import log2
import statistics
import matplotlib.pyplot as plt

'''
Function to parse the loop dataframe and obtain all of the loop widths 
to be plotted in a violin plot
'''


def get_loop_widths(loop_df):
    # list to contain log-transformed loop_widths
    plotting_loop_widths = []
    # iterate through the loop_df loops
    for index, row in loop_df.iterrows():
        # calculate the loop_width
        loop_width = loop_df['y1'][index] - loop_df['x1'][index]
        # log transform the loop_widths for better visualization
        # if they aren't 0 then add it to the loop_width list
        if loop_width != 0:
            plotting_loop_widths.append(log2(loop_width))
        # if it is 0 then add 1 to the loop width b/c cannot take log of 0
        else:
            plotting_loop_widths.append(log2(loop_width + 1))

    return plotting_loop_widths


def main():
    # Create the parser
    parser = argparse.ArgumentParser(usage="Python script to create a violin plot showing loop width distribution.")
    # Add an argument
    parser.add_argument('--loop', type=str, required=True, help="REQUIRED: Path to the loop file(s) in bedpe format "
                                                                "(https://bedtools.readthedocs.io/en/latest/content/general-usage.html) "
                                                                " with a header line. If more than one loop file is to be plotted, "
                                                                "enter in the loop_files separated by commas.")
    parser.add_argument('--labels', type=str, required=True, help="REQUIRED: string of x-axis labels for the violin plots. If"
                                                                  "more than one loop file is to be plotted, enter in the "
                                                                  "labels in comma-separated format.")
    parser.add_argument('--output', type=str, required=True, help="REQUIRED: Path for output violin plot. Only in matplotlib accepted picture format.")
    parser.add_argument('--figWidth', type=int, required=False, help="OPTIONAL: integer for output figure width. Default is 7.")
    parser.add_argument('--figHeight', type=int, required=False,
                        help="OPTIONAL: integer for output figure height. Default is 7.")

    # Parse the argument
    args = parser.parse_args()
    # split the files by commas
    files = args.loop.split(',')
    # split the labels by commas
    labels_split = args.labels.split(',')
    # create empty list to add the loop widths onto for that file
    combined_data_to_plot = []
    if len(files) != len(labels_split):
        raise argparse.ArgumentTypeError("Error. Number of loop files does not equal number of labels.")
    else:
        # iterate through all the loop files given
        for file in files:
            # read in the loop file into a pandas dataframe
            loop_df = pandas.read_csv(file,
                                  skiprows=1,
                                  usecols=[0, 1, 2, 3, 4, 5],
                                  names=['chr1', 'x1', 'x2', 'chr2', 'y1', 'y2'],
                                  delimiter='\t')
            # get the log-transformed loop_widths of the loop file
            plotting_loop_widths = get_loop_widths(loop_df)
            # Print out the mean and median of the log2(width) for the specific file
            print(" Mean Log2(width) for ", file, "is: ", statistics.mean(plotting_loop_widths))
            print(" Median Log2(width) for ", file, "is: ", statistics.median(plotting_loop_widths))
            # append the list of loop_widths onto the combined_data_to_plot list for plotting
            combined_data_to_plot.append(plotting_loop_widths)
        sns.set()
        if args.figWidth is not None:
            if args.figHeight is not None:
                fig, axes = plt.subplots(figsize=(args.figWidth, args.figHeight))
            else:
                fig, axes = plt.subplots(figsize=(args.figWidth, 7))
        elif args.figHeight is not None:
            if args.figWidth is None:
                fig, axes = plt.subplots(figsize=(7, args.figHeight))
        else:
            fig, axes = plt.subplots(figsize=(7, 7))
        sns.set(style="whitegrid")
        # get list for axes
        axis_ticks = list(range(1, len(files) + 1))
        # set the x axis ticks
        axes.set_xticks(axis_ticks)
        axes.set_ylabel('log2(Loop Width)')
        ax = sns.violinplot(data=combined_data_to_plot, ax=axes, orient='v', inner='box')
        # set the x axis tick labels
        ax.set_xticklabels(labels_split)
        # Save figure
        fig.savefig(args.output)




if __name__ == "__main__":
    main()







