"Example TPM3-NTRK1 fusion drawn from previous VICC Fusion Curation draft material.Represented in nomenclature as refseq:NM_152263.3(TPM3):e.8::refseq:NM_002529.3(NTRK1):e.10 "



{  # NOTE: specifing the context of the gene fusions
    "type": "AssayedFusion",
    # NOTE: List that contains two structural elements
    "structural_elements": [
      {
        # NOTE: Seems to me this is the Segment Boundary object
        "type": "TranscriptSegmentElement",
        "transcript": "refseq:NM_152263.3",
        "exon_end": 8,
        "exon_end_offset": 0,

        # NOTE: This is optional: 
        "gene_descriptor": {
          "id": "normalize.gene:TPM3", # what the user searched for 
          "type": "GeneDescriptor",
          "label": "TPM3",# what we were hoping to find 
          "gene_id": "hgnc:12012"
        },

        # NOTE: Would this be the end of of TPM3. 
        "element_genomic_end": { # is this representing the 3' segment boudnary because its the end?
          "id": "fusor.location_descriptor:NC_000001.11", # extra info 
          "type": "LocationDescriptor", # extra info 
          "label": "NC_000001.11", # extra info 

          # NOTE: Genomic location:  Location: pulled from the VRS Schema.
          "location": {
            "type": "SequenceLocation",
            "sequence_id": "refseq:NC_000001.11",
            "interval": {
              "type": "SequenceInterval",
              "start": {
                "type": "Number",
                "value": 154170399
              },
              "end": {
                "type": "Number",
                "value": 154170400
              }
            }
          }


        }
      },
      {
        "type": "TranscriptSegmentElement",
        "transcript": "refseq:NM_002529.3",
        "exon_start": 10,
        "exon_start_offset": 0,
        "gene_descriptor": {
          "id": "normalize.gene:NTRK1",
          "type": "GeneDescriptor",
          "label": "NTRK1",
          "gene_id": "hgnc:8031"
        },
        "element_genomic_start": {
          "id": "fusor.location_descriptor:NC_000001.11",
          "type": "LocationDescriptor",
          "label": "NC_000001.11",
          "location": {
            "type": "SequenceLocation",
            "sequence_id": "refseq:NC_000001.11",
            "interval": {
              "type": "SequenceInterval",
              "start": {
                "type": "Number",
                "value": 156874626
              },
              "end": {
                "type": "Number",
                "value": 156874627
              }
            }
          }
        }
      }
    ],
    # NOTE: everything below here describes the Context of this gene fusion. For this example this is an Assay
    "causative_event": {
      "type": "CausativeEvent",
      "event_type": "rearrangement"
    },
    "assay": {
      "type": "Assay",
      "assay_name": "fluorescence in-situ hybridization assay",
      "assay_id": "obi:OBI_0003094",
      "fusion_detection": "inferred",
      "method_uri": "pmid:33576979"
    },
    "regulatory_elements": []
  }







# this object is non-sense and has been deleted- made up fusions 
"epcam_msh2.json: Example EPCAM-MSH2 fusion. Represented in nomenclature as refseq:NM_002354.2(EPCAM):e.5::AGGCTCCCTTGG::refseq:NM_000251.2(MSH2):e.2."

