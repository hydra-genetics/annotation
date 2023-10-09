__author__ = "Jonas Almlöf"
__copyright__ = "Copyright 2021, Jonas Almlöf"
__email__ = "jonas.almlof@scilifelab.uu.se"
__license__ = "GPL-3"


rule artifact_annotation:
    input:
        artifacts=config.get("reference", {}).get("artifacts", ""),
        vcf="{file}.vcf",
    output:
        vcf=temp("{file}.artifact_annotated.vcf"),
    log:
        "{file}.artifact_annotated.vcf.log",
    benchmark:
        repeat(
            "{file}.artifact_annotated.vcf.benchmark.tsv",
            config.get("artifact_annotated", {}).get("benchmark_repeats", 1),
        )
    threads: config.get("artifact_annotation", {}).get("threads", config["default_resources"]["threads"])
    resources:
        mem_mb=config.get("artifact_annotation", {}).get("mem_mb", config["default_resources"]["mem_mb"]),
        mem_per_cpu=config.get("artifact_annotation", {}).get("mem_per_cpu", config["default_resources"]["mem_per_cpu"]),
        partition=config.get("artifact_annotation", {}).get("partition", config["default_resources"]["partition"]),
        threads=config.get("artifact_annotation", {}).get("threads", config["default_resources"]["threads"]),
        time=config.get("artifact_annotation", {}).get("time", config["default_resources"]["time"]),
    container:
        config.get("artifact_annotation", {}).get("container", config["default_container"])
    message:
        "{rule}: artifact annotation of vcf in {output.vcf}"
    script:
        "../scripts/artifact_annotation.py"
