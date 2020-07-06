# reindent
Packaged Tools/scripts/reindent from cpython

reindent [-d][-r][-v] [ path ... ]

-d (--dryrun)   Dry run.   Analyze, but don't make any changes to, files.
-r (--recurse)  Recurse.   Search for all .py files in subdirectories too.
-n (--nobackup) No backup. Does not make a ".bak" file before reindenting.
-v (--verbose)  Verbose.   Print informative msgs; else no output.
   (--newline)  Newline.   Specify the newline character to use (CRLF, LF).
                           Default is the same as the original file.
-h (--help)     Help.      Print this usage information and exit.

Change Python (.py) files to use 4-space indents and no hard tab characters.
Also trim excess spaces and tabs from ends of lines, and remove empty lines
at the end of files.  Also ensure the last line ends with a newline.

If no paths are given on the command line, reindent operates as a filter,
reading a single source file from standard input and writing the transformed
source to standard output.  In this case, the -d, -r and -v flags are
ignored.

You can pass one or more file and/or directory paths.  When a directory
path, all .py files within the directory will be examined, and, if the -r
option is given, likewise recursively for subdirectories.

If output is not to standard output, reindent overwrites files in place,
renaming the originals with a .bak extension.  If it finds nothing to
change, the file is left alone.  If reindent does change a file, the changed
file is a fixed-point for future runs (i.e., running reindent on the
resulting .py file won't change it again).

The hard part of reindenting is figuring out what to do with comment
lines.  So long as the input files get a clean bill of health from
tabnanny.py, reindent should do a good job.

The backup file is a copy of the one that is being reindented. The ".bak"
file is generated with shutil.copy(), but some corner cases regarding
user/group and permissions could leave the backup file more readable than
you'd prefer. You can always use the --nobackup option to prevent this.
