# Covid Vaccine Patient List
This is a Python program that sorts a patient list where a patient with highest priority can get the vaccine first.

## Project Specification

The priority number of a patient is given by a rating system based on different factors such as their job, age group, underlying medical condition, and more. Each patient is assigned a number between 1 to 10, where 10 means highest priority and 1 means lowest priority. This program prints out a patient list based on their priority number where a patient with highest priority will be on top of the list, and this is where priority queue comes in handy.

Two different input files are given, `priority.txt` and `patient_info.txt`. There are two columns in the `'priority.txt'` file, which are ***Priority*** and ***Patient ID***. On the other hand, the `'patient_info.txt'` file contains 3 columns, which are ***Patient ID***, ***Full Name***, and ***Contact Number***.

This program performs the following tasks to obtain the final list:

1. Read each row from the given input file `priority.txt`, then store all the data in a max-priority queue. The priority queue is implemented using a linked list. While setting this up, the ***Priority*** is used as key and ***Patient ID*** is used as value for the priority queue. 
2. Read each row from the second input file `patient_info.txt` and store all the information in another linked list. Here, the ***Patient ID*** is used as key. 
3. After all data structures are ready, start taking each entry (high priority to low priority) from the max-priority queue that was created in Step 1. Get the ***Patient ID*** and use it to search in the other linked list, then print out the patient's information. 

>No data or values should be hardcoded except file names.

## Sample Output

![Screen Shot 2022-05-26 at 1 41 26 PM](https://user-images.githubusercontent.com/105037989/170544870-afab1fbb-14a2-41e6-a0cd-60675e9f4def.png)
