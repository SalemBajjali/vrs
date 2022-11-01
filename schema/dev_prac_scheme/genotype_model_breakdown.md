Example is from: https://www.ncbi.nlm.nih.gov/clinvar/variation/431013/?new_evidence=false
From: Larry Babb on github: https://github.com/ga4gh/vrs/issues/393

Big picture: larry is presenting a example of how he would generate a genotype object.

NM_016035.4(COQ4):c.[23_33delTCCTCCGTCGG];[331G>T;356C>T]



GenotypeMember{
    type: GenotypeMember
    count: 




# GenotypeMember breakdown

# Breakdown step 1: NM_016035.4(COQ4):c.[23_33delTCCTCCGTCGG]
allele 1 
    location: 
        sequenceLocation: 
            Interval: 
                SequenceInterval:
                    Number: 
                        start: 23 
                        end: 33
    state: 
        literalSequenceExpr
            sequence: TCCTCCGTCGG

# Breakdown step 2: NM_016035.4(COQ4):c.[331G>T;356C>T]

Haplotypes 
    [ 
    allele 2 
        location: 
            sequenceLocation: 
                Interval: 
                    SequenceInterval:
                        Number: 
                            start: ~ 
                            end: 331
        state:
            literalSequenceExpr
                sequence: T
    allele 3 
        location: 
            sequenceLocation: 
                Interval: 
                    SequenceInterval:
                        Number: 
                            start: ~
                            end: 356
        state:
            literalSequenceExpr
                sequence: T
    ]
    
]
}






# Genotype breakdown
{
    type: "Genotype"
    members:,
    count: {
        type: Number, 
        value: 
    }
}



# Everything put together
{
    type: "Genotype",
    members: 
    [{
        type: "GenotypeMember",
        count: {
            type: Number
            value: 1
        },
        varation: {
            type: Allele
                location: 
                    sequenceLocation: 
                        Interval: 
                            SequenceInterval:
                                Number: 
                                    start: 23 
                                    end: 33
                state: 
                    literalSequenceExpr
                        sequence: TCCTCCGTCGG
        },
        type: "GenotypeMember",
        count: {
            type: Number
            value: 1 #this should not be 2:  this would be value one because its 1 copy of the haplotype. even though there is two varients that make up that one haplotype, that haplotype only occurs once. 
        },
        varation: {
            type: Haplotype
                    [ 
                    allele 2 
                        location: 
                            sequenceLocation: 
                                Interval: 
                                    SequenceInterval:
                                        Number: 
                                            start: ~ 
                                            end: 331
                        state:
                            literalSequenceExpr
                                sequence: T
                    allele 3 
                        location: 
                            sequenceLocation: 
                                Interval: 
                                    SequenceInterval:
                                        Number: 
                                            start: ~
                                            end: 356
                        state:
                            literalSequenceExpr
                                sequence: T
                    ]
        },  
    }]
    count: {
        type: Number, 
        value: 2
    }

}

If greater than the total counts, this implies additional Molecular Variation that are expected to exist but are not explicitly indicated.

benign polymorphism 


VRS does not define a diplotype class: 
- most people will assume we have two copies of a given locis
- we are not forces into that assumption in VRS
- wants us to say what is at this locus. 


This will be reviewed shortly.