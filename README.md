## Citation Manager

A little QT app that allows one to keep track of citations. It will live render markdown (without MathJax).

### Requirements

- markdown2
- PyQt4

### Usage

One can run the GUI in by running `python main.py` inside the `GUI/` directory.

Open a new JSON file using "Ctrl+O", and save new JSON and HTML files using "Ctrl+S". Seperate menu options exist for each of these actions.

Double click elements in the left most column to edit the associated note.

### Known Bugs

- If trying to select the first element in the left most column, one cannot click on the first half of the element -- it simply doesn't select. 

