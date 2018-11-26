
    
DPLAschema = {
  "definitions": {},
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "http://example.com/root.json",
  "type": "object",
  "title": "The Root Schema",
  "required": [
    "isShownAt",
    "dataProvider",
    "hasView",
    "provider",
    "object",
    "sourceResource",
    "@id",
  ],
  "properties": {
    "isShownAt": {
      "$id": "#/properties/isShownAt",
      "type": "string",
      "title": "The Isshownat Schema",
      "default": "",
      "examples": [
        "http://dl.mospace.umsystem.edu/umsl/islandora/object/umsl:112368"
      ],
      "pattern": "^(.*)$"
    },
    "dataProvider": {
      "$id": "#/properties/dataProvider",
      "type": "string",
      "title": "The Dataprovider Schema",
      "default": "",
      "examples": [
        "St. Louis Mercantile Library - University of Missouri-St. Louis"
      ],
      "pattern": "^(.*)$"
    },
    "hasView": {
      "$id": "#/properties/hasView",
      "type": "object",
      "title": "The Hasview Schema",
      "required": [
        "@id"
      ],
      "properties": {
        "@id": {
          "$id": "#/properties/hasView/properties/@id",
          "type": "string",
          "title": "The @id Schema",
          "default": "",
          "examples": [
            "http://dl.mospace.umsystem.edu/umsl/islandora/object/umsl:112368"
          ],
          "pattern": "^(.*)$"
        }
      }
    },
    "provider": {
      "$id": "#/properties/provider",
      "type": "object",
      "title": "The Provider Schema",
      "required": [
        "@id",
        "name"
      ],
      "properties": {
        "@id": {
          "$id": "#/properties/provider/properties/@id",
          "type": "string",
          "title": "The @id Schema",
          "default": "",
          "examples": [
            "http://dp.la/api/contributor/missouri-hub"
          ],
          "pattern": "^(.*)$"
        },
        "name": {
          "$id": "#/properties/provider/properties/name",
          "type": "string",
          "title": "The Name Schema",
          "default": "",
          "examples": [
            "Missouri Hub"
          ],
          "pattern": "^(.*)$"
        }
      }
    },
    "object": {
      "$id": "#/properties/object",
      "type": "string",
      "title": "The Object Schema",
      "default": "",
      "examples": [
        "http://dl.mospace.umsystem.edu/umsl/islandora/object/umsl:112368/datastream/TN/view"
      ],
      "pattern": "^(.*)$"
    },
    "sourceResource": {
      "$id": "#/properties/sourceResource",
      "type": "object",
      "title": "The Sourceresource Schema",
      "required": [
        "title",
        "rights",
        "@id",
        "language",
        "stateLocatedIn",
        "identifier"
      ],
      "properties": {
        "title": {
          "$id": "#/properties/sourceResource/properties/title",
          "type": "array",
          "title": "The Title Schema",
          "items": {
            "$id": "#/properties/sourceResource/properties/title/items",
            "type": "string",
            "title": "The Items Schema",
            "default": "",
            "examples": [
              "Towboat"
            ],
            "pattern": "^(.*)$"
          }
        },
        "@id": {
          "$id": "#/properties/sourceResource/properties/@id",
          "type": "string",
          "title": "The @id Schema",
          "default": "",
          "examples": [
            "http://dp.la/api/items/246eb2ec1f7469d62304485df6e3f017#sourceResource"
          ],
          "pattern": "^(.*)$"
        },
        "language": {
          "$id": "#/properties/sourceResource/properties/language",
          "type": "array",
          "title": "The Language Schema",
          "items": {
            "$id": "#/properties/sourceResource/properties/language/items",
            "type": "object",
            "title": "The Items Schema",
            "required": [
              "iso639_3",
              "name"
            ],
            "properties": {
              "iso639_3": {
                "$id": "#/properties/sourceResource/properties/language/items/properties/iso639_3",
                "type": "string",
                "title": "The Iso639_3 Schema",
                "default": "",
                "examples": [
                  "eng"
                ],
                "pattern": "^(.*)$"
              },
              "name": {
                "$id": "#/properties/sourceResource/properties/language/items/properties/name",
                "type": "string",
                "title": "The Name Schema",
                "default": "",
                "examples": [
                  "English"
                ],
                "pattern": "^(.*)$"
              }
            }
          }
        },
        "stateLocatedIn": {
          "$id": "#/properties/sourceResource/properties/stateLocatedIn",
          "type": "array",
          "title": "The Statelocatedin Schema",
          "items": {
            "$id": "#/properties/sourceResource/properties/stateLocatedIn/items",
            "type": "object",
            "title": "The Items Schema",
            "required": [
              "name"
            ],
            "properties": {
              "name": {
                "$id": "#/properties/sourceResource/properties/stateLocatedIn/items/properties/name",
                "type": "string",
                "title": "The Name Schema",
                "default": "",
                "examples": [
                  "Missouri"
                ],
                "pattern": "^(.*)$"
              }
            }
          }
        },
        "identifier": {
          "$id": "#/properties/sourceResource/properties/identifier",
          "type": "array",
          "title": "The Identifier Schema",
          "items": {
            "$id": "#/properties/sourceResource/properties/identifier/items",
            "type": "string",
            "title": "The Items Schema",
            "default": "",
            "examples": [
              "http://dl.mospace.umsystem.edu/umsl/islandora/object/umsl:112368"
            ],
            "pattern": "^(.*)$"
          }
        },
      }
    },
    "@id": {
      "$id": "#/properties/@id",
      "type": "string",
      "title": "The @id Schema",
      "default": "",
      "examples": [
        "http://dp.la/api/items/246eb2ec1f7469d62304485df6e3f017"
      ],
      "pattern": "^(.*)$"
    }
  }
}
