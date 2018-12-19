import sys
import logging

from configure import sources
from gleanomatic import ESLoader as el

def esIngest(sourceNamespace,setNamespace):
    try:
        sourceConfig = sources[sourceNamespace]
        setConfig = sourceConfig['sets'][setNamespace]
    except AttributeError:
        raise ValueError("No config found for given namespaces")
    esLoader = el.ESLoader(sourceNamespace,setNamespace,setConfig)
    esLoader.run()
    return esLoader.getSummary()
    

if __name__ == "__main__":
    sourceID = sys.argv[1]
    if not "/" in sourceID:
        print("USAGE: esIngest.py {sourceNamespace}/{setNamespace}\n")
        raise Exception("Incorrect identifier format")
    parts = sourceID.split("/")
    sourceNamespace = parts[0]
    setNamespace = parts[1]
    result = esIngest(sourceNamespace,setNamespace)
    logging.info(result)
    

