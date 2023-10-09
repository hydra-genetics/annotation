__author__ = "Jonas Almlöf"
__copyright__ = "Copyright 2021, Jonas Almlöf"
__email__ = "jonas.almlof@scilifelab.uu.se"
__license__ = "GPL-3"


rule background_annotation:
    input:
        background=config.get("reference").get("background", ""),
        vcf="{file}.vcf",
    output:
        vcf=temp("{file}.background_annotated.vcf"),
    params:
        nr_min_sd=config.get("background_annotated", {}).get("nr_min_sd", 5),
    log:
        "{file}.background_annotated.vcf.log",
    benchmark:
        repeat(
            "{file}.background_annotated.vcf.benchmark.tsv",
            config.get("background_annotation", {}).get("benchmark_repeats", 1),
        )
    threads: config.get("background_annotation", {}).get("threads", config["default_resources"]["threads"])
    resources:
        mem_mb=config.get("background_annotation", {}).get("mem_mb", config["default_resources"]["mem_mb"]),
        mem_per_cpu=config.get("background_annotation", {}).get("mem_per_cpu", config["default_resources"]["mem_per_cpu"]),
        partition=config.get("background_annotation", {}).get("partition", config["default_resources"]["partition"]),
        threads=config.get("background_annotation", {}).get("threads", config["default_resources"]["threads"]),
        time=config.get("background_annotation", {}).get("time", config["default_resources"]["time"]),
    container:
        config.get("background_annotation", {}).get("container", config["default_container"])
    message:
        "{rule}: background annotation of vcf in {output.vcf}"
    script:
        "../scripts/background_annotation.py"
