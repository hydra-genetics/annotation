# vim: syntax=python tabstop=4 expandtab
# coding: utf-8

__author__ = "Jonas Almlöf"
__copyright__ = "Copyright 2021, Jonas Almlöf"
__email__ = "jonas.almlof@scilifelab.uu.se"
__license__ = "GPL-3"


rule vep:
    input:
        vcf="snv_indels/{caller}/{file}.vcf.gz",
        tabix="snv_indels/{caller}/{file}.vcf.gz.tbi",
        cache=config["vep"]["vep_cache"],
        fasta=config["reference"]["fasta"],
    output:
        vcf=temp("snv_indels/{caller}/{file}.vep_annotated.vcf"),
    params:
        extra=config.get("vep", {}).get("extra", ""),
        mode=config.get("vep", {}).get("mode", "--offline --cache"),
    log:
        "snv_indels/{caller}/{file}.vep_annotated.vcf.gz.log",
    benchmark:
        repeat(
            "snv_indels/{caller}/{file}.vep_annotated.vcf.gz.benchmark.tsv",
            config.get("vep", {}).get("benchmark_repeats", 1),
        )
    threads: config.get("vep", {}).get("threads", config["default_resources"]["threads"])
    resources:
        threads=config.get("vep", {}).get("threads", config["default_resources"]["threads"]),
        time=config.get("vep", {}).get("time", config["default_resources"]["time"]),
    container:
        config.get("vep", {}).get("container", config["default_container"])
    conda:
        "../envs/vep.yaml"
    message:
        "{rule}: Annotate with VEP: snv_indels/{wildcards.caller}/{wildcards.file}.vep_annotated.vcf.gz"
    shell:
        "(vep --vcf --no_stats -o {output.vcf} -i {input.vcf} --dir_cache {input.cache} --fork {threads} --refseq {params.mode} --fasta {input.fasta} {params.extra} ) &> {log}"
