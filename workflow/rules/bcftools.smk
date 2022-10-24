__author__ = "Jonas Almlöf, Patrik Smeds"
__copyright__ = "Copyright 2021, Jonas Almlöf"
__email__ = "jonas.almlof@scilifelab.uu.se"
__license__ = "GPL-3"


rule sort_vcf:
    input:
        vcf="annotation/add_multi_snv_in_codon/{file}.vcf",
    output:
        vcf=temp("annotation/add_multi_snv_in_codon/{file}.sorted.vcf"),
    log:
        "annotation/add_multi_snv_in_codon/{file}.sorted.vcf.gz.log",
    benchmark:
        repeat(
            "annotation/add_multi_snv_in_codon/{file}.sorted.vcf.gz.benchmark.tsv",
            config.get("sort_vcf", {}).get("benchmark_repeats", 1),
        )
    threads: config.get("sort_vcf", {}).get("threads", config["default_resources"]["threads"])
    resources:
        mem_mb=config.get("sort_vcf", {}).get("mem_mb", config["default_resources"]["mem_mb"]),
        mem_per_cpu=config.get("sort_vcf", {}).get("mem_per_cpu", config["default_resources"]["mem_per_cpu"]),
        partition=config.get("sort_vcf", {}).get("partition", config["default_resources"]["partition"]),
        threads=config.get("sort_vcf", {}).get("threads", config["default_resources"]["threads"]),
        time=config.get("sort_vcf", {}).get("time", config["default_resources"]["time"]),
    container:
        config.get("sort_vcf", {}).get("container", config["default_container"])
    conda:
        "../envs/sort_vcf.yaml"
    message:
        "{rule}: sort vcf {input.vcf}"
    wrapper:
        "0.79.0/bio/bcftools/sort"
