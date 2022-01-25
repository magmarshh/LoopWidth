# LoopWidth
Python package that produces piecharts and violin plots for visualizing chromatin loop widths from any file in paired bed format. 

## LoopWidth_piechart
Creates a piechart showing loop width distribution in any [matplotlib](https://matplotlib.org/2.1.2/api/_as_gen/matplotlib.pyplot.savefig.html)-accepted format. 

### Requirements
- python >=  3.7 
- pandas
- matplotlib


###  Usage

```{bash echo=FALSE}
python LoopWidth_piechart.py  --loop <bedpe file> --bins <user-defined bin widths>  --res <bedpe resolution> --output <path to output piechart>
```
### Parameters
- --loop: **REQUIRED** loop file in bedpe format (see [bedtools documentation](https://bedtools.readthedocs.io/en/latest/content/general-usage.html) for more information), *with* a header row. 
-  --bins: **OPTIONAL** string of comma-separated user-defined resolution bins for loop widths to be binned into. Will also be used as the labels for the piechart. The ranges must start with one coordinate (ex. 1Mb) followed by a range (ex. 1Mb-4Mb), ending with one coordinate (4Mb+) with a '+' symbol at the end of the last coordinate. The coordinates may be in basepair format or Kb/Mb format (i.e 10000 or 10Kb). The first coordinate will be interpreted as "less than or equal to", and the last coordinate will be interpreted as "greater than". See example below for more information regarding the accepted format. 
-  --res: **OPTIONAL** integer input of loop file resolution. Must be **10000, 25000, 50000, or 100000**. Pre-defined bins according to the resolution will be used, if different bins are preferred use the `--bins` argument. 
-  --output: **REQUIRED** file path to outputted piechart in any matplotlib accepted format (see [matplotlib picture formats](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html) for more information)

**NOTE: Either `--bins` or `--res` argument MUST be supplied, if both are supplied then the res argument will take precedence, as the allowed values for `--res` have predefined default bin values. The `--bins` argument should be used if the default bins for the resolution are not suitable to the data, or the data is in a different resolution.**


### Examples: 
```{bash echo=FALSE}
python LoopWidth_piechart.py  --loop Examples/test_loop_file.bedpe --bins 1Mb,1Mb-3Mb,3Mb-6Mb,6Mb+ --output Examples/piechart_bins_example.png
```
```{bash echo=FALSE}
python LoopWidth_piechart.py  --loop Examples/test_loop_file.bedpe --res 100000 --output Examples/piechart_res_example.png
```
## LoopWidth_violinplot
Creates a violin plot and outputs the log2(width) mean and median for bedpe file(s).

### Requirements
- python >=  3.7 
- pandas
- matplotlib
- seaborn
- statistics

###  Usage

```{bash echo=FALSE}
python LoopWidth_violinplot.py --loop <bedpe file(s)> --labels <plot label(s)> --figWidth <figure width> --figHeight <figure height> --output <path to violinplot output>

```
### Parameters
- --loop: **REQUIRED** loop file(s) in bedpe format (see [bedtools documentation](https://bedtools.readthedocs.io/en/latest/content/general-usage.html) for more information), with a header row. If multiple loop files are to be plotted on the same plot, enter loop file paths separated by commas. 
- --labels: **REQUIRED** labels for violin plot(s) corresponding to the order given in the `loop` parameter. If multiple, separate with commas. 
- --output: **REQUIRED** file path to outputted violin plot in any matplotlib accepted format (see [matplotlib picture formats](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html) for more info)
- --figWidth: **OPTIONAL** figure width in integer format. Default is 7. 
- --figHeight: **OPTIONAL** figure height in integer format. Default is 7. 

### Examples: 
```{bash echo=FALSE}
python LoopWidth_violinplot.py --loop Examples/test_loop_file.bedpe,Examples/test_loop_file2.bedpe --labels test1,test2 --output Examples/violin_plot_multiple_files_example.png
```

  **Output:**
    
   Mean Log2(width) for  Examples/test_loop_file.bedpe is:  21.782055367961732
   
   Median Log2(width) for  Examples/test_loop_file.bedpe is:  22.05248866110651
   
   Mean Log2(width) for  Examples/test_loop_file2.bedpe is:  22.51408577126218
   
   Median Log2(width) for  Examples/test_loop_file2.bedpe is:  22.620867729860066

```{bash echo=FALSE}
python LoopWidth_violinplot.py --loop Examples/test_loop_file.bedpe --labels test1 --output Examples/violin_plot_one_file_example.png --figWidth 6 --figHeight 4
```
 
 **Output:**
    
   Mean Log2(width) for  Examples/test_loop_file.bedpe is:  21.782055367961732
   
   Median Log2(width) for  Examples/test_loop_file.bedpe is:  22.05248866110651
    





