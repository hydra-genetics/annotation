__author__ = "Martin Rippin"
__copyright__ = "Copyright 2022, Martin Rippin"
__email__ = "martin.rippin@scilifelab.uu.se"
__license__ = "GPL-3"


rule simple_sv_annotation:
    input:
        fusion_pairs=config.get("simple_sv_annotation", {}).get("fusion_pairs", ""),
        panel=config.get("simple_sv_annotation", {}).get("panel", ""),
        vcf="{path}/{sample}_{type}.{file_tags}.vcf.gz",
    output:
        vcf=temp("{path}/{sample}_{type}.{file_tags}.ss_annotated.vcf"),
    log:
        "{path}/{sample}_{type}.{file_tags}.ss_annotated.vcf.log",
    benchmark:
        repeat("{path}/{sample}_{type}.{file_tags}.ss_annotated.vcf.benchmark.tsv", config.get("simple_sv_annotation", {}).get("benchmark_repeats", 1))
    wildcard_constraints:
        file_tags="[a-zA-Z0-9_.]*snpeff_annotated[a-zA-Z0-9_.]*",
    threads: config.get("simple_sv_annotation", {}).get("threads", config["default_resources"]["threads"])
    resources:
        mem_mb=config.get("simple_sv_annotation", {}).get("mem_mb", config["default_resources"]["mem_mb"]),
        mem_per_cpu=config.get("simple_sv_annotation", {}).get("mem_per_cpu", config["default_resources"]["mem_per_cpu"]),
        partition=config.get("simple_sv_annotation", {}).get("partition", config["default_resources"]["partition"]),
        threads=config.get("simple_sv_annotation", {}).get("threads", config["default_resources"]["threads"]),
        time=config.get("simple_sv_annotation", {}).get("time", config["default_resources"]["time"]),
    container:
        config.get("simple_sv_annotation", {}).get("container", config["default_container"])
    message:
        "{rule}: annotate {input.vcf} with simple_sv_annotation"
    shell:
        "simple_sv_annotation.py "
        "--gene_list {input.panel} "
        "--known_fusion_pairs {input.fusion_pairs} "
        "--output {output.vcf} "
        "{input.vcf} &> {log}"
