# Project modalities

This project will be realized individually, in the language of your choice : Java, Python, or JS.

# Subject

Implement a project that monitors directories and processes all files found in this directories.

A lots of files are produced in this directory : CSV files containing temperature measure for a given sensor.

The file name follows this structure <Sensor_Id>/<YYYYMMDDmmssSSS>.tgz

The files contain lines with this structure : timestamp,temperature,humidity

ex : 20210305142905126,11.2,84.1

The program has to : 

- periodically launch threads to scan for each input directory, 
- process in a dedicated thread each file found in the directory for populating a database 
- move the processed files to another directory
- periodically realize a zip with the processed files to archive them
- delete the file once zipped in archive

# Output

The expected deliverable is a Git repo or a zip of your source code, with all your source files, and your slides.

Due date is 06/06/2022 at 00:00:00.

Send the URL of the Git repo or the zip by Mootse or by mail to your teacher : remy.girodon@gmail.com