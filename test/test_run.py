#!/usr/bin/python3
import os
import json
import time
import requests
from jinja2 import Template
from bs4 import BeautifulSoup

panel = [
    {
        "hugoSymbol": "ALK",
        "nNGM": {
            "grch37RefSeq": "NM_004304.5",
            "hugoSymbol": "ALK",
            "exonCount": 29,
            "expVariants": 190,
            "exons": {
                22: {
                    "expVariants": 23,
                },
                23: {
                    "expVariants": 49,
                },
                24: {
                    "expVariants": 30,
                },
                25: {
                    "expVariants": 28,
                },
            },
        },
    },

    {
        "hugoSymbol": "BRAF",
        "nNGM": {
            "grch37RefSeq": "NM_004333.6",
            "hugoSymbol": "BRAF",
            "exonCount": 18,
            "expVariants": 164,
            "exons": {
                11: {
                    "expVariants": 61,
                },
                15: {
                    "expVariants": 99,
                },
            },
        },
    },

    {
        "hugoSymbol": "CTNNB1",
        "nNGM": {
            "grch37RefSeq": "NM_001904.4",
            "hugoSymbol": "CTNNB1",
            "exonCount": 15,
            "expVariants": 64,
            "exons": {
                3: {
                    "expVariants": 60,
                },
            },
        },
    },

    {
        "hugoSymbol": "EGFR",
        "nNGM": {
            "grch37RefSeq": "NM_005228.5",
            "hugoSymbol": "EGFR",
            "exonCount": 28,
            "expVariants": 406,
            "exons": {
                18: {
                    "expVariants": 52,
                },
                19: {
                    "expVariants": 107,
                },
                20: {
                    "expVariants": 106,
                },
                21: {
                    "expVariants": 68,
                },
            },
        },
    },

    {
        "hugoSymbol": "ERBB2",
        "nNGM": {
            "grch37RefSeq": "NM_004448.4",
            "hugoSymbol": "ERBB2",
            "exonCount": 27,
            "expVariants": 132,
            "exons": {
                8: {
                    "expVariants": 15,
                },
                19: {
                    "expVariants": 41,
                },
                20: {
                    "expVariants": 52,
                },
            },
        },
    },

    {
        "hugoSymbol": "FGFR1",
        "nNGM": {
            "grch37RefSeq": "NM_023110.3",
            "hugoSymbol": "FGFR1",
            "exonCount": 18,
            "expVariants": 105,
            "exons": {
                4: {
                    "expVariants": 15,
                },
                5: {
                    "expVariants": 13,
                },
                6: {
                    "expVariants": 7,
                },
                7: {
                    "expVariants": 23,
                },
                10: {
                    "expVariants": 12,
                },
                12: {
                    "expVariants": 5,
                },
                13: {
                    "expVariants": 12,
                },
                14: {
                    "expVariants": 3,
                },
                15: {
                    "expVariants": 7,
                },
            },
        },
    },

    {
        "hugoSymbol": "FGFR2",
        "nNGM": {
            "grch37RefSeq": "NM_000141.5",
            "hugoSymbol": "FGFR2",
            "exonCount": 18,
            "expVariants": 212,
            "exons": {
                6: {
                    "expVariants": 11,
                },
                7: {
                    "expVariants": 25,
                },
                8: {
                    "expVariants": 23,
                },
                9: {
                    "expVariants": 21,
                },
                10: {
                    "expVariants": 19,
                },
                11: {
                    "expVariants": 6,
                },
                12: {
                    "expVariants": 12,
                },
                13: {
                    "expVariants": 10,
                },
                14: {
                    "expVariants": 18,
                },
                15: {
                    "expVariants": 10,
                },
                18: {
                    "expVariants": 26,
                },
            },
        },
    },

    {
        "hugoSymbol": "FGFR2",
        "nNGM": {
            "grch37RefSeq": "NM_022970.3",
            "hugoSymbol": "FGFR2 (alt exon 8)",
            "exonCount": 18,
            "expVariants": 212,
            "exons": {
                8: {
                    "expVariants": 12,
                },
            },
        },
    },

    {
        "hugoSymbol": "FGFR3",
        "nNGM": {
            "grch37RefSeq": "NM_000142.5",
            "hugoSymbol": "FGFR3",
            "exonCount": 18,
            "expVariants": 183,
            "exons": {
                3: {
                    "expVariants": 19,
                },
                6: {
                    "expVariants": 0,
                },
                7: {
                    "expVariants": 38,
                },
                9: {
                    "expVariants": 30,
                },
                10: {
                    "expVariants": 13,
                },
                12: {
                    "expVariants": 2,
                },
                14: {
                    "expVariants": 23,
                },
                16: {
                    "expVariants": 7,
                },
                18: {
                    "expVariants": 13,
                },
            },
        },
    },

    {
        "hugoSymbol": "FGFR4",
        "nNGM": {
            "grch37RefSeq": "NM_213647.3",
            "hugoSymbol": "FGFR4",
            "exonCount": 18,
            "expVariants": 98,
            "exons": {
                3: {
                    "expVariants": 22,
                },
                6: {
                    "expVariants": 10,
                },
                9: {
                    "expVariants": 21,
                },
                12: {
                    "expVariants": 7,
                },
                13: {
                    "expVariants": 23,
                },
                15: {
                    "expVariants": 4,
                },
                16: {
                    "expVariants": 5,
                },
            },
        },
    },

    {
        "hugoSymbol": "HRAS",
        "nNGM": {
            "grch37RefSeq": "NM_005343.4",
            "hugoSymbol": "HRAS",
            "exonCount": 6,
            "expVariants": 25,
            "exons": {
                2: {
                    "expVariants": 6,
                },
                3: {
                    "expVariants": 13,
                },
                4: {
                    "expVariants": 6,
                },
            },
        },
    },

    {
        "hugoSymbol": "IDH1",
        "nNGM": {
            "grch37RefSeq": "NM_005896.4",
            "hugoSymbol": "IDH1",
            "exonCount": 10,
            "expVariants": 26,
            "exons": {
                4: {
                    "expVariants": 26,
                },
            },
        },
    },

    {
        "hugoSymbol": "IDH2",
        "nNGM": {
            "grch37RefSeq": "NM_002168.4",
            "hugoSymbol": "IDH2",
            "exonCount": 11,
            "expVariants": 15,
            "exons": {
                4: {
                    "expVariants": 14,
                },
            },
        },
    },

    {
        "hugoSymbol": "KEAP1",
        "nNGM": {
            "grch37RefSeq": "NM_203500.2",
            "hugoSymbol": "KEAP1",
            "exonCount": 6,
            "expVariants": 676,
            "exons": {
                2: {
                    "expVariants": 198,
                },
                3: {
                    "expVariants": 284,
                },
                4: {
                    "expVariants": 76,
                },
                5: {
                    "expVariants": 61,
                },
                6: {
                    "expVariants": 44,
                },
            },
        },
    },

    {
        "hugoSymbol": "KRAS",
        "nNGM": {
            "grch37RefSeq": "NM_033360.4",
            "hugoSymbol": "KRAS",
            "exonCount": 6,
            "expVariants": 134,
            "exons": {
                2: {
                    "expVariants": 48,
                },
                3: {
                    "expVariants": 54,
                },
                4: {
                    "expVariants": 29,
                },
            },
        },
    },

    {
        "hugoSymbol": "MAP2K1",
        "nNGM": {
            "grch37RefSeq": "NM_002755.4",
            "hugoSymbol": "MAP2K1",
            "exonCount": 11,
            "expVariants": 90,
            "exons": {
                2: {
                    "expVariants": 72,
                },
                3: {
                    "expVariants": 16,
                },
            },
        },
    },

    {
        "hugoSymbol": "MET",
        "nNGM": {
            "grch37RefSeq": "NM_001127500.3",
            "hugoSymbol": "MET",
            "exonCount": 21,
            "intronCount": 20,
            "expVariants": 562,
            "exons": {
                14: {
                    "expVariants": 162,
                },
                16: {
                    "expVariants": 13,
                },
                17: {
                    "expVariants": 19,
                },
                18: {
                    "expVariants": 9,
                },
                19: {
                    "expVariants": 16,
                },
            },
            "introns": {
                13: {
                    "expVariants": 236,
                },
                14: {
                    "expVariants": 173,
                },
            },
        },
    },

    {
        "hugoSymbol": "NRAS",
        "nNGM": {
            "grch37RefSeq": "NM_002524.5",
            "hugoSymbol": "NRAS",
            "exonCount": 7,
            "expVariants": 106,
            "exons": {
                2: {
                    "expVariants": 24,
                },
                3: {
                    "expVariants": 56,
                },
                4: {
                    "expVariants": 21,
                },
            },
        },
    },

    {
        "hugoSymbol": "NTRK1",
        "nNGM": {
            "grch37RefSeq": "NM_002529.4",
            "hugoSymbol": "NTRK1",
            "exonCount": 17,
            "expVariants": 6,
            "exons": {
                13: {
                    "expVariants": 0,
                },
                14: {
                    "expVariants": 0,
                },
                15: {
                    "expVariants": 4,
                },
                16: {
                    "expVariants": 0,
                },
                17: {
                    "expVariants": 2,
                },
            },
        },
    },

    {
        "hugoSymbol": "NTRK2",
        "nNGM": {
            "grch37RefSeq": "NM_006180.6",
            "hugoSymbol": "NTRK2",
            "exonCount": 21,
            "expVariants": 0,
            "exons": {
                14: {
                    "expVariants": 0,
                },
                15: {
                    "expVariants": 0,
                },
                16: {
                    "expVariants": 0,
                },
                17: {
                    "expVariants": 0,
                },
                18: {
                    "expVariants": 0,
                },
                19: {
                    "expVariants": 0,
                },
            },
        },
    },

    {
        "hugoSymbol": "NTRK3",
        "nNGM": {
            "grch37RefSeq": "NM_001012338.3",
            "hugoSymbol": "NTRK3",
            "exonCount": 19,
            "expVariants": 0,
            "exons": {
                14: {
                    "expVariants": 0,
                },
                15: {
                    "expVariants": 0,
                },
                16: {
                    "expVariants": 0,
                },
                17: {
                    "expVariants": 0,
                },
                18: {
                    "expVariants": 0,
                },
                19: {
                    "expVariants": 0,
                },
            },
        },
    },

    {
        "hugoSymbol": "PIK3CA",
        "nNGM": {
            "grch37RefSeq": "NM_006218.4",
            "hugoSymbol": "PIK3CA",
            "exonCount": 21,
            "expVariants": 149,
            "exons": {
                8: {
                    "expVariants": 4,
                },
                10: {
                    "expVariants": 46,
                },
                21: {
                    "expVariants": 79,
                },
            },
        },
    },

    {
        "hugoSymbol": "PTEN",
        "nNGM": {
            "grch37RefSeq": "NM_000314.8",
            "hugoSymbol": "PTEN",
            "exonCount": 9,
            "expVariants": 592,
            "exons": {
                1: {
                    "expVariants": 52,
                },
                2: {
                    "expVariants": 50,
                },
                3: {
                    "expVariants": 23,
                },
                4: {
                    "expVariants": 23,
                },
                5: {
                    "expVariants": 141,
                },
                6: {
                    "expVariants": 75,
                },
                7: {
                    "expVariants": 79,
                },
                8: {
                    "expVariants": 88,
                },
            },
        },
    },

    {
        "hugoSymbol": "RET",
        "nNGM": {
            "grch37RefSeq": "NM_020975.6",
            "hugoSymbol": "RET",
            "exonCount": 20,
            "expVariants": 5,
            "exons": {
                10: {
                    "expVariants": 0,
                },
                11: {
                    "expVariants": 1,
                },
                12: {
                    "expVariants": 0,
                },
                13: {
                    "expVariants": 0,
                },
                14: {
                    "expVariants": 0,
                },
                15: {
                    "expVariants": 0,
                },
                16: {
                    "expVariants": 0,
                },
                17: {
                    "expVariants": 0,
                },
                18: {
                    "expVariants": 1,
                },
            },
        },
    },

    {
        "hugoSymbol": "ROS1",
        "nNGM": {
            "grch37RefSeq": "NM_002944.3",
            "hugoSymbol": "ROS1",
            "exonCount": 43,
            "expVariants": 124,
            "exons": {
                34: {
                    "expVariants": 2,
                },
                35: {
                    "expVariants": 18,
                },
                36: {
                    "expVariants": 22,
                },
                37: {
                    "expVariants": 5,
                },
                38: {
                    "expVariants": 19,
                },
                39: {
                    "expVariants": 4,
                },
                40: {
                    "expVariants": 20,
                },
                41: {
                    "expVariants": 9,
                },
            },
        },
    },

    {
        "hugoSymbol": "STK11",
        "nNGM": {
            "grch37RefSeq": "NM_000455.5",
            "hugoSymbol": "STK11",
            "exonCount": 10,
            "expVariants": 38,
            "exons": {
                1: {
                    "expVariants": 13,
                },
                2: {
                    "expVariants": 0,
                },
                3: {
                    "expVariants": 4,
                },
                4: {
                    "expVariants": 4,
                },
                5: {
                    "expVariants": 1,
                },
                6: {
                    "expVariants": 5,
                },
                7: {
                    "expVariants": 1,
                },
                8: {
                    "expVariants": 4,
                },
                9: {
                    "expVariants": 2,
                },
            },
        },
    },

    {
        "hugoSymbol": "TP53",
        "nNGM": {
            "grch37RefSeq": "NM_000546.6",
            "hugoSymbol": "TP53",
            "exonCount": 11,
            "expVariants": 2225,
            "exons": {
                4: {
                    "expVariants": 486,
                },
                5: {
                    "expVariants": 474,
                },
                6: {
                    "expVariants": 281,
                },
                7: {
                    "expVariants": 267,
                },
                8: {
                    "expVariants": 318,
                },
            },
        },
    },

]


