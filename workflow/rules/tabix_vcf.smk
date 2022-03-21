__author__ = "Jonas Almlöf, Patrik Smeds"
__copyright__ = "Copyright 2021, Jonas Almlöf"
__email__ = "jonas.almlof@scilifelab.uu.se"
__license__ = "GPL-3"


rule tabix_vcf:
    input:
        "annotation/{file}.vcf.gz",
    output:
        temp("annotation/{file}.vcf.gz.tbi"),
    params:
        config.get("tabix_vcf", {}).get("extra", ""),
    log:
        "annotation/{file}.vcf.gz.tbi.log",
    benchmark:
        repeat(
            "annotation/{file}.vcf.gz.tbi.benchmark.tsv",
            config.get("tabix_vcf", {}).get("benchmark_repeats", 1),
        )
    threads: config.get("tabix_vcf", {}).get("threads", config["default_resources"]["threads"])
    resources:
        threads=config.get("tabix_vcf", {}).get("threads", config["default_resources"]["threads"]),
        time=config.get("tabix_vcf", {}).get("time", config["default_resources"]["time"]),
        mem_mb=config.get("tabix_vcf", {}).get("mem_mb", config["default_resources"]["mem_mb"]),
        mem_per_cpu=config.get("tabix_vcf", {}).get("mem_per_cpu", config["default_resources"]["mem_per_cpu"]),
        partition=config.get("tabix_vcf", {}).get("partition", config["default_resources"]["partition"]),
    container:
        config.get("tabix_vcf", {}).get("container", config["default_container"])
    conda:
        "../envs/tabix_vcf.yaml"
    message:
        "{rule}: Tabix index annotation/{wildcards.file}.vcf.gz"
    wrapper:
        "0.79.0/bio/tabix"
