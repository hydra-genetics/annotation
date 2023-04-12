__author__ = "Jonas Almlöf"
__copyright__ = "Copyright 2022, Jonas Almlöf"
__email__ = "jonas.almlof@igp.uu.se"
__license__ = "GPL-3"


rule add_mosdepth_coverage_to_gvcf:
    input:
        coverage="qc/mosdepth_bed/{sample}_{type}.per-base.bed.gz",
        gvcf="snv_indels/gatk_mutect2_gvcf/{sample}_{type}.merged.g.vcf.gz",
    output:
        gvcf=temp("qc/add_mosdepth_coverage_to_gvcf/{sample}_{type}.mosdepth.g.vcf"),
    log:
        "qc/add_mosdepth_coverage_to_gvcf/{sample}_{type}.mosdepth.g.vcf.log",
    threads: config.get("add_mosdepth_coverage_to_gvcf", {}).get("threads", config["default_resources"]["threads"])
    resources:
        mem_mb=config.get("add_mosdepth_coverage_to_gvcf", {}).get("mem_mb", config["default_resources"]["mem_mb"]),
        mem_per_cpu=config.get("add_mosdepth_coverage_to_gvcf", {}).get("mem_per_cpu", config["default_resources"]["mem_per_cpu"]),
        partition=config.get("add_mosdepth_coverage_to_gvcf", {}).get("partition", config["default_resources"]["partition"]),
        threads=config.get("add_mosdepth_coverage_to_gvcf", {}).get("threads", config["default_resources"]["threads"]),
        time=config.get("add_mosdepth_coverage_to_gvcf", {}).get("time", config["default_resources"]["time"]),
    benchmark:
        repeat(
            "qc/add_mosdepth_coverage_to_gvcf/{sample}_{type}.mosdepth.g.vcf.benchmark.tsv",
            config.get("add_mosdepth_coverage_to_gvcf", {}).get("benchmark_repeats", 1),
        )
    container:
        config.get("add_mosdepth_coverage_to_gvcf", {}).get("container", config["default_container"])
    message:
        "{rule}: add mosdepth read depth info to: {output.gvcf}"
    script:
        "../scripts/add_mosdepth_coverage_to_gvcf.py"