def strip(string):
    return string.replace("\n", "").replace("\t", "").replace(" ", "")




def populateJAXCKB(panel):
    assert isinstance(panel,list)
    # os.popen( "git clone https://github.com/znestor/ckb.jax.org" )

    # https://stackoverflow.com/a/10378012
    path = "ckb.jax.org/geneVariant/"
    directory = os.fsencode(path)

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.startswith("show"):

            content = os.popen("cat {0}/{1}".format(path, filename)).read()
            soup = BeautifulSoup(content, features="lxml")

            hugoSymbol = strip( soup.find(class_="btn btn-default btn-gene").get_text() )
            print(hugoSymbol)

            try:
                JAXCKB = dict( (strip( elem.td.get_text() ), strip(elem.td.find_next_sibling().get_text()) ) for elem in soup.find(id="TranscriptTabTable").children if getattr(elem, "name", None) == "tr" )
                for panelItem in panel:
                    if panelItem["hugoSymbol"] == hugoSymbol:
                        panelItem["JAXCKB"] = JAXCKB
                        # if hugoSymbol == "TP53":
                        #     return
            except:
                pass





populateJAXCKB(panel)



def addTranscripts( element, accession, version ):

    _version = 1
    while True: # check all possible versions

        try:

            response = requests.get( "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=fasta_cds_aa&id={0}.{1}".format( accession, _version ) )
            response.raise_for_status()

            fasta = "".join( response.text.split("\n")[1:] ) # remove definition line, leave bare sequence

            element.setdefault("transcripts", {}).setdefault( accession + "." + str(_version), {} ).setdefault( "fasta", fasta )

            time.sleep(1)

            _version += 1

        except:

            if version >= _version:

                raise ValueError("Cound not obtain requested transcript version {0}.{1} from NCBI, stopped at {0}.{2} aborting".format( accession, version, _version ))

            break



