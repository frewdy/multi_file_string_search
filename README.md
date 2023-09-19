# multi_file_string_search

The purpose of this code was to solve a problem that I was experiencing at work. In aerospace engineering, finite element modeling is used for the complex analysis of various systems and subsystems. One of the programs used on my team is NASTRAN. Typical NASTRAN files are text files that contain the input data for CAE simulation software. They are formatted under “NASTRAN format."

In order to have a full engineering model that can be analyzed for static and dynamic loads, an "include" file is utilized that references other files with relevant information such as geometry, temperature defintion, grid/node definition, etc. When making changes to a model of that scale (100+ GB for a jet engine!), however, it becomes critical to be able to locate items of interest quickly so that changes can be made easily or problems can be diagnosed.

This is not the original code that I wrote as my original code contained proprietary information and was written for a Windows ecosystem (this version was adapted for MacOS) but it effectively accomplishes the same thing.

When ran, the code asks for a string (let's say we input 12345) and the name of an output file (let's say we input results.txt). I supplied dummy folders and dummy files. With the string of interest inputted, the code uses the include file, searches it for filepaths by using the information after the 'INCLUDE' buzzword, stores those filepaths in an array, and iterates through them. It opens each of these files and searches for that initial input string. It then outputs the file paths where that string was located and the lines in which it was present into the results.txt file that was created.
