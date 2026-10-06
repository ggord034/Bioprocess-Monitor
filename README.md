#Bioprocess Monitor for a Fermentation Process
The corresponding file exports figures and tables for the purpose of visualizing data obtained during a fermentation process and stored in a .csv file. 

##Overview
The objective was to produce a python code that takes data from a .csv file and generates plots showing pH, dissolved oxygen, temperature, and concentration as a function of time. Two modes were to be analyzed, each with different defined acceptable ranges to indicate the importance of the data. 

##Features
The custom BioprocessMonitor class reads a .csv dataset and then extracts individual batches and sorts entries by time. It identifies the pH and temperature values that are within limits and then exports a dashboard showing product concentrations, temperature, pH, and dissolved oxygen as functions of time. It then outputs the generated results in their corresponding folders. 

##Technologies Used
- PyCharm IDE
- Python 3.14
- Libraries:
  - Pandas 3.0.5
  - Matplotlib 3.11.0
  - pathlib (included in Python 3.14)

##Code Design
Running main.py generates two sets of limits: mode A has pH limits of 4.8 to 5.6, and temperature limits of 34.0 - 36.0 C. Mode B has limits of 5.1 - 5.5 and 34.5 - 35.5 C for pH and temperature, respectively. It extracts data for all five batches using pandas, then compares values to the limits. It generates a dashboard for each batch, analyzed using the limits from both modes A and B, end exports them to the figures file. After processing the batches, it exports a summary of the amount of values within spec for each batch to the tables file. 

##Dashboard Example
<img width="2340" height="1620" alt="image" src="https://github.com/user-attachments/assets/fff78fe0-529f-428a-a8d5-98574eba6373" />
The attached dashboard shows a summary from batch 1, analyzed under mode A's limits. The upper left hand panel shows concentration profiles over time, the lower left hand panel shows pH over time, the upper right hand panel shows the temperature profile, and the final panel is a plot of dissolved oxygen over time. Since limits were generated using mode A, they are very generous, and almost all data points for pH and temperature are within range (as shown by the green dots and red X's)

##Summary Table
  |batch_id|ph_optimal_percent|temperature_optimal_percent|C_product_g_L^-1_final|
|--------|------------------|---------------------------|----------------------|
|1       |93.81             |97.94                      |46.5                  |
|2       |96.69             |97.52                      |50.8                  |
|3       |95.89             |93.15                      |44.6                  |
|4       |100.0             |96.47                      |48.6                  |
|5       |48.62             |99.08                      |24.7                  |

The summary table shows the percentages of recorded measurements that are within specification for a given mode. The attached example is the summary table generated for mode A. Each row corresponds to a different batch ( 1 through 5). The first two columns indicate the percentage of data points that were within the provided limits for pH and temperature. The final column indicates the amount of product produced by that batch. 