def getAllTranscripts(element):
    assert isinstance(element,dict)

    transcripts = dict()

    file = open("transcripts.fasta", "w")
    file.close()

    # nNGM
    print( element.get("nNGM").get("grch37RefSeq").split(".") )
    ( accession, version ) = element.get("nNGM").get("grch37RefSeq").split(".")

    addTranscripts( element, accession, int(version) )

    print( element.get("oncoKB").get("grch37RefSeq").split(".") )
    ( accession, version ) = element.get("oncoKB").get("grch37RefSeq").split(".")

    addTranscripts( element, accession, int(version) )


    try:
        print( element.get("JAXCKB").get("Transcript").split(".") )
        ( accession, version ) = element.get("JAXCKB").get("Transcript").split(".")

        addTranscripts( element, accession, int(version) )
    except:
        pass

    blastAllTranscripts( element )

    print( element )


def blastAllTranscripts( element ):

    with open("transcripts.fasta", "w") as file:

        for transcriptID, value in element["transcripts"].items():
            file.write( ">{0}\n{1}\n".format( transcriptID, value["fasta"] ) )

    file.close()

    os.popen("diamond makedb --in transcripts.fasta --db transcripts").read()
    for line in os.popen("diamond blastp --query transcripts.fasta --db transcripts --masking 0 --max-target-seqs 0 --outfmt 6 qseqid sseqid pident").readlines():
        ( query, subject, score ) = line.rstrip().split()

        element["transcripts"].setdefault( query, {} ).setdefault( subject, float(score) )



