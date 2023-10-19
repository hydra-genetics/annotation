__author__ = "Martin Rippin"
__copyright__ = "Copyright 2022, Martin Rippin"
__email__ = "martin.rippin@scilifelab.uu.se"
__license__ = "GPL-3"


rule snpeff:
    input:
        vcf="{file}.vcf.gz",
        db=config.get("snpeff", {}).get("db", ""),
        tabix="{file}.vcf.gz.tbi",
    output:
        calls=temp("{file}.snpeff_annotated.vcf.gz"),
        csvstats=temp("{file}.snpeff.csv"),
        genes=temp("{file}.snpeff.genes.txt"),
    params:
        extra=config.get("snpeff", {}).get("extra", "-nodownload"),
    log:
        "{file}.snpeff_annotated.vcf.gz.log",
    benchmark:
        repeat("{file}.snpeff_annotated.vcf.gz.benchmark.tsv", config.get("snpeff", {}).get("benchmark_repeats", 1))
    threads: config.get("snpeff", {}).get("threads", config["default_resources"]["threads"])
    resources:
        mem_mb=config.get("snpeff", {}).get("mem_mb", config["default_resources"]["mem_mb"]),
        mem_per_cpu=config.get("snpeff", {}).get("mem_per_cpu", config["default_resources"]["mem_per_cpu"]),
        partition=config.get("snpeff", {}).get("partition", config["default_resources"]["partition"]),
        threads=config.get("snpeff", {}).get("threads", config["default_resources"]["threads"]),
        time=config.get("snpeff", {}).get("time", config["default_resources"]["time"]),
    container:
        config.get("snpeff", {}).get("container", config["default_container"])
    message:
        "{rule}: annotate {input.vcf} with SnpEff"
    wrapper:
        "0.85.0/bio/snpeff/annotate"
