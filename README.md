# Geocoding

Borrowed from:

https://towardsdatascience.com/how-to-build-your-geocoding-web-app-with-python-133e1e9e2d1a


* Geocoding tutorial in Python. If you want to expiriment the Jupyter notebook of this article, you can use Launch Binder below.
    [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/shakasom/geocoding/master)

    This code includes the "Pandas" thing that ran on Streamlit.  Had to 
    change the name to "runningpandas.py" because of import conflicts with other files.

    Also has the "chunk" method for geocoding.  This breaks up the input file into 10 reqests at a time.

    To geocode:

    1.  Run chunks.py.  This sets up the directory structure and creates the small files.  They are loaded into an input directory.  The input file is hard coded as is the chuck size of 10.

    2.  Run process_chunks.py - this reads each chunk file and attempts to geocode it.  It writes the current file being coded to the current directory and deletes it from the input.  The output is found in the "output" file.

         THis code encounters timeout exceptions that terminate the program at the moment.  Simply restart process_chunks.py.  It begins with the next file in the input.  The bad file remains in the current directory.  If a file successfully processes, it is deleted from the current directory.  At the end of the run all bad files are in the current directory.  Nothing is done with themn at the moment.
    3.  Run append_chunks.py - This puts all the files back together.  There are 4 output files:

         a.  "found" those that are geocoded.
         b.  "no found" those that are not geocoded
         c.  "bad files" those that caused the program to terminate and were left in the current dictory
         d    "geocoded" - the found and not found together.    



* Reverse Geocoding 
  [Google Colab Notebook](https://github.com/shakasom/geocoding/blob/master/ReverseGeocoding.ipynb)

* Streamlit application.
  https://share.streamlit.io/marilynwaldman/streamlit_geocoding/main/pandas.py

  upload csv file durango_addresses.csv

  to run locally - git clone, cd to streamlit_geocoding, then run

  ```
  streamlit run pandas.py

  ```

