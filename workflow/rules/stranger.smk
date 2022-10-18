__author__ = "Padraic Corcoran"
__copyright__ = "Copyright 2022, Padraic Corcoran"
__email__ = "padraic.corcoran@scilifelab.uu.se"
__license__ = "GPL-3"


rule stranger:
    input:
        vcf="cnv_sv/expansionhunter/{sample}_{type}.vcf",
        cat=config.get("stranger", {}).get("catalog", ""),
    output:
        "cnv_sv/expansionhunter/{sample}_{type}.stranger.vcf",
    params:
        extra=config.get("stranger", {}).get("extra", ""),
    log:
        "annotation/stranger/{sample}_{type}.stranger.vcf.log",
    benchmark:
        repeat(
            "annotation/stranger/{sample}_{type}.stranger.vcf.benchmark.tsv",
            config.get("stranger", {}).get("benchmark_repeats", 1)
        )
    threads: config.get("stranger", {}).get("threads", config["default_resources"]["threads"])
    resources:
        mem_mb=config.get("stranger", {}).get("mem_mb", config["default_resources"]["mem_mb"]),
        mem_per_cpu=config.get("stranger", {}).get("mem_per_cpu", config["default_resources"]["mem_per_cpu"]),
        partition=config.get("stranger", {}).get("partition", config["default_resources"]["partition"]),
        threads=config.get("stranger", {}).get("threads", config["default_resources"]["threads"]),
        time=config.get("stranger", {}).get("time", config["default_resources"]["time"]),
    container:
        config.get("stranger", {}).get("container", config["default_container"])
    conda:
        "../envs/stranger.yaml"
    message:
        "{rule}: Annotate cnv_sv/expansionhunter/{wildcards.sample}_{wildcards.type}.vcf with stranger"
    shell:
        "stranger "
        "-f {input.cat} "
        "{input.vcf} > {output} &> {log}"
