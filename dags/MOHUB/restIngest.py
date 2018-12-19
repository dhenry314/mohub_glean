import sys
import logging

from configure import sources
from gleanomatic import RESTLoader as rl

def restIngest(sourceNamespace,setNamespace):
    try:
        sourceConfig = sources[sourceNamespace]
        setConfig = sourceConfig['sets'][setNamespace]
    except AttributeError:
        raise ValueError("No config found for given namespaces")
    restLoader = rl.RESTLoader(sourceNamespace,setNamespace,setConfig)
    restLoader.run()
    return restLoader.getSummary()
    

if __name__ == "__main__":
    sourceID = sys.argv[1]
    if not "/" in sourceID:
        print("USAGE: restIngest.py {sourceNamespace}/{setNamespace}\n")
        raise Exception("Incorrect identifier format")
    parts = sourceID.split("/")
    sourceNamespace = parts[0]
    setNamespace = parts[1]
    result = restIngest(sourceNamespace,setNamespace)
    logging.info(result)
    

