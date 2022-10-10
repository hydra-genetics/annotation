__author__ = "Jonas Almlöf, Patrik Smeds"
__copyright__ = "Copyright 2021, Jonas Almlöf"
__email__ = "jonas.almlof@scilifelab.uu.se"
__license__ = "GPL-3"


rule bgzip_vcf:
    input:
        "annotation/{file}.vcf",
    output:
        temp("annotation/{file}.vcf.gz"),
    log:
        "annotation/{file}.vcf.gz.log",
    benchmark:
        repeat("annotation/{file}.vcf.gz.benchmark.tsv", config.get("bgzip_vcf", {}).get("benchmark_repeats", 1))
    threads: config.get("bgzip_vcf", {}).get("threads", config["default_resources"]["threads"])
    resources:
        mem_mb=config.get("bgzip_vcf", {}).get("mem_mb", config["default_resources"]["mem_mb"]),
        mem_per_cpu=config.get("bgzip_vcf", {}).get("mem_per_cpu", config["default_resources"]["mem_per_cpu"]),
        partition=config.get("bgzip_vcf", {}).get("partition", config["default_resources"]["partition"]),
        threads=config.get("bgzip_vcf", {}).get("threads", config["default_resources"]["threads"]),
        time=config.get("bgzip_vcf", {}).get("time", config["default_resources"]["time"]),
    container:
        config.get("bgzip_vcf", {}).get("container", config["default_container"])
    conda:
        "../envs/bgzip_vcf.yaml"
    message:
        "{rule}: bgzip {input.vcf}"
    shell:
        "(bgzip -c {input} > {output}) &> {log}"
