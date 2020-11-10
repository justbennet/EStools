-- local variables to be used inside the module file
local installDir   = "/sw/arcts/centos7/EStools"
local app          = "EStools"

depends_on('python3.7-anaconda/2020.02')

local helpMsg = [[

    EStools is a small Python library for querying ARCTS Elasticsearch.  It is
    meant to be an example so far, not a fully fledged collection of functions
    for reporting.

]]
help(helpMsg)

-- general system variables
prepend_path('PYTHONPATH',  pathJoin(installDir, 'lib/python3.7/site-packages'))
prepend_path('PYTHONPATH',  pathJoin(installDir, 'examples'))
