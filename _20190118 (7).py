import sys
inname, outname = (
    "_20190118in.txt", "_20190118out.txt"
)

with open(inname) as infile:
    with open(outname, "w") as outfile:
        warnings = (
            i.replace("\tWARNING", "") for i in infile if "WARNING" in i 
        )
        for i in warnings:
            print(i)