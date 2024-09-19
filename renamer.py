#!/usr/bin/env python3
import sys
import urllib.request
from io import StringIO
import os

import pandas as pd

#global variables
NCBI_URL = "https://ftp.ncbi.nlm.nih.gov/genomes/all/"

def report_downloader(acc, url, r_file):
    """download assembly report from NCBI ftp"""
    acc_split = acc.split("_")
    prefix = acc_split[0]
    suffix = acc_split[1]
    suffix1 = suffix[0:3]
    suffix2 = suffix[3:6]
    suffix3 = suffix[6:9]
    suffix4 = suffix.split(".")[0]
    while suffix4.startswith("0"):
        suffix4 = suffix4[1:]
    suffix4 = suffix4[0:-1]
    version = suffix.split(".")[1]
    assembly_url = url+prefix+"/"+suffix1+"/"+suffix2+"/"+suffix3+"/"+acc+"_ASM"+suffix4+"v"+version+"/"+acc+"_ASM"+suffix4+"v"+version+"_assembly_report.txt"
    urllib.request.urlretrieve(assembly_url, r_file)

#create equivalencies table
def parse_assembly_report(r_file):
    """extract information about chromosome/plasmids names and accession numbers"""
    new_string = ""
    with open(r_file, encoding = "utf-8") as infile:
        for line in infile.readlines():
            if line.startswith("#"):
                continue
            else:
                new_string += line
    print(new_string)

    #convert string for pandas
    string_data = StringIO(new_string)
    df = pd.read_csv(string_data, header = None, sep = "\t", usecols = [0,4,6], names = ["Sequence-Name","GenBank-Accn","RefSeq-Accn"])
    conversion_dict = {}
    for index,row in df.iterrows():
        conversion_dict[row["GenBank-Accn"]] = row["Sequence-Name"]
        conversion_dict[row["RefSeq-Accn"]] = row["Sequence-Name"]
    print(conversion_dict)
    return(conversion_dict)

#rename vcf file
def rename_vcf(conversion, vcf):
    """substitutes the accession numbers in the vcf file for the Sequence-Name used by SnpEff"""
    with open(vcf, encoding = "utf-8") as infile:
        data = infile.read()
        for k,v in conversion.items():
            data = data.replace(k,v)
    out_vcf = vcf.replace(".vcf","_fixed.vcf")
    with open(out_vcf, "w", encoding = "utf-8") as outfile:
        outfile.write(data)

#main function
if __name__ == "__main__":
    accession_number = sys.argv[1]
    vcf_file = sys.argv[2]
    output_folder = os.path.dirname(vcf_file)
    report_file = output_folder+"/assembly_report.txt"
    report_downloader(accession_number, NCBI_URL, report_file)
    conversion_table = parse_assembly_report(report_file)
    rename_vcf(conversion_table, vcf_file)