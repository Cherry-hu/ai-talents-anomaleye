# ai-talents-anomaleye
 ANOMALeye is a product used for anti-money laundering. It can analyze bank transaction data, record the user's mouse movement, combine user feedback and a skilled human decision-making processes to noticebaly reduce the false positive rate.
 
 For the data analytics approach,once the transaction data is collected, do the following:
 1. Select the ones where counterparty countries are highly involved in money laundering
 2. Select the ones with an amount larger than 15000
 3. Drop the duplicates
 
 Prerequisites:
 
 install pandas
 
 install jupyterlab(optional)
 
 For mouse movement data, once the mouse movement is recorded, do the following:
 1. Use 3 coordinates to adjust the data set: X, Y, waiting time
 2. Create a heatmap
 
 Prerequisites:
 
 install pandas
 
 install matplotlib
 
 install seaborn
 
 install jupyterlab
 
 The heat map can only be displayed in jupyter notebook, so please execute the command first to open jupyterlab:
 
 $ jupyter-lab
 
 
 