{
    "type": "CategoricalFusion",
    "critical_functional_domains": [],
    "structural_elements": [
      {
        "type": "TranscriptSegmentElement",
        "transcript": "refseq:NM_002354.2",
        "exon_end": 5,
        "exon_end_offset": 0,
        "gene_descriptor": {
          "id": "normalize.gene:EPCAM",
          "type": "GeneDescriptor",
          "label": "EPCAM",
          "gene_id": "hgnc:11529"
        },
        "element_genomic_end": {
          "id": "fusor.location_descriptor:NC_000002.12",
          "type": "LocationDescriptor",
          "label": "NC_000002.12",
          "location": {
            "type": "SequenceLocation",
            "sequence_id": "refseq:NC_000002.12",
            "interval": {
              "type": "SequenceInterval",
              "start": {
                "type": "Number",
                "value": 47377013
              },
              "end": {
                "type": "Number",
                "value": 47377014
              }
            }
          }
        }
      },
      {
        "type": "LinkerSequenceElement",
        "linker_sequence": {
          "id": "fusor.sequence:AGGCTCCCTTGG", # user entered this
          "type": "SequenceDescriptor", 
          "sequence": "AGGCTCCCTTGG", 
          "residue_type": "SO:0000348" # this is the user output 
        }
      },
      {
        "type": "TranscriptSegmentElement",
        "transcript": "refseq:NM_000251.2",
        "exon_start": 2,
        "exon_start_offset": 0,
        "gene_descriptor": {
          "id": "normalize.gene:MSH2",
          "type": "GeneDescriptor",
          "label": "MSH2",
          "gene_id": "hgnc:7325"
        },
        "element_genomic_start": {
          "id": "fusor.location_descriptor:NC_000002.12",
          "type": "LocationDescriptor",
          "label": "NC_000002.12",
          "location": {
            "type": "SequenceLocation",
            "sequence_id": "refseq:NC_000002.12",
            "interval": {
              "type": "SequenceInterval",
              "start": {
                "type": "Number",
                "value": 47408555
              },
              "end": {
                "type": "Number",
                "value": 47408556
              }
            }
          }
        }
      }
    ],
    "regulatory_elements": []
  }


"tpm3_pdgfrb.json: Example fusion TPM3 fusion. Represented in nomenclature as refseq:NM_152263.3(TPM3):e.8::refseq:NM_002609.3(PDGFRB):e.11"

{
    "type": "CategoricalFusion",
    "critical_functional_domains": [],
    "structural_elements": [
      {
        "type": "TranscriptSegmentElement",
        "transcript": "refseq:NM_152263.3",
        "exon_end": 8,
        "exon_end_offset": 0,
        "gene_descriptor": {
          "id": "normalize.gene:TPM3",
          "type": "GeneDescriptor",
          "label": "TPM3",
          "gene_id": "hgnc:12012"
        },
        "element_genomic_end": {
          "id": "fusor.location_descriptor:NC_000001.11",
          "type": "LocationDescriptor",
          "label": "NC_000001.11",
          "location": {
            "type": "SequenceLocation",
            "sequence_id": "refseq:NC_000001.11",
            "interval": {
              "type": "SequenceInterval",
              "start": {
                "type": "Number",
                "value": 154170399
              },
              "end": {
                "type": "Number",
                "value": 154170400
              }
            }
          }
        }
      },
      {
        "type": "TranscriptSegmentElement",
        "transcript": "refseq:NM_002609.3",
        "exon_start": 11,
        "exon_start_offset": 0,
        "gene_descriptor": {
          "id": "normalize.gene:PDGFRB",
          "type": "GeneDescriptor",
          "label": "PDGFRB",
          "gene_id": "hgnc:8804"
        },
        "element_genomic_start": {
          "id": "fusor.location_descriptor:NC_000005.10",
          "type": "LocationDescriptor",
          "label": "NC_000005.10",
          "location": {
            "type": "SequenceLocation",
            "sequence_id": "refseq:NC_000005.10",
            "interval": {
              "type": "SequenceInterval",
              "start": {
                "type": "Number",
                "value": 150125577
              },
              "end": {
                "type": "Number",
                "value": 150125578
              }
            }
          }
        }
      }
    ],
    "regulatory_elements": []
  }




#NOTE: for regulatory elements you can either have a feature ID or a Feature location.
# must have everything else. 
{
  "type": "CategoricalFusion",
  "regulatory_element": {
    "type": "RegulatoryElement",
    "regulatory_class": "enhancer",
    "associatted_gene": { # optional, this is a nomenclature 
      "type": "GeneDescriptor",
      "label": "IGH",
      "gene_id": "hgnc:5477",
      "id": "normalize.gene:IGH"
    },
    "feature_id": "EH38E3121735"
  },
  "structural_elements": [
    {
      "type": "GeneElement",
      "gene_descriptor": {
        "type": "GeneDescriptor",
        "label": "MYC",
        "gene_id": "hgnc:7553",
        "id": "normalize.gene:MYC"
      }
    }
  ]
}

