# vim: syntax=python tabstop=4 expandtab
# coding: utf-8

__author__ = "Jonas Almlöf"
__copyright__ = "Copyright 2021, Jonas Almlöf"
__email__ = "jonas.almlof@scilifelab.uu.se"
__license__ = "GPL-3"


rule calculate_run_background:
    input:
        gvcfs=lambda wildcards: [
            "snv_indels/mutect2_gvcf/%s_%s.merged.gvcf.gz" % sample_run for sample_run in get_units_per_run(units, wildcards)
        ],
    output:
        background=temp("annotation/calculate_run_background/{run}_run_background.tsv"),
    params:
        type="run",
    log:
        "annotation/calculate_run_background/{run}_run_background.tsv.log",
    benchmark:
        repeat(
            "annotation/calculate_run_background/{run}_run_background.tsv.benchmark.tsv",
            config.get("calculate_run_background", {}).get("benchmark_repeats", 1),
        )
    threads: config.get("calculate_run_background", config["default_resources"]).get("threads", config["default_resources"]["threads"])
    container:
        config.get("calculate_run_background", {}).get("container", config["default_container"])
    conda:
        "../envs/calculate_run_background.yaml"
    message:
        "{rule}: Calculate background for the sequencing run: annotation/calculate_run_background/{wildcards.run}_run_background.tsv"
    script:
        "../scripts/calculate_background.py"
