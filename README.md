# h1b_statistics
##  Insight Data Engineering Code Challenge   

This challenge is to implement two metrics:

Top 10 job titles with corresponding number of certified applications and their percentages.    
Top 10 states with corresponding number of certified applications and their percentages.    

To execute the programs, please execute run.sh as an executable. The output of the programs can be found under OUTPUT founder.  
The main functions are written in python, see ./src/h1b_counting.py.    

Workflow of the code:

1. Import the raw data and the headers;        
2. Iterate through all records while counting the number of certified applications for each job title(SOC code) and state, saving in their corresponding dictionary;        
3. Sort the dictionaries accordingly;      
4. Write the result to corresponding text files.    

