Sales Data Cleaner

1. Project Title & Goal

Sales Data Cleaner :- This project reads a messy sales CSV file, cleans the data, removes duplicate entries, converts prices from USD to INR, 
                      and saves the final clean data into a JSON file.

2. Setup Instructions Requirements

--> Python 3 installed on your system

   Make sure the following files are in the same folder:

   --> sales.csv
   --> sales_cleaner.py
   --> Open a terminal or command prompt in that folder.
   --> Run the script using:
       "python sales_cleaner.py"

   After running the script, a file named clean_sales.json will be created containing the cleaned data.

3. The Logic (How I Thought)
   Why did I choose this approach?

   I used a simple, step-by-step approach using core Python concepts like file handling, loops, lists, sets, and dictionaries. Since the dataset was small and the task focused on data cleaning logic, this approach kept the code easy to understand, debug, and explain without using external libraries.

   What was the hardest bug you faced, and how did you fix it?

   The main issue I faced was an IndexError while reading and splitting rows from the CSV file. Some rows did not split into the expected number of columns, which caused the program to crash when accessing list indexes.

   To fix this, I added a check to skip empty or malformed rows before processing them. This made the script more stable and prevented it from failing when the input data was not perfectly formatted.

4. Output Screenshots

   ![Clean Sales Output](sales_clean_output.png)


5. Future Improvements

   If I had two more days, I would:
   --> Use Python’s built-in csv module to handle CSV parsing more reliably.
   --> Add proper error handling for invalid numeric values.
   --> Make the currency conversion rate configurable instead of hardcoded.



