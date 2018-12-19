import sys
import logging

from configure import sources
from gleanomatic import ListLoader as ll

def listIngest(sourceNamespace,setNamespace):
    try:
        sourceConfig = sources[sourceNamespace]
        setConfig = sourceConfig['sets'][setNamespace]
    except AttributeError:
        raise ValueError("No config found for given namespaces")
    listLoader = ll.ListLoader(sourceNamespace,setNamespace,setConfig)
    listLoader.run()
    return listLoader.getSummary()
    

if __name__ == "__main__":
    sourceID = sys.argv[1]
    if not "/" in sourceID:
        print("USAGE: listIngest.py {sourceNamespace}/{setNamespace}\n")
        raise Exception("Incorrect identifier format")
    parts = sourceID.split("/")
    sourceNamespace = parts[0]
    setNamespace = parts[1]
    result = listIngest(sourceNamespace,setNamespace)
    logging.info(result)
    

