# How To Use

Takes a text file, filters out the password, checks how complex.

Expect to have to adjust the parsing.

`python password_checker.py file1 file2 file3`

Uses the delimiter `:` unless specified with `--dl`

`python password_checker.py file1 --dl '|'`

Output will be the lines which have 3/4 or 4/4 complexity parameters.