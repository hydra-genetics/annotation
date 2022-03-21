# vim: syntax=python tabstop=4 expandtab
# coding: utf-8

__author__ = "Jonas Almlöf"
__copyright__ = "Copyright 2021, Jonas Almlöf"
__email__ = "jonas.almlof@scilifelab.uu.se"
__license__ = "GPL-3"


rule add_multi_snv_in_codon:
    input:
        vcf="snv_indels/ensemble_vcf/{sample}_{type}.ensembled.vep_annotated.vcf",
        ref=config["reference"]["fasta"],
    output:
        vcf=temp("annotation/add_multi_snv_in_codon/{sample}_{type}.codon_snvs.vcf"),
    params:
        af_limit=config.get("add_multi_snv_in_codon", {}).get("af_limit", 0.05),
    log:
        "annotation/add_multi_snv_in_codon/{sample}_{type}.codon_snvs.vcf.log",
    benchmark:
        repeat(
            "annotation/add_multi_snv_in_codon/{sample}_{type}.codon_snvs.vcf.benchmark.tsv",
            config.get("add_multi_snv_in_codon", {}).get("benchmark_repeats", 1),
        )
    threads: config.get("add_multi_snv_in_codon", {}).get("threads", config["default_resources"]["threads"])
    resources:
        threads=config.get("add_multi_snv_in_codon", {}).get("threads", config["default_resources"]["threads"]),
        time=config.get("add_multi_snv_in_codon", {}).get("time", config["default_resources"]["time"]),
        mem_mb=config.get("add_multi_snv_in_codon", {}).get("mem_mb", config["default_resources"]["mem_mb"]),
        mem_per_cpu=config.get("add_multi_snv_in_codon", {}).get("mem_per_cpu", config["default_resources"]["mem_per_cpu"]),
        partition=config.get("add_multi_snv_in_codon", {}).get("partition", config["default_resources"]["partition"]),
    container:
        config.get("add_multi_snv_in_codon", {}).get("container", config["default_container"])
    conda:
        "../envs/add_multi_snv_in_codon.yaml"
    message:
        "{rule}: Add multivariants to vcf if they ar in same codon: annotation/add_multi_snv_in_codon/{wildcards.sample}_{wildcards.type}"
    script:
        "../scripts/add_multi_snv_in_codon.py"
