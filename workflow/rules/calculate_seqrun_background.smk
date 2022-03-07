# vim: syntax=python tabstop=4 expandtab
# coding: utf-8

__author__ = "Jonas Almlöf"
__copyright__ = "Copyright 2021, Jonas Almlöf"
__email__ = "jonas.almlof@scilifelab.uu.se"
__license__ = "GPL-3"


rule calculate_seqrun_background:
    input:
        gvcfs=lambda wildcards: [
            "snv_indels/mutect2_gvcf/%s_%s.merged.gvcf.gz" % sample_run
            for sample_run in get_units_per_flowcell(units, wildcards)
        ],
    output:
        background=temp("annotation/calculate_seqrun_background/{flowcell}_seqrun_background.tsv"),
    params:
        type="seqrun",
    log:
        "annotation/calculate_seqrun_background/{flowcell}_seqrun_background.tsv.log",
    benchmark:
        repeat(
            "annotation/calculate_seqrun_background/{flowcell}_seqrun_background.tsv.benchmark.tsv",
            config.get("calculate_seqrun_background", {}).get("benchmark_repeats", 1),
        )
    threads: config.get("calculate_seqrun_background", {}).get("threads", config["default_resources"]["threads"])
    resources:
        threads=config.get("calculate_seqrun_background", {}).get("threads", config["default_resources"]["threads"]),
        time=config.get("calculate_seqrun_background", {}).get("time", config["default_resources"]["time"]),
        mem_mb=config.get("calculate_seqrun_background", {}).get("mem_mb", config["default_resources"]["mem_mb"]),
        mem_per_cpu=config.get("calculate_seqrun_background", {}).get("mem_per_cpu", config["default_resources"]["mem_per_cpu"]),
        partition=config.get("calculate_seqrun_background", {}).get("partition", config["default_resources"]["partition"]),
    container:
        config.get("calculate_seqrun_background", {}).get("container", config["default_container"])
    conda:
        "../envs/calculate_seqrun_background.yaml"
    message:
        "{rule}: Calculate background for the sequencing run: annotation/calculate_seqrun_background/{wildcards.flowcell}_seqrun_background.tsv"
    script:
        "../scripts/calculate_background.py"