def populateOncoKB(panel):
    assert isinstance(panel,list)
    headers = { "Authorization": "Bearer ANON" }
    response = requests.get( "https://www.oncokb.org/api/v1/utils/allCuratedGenes", headers=headers )
    for panelItem in panel:
        for apiItem in response.json():
            if panelItem["hugoSymbol"] == apiItem["hugoSymbol"]:
                panelItem["oncoKB"] = apiItem


populateOncoKB(panel)


print(panel)




for element in panel:

    getAllTranscripts(element)

    for exonNR in range(1, element["nNGM"]["exonCount"]+1):
                                              #|EXON/TOTALEX||TRANSCRIPT|
                                                    #[0-9]*/*[0-9]* has to be there, because some variants match exon AND an intron at the same time
        expVariants = element["nNGM"]["exons"].setdefault(exonNR, {"expVariants": "Not profiled", "obsVariants": "Not profiled"}).get("expVariants")
        obsVariants = int( os.popen('grep -c "|{0}/{1}|[0-9]*/*[0-9]*|{2}" ../output/output.test_hg19_VEP_RefSeq.vcf '.format( exonNR, element["nNGM"]["exonCount"], element["nNGM"]["grch37RefSeq"] ) ).read() )

        if str(expVariants) != "Not profiled":
            difference = obsVariants - expVariants
            if difference != 0:
                print( "Warning, for {0}, exon {1} expected {2}, got {3} calls".format( element["nNGM"]["grch37RefSeq"], exonNR, element["nNGM"]["exons"].get(exonNR).get("expVariants"), int(obsVariants) ) )
            element["nNGM"]["exons"].get(exonNR)["obsVariants"] = obsVariants




