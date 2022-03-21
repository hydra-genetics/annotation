# vim: syntax=python tabstop=4 expandtab
# coding: utf-8

__author__ = "Jonas Almlöf"
__copyright__ = "Copyright 2021, Jonas Almlöf"
__email__ = "jonas.almlof@scilifelab.uu.se"
__license__ = "GPL-3"


rule background_annotation:
    input:
        vcf="annotation/background_annotation/{sample}_{type}.artifact_annotation.vcf",
        background=config["reference"]["background"],
    output:
        vcf=temp("annotation/background_annotation/{sample}_{type}.background_filter.vcf"),
    params:
        nr_min_sd=config.get("background_annotation", {}).get("nr_min_sd", 5),
    log:
        "annotation/background_annotation/{sample}_{type}.background_annotation.vcf.log",
    benchmark:
        repeat(
            "annotation/background_annotation/{sample}_{type}.background_annotation.vcf.benchmark.tsv",
            config.get("background_annotation", {}).get("benchmark_repeats", 1),
        )
    threads: config.get("background_annotation", {}).get("threads", config["default_resources"]["threads"])
    resources:
        threads=config.get("background_annotation", {}).get("threads", config["default_resources"]["threads"]),
        time=config.get("background_annotation", {}).get("time", config["default_resources"]["time"]),
        mem_mb=config.get("background_annotation", {}).get("mem_mb", config["default_resources"]["mem_mb"]),
        mem_per_cpu=config.get("background_annotation", {}).get("mem_per_cpu", config["default_resources"]["mem_per_cpu"]),
        partition=config.get("background_annotation", {}).get("partition", config["default_resources"]["partition"]),
    container:
        config.get("background_annotation", {}).get("container", config["default_container"])
    conda:
        "../envs/background_annotation.yaml"
    message:
        "{rule}: Background annotation vcf in annotation/background_annotation/{wildcards.sample}_{wildcards.type}"
    script:
        "../scripts/background_annotation.py"
