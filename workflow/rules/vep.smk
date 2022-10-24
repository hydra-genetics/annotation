# vim: syntax=python tabstop=4 expandtab
# coding: utf-8

__author__ = "Jonas Almlöf"
__copyright__ = "Copyright 2021, Jonas Almlöf"
__email__ = "jonas.almlof@scilifelab.uu.se"
__license__ = "GPL-3"


rule vep:
    input:
        cache=config.get("vep", {}).get("vep_cache", ""),
        fasta=config["reference"]["fasta"],
        tabix="{file}.vcf.gz.tbi",
        vcf="{file}.vcf.gz",
    output:
        vcf=temp("{file}.vep_annotated.vcf"),
    params:
        extra=config.get("vep", {}).get("extra", "--pick"),
        mode=config.get("vep", {}).get("mode", "--offline --cache"),
    log:
        "{file}.vep_annotated.vcf.log",
    benchmark:
        repeat("{file}.vep_annotated.vcf.benchmark.tsv", config.get("vep", {}).get("benchmark_repeats", 1))
    threads: config.get("vep", {}).get("threads", config["default_resources"]["threads"])
    resources:
        mem_mb=config.get("vep", {}).get("mem_mb", config["default_resources"]["mem_mb"]),
        mem_per_cpu=config.get("vep", {}).get("mem_per_cpu", config["default_resources"]["mem_per_cpu"]),
        partition=config.get("vep", {}).get("partition", config["default_resources"]["partition"]),
        threads=config.get("vep", {}).get("threads", config["default_resources"]["threads"]),
        time=config.get("vep", {}).get("time", config["default_resources"]["time"]),
    container:
        config.get("vep", {}).get("container", config["default_container"])
    conda:
        "../envs/vep.yaml"
    message:
        "{rule}: vep annotate {input.vcf}"
    shell:
        "(vep "
        "--vcf "
        "--no_stats "
        "-o {output.vcf} "
        "-i {input.vcf} "
        "--dir_cache {input.cache} "
        "--fork {threads} "
        "--refseq {params.mode} "
        "--fasta {input.fasta} "
        "{params.extra} ) &> {log}"
