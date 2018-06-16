import json

# Edit this
path="/path/to/qc/"

# Edit this, assuming raw QC files are similarly generated as the ones below
files = {
    "Batch File Request for Alaska off grid Site Class A.csv": "Batch Request Results for Alaska off grid Site Class A.csv",
    "Batch File Request for Alaska off grid Site Class B.csv": "Batch Request Results for Alaska off grid Site Class B.csv",
    "Batch File Request for Alaska off grid Site Class C.csv": "Batch Request Results for Alaska off grid Site Class C.csv",
    "Batch File Request for Alaska off grid Site Class D.csv": "Batch Request Results for Alaska off grid Site Class D.csv",
    "Batch File Request for Alaska off grid Site Class E.csv": "Batch Request Results for Alaska off grid Site Class E.csv",
    "Batch File Request for ConUS off grid Site Class A.csv": "Batch Request Results for ConUS off grid Site Class A.csv",
    "Batch File Request for ConUS off grid Site Class B.csv": "Batch Request Results for ConUS off grid Site Class B.csv",
    "Batch File Request for ConUS off grid Site Class C.csv": "Batch Request Results for ConUS off grid Site Class C.csv",
    "Batch File Request for ConUS off grid Site Class D.csv": "Batch Request Results for ConUS off grid Site Class D.csv",
    "Batch File Request for ConUS off grid Site Class E.csv": "Batch Request Results for ConUS off grid Site Class E.csv",
    "Batch File Request for Hawaii off grid Site Class A.csv": "Batch Request Results for Hawaii off grid Site Class A.csv",
    "Batch File Request for Hawaii off grid Site Class B.csv": "Batch Request Results for Hawaii off grid Site Class B.csv",
    "Batch File Request for Hawaii off grid Site Class C.csv": "Batch Request Results for Hawaii off grid Site Class C.csv",
    "Batch File Request for Hawaii off grid Site Class D.csv": "Batch Request Results for Hawaii off grid Site Class D.csv",
    "Batch File Request for Hawaii off grid Site Class E.csv": "Batch Request Results for Hawaii off grid Site Class E.csv",
    "Batch File Request for PRVI off grid Site Class A.csv": "Batch Request Results for PRVI off grid Site Class A.csv",
    "Batch File Request for PRVI off grid Site Class B.csv": "Batch Request Results for PRVI off grid Site Class B.csv",
    "Batch File Request for PRVI off grid Site Class C.csv": "Batch Request Results for PRVI off grid Site Class C.csv",
    "Batch File Request for PRVI off grid Site Class D.csv": "Batch Request Results for PRVI off grid Site Class D.csv",
    "Batch File Request for PRVI off grid Site Class E.csv": "Batch Request Results for PRVI off grid Site Class E.csv"
} 

qc_arr = []

for key, value in files.items():

    key_lines = []
    value_lines = []

    file = open(path+key, "r")
    for line in file:
        key_lines.append(line)

    file = open(path+value, "r")
    for line in file:
        value_lines.append(line)

    # Iterate over arrays
    for kl in key_lines:

        qc = {
            "request": {
                "referenceDocument": "AASHTO-2009",
                "status": "success",
                "url": "",
                "parameters": {
                    "latitude": 0,
                    "longitude": 0,
                    "riskCategory": "I",
                    "title": "",
                    "siteClass": ""
                }
            },
            "response": {
                "data": {
                    "pga": 0,
                    "fpga": 0,
                    "as": 0,
                    "sds": 0
                }
            }
        }

        key_values = kl.split(",")

        key_lat = key_values[0].strip()
        key_long = key_values[1].strip()
        key_class = key_values[2].strip()
        
        key_class_s = ""
        if (int(key_class) == 0):
            key_class_s = "A"
        if (int(key_class) == 1):
            key_class_s = "B"
        if (int(key_class) == 2):
            key_class_s = "C"
        if (int(key_class) == 3):
            key_class_s = "D"
        if (int(key_class) == 4):
            key_class_s = "E"

        key_area = key_values[4].strip()

        for vl in value_lines:
            value_values = vl.split(",")
            value_lat = value_values[0].strip()
            value_long = value_values[1].strip()

            if ( (key_lat == value_lat) and (key_long == value_long) ):
                value_sc = value_values[2]
                value_pga = value_values[3]
                value_fpga = value_values[6]
                value_as = value_values[9]
                value_sds = value_values[10]

                qc["request"]["parameters"]["latitude"] = value_lat
                qc["request"]["parameters"]["longitude"] = value_long
                qc["request"]["parameters"]["title"] = key_area
                qc["request"]["parameters"]["siteClass"] = key_class_s
                qc["response"]["data"]["pga"] = value_pga
                qc["response"]["data"]["fpga"] = value_fpga
                qc["response"]["data"]["as"] = value_as
                qc["response"]["data"]["sds"] = value_sds

                qc_arr.append(qc)

print(json.dumps(qc_arr, indent=4, sort_keys=False))
#print "Records: " + str(len(qc_arr))
