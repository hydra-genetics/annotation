__author__ = "Martin Rippin"
__copyright__ = "Copyright 2022, Martin Rippin"
__email__ = "martin.rippin@scilifelab.uu.se"
__license__ = "GPL-3"


rule simple_sv_annotation:
    input:
        vcf="{file}.snpeff.vcf.gz",
        panel=config.get("simple_sv_annotation", {}).get("panel", ""),
        fusion_pairs=config.get("simple_sv_annotation", {}).get("fusion_pairs", ""),
    output:
        vcf=temp("{file}.ssa.vcf.gz"),
    log:
        "{file}.ssa.vcf.gz.log",
    benchmark:
        repeat(
            "{file}.ssa.vcf.gz.benchmark.tsv",
            config.get("simple_sv_annotation", {}).get("benchmark_repeats", 1),
        )
    threads: config.get("simple_sv_annotation", {}).get("threads", config["default_resources"]["threads"])
    resources:
        threads=config.get("simple_sv_annotation", {}).get("threads", config["default_resources"]["threads"]),
        time=config.get("simple_sv_annotation", {}).get("time", config["default_resources"]["time"]),
        mem_mb=config.get("simple_sv_annotation", {}).get("mem_mb", config["default_resources"]["mem_mb"]),
        mem_per_cpu=config.get("simple_sv_annotation", {}).get("mem_per_cpu", config["default_resources"]["mem_per_cpu"]),
        partition=config.get("simple_sv_annotation", {}).get("partition", config["default_resources"]["partition"]),
    container:
        config.get("simple_sv_annotation", {}).get("container", config["default_container"])
    conda:
        "../envs/simple_sv_annotation.yaml"
    message:
        "{rule}: Annotate {wildcards.file}.snpeff.vcf.gz with simple_sv_annotation"
    shell:
        "simple_sv_annotation.py "
        "--gene_list {input.panel} "
        "--known_fusion_pairs {input.fusion_pairs} "
        "--output {output.vcf} "
        "{input.vcf} &> {log}"
