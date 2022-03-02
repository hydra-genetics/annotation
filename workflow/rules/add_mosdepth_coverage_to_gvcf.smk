# vim: syntax=python tabstop=4 expandtab
# coding: utf-8

__author__ = "Jonas Almlöf"
__copyright__ = "Copyright 2022, Jonas Almlöf"
__email__ = "jonas.almlof@igp.uu.se"
__license__ = "GPL-3"


rule add_mosdepth_coverage_to_gvcf:
    input:
        coverage="qc/mosdepth_bed/{sample}_{type}.per-base.bed.gz",
        gvcf="snv_indels/mutect2_gvcf/{sample}_{type}.merged.gvcf.gz",
    output:
        gvcf=temp("qc/add_mosdepth_coverage_to_gvcf/{sample}_{type}.mosdepth.gvcf.gz"),
    log:
        "qc/add_mosdepth_coverage_to_gvcf/{sample}_{type}.mosdepth.gvcf.gz.log",
    threads: config.get("add_mosdepth_coverage_to_gvcf", {}).get("threads", config["default_resources"]["threads"])
    resources:
        threads=config.get("add_mosdepth_coverage_to_gvcf", {}).get("threads", config["default_resources"]["threads"]),
        time=config.get("add_mosdepth_coverage_to_gvcf", {}).get("time", config["default_resources"]["time"]),
        mem_mb=config.get("add_mosdepth_coverage_to_gvcf", {}).get("mem_mb", config["default_resources"]["mem_mb"]),
        mem_per_cpu=config.get("add_mosdepth_coverage_to_gvcf", {}).get("mem_per_cpu", config["default_resources"]["mem_per_cpu"]),
        partition=config.get("hotspadd_mosdepth_coverage_to_gvcfot_info", {}).get(
            "partition", config["default_resources"]["partition"]
        ),
    benchmark:
        repeat(
            "qc/add_mosdepth_coverage_to_gvcf/{sample}_{type}.mosdepth.gvcf.gz.benchmark.tsv",
            config.get("add_mosdepth_coverage_to_gvcf", {}).get("benchmark_repeats", 1),
        )
    conda:
        "../envs/add_mosdepth_coverage_to_gvcf.yaml"
    container:
        config.get("add_mosdepth_coverage_to_gvcf", {}).get("container", config["default_container"])
    message:
        "{rule}: Add mosdepth read depth info to: qc/add_mosdepth_coverage_to_gvcf/{wildcards.sample}_{wildcards.type}"
    script:
        "../scripts/add_mosdepth_coverage_to_gvcf.py"
