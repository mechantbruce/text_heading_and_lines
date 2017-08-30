# text_heading_and_lines
will process a text file and look for a specific heading line, print that, and also print some specific lines following it.

In this specific use, I read a file containing the output from a WLC "show run-config". I then look for any line containing an AP name, and print the AP name followed by that APs primary/secondary/tertiary WLC configuration. This information appears twice in the "show run-config" so it is printed twice by my program.
