import jsonschema
from jsonschema import validate

def validate(item):
    try:
        validate(item, schema)
        #sys.stdout.write("Record #{}: OK\n".format(idx))
    except jsonschema.exceptions.ValidationError as ve:
        #sys.stderr.write("Record #{}: ERROR\n".format(idx))
        #sys.stderr.write(str(ve) + "\n")

schema = {
  "definitions": {},
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "http://example.com/root.json",
  "type": "object",
  "title": "The Root Schema",
  "required": [
    "@context",
    "isShownAt",
    "dataProvider",
    "@type",
    "hasView",
    "provider",
    "object",
    "aggregatedCHO",
    "sourceResource",
    "admin",
    "@id",
    "ingestType",
    "originalRecord"
  ],
  "properties": {
    "@context": {
      "$id": "#/properties/@context",
      "type": "string",
      "title": "The @context Schema",
      "default": "",
      "examples": [
        "http://dp.la/api/items/context"
      ],
      "pattern": "^(.*)$"
    },
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
    "@type": {
      "$id": "#/properties/@type",
      "type": "string",
      "title": "The @type Schema",
      "default": "",
      "examples": [
        "ore:Aggregation"
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
    "aggregatedCHO": {
      "$id": "#/properties/aggregatedCHO",
      "type": "string",
      "title": "The Aggregatedcho Schema",
      "default": "",
      "examples": [
        "#sourceResource"
      ],
      "pattern": "^(.*)$"
    },
    "sourceResource": {
      "$id": "#/properties/sourceResource",
      "type": "object",
      "title": "The Sourceresource Schema",
      "required": [
        "title",
        "description",
        "subject",
        "temporal",
        "rights",
        "@id",
        "language",
        "stateLocatedIn",
        "format",
        "identifier",
        "creator",
        "specType"
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
        "description": {
          "$id": "#/properties/sourceResource/properties/description",
          "type": "array",
          "title": "The Description Schema",
          "items": {
            "$id": "#/properties/sourceResource/properties/description/items",
            "type": "string",
            "title": "The Items Schema",
            "default": "",
            "examples": [
              "Modern towboats are steamlined - 1940."
            ],
            "pattern": "^(.*)$"
          }
        },
        "subject": {
          "$id": "#/properties/sourceResource/properties/subject",
          "type": "array",
          "title": "The Subject Schema",
          "items": {
            "$id": "#/properties/sourceResource/properties/subject/items",
            "type": "object",
            "title": "The Items Schema",
            "required": [
              "name"
            ],
            "properties": {
              "name": {
                "$id": "#/properties/sourceResource/properties/subject/items/properties/name",
                "type": "string",
                "title": "The Name Schema",
                "default": "",
                "examples": [
                  "Towboats"
                ],
                "pattern": "^(.*)$"
              }
            }
          }
        },
        "temporal": {
          "$id": "#/properties/sourceResource/properties/temporal",
          "type": "array",
          "title": "The Temporal Schema",
          "items": {
            "$id": "#/properties/sourceResource/properties/temporal/items",
            "type": "object",
            "title": "The Items Schema",
            "required": [
              "displayDate",
              "end",
              "begin"
            ],
            "properties": {
              "displayDate": {
                "$id": "#/properties/sourceResource/properties/temporal/items/properties/displayDate",
                "type": "string",
                "title": "The Displaydate Schema",
                "default": "",
                "examples": [
                  "1940-1949"
                ],
                "pattern": "^(.*)$"
              },
              "end": {
                "$id": "#/properties/sourceResource/properties/temporal/items/properties/end",
                "type": "string",
                "title": "The End Schema",
                "default": "",
                "examples": [
                  "1949"
                ],
                "pattern": "^(.*)$"
              },
              "begin": {
                "$id": "#/properties/sourceResource/properties/temporal/items/properties/begin",
                "type": "string",
                "title": "The Begin Schema",
                "default": "",
                "examples": [
                  "1940"
                ],
                "pattern": "^(.*)$"
              }
            }
          }
        },
        "rights": {
          "$id": "#/properties/sourceResource/properties/rights",
          "type": "array",
          "title": "The Rights Schema",
          "items": {
            "$id": "#/properties/sourceResource/properties/rights/items",
            "type": "string",
            "title": "The Items Schema",
            "default": "",
            "examples": [
              "Items in the UMSL Digital Library are protected by copyright, with all rights reserved, unless otherwise indicated. The contents of the UMSL Digital Library are made publicly available for use in research, teaching, and private study. Although the nature of archival and manuscript materials sometimes makes it difficult to determine the copyright status of an item, it is the user's responsibility to use them according to all applicable terms. Please contact the contributing partner for additional information regarding copyright status of a particular digital image, text, data set, or sound or video recording."
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
        "format": {
          "$id": "#/properties/sourceResource/properties/format",
          "type": "string",
          "title": "The Format Schema",
          "default": "",
          "examples": [
            "Photograph/Pictorial Works"
          ],
          "pattern": "^(.*)$"
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
        "creator": {
          "$id": "#/properties/sourceResource/properties/creator",
          "type": "array",
          "title": "The Creator Schema",
          "items": {
            "$id": "#/properties/sourceResource/properties/creator/items",
            "type": "string",
            "title": "The Items Schema",
            "default": "",
            "examples": [
              "Hartford, John",
              "Ramsey, Carolyn"
            ],
            "pattern": "^(.*)$"
          }
        },
        "specType": {
          "$id": "#/properties/sourceResource/properties/specType",
          "type": "array",
          "title": "The Spectype Schema",
          "items": {
            "$id": "#/properties/sourceResource/properties/specType/items",
            "type": "string",
            "title": "The Items Schema",
            "default": "",
            "examples": [
              "Photograph/Pictorial Works"
            ],
            "pattern": "^(.*)$"
          }
        }
      }
    },
    "admin": {
      "$id": "#/properties/admin",
      "type": "object",
      "title": "The Admin Schema",
      "required": [
        "sourceResource"
      ],
      "properties": {
        "sourceResource": {
          "$id": "#/properties/admin/properties/sourceResource",
          "type": "object",
          "title": "The Sourceresource Schema",
          "required": [
            "title"
          ],
          "properties": {
            "title": {
              "$id": "#/properties/admin/properties/sourceResource/properties/title",
              "type": "string",
              "title": "The Title Schema",
              "default": "",
              "examples": [
                "Towboat"
              ],
              "pattern": "^(.*)$"
            }
          }
        }
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
    },
    "ingestType": {
      "$id": "#/properties/ingestType",
      "type": "string",
      "title": "The Ingesttype Schema",
      "default": "",
      "examples": [
        "item"
      ],
      "pattern": "^(.*)$"
    },
    "originalRecord": {
      "$id": "#/properties/originalRecord",
      "type": "object",
      "title": "The Originalrecord Schema",
      "required": [
        "id",
        "provider",
        "collection",
        "header",
        "metadata"
      ],
      "properties": {
        "id": {
          "$id": "#/properties/originalRecord/properties/id",
          "type": "string",
          "title": "The Id Schema",
          "default": "",
          "examples": [
            "urn:data.mohistory.org:umsl_dl:oai:dl.mospace.umsystem.edu/umsl/:umsl_112368"
          ],
          "pattern": "^(.*)$"
        },
        "provider": {
          "$id": "#/properties/originalRecord/properties/provider",
          "type": "object",
          "title": "The Provider Schema",
          "required": [
            "@id",
            "name"
          ],
          "properties": {
            "@id": {
              "$id": "#/properties/originalRecord/properties/provider/properties/@id",
              "type": "string",
              "title": "The @id Schema",
              "default": "",
              "examples": [
                "http://dp.la/api/contributor/missouri-hub"
              ],
              "pattern": "^(.*)$"
            },
            "name": {
              "$id": "#/properties/originalRecord/properties/provider/properties/name",
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
        "collection": {
          "$id": "#/properties/originalRecord/properties/collection",
          "type": "object",
          "title": "The Collection Schema",
          "required": [
            "id",
            "description",
            "title",
            "@id"
          ],
          "properties": {
            "id": {
              "$id": "#/properties/originalRecord/properties/collection/properties/id",
              "type": "string",
              "title": "The Id Schema",
              "default": "",
              "examples": [
                "245f720fd4b2a8a8daad09bc1333bf07"
              ],
              "pattern": "^(.*)$"
            },
            "description": {
              "$id": "#/properties/originalRecord/properties/collection/properties/description",
              "type": "string",
              "title": "The Description Schema",
              "default": "",
              "examples": [
                ""
              ],
              "pattern": "^(.*)$"
            },
            "title": {
              "$id": "#/properties/originalRecord/properties/collection/properties/title",
              "type": "string",
              "title": "The Title Schema",
              "default": "",
              "examples": [
                "umsl_dl"
              ],
              "pattern": "^(.*)$"
            },
            "@id": {
              "$id": "#/properties/originalRecord/properties/collection/properties/@id",
              "type": "string",
              "title": "The @id Schema",
              "default": "",
              "examples": [
                "http://dp.la/api/collections/245f720fd4b2a8a8daad09bc1333bf07"
              ],
              "pattern": "^(.*)$"
            }
          }
        },
        "header": {
          "$id": "#/properties/originalRecord/properties/header",
          "type": "object",
          "title": "The Header Schema",
          "required": [
            "expirationdatetime",
            "datestamp",
            "identifier",
            "setSpec"
          ],
          "properties": {
            "expirationdatetime": {
              "$id": "#/properties/originalRecord/properties/header/properties/expirationdatetime",
              "type": "string",
              "title": "The Expirationdatetime Schema",
              "default": "",
              "examples": [
                "2017-04-04T21:34:20Z"
              ],
              "pattern": "^(.*)$"
            },
            "datestamp": {
              "$id": "#/properties/originalRecord/properties/header/properties/datestamp",
              "type": "string",
              "title": "The Datestamp Schema",
              "default": "",
              "examples": [
                "2016-10-04T13:19:05Z"
              ],
              "pattern": "^(.*)$"
            },
            "identifier": {
              "$id": "#/properties/originalRecord/properties/header/properties/identifier",
              "type": "string",
              "title": "The Identifier Schema",
              "default": "",
              "examples": [
                "urn:data.mohistory.org:umsl_dl:oai:dl.mospace.umsystem.edu/umsl/:umsl_112368"
              ],
              "pattern": "^(.*)$"
            },
            "setSpec": {
              "$id": "#/properties/originalRecord/properties/header/properties/setSpec",
              "type": "string",
              "title": "The Setspec Schema",
              "default": "",
              "examples": [
                "umsl_dl"
              ],
              "pattern": "^(.*)$"
            }
          }
        },
        "metadata": {
          "$id": "#/properties/originalRecord/properties/metadata",
          "type": "object",
          "title": "The Metadata Schema",
          "required": [
            "mods"
          ],
          "properties": {
            "mods": {
              "$id": "#/properties/originalRecord/properties/metadata/properties/mods",
              "type": "object",
              "title": "The Mods Schema",
              "required": [
                "genre",
                "accessCondition",
                "location",
                "subject",
                "name",
                "physicalDescription",
                "xmlns",
                "language",
                "titleInfo",
                "identifier",
                "note"
              ],
              "properties": {
                "genre": {
                  "$id": "#/properties/originalRecord/properties/metadata/properties/mods/properties/genre",
                  "type": "string",
                  "title": "The Genre Schema",
                  "default": "",
                  "examples": [
                    "Photograph/Pictorial Works"
                  ],
                  "pattern": "^(.*)$"
                },
                "accessCondition": {
                  "$id": "#/properties/originalRecord/properties/metadata/properties/mods/properties/accessCondition",
                  "type": "string",
                  "title": "The Accesscondition Schema",
                  "default": "",
                  "examples": [
                    "Items in the UMSL Digital Library are protected by copyright, with all rights reserved, unless otherwise indicated. The contents of the UMSL Digital Library are made publicly available for use in research, teaching, and private study. Although the nature of archival and manuscript materials sometimes makes it difficult to determine the copyright status of an item, it is the user's responsibility to use them according to all applicable terms. Please contact the contributing partner for additional information regarding copyright status of a particular digital image, text, data set, or sound or video recording."
                  ],
                  "pattern": "^(.*)$"
                },
                "location": {
                  "$id": "#/properties/originalRecord/properties/metadata/properties/mods/properties/location",
                  "type": "object",
                  "title": "The Location Schema",
                  "required": [
                    "url"
                  ],
                  "properties": {
                    "url": {
                      "$id": "#/properties/originalRecord/properties/metadata/properties/mods/properties/location/properties/url",
                      "type": "array",
                      "title": "The Url Schema",
                      "items": {
                        "$id": "#/properties/originalRecord/properties/metadata/properties/mods/properties/location/properties/url/items",
                        "type": "object",
                        "title": "The Items Schema",
                        "required": [
                          "#text",
                          "access"
                        ],
                        "properties": {
                          "#text": {
                            "$id": "#/properties/originalRecord/properties/metadata/properties/mods/properties/location/properties/url/items/properties/#text",
                            "type": "string",
                            "title": "The #text Schema",
                            "default": "",
                            "examples": [
                              "http://dl.mospace.umsystem.edu/umsl/islandora/object/umsl:112368"
                            ],
                            "pattern": "^(.*)$"
                          },
                          "access": {
                            "$id": "#/properties/originalRecord/properties/metadata/properties/mods/properties/location/properties/url/items/properties/access",
                            "type": "string",
                            "title": "The Access Schema",
                            "default": "",
                            "examples": [
                              "object in context"
                            ],
                            "pattern": "^(.*)$"
                          }
                        }
                      }
                    }
                  }
                },
                "subject": {
                  "$id": "#/properties/originalRecord/properties/metadata/properties/mods/properties/subject",
                  "type": "array",
                  "title": "The Subject Schema",
                  "items": {
                    "$id": "#/properties/originalRecord/properties/metadata/properties/mods/properties/subject/items",
                    "type": "object",
                    "title": "The Items Schema",
                    "required": [
                      "topic"
                    ],
                    "properties": {
                      "topic": {
                        "$id": "#/properties/originalRecord/properties/metadata/properties/mods/properties/subject/items/properties/topic",
                        "type": "string",
                        "title": "The Topic Schema",
                        "default": "",
                        "examples": [
                          "Towboats"
                        ],
                        "pattern": "^(.*)$"
                      }
                    }
                  }
                },
                "name": {
                  "$id": "#/properties/originalRecord/properties/metadata/properties/mods/properties/name",
                  "type": "array",
                  "title": "The Name Schema",
                  "items": {
                    "$id": "#/properties/originalRecord/properties/metadata/properties/mods/properties/name/items",
                    "type": "object",
                    "title": "The Items Schema",
                    "required": [
                      "role",
                      "namePart"
                    ],
                    "properties": {
                      "role": {
                        "$id": "#/properties/originalRecord/properties/metadata/properties/mods/properties/name/items/properties/role",
                        "type": "object",
                        "title": "The Role Schema",
                        "required": [
                          "roleTerm"
                        ],
                        "properties": {
                          "roleTerm": {
                            "$id": "#/properties/originalRecord/properties/metadata/properties/mods/properties/name/items/properties/role/properties/roleTerm",
                            "type": "string",
                            "title": "The Roleterm Schema",
                            "default": "",
                            "examples": [
                              "creator"
                            ],
                            "pattern": "^(.*)$"
                          }
                        }
                      },
                      "namePart": {
                        "$id": "#/properties/originalRecord/properties/metadata/properties/mods/properties/name/items/properties/namePart",
                        "type": "string",
                        "title": "The Namepart Schema",
                        "default": "",
                        "examples": [
                          "Hartford, John"
                        ],
                        "pattern": "^(.*)$"
                      }
                    }
                  }
                },
                "physicalDescription": {
                  "$id": "#/properties/originalRecord/properties/metadata/properties/mods/properties/physicalDescription",
                  "type": "object",
                  "title": "The Physicaldescription Schema",
                  "required": [
                    "note"
                  ],
                  "properties": {
                    "note": {
                      "$id": "#/properties/originalRecord/properties/metadata/properties/mods/properties/physicalDescription/properties/note",
                      "type": "string",
                      "title": "The Note Schema",
                      "default": "",
                      "examples": [
                        "still image"
                      ],
                      "pattern": "^(.*)$"
                    }
                  }
                },
                "xmlns": {
                  "$id": "#/properties/originalRecord/properties/metadata/properties/mods/properties/xmlns",
                  "type": "string",
                  "title": "The Xmlns Schema",
                  "default": "",
                  "examples": [
                    "http://www.loc.gov/mods/v3"
                  ],
                  "pattern": "^(.*)$"
                },
                "language": {
                  "$id": "#/properties/originalRecord/properties/metadata/properties/mods/properties/language",
                  "type": "object",
                  "title": "The Language Schema",
                  "required": [
                    "languageTerm"
                  ],
                  "properties": {
                    "languageTerm": {
                      "$id": "#/properties/originalRecord/properties/metadata/properties/mods/properties/language/properties/languageTerm",
                      "type": "string",
                      "title": "The Languageterm Schema",
                      "default": "",
                      "examples": [
                        "eng"
                      ],
                      "pattern": "^(.*)$"
                    }
                  }
                },
                "titleInfo": {
                  "$id": "#/properties/originalRecord/properties/metadata/properties/mods/properties/titleInfo",
                  "type": "object",
                  "title": "The Titleinfo Schema",
                  "required": [
                    "title"
                  ],
                  "properties": {
                    "title": {
                      "$id": "#/properties/originalRecord/properties/metadata/properties/mods/properties/titleInfo/properties/title",
                      "type": "string",
                      "title": "The Title Schema",
                      "default": "",
                      "examples": [
                        "Towboat"
                      ],
                      "pattern": "^(.*)$"
                    }
                  }
                },
                "identifier": {
                  "$id": "#/properties/originalRecord/properties/metadata/properties/mods/properties/identifier",
                  "type": "string",
                  "title": "The Identifier Schema",
                  "default": "",
                  "examples": [
                    "http://dl.mospace.umsystem.edu/umsl/islandora/object/umsl:112368"
                  ],
                  "pattern": "^(.*)$"
                },
                "note": {
                  "$id": "#/properties/originalRecord/properties/metadata/properties/mods/properties/note",
                  "type": "array",
                  "title": "The Note Schema",
                  "items": {
                    "$id": "#/properties/originalRecord/properties/metadata/properties/mods/properties/note/items",
                    "type": "string",
                    "title": "The Items Schema",
                    "default": "",
                    "examples": [
                      "Modern towboats are steamlined - 1940."
                    ],
                    "pattern": "^(.*)$"
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
