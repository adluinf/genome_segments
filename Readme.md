# Genome Segments Readme

## What does it do ?

This program uses input data about segments and functions on the genome to
compute: overlap between segments, the correlation between functions or the
average of a function on certain segments.

## Where to put data ?

The default location for data is in "../data/". You can also use a folder of your choice and specify it when you run the program.

## How to run it ?

This is a python program and can be run from the command line (for example in
bash or another shell) using:
```
  python main.py
```
You will then be asked to enter the file path to the data, and select the data
files that you wish to use.

## Dependencies

- numpy

## Implementation choices

The current implementation uses methods from the *numpy* packages for the Pearson correlation
coefficient and file reading because these are highly efficient. 
Therefore numpy needs to be installed.

---

Tested with python 3.8.5.

