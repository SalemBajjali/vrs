
{
    "Segment":
    [
        {
            "JoinedRegion":
            {
                "Region":
                {
                    "RegionCoordinates":
                    {
                        "Ref":
                        {
                            "GenomeAssembly": "GRCH37",
                            "chromosome": "2"
                        },
                        "Start":
                        {
                            "Min": 431,
                            "Max":481
                        },
                        "Stop":
                        {
                            "Min": 490,
                            "Max":511
                        },
                        "RegionExpression": null
                    },
                    "NamedRegion": null
                },
                "ResidueLiteral": null,
                "copies": null,
                "isInverted": false
            }
        }
    ]
}




# Creating this idea of containerizing segments.


- Idea here is that we start off with a segment
- These segments can be combined together to show the fussion. 

- If segmant 1 bind to segment 2 and segment 3 and 4 are not clinically releavent then all we need to do is represent segment 1 and 2. 
- If segmant 1,2,3,4 are all relavent, then we have create two fussion objects, and then we can containerize these two fussion objects as 1 large molecule. 
- If we are dealing with a case where there segment 1 and 2 create a fussion, but segment 3 is a telemore and sendment 4 is a promoter region that is clinically releavent. Then we can represent seg 1 and 2 as a fussion, segment 4 as a stand alone segment, but we can combine these 3 parts as a larger molecule. 
- If we have a translocation insertion, this means that segment 1 got devided into two parts we would represent this as 3 different segments.

