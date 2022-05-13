__author__ = "Jonas Almlöf"
__copyright__ = "Copyright 2021, Jonas Almlöf"
__email__ = "jonas.almlof@scilifelab.uu.se"
__license__ = "GPL-3"


rule hotspot_annotation:
    input:
        vcf="annotation/add_multi_snv_in_codon/{sample}_{type}.codon_snvs.sorted.vep_annotated.vcf",
        hotspot=config.get("hotspot_annotation", {}).get("hotspots", ""),
        chr_mapping=config.get("hotspot_annotation", {}).get("chr_translation_file", ""),
    output:
        vcf=temp("annotation/hotspot_annotation/{sample}_{type}.hotspot_annotation.vcf"),
    log:
        "annotation/hotspot_annotation/{sample}_{type}.hotspot_annotation.vcf.log",
    benchmark:
        repeat(
            "annotation/hotspot_annotation/{sample}_{type}.hotspot_annotation.vcf.benchmark.tsv",
            config.get("hotspot_annotation", {}).get("benchmark_repeats", 1),
        )
    threads: config.get("hotspot_annotation", {}).get("threads", config["default_resources"]["threads"])
    resources:
        mem_mb=config.get("hotspot_annotation", {}).get("mem_mb", config["default_resources"]["mem_mb"]),
        mem_per_cpu=config.get("hotspot_annotation", {}).get("mem_per_cpu", config["default_resources"]["mem_per_cpu"]),
        partition=config.get("hotspot_annotation", {}).get("partition", config["default_resources"]["partition"]),
        threads=config.get("hotspot_annotation", {}).get("threads", config["default_resources"]["threads"]),
        time=config.get("hotspot_annotation", {}).get("time", config["default_resources"]["time"]),
    container:
        config.get("hotspot_annotation", {}).get("container", config["default_container"])
    conda:
        "../envs/hotspot_annotation.yaml"
    message:
        "{rule}: hotspot annotation vcf in annotation/hotspot_annotation/{wildcards.sample}_{wildcards.type}"
    script:
        "../scripts/add_hotspot_information.py"
