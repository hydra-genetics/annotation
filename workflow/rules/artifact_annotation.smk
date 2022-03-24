__author__ = "Jonas Almlöf"
__copyright__ = "Copyright 2021, Jonas Almlöf"
__email__ = "jonas.almlof@scilifelab.uu.se"
__license__ = "GPL-3"


rule artifact_annotation:
    input:
        vcf="annotation/add_multi_snv_in_codon/{sample}_{type}.codon_snvs.sorted.vep_annotated.vcf",
        artifacts=config.get("reference", {}).get("artifacts", ""),
    output:
        vcf=temp("annotation/artifact_annotation/{sample}_{type}.artifact_annotation.vcf"),
    log:
        "annotation/artifact_annotation/{sample}_{type}.artifact_annotation.vcf.log",
    benchmark:
        repeat(
            "annotation/artifact_annotation/{sample}_{type}.artifact_annotation.vcf.benchmark.tsv",
            config.get("artifact_annotation", {}).get("benchmark_repeats", 1),
        )
    threads: config.get("artifact_annotation", {}).get("threads", config["default_resources"]["threads"])
    resources:
        threads=config.get("artifact_annotation", {}).get("threads", config["default_resources"]["threads"]),
        time=config.get("artifact_annotation", {}).get("time", config["default_resources"]["time"]),
        mem_mb=config.get("artifact_annotation", {}).get("mem_mb", config["default_resources"]["mem_mb"]),
        mem_per_cpu=config.get("artifact_annotation", {}).get("mem_per_cpu", config["default_resources"]["mem_per_cpu"]),
        partition=config.get("artifact_annotation", {}).get("partition", config["default_resources"]["partition"]),
    container:
        config.get("artifact_annotation", {}).get("container", config["default_container"])
    conda:
        "../envs/artifact_annotation.yaml"
    message:
        "{rule}: artifact annotation vcf in annotation/artifact_annotation/{wildcards.sample}_{wildcards.type}"
    script:
        "../scripts/artifact_annotation.py"
