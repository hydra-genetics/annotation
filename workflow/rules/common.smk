__author__ = "Jonas A"
__copyright__ = "Copyright 2021, Jonas A"
__email__ = "jonas.almlof@igp.uu.se"
__license__ = "GPL-3"

import pandas as pd
from snakemake.utils import validate
from snakemake.utils import min_version

from hydra_genetics.utils.resources import load_resources
from hydra_genetics.utils.samples import *
from hydra_genetics.utils.units import *

min_version("7.13.0")

### Set and validate config file

if not workflow.overwrite_configfiles:
    sys.exit("At least one config file must be passed using --configfile/--configfiles, by command line or a profile!")


validate(config, schema="../schemas/config.schema.yaml")
config = load_resources(config, config["resources"])
validate(config, schema="../schemas/resources.schema.yaml")


### Read and validate samples file

samples = pd.read_table(config["samples"], dtype=str).set_index("sample", drop=False)
validate(samples, schema="../schemas/samples.schema.yaml")

### Read and validate units file

units = (
    pandas.read_table(config["units"], dtype=str)
    .set_index(["sample", "type", "flowcell", "lane", "barcode"], drop=False)
    .sort_index()
)

### Set wildcard constraints


wildcard_constraints:
    barcode="[A-Z+]+",
    flowcell="[A-Z0-9]+",
    lane="L[0-9]+",
    sample="|".join(get_samples(samples)),
    type="N|T|R",
    tag="[^.]+",


def compile_output_list(wildcards):
    files = {
        "qc/add_mosdepth_coverage_to_gvcf": [".mosdepth.g.vcf"],
        "snv_indels/bcbio_variation_recall_ensemble": [".ensembled.vep_annotated.vcf", ".ensembled.ssa.vcf"],
        "annotation/background_annotation": [".background_annotation.vcf.gz", ".background_annotation.vcf.gz.tbi"],
        "annotation/add_multi_snv_in_codon": [".background_annotation.include.exon.filter.snv_hard_filter.codon_snvs.sorted.vcf"],
        "cnv_sv/stranger": [".stranger.vcf"],
        "cnv_sv/svdb_query": [".svdb_query.annotate_cnv.cnv_amp_genes.vcf"],
        "annotation/background_annotation": [".background_annotation.bcftools_annotated.vcf.gz"],
    }
    output_files = [
        "%s/%s_%s%s" % (prefix, sample, unit_type, suffix)
        for prefix in files.keys()
        for sample in get_samples(samples)
        for unit_type in get_unit_types(units, sample)
        for suffix in files[prefix]
    ]
    output_files.append(["annotation/calculate_seqrun_background/%s_seqrun_background.tsv" % ("1")])
    return output_files
