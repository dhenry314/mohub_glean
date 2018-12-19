from datetime import datetime, timedelta

startTime = datetime.combine(datetime.today() - timedelta(1), datetime.min.time())

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': startTime,
    'email': ['dhenry@mohistory.org'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=10),
}

sources = {
         "mhs": {
             "name": "Missouri Historical Society",
             "sets": {
                 "all": {
                      "ESHost": "158.69.188.242",
                      "ESPort":9200,
                      "ESIndex":"ccsearch",
                      "ESType":"record",
                      "body": {
						  "query" : {
							"bool" : {
							  "must_not": [
							   
							  {
								"match": {
									"ids": "CDM:Text:"
								}
							  },
							  {
								"match": {
									"ids": "CDM:RagVideoNew:"
								}
							  },
							 {
								"match": {
									"ids": "CDM:lib:"
								}
							},
							{
								"match": {
									"ids": "CDM:MHSMaps:"
								}
							},
							{
								"match": {
									"ids": "CDM:gs:"
								}
							}],
							"must": {
							   "match": {"hasImage":1}
							}
						}
					   }
				   },
				   "transforms": {
				       "map": {
				           "transformName": "MimsyMap",
				           "targetSet": "mohub/mhm_all"
				       }
				   }
				}
             }
         },
         "msu": {
             "name": "Missouri State University",
             "sets": {
                 "all": {
                     "OAISource": "http://digitalcollections.missouristate.edu/oai/oai.php",
                     "OAIMetaDataPrefix": "oai_dc",
                     "transforms": {
						 "map": {
							 "transformName": "DCMap",
							 "targetSet": "mohub/msu_all"
						 }
					 }
                 }
             }
         },
         "kcpl": {
             "name": "Kansas City Public Library",
             "sets": {
                 "all": {
                     "OAISource": "TBD",
                     "OAIMetaDataPrefix": "TBD"
                  },
                 "pdr": {
                     "OAISource": "http://pendergastkc.org/oai",
                     "OAIMetaDataPrefix": "oai_dc",
                     "transforms": {
						 "map": {
							 "transformName": "DCMap",
							 "targetSet": "mohub/kcpl_pdr"
						 }
					 }
                  }
             }
        },
       "lhl": {
             "name": "Linda Hall Library",
             "sets": {
                 "dl": {
                     "OAISource": "http://lhldigital.lindahall.org/oai/oai.php",
                     "OAIMetaDataPrefix": "oai_dc",
                     "OAISets": ["astro_atlas","astro_early","astro_images","catalog","color","cosmology","darwin","dino","earththeory","egypt","eng_tech","hedgehog","histindexes","human","ice","math","nat_hist","panama","parachute","philsci","physics","railroad","rrjournal","rr_maps","sciwest","time"],
                     "transforms": {
						 "map": {
							 "transformName": "DCMap",
							 "targetSet": "mohub/lhl_dl"
						 }
					 }
                 }
             }
        }, 
       "shsmo": {
             "name": "State Historical Society of Missouri collections",
             "sets": {
                 "all": {
                     "OAISource": "http://cdm17228.contentdm.oclc.org/oai/oai.php",
                     "OAIMetaDataPrefix": "oai_dc",
                     "OAISets": ["aerial","amcw","ec","imc","nwm","ohc","plat","wwi"],
                     "transforms": {
						 "map": {
							 "transformName": "DCMap",
							 "targetSet": "mohub/shsmo_all"
						 }
					 }
                 }
             }
        },
        "wustl": {
             "name": "Washington University in St. Louis",
             "sets": {
                 "omeka": {
                     "OAISource": "http://omeka.wustl.edu/omeka/oai-pmh-repository/request",
                     "OAIMetaDataPrefix": "oai_dc",
                     "OAISets": ["1","10","13","14","2","41","42","44","45","46","47","48","50","51","52","54","55","58","6","60","61","64","66","67","74","69","76"],
                     "transforms": {
						 "map": {
							 "transformName": "DCMap",
							 "targetSet": "mohub/wustl_omeka"
						 }
					 }
                 },
                 "ccr": {
                     "ListSource": "http://data.mohistory.org/missourihub/staticOAI.php?path=ccr-dc&mode=listIDs",
                     "transforms": {
						 "map": {
							 "transformName": "DCMap",
							 "targetSet": "mohub/wustl_ccr"
						 }
					 }
                 },
                 "ferguson": {
                     "OAISource": "http://documentingferguson.wustl.edu/omeka/oai-pmh-repository/request",
                     "OAIMetaDataPrefix": "oai_dc",
                     "transforms": {
						 "map": {
							 "transformName": "DCMap",
							 "targetSet": "mohub/wustl_ferguson"
						 }
					 }
                 }
             }
        },
        "mdh": {
            "name": "Missouri Digital Heritage",
            "sets": {
                "all": {
                    "OAISource": "http://cdm16795.contentdm.oclc.org/oai/oai.php",
                    "OAIMetaDataPrefix": "oai_dc",
                    "OAISets": ["msaceg","jessejames","moconserv","divtour","mocases","p16795coll1","msaboggs","msareynold","msaedwards","msaking","msapolk","msamerge","msaphelps","msamarm","msafran","msastone","p16795coll6","msa","msaphotos","housej","senatej","bluebook","regdarpen","rgdarpenind","p16795coll5","postjc","vetstj"],
                    "transforms": {
						 "map": {
							 "transformName": "DCMap",
							 "targetSet": "mohub/mdh_all"
						 }
					 }
                }
            }
        },
        "slu": {
            "name": "St. Louis University Digital Library",
            "sets": {
                "dl": {
                    "OAISource": "http://cdm17321.contentdm.oclc.org/oai/oai.php",
                    "OAIMetaDataPrefix": "oai_dc",
                    "transforms": {
						 "map": {
							 "transformName": "DCMap",
							 "targetSet": "mohub/slu_dl"
						 }
					 }
                }
            }
        },
        "slpl": {
            "name": "St. Louis Public Library",
            "sets": {
                "dl": {
                    "OAISource": "http://collections.slpl.org/oai/oai.php",
                    "OAIMetaDataPrefix": "oai_dc",
                    "transforms": {
						 "map": {
							 "transformName": "DCMap",
							 "targetSet": "mohub/slpl_dl"
						 }
					 }
                }
            }
        },
        "frbstl": {
            "name":"Federal Reserve Bank of St. Louis",
            "sets": {
                "fraser": {
                     "OAISource":"https://fraser.stlouisfed.org/oai",
                     "OAIMetaDataPrefix":"mods",
                     "transforms": {
						 "map": {
							 "transformName": "MODSMap",
							 "targetSet": "mohub/frbstl_fraser"
						 }
					 }
                }
            }
        },
        "umsl": {
            "name": "University of Missouri - St. Louis",
            "sets": {
                "dl": {
                     "OAISource":"http://dl.mospace.umsystem.edu/umsl/oai2",
                     "OAIMetaDataPrefix":"mods",
                     "transforms": {
						 "map": {
							 "transformName": "MODSMap",
							 "targetSet": "mohub/umsl_dl"
						 }
					 }
                }
            }
        },
        "umkc": {
            "name": "University of Missouri- Kansas City",
            "sets": {
                "dl": {
					"OAISource":"http://dl.mospace.umsystem.edu/umkc/oai2",
					"OAIMetaDataPrefix":"mods",
					"transforms": {
						 "map": {
							 "transformName": "MODSMap",
							 "targetSet": "mohub/umkc_dl"
						 }
					 }
                }
            }
        }
}
