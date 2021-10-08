# LoopWidth
Calculating and visualizing loop widths from paired bed file

## LoopWidth_piechart
Creates a piechart in any matplotlib-accepted format of loop width distributions. 

### Requirements
- pandas
- matplotlib
- >= python 3.7 


###  Usage

```{bash echo=FALSE}
python LoopWidth_piechart.py  --loop <bedpe file> --bins <user-defined bin widths>  --res <bedpe resolution> --output <path to output piechart>
```
### Parameters
- --loop: **REQUIRED** loop file in bedpe format (see [bedtools documentation](https://bedtools.readthedocs.io/en/latest/content/general-usage.html) for more information), with a header row. 
-  --bins: **OPTIONAL** string of user-defined resolution bins for loop widths to be binned into. Will also be used as the labels for the piechart. The ranges must start with one coordinate (ex. 1Mb) followed by a range (ex. 1Mb-4Mb), ending with one coordinate (4Mb+) with a '+' symbol at the end of the last coordinate. The coordinates may be in basepair format or Kb/Mb format, but mmust use 





