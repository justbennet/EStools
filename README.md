The EStools module is self-contained in the EStools.py file.  They leave
a lot to be desired, and only very basic functionality is represented.

These are meant to be run in the ARC-TS environment at the University
of Michigan. They assume that the Elasticsearch Python libraries are
installed and available in your `PYTHONPATH`.

On the Great Lakes cluster, 

Functions available so far

    es_info()
        Prints information about the ES server.

    get_syslog_index_names(clustername)
        Returns a list of syslog index names for the clustername given as an
        argument.

Examples of using the tools in EStools can be found in test.py


