The EStools module is self-contained in the EStools.py file.  They leave
a lot to be desired, and only very basic functionality is represented.

Functions available so far

    es_info()
        Prints information about the ES server.

    get_syslog_index_names(clustername)
        Returns a list of syslog index names for the clustername given as an
        argument.

Examples of using the tools in EStools can be found in test.py

You need to

    $ module purge
    $ module load python3.7-anaconda/2020.02
    $ export PYTHONPATH=/sw/arcts/centos7/EStools/lib/python3.7/site-packages
    $ export PYTHONPATH=$PYTHONPATH:/sw/arcts/centos7/EStools/examples
    $ python3 /sw/arcts/centos7/EStools/examples/test.py
