# vcf-snpeff-formatter

Tool to format standard VCF files for compatibility with SnpEff.
Solves the error: **Chromosome not found**, when the input VCF file has chromosome names that do not match SnpEff's database.

## Description

Downloads the assembly report from the NCBI, and replaces the original chromosome names in the VCF file for those used by SnpEff tool.

## Requirements

### Docker

Docker image in [dockerhub](https://hub.docker.com/r/lalvarezmunoz/vcf-snpeff-formatter/tags) `lalvarezmunoz/vcf-snpeff-formatter` for direct use.


### Python

- Python >= 3.11.10
- Pandas >= 2.2.2


## Usage

Standard CLI code:

```bash
python3 renamer.py <ACCESSION_NUMBER> <VCF_FILE>
```


Example:

```bash
python3 renamer.py GCA_000092025.1 test.vcf
```

## Input and Output

### Accession number

Assembly accession numbers from NCBI: GCF_xxxxxxxxx.x or GCA_xxxxxxxxx.x

Example:

```bash
Taxon  Agrobacterium fabrum str. C58
NCBI RefSeq assembly  GCF_000092025.1
Submitted GenBank assembly  GCA_000092025.1
```


### Input VCF file

Standard VCF file:

```bash
[...]
AE007869.2	87424	.	C	T	608.949	.	AB=0;ABP=0;AC=1;AF=1;AN=1;AO=19;...
AE007869.2	221771	.	C	T	544.258	.	AB=0;ABP=0;AC=1;AF=1;AN=1;AO=17;...
AE007869.2	242233	.	A	G	345.694	.	AB=0;ABP=0;AC=1;AF=1;AN=1;AO=11;...
AE007870.2	2075552	.	A	G	449.649	.	AB=0;ABP=0;AC=1;AF=1;AN=1;AO=16;...
AE007871.2	101761	.	C	T	447.571	.	AB=0;ABP=0;AC=1;AF=1;AN=1;AO=14;...
AE007871.2	136455	.	G	A	290.434	.	AB=0;ABP=0;AC=1;AF=1;AN=1;AO=9;...
[...]
```

### Output VCF file

Renamed VCF file:

```bash
[...]
circular	87424	.	C	T	608.949	.	AB=0;ABP=0;AC=1;AF=1;AN=1;AO=19;...
circular	221771	.	C	T	544.258	.	AB=0;ABP=0;AC=1;AF=1;AN=1;AO=17;...
circular	242233	.	A	G	345.694	.	AB=0;ABP=0;AC=1;AF=1;AN=1;AO=11;...
linear	2075552	.	A	G	449.649	.	AB=0;ABP=0;AC=1;AF=1;AN=1;AO=16;...
Ti	101761	.	C	T	447.571	.	AB=0;ABP=0;AC=1;AF=1;AN=1;AO=14;...
Ti	136455	.	G	A	290.434	.	AB=0;ABP=0;AC=1;AF=1;AN=1;AO=9;...
[...]
```

### Assembly report file

Assembly report file from NCBI FTP repositories.

Example:
```bash
# Assembly name:  ASM9202v1
# Organism name:  Agrobacterium fabrum str. C58 (a-proteobacteria)
# Infraspecific name:  strain=C58
# Taxid:          176299
# BioSample:      SAMN02603108
# BioProject:     PRJNA283
# Submitter:      Cereon
# Date:           2007-11-05
# Assembly type:  na
# Release type:   major
# Assembly level: Complete Genome
# Genome representation: full
# Relation to type material: assembly from type material
# RefSeq category: Representative Genome
# GenBank assembly accession: GCA_000092025.1
# RefSeq assembly accession: GCF_000092025.1
# RefSeq assembly and GenBank assemblies identical: yes
#
## Assembly-Units:
## GenBank Unit Accession	RefSeq Unit Accession	Assembly-Unit name
## GCA_000092035.1	GCF_000092035.1	Primary Assembly
#
# Ordered by chromosome/plasmid; the chromosomes/plasmids are followed by
# unlocalized scaffolds.
# Unplaced scaffolds are listed at the end.
# RefSeq is equal or derived from GenBank object.
#
# Sequence-Name	Sequence-Role	Assigned-Molecule	Assigned-Molecule-Location/Type	GenBank-Accn	Relationship	RefSeq-Accn	Assembly-Unit	Sequence-Length	UCSC-style-name
circular	assembled-molecule	circular	Chromosome	AE007869.2	=	NC_003062.2	Primary Assembly	2841580	na
linear	assembled-molecule	linear	Chromosome	AE007870.2	=	NC_003063.2	Primary Assembly	2075577	na
At	assembled-molecule	At	Plasmid	AE007872.2	=	NC_003064.2	Primary Assembly	542868	na
Ti	assembled-molecule	Ti	Plasmid	AE007871.2	=	NC_003065.3	Primary Assembly	214233	na
```