with open("test.template") as file:
    template = Template(file.read())
html = template.render( panel = json.dumps( panel, indent=4, sort_keys=True ) )
file.close()

with open("test.html", "w") as file:
    file.write( html )
file.close()


# print( json.dumps( panel, indent=4, sort_keys=True ) )


for element in panel:

    for exonNR in range(1, element["nNGM"]["exonCount"]+1):
                                              #|EXON/TOTALEX||TRANSCRIPT|
                                                    #[0-9]*/*[0-9]* has to be there, because some variants match exon AND an intron at the same time
        expVariants = element["nNGM"]["exons"].setdefault(exonNR, {"expVariants": "Not profiled", "obsVariants": "Not profiled"}).get("expVariants")
        obsVariants = int( os.popen('grep -c "|{0}/{1}|[0-9]*/*[0-9]*|{2}" ../output/output.test_hg19_VEP_RefSeq.vcf '.format( exonNR, element["nNGM"]["exonCount"], element["nNGM"]["grch37RefSeq"] ) ).read() )

        if str(expVariants) != "Not profiled":
            difference = obsVariants - expVariants
            if difference != 0:
                print( "Warning, for {0}, exon {1} expected {2}, got {3} calls".format( element["nNGM"]["grch37RefSeq"], exonNR, element["nNGM"]["exons"].get(exonNR).get("expVariants"), int(obsVariants) ) )
            element["nNGM"]["exons"].get(exonNR)["obsVariants"] = obsVariants
