# Data Files - personal_info.csv
#              vehicles.csv
#              employemnt.csv
#              update_status.csv
             
# Each file contains key that uniquely identifies each row - SSN 
# YOU ARE GURanteed that every SSN number
# -> appears only once in every file.
# -> is present in all 4 files.
# -> the order of SSN in each file is the same.

# Goal !
# Create (lazy) iterators for each of the four files.
# -> returns named tuples.
# -> data types are appropriate (string, date, int, etc)
# -> the 4 integers are independent of each other (for now)
Goal 2
Create a single iterable that combines all the data from all four files.
-> try to re-use tyhe iterators you created in Goal1.
-> by combining I mean one row per SSNcontaining data from all four files in a single named tuple.

Goal 3
Some records are stale (not updated recently enough) (stale < 3/1//2017)

Goal 4
for non-stale records generate lists of numbers of car makes by gender.







