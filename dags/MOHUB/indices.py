mohub = 
{
  "mappings": {
    "_doc": {
      "dynamic": false,
      "properties": {
            "isShownAt": {"type":"keyword"},
            "dataProvider": {"type":"keyword"},
            "hasView": {
				"type":"object",
				"properties": {
				   "@id": {"type":"keyword"}
				}
			},
			"object": {"type":"keyword"},
			"sourceResource": {
			    "type":"object",
			    "properties": {
				    "title": {"type":"keyword"},
				    "description": {"type":"keyword"},
				    "rights": {"type":"keyword"},
				    "@id": None,
				    "language": [{
					    "iso639_3": "eng",
					    "name": "English"
				    }],
				    "stateLocatedIn": [{
					    "name": "Missouri"
				    }],
				    "format": "Book",
				    "identifier": [],
				    "creator": [],
				    "specType": []
				}
			},
			"@id": None
      }
    }
  }
}
