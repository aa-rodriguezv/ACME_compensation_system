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

1. First step was finding out a way to store the values for compensation. A Dictionary was the structure chosen, because of the ease of access. In order to summarize, the compensation was divided into **'WEEKDAY'**, for Monday through Friday, and **'WEEKEND'** for Saturday and Sunday. Each value is another dictionary, that includes the first hour of the intervals (**'00', '09', ''18**). The values for those keys correspond to the dollars that need to be paid for that interval in that type of day.

### Testing

### Design Considerations

## Results

### Going Beyond

### Known Limitations
