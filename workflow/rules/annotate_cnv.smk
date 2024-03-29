__author__ = "Patrik Smeds, Almlöf"
__copyright__ = "Copyright 2021, Patrik Smeds, Jonas Almlöf"
__email__ = "patrik.smeds@scilifelab.uu.se, jonas.almlof@scilifelab.uu.se"
__license__ = "GPL3"


rule annotate_cnv:
    input:
        vcf="{file}.vcf",
    output:
        vcf=temp("{file}.annotate_cnv.{tag}.vcf"),
    params:
        bed=lambda wildcards: config.get("annotate_cnv", {}).get(wildcards.tag, ""),
    log:
        "{file}.annotate_cnv.{tag}.vcf.log",
    benchmark:
        repeat(
            "{file}.annotate_cnv.{tag}.vcf.benchmark.tsv",
            config.get("annotate_cnv", {}).get("benchmark_repeats", 1),
        )
    threads: config.get("annotate_cnv", {}).get("threads", config["default_resources"]["threads"])
    resources:
        mem_mb=config.get("annotate_cnv", {}).get("mem_mb", config["default_resources"]["mem_mb"]),
        mem_per_cpu=config.get("annotate_cnv", {}).get("mem_per_cpu", config["default_resources"]["mem_per_cpu"]),
        partition=config.get("annotate_cnv", {}).get("partition", config["default_resources"]["partition"]),
        threads=config.get("annotate_cnv", {}).get("threads", config["default_resources"]["threads"]),
        time=config.get("annotate_cnv", {}).get("time", config["default_resources"]["time"]),
    container:
        config.get("annotate_cnv", {}).get("container", config["default_container"])
    message:
        "{rule}: annotate cnv based on gene bed file into: {output.vcf}"
    script:
        "../scripts/annotate_cnv.py"
