import sys
import logging

from configure import sources
from gleanomatic import Transformer as tr

def transform(sourceNamespace,setNamespace,transformType,mode='latest'):
    try:
        sourceConfig = sources[sourceNamespace]
        setConfig = sourceConfig['sets'][setNamespace]
        transformConfig = setConfig['transforms'][transformType]
    except AttributeError:
        raise ValueError("No config found for given namespaces")
    transformer = tr.Transformer(sourceNamespace,setNamespace,transformConfig,mode)
    result = transformer.run()
    return result
    

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("USAGE: transform.py {sourceNamespace}/{setNamespace} {transformName} {mode ['latest'|'all']}\n")
        exit()
    sourceID = sys.argv[1]
    transformType = sys.argv[2]
    mode = sys.argv[3]
    parts = sourceID.split("/")
    sourceNamespace = parts[0]
    setNamespace = parts[1]
    result = transform(sourceNamespace,setNamespace,transformType,mode)
    logging.info(result)
    

