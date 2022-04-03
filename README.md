# ACME_compensation_system

## Installation Instructions
### Previous Requirements
The local machine has to have Python 3 installed. No other dependencies are necessary to execute the core of the app (txt_processor.py). However, to execute the testing program, the pytest module has to be installed (i.e. via ```pip```).  

### Up & Running
1. Download the repo either as .zip compressed file (and decompress afterwards) or clone it into your local computer.
2. Open up a terminal and ```cd``` into the [ACME_compensation_system](https://github.com/aa-rodriguezv/ACME_compensation_system/) folder.
3. Execute ```python txt_processor.py```. By default the app processes the [test.txt](test.txt) you can find in the same folder of the repo. But, it is resilient enough to process other files that can be find in the local system, what you would need to do, in order to execute such behavior, is run ```python txt_processor.py [PATH_TO_FILE]``` where PATH_TO_FILE is the absolute path to the file that needs to be processed.   

## Developing Process
This section describes the path followed to solve the problem. 

### Step by Step
#### Designing the API
The [hourly_compensation_API.py](API) focuses on the core processing to solve the problem. Goes as far as calculate the compensation for each worker.

1. First step was finding out a way to store the values for compensation. A Dictionary was the structure chosen, because of the ease of access. In order to summarize, the compensation was divided into **'WEEKDAY'**, for Monday through Friday, and **'WEEKEND'** for Saturday and Sunday. Each value is another dictionary, that includes the first hour of the intervals (**'00', '09', '18'**). The values for those keys correspond to the dollars that need to be paid for that interval in that type of day.
2. Second, was finding out a way to access the Dictionary, based on the values that can be received as input.
  - To know the type of day, and taking advantage of how the days of the week are named (in English), it is a simple check. If the first letter of the day starts with **'S'** we know it must be a day of the **'WEEKEND'**, otherwise it must be a **'WEEKDAY'**.    
  - To find out the interval, the process is a little more complicated. First we need to split the timeframe and check for hours and minutes. If the hour number is greater than 18, is equal to 18 and the minutes are greater than 0 or both the hour number and the minutes are equal to 0 the timeframe is **'18'**. If the hour does not fall in any of the previouse cases, it checks if the hour is greater than 9 or is equal to 9 and minutes are greater than 0, so the interval would be **'09'**. Any other case, the timeframe is **'00'**.
3. After knowing the type of day and hour interval, what is left is to calculate the compensation. For this, the time difference of each interval registered by the worker needs to be multiplied by the price for that timeframe. To calculate the difference I first divide the minutes by 60, then add them to each hour, to then calculate the difference as the ```second_hour_plus_minutes - first_hour_plus_minutes```.
4. Lastly, the total compensation for each worker needs to be calculated. This is just a loop, after splitting the data by commas to sum every compensation for each interval registry.

#### Processing the File
The [txt_processor.py](File Processor) is the final point of access for the user to solve the problem based on a file that can be either passed as a parameter or they can use the [test.txt](test) file that comes with the repo. This program focuses on processing the file and uses the API to process each line in the file.

1. The processor determines if there were any other arguments added for the execution, if so, it processes the file passed as an argument, if not it uses the default file.
2. It reads the file and splits the data by new lines.
3. For each line read the processor uses the API and prints the result.

### Testing

### Design Considerations

## Results

### Going Beyond

### Known Limitations
