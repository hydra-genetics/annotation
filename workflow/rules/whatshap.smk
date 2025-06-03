__author__ = "Andrei Guliaev"
__copyright__ = "Copyright 2025, Andrei Guliaev"
__email__ = "andrei.guliaev@scilifelab.uu.se"
__license__ = "GPL-3"


rule whatshap_phase:
    input:
        bai="alignment/pbmm2_align/{sample}_{type}.bam.bai",
        bam="alignment/pbmm2_align/{sample}_{type}.bam",
        fasta=config.get("reference", {}).get("fasta", ""),
        vcf="snv_indels/deepsomatic_t_only/{sample}_{type}.vcf.gz",
    output:
        vcf="annotation/whatshap_phase/{sample}_{type}.phased.vcf.gz",
    params:
        extra=config.get("whatshap_phase", {}).get("extra", ""),
    log:
        "annotation/whatshap_phase/{sample}_{type}.phased.vcf.gz.log",
    benchmark:
        repeat(
            "annotation/whatshap_phase/{sample}_{type}.phased.vcf.gz.benchmark.tsv",
            config.get("whatshap_phase", {}).get("benchmark_repeats", 1),
        )
    threads: config.get("whatshap_phase", {}).get("threads", config["default_resources"]["threads"])
    resources:
        mem_mb=config.get("whatshap_phase", {}).get("mem_mb", config["default_resources"]["mem_mb"]),
        mem_per_cpu=config.get("whatshap_phase", {}).get("mem_per_cpu", config["default_resources"]["mem_per_cpu"]),
        partition=config.get("whatshap_phase", {}).get("partition", config["default_resources"]["partition"]),
        threads=config.get("whatshap_phase", {}).get("threads", config["default_resources"]["threads"]),
        time=config.get("whatshap_phase", {}).get("time", config["default_resources"]["time"]),
    container:
        config.get("whatshap_phase", {}).get("container", config["default_container"])
    message:
        "{rule}: do variants phasing on {input.vcf}"
    shell:
        "whatshap phase -o {output.vcf} --reference {input.fasta} {params.extra} {input.vcf} {input.bam} &> {log} "


rule whatshap_haplotag:
    input:
        "annotation/whatshap_phase/{sample}_{type}.phased.vcf.gz.tbi",
        "alignment/pbmm2_align/{sample}_{type}.bam.bai",
        config.get("reference", {}).get("fai", ""),
        aln="alignment/pbmm2_align/{sample}_{type}.bam",
        ref=config.get("reference", {}).get("fasta", ""),
        vcf="annotation/whatshap_phase/{sample}_{type}.phased.vcf.gz",
    output:
        "annotation/whatshap_haplotag/{sample}_{type}.haplotagged.bam",
    params:
        extra=config.get("whatshap_haplotag", {}).get("extra", ""),
    log:
        "annotation/whatshap_haplotag/{sample}_{type}.haplotagged.bam.log",
    benchmark:
        repeat(
            "annotation/whatshap_haplotag/{sample}_{type}.haplotagged.bam.benchmark.tsv",
            config.get("whatshap_haplotag", {}).get("benchmark_repeats", 1),
        )
    threads: config.get("whatshap_haplotag", {}).get("threads", config["default_resources"]["threads"])
    resources:
        mem_mb=config.get("whatshap_haplotag", {}).get("mem_mb", config["default_resources"]["mem_mb"]),
        mem_per_cpu=config.get("whatshap_haplotag", {}).get("mem_per_cpu", config["default_resources"]["mem_per_cpu"]),
        partition=config.get("whatshap_haplotag", {}).get("partition", config["default_resources"]["partition"]),
        threads=config.get("whatshap_haplotag", {}).get("threads", config["default_resources"]["threads"]),
        time=config.get("whatshap_haplotag", {}).get("time", config["default_resources"]["time"]),
    container:
        config.get("whatshap_haplotag", {}).get("container", config["default_container"])
    message:
        "{rule}: do haplotagging on {input.aln}"
    wrapper:
        "v6.0.0/bio/whatshap/haplotag"
