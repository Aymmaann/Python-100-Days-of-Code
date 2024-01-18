# Mail Merge 

## Overview
This Python project demonstrates basic file manipulation for mail merge purposes. The code reads a starting letter template from the "starting_letter.txt" file and replaces the placeholder "[name]" with names from the "name.txt" file. It generates individualized letters for each name and saves them in the "Output/ReadyToSend/" folder.

## Project Structure
The project is organized as follows:
- `main.py`: The main Python script containing the code for mail merging.
- `Input/`: A folder containing input files.
  - `Letter/`: Subfolder containing the starting letter template file (`starting_letter.txt`).
  - `Names/`: Subfolder containing the list of names file (`name.txt`).
- `Output/`: A folder containing output files.
  - `ReadyToSend/`: Subfolder where the generated letters are saved.

## How to Run
1. Clone or download the project to your local machine.
2. Navigate to the project directory.
3. Run the main script.
``` bash
python main.py
```

## Example File Paths
- Starting Letter Template: Input/Letter/starting_letter.txt
- List of Names: Input/Names/name.txt
- Output Folder: Output/ReadyToSend/

## Important Note
Ensure that the folder structure remains intact for the code to work correctly. The code uses relative paths, so running it from the project directory is crucial.

Feel free to modify the template, add more features, or adapt the code for your specific needs.

*Enjoy exploring Python file manipulation with this project!*