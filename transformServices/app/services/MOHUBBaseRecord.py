
class MOHUBBaseRecord():

    def getBaseRecord(self):
        baseRecord =  {
			"@context": "http://dp.la/api/items/context",
			"isShownAt": None,
			"dataProvider": None,
			"@type": "ore:Aggregation",
			"hasView": {
				"@id": None
			},
			"provider": {
				"@id": "http://dp.la/api/contributor/missouri-hub",
				"name": "Missouri Hub"
			},
			"object": None,
			"aggregatedCHO": "#sourceResource",
			"sourceResource": {
				"title": [],
				"description": [],
				"subject": [],
				"temporal": [],
				"rights": [],
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
			},
			"@id": None
		}
        return baseRecord
