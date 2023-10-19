__author__ = "Jonas Almlöf"
__copyright__ = "Copyright 2021, Jonas Almlöf"
__email__ = "jonas.almlof@scilifelab.uu.se"
__license__ = "GPL-3"


rule add_multi_snv_in_codon:
    input:
        artifacts=config.get("reference", {}).get("artifacts", ""),
        ref=config["reference"]["fasta"],
        vcf="{path}/{sample}_{type}.{file_tags}.vcf",
    output:
        vcf=temp("{path}/{sample}_{type}.{file_tags}.codon_snvs.vcf"),
    params:
        af_limit=config.get("add_multi_snv_in_codon", {}).get("af_limit", 0.05),
        artifact_limit=config.get("add_multi_snv_in_codon", {}).get("artifact_limit", 3),
    log:
        "{path}/{sample}_{type}.{file_tags}.codon_snvs.vcf.log",
    benchmark:
        repeat(
            "{path}/{sample}_{type}.{file_tags}.codon_snvs.vcf.benchmark.tsv",
            config.get("add_multi_snv_in_codon", {}).get("benchmark_repeats", 1),
        )
    wildcard_constraints:
        file_tags="[a-zA-Z0-9_.]*vep_annotated[a-zA-Z0-9_.]*",
    threads: config.get("add_multi_snv_in_codon", {}).get("threads", config["default_resources"]["threads"])
    resources:
        mem_mb=config.get("add_multi_snv_in_codon", {}).get("mem_mb", config["default_resources"]["mem_mb"]),
        mem_per_cpu=config.get("add_multi_snv_in_codon", {}).get("mem_per_cpu", config["default_resources"]["mem_per_cpu"]),
        partition=config.get("add_multi_snv_in_codon", {}).get("partition", config["default_resources"]["partition"]),
        threads=config.get("add_multi_snv_in_codon", {}).get("threads", config["default_resources"]["threads"]),
        time=config.get("add_multi_snv_in_codon", {}).get("time", config["default_resources"]["time"]),
    container:
        config.get("add_multi_snv_in_codon", {}).get("container", config["default_container"])
    message:
        "{rule}: add multivariants to vcf if they are in same codon: {output.vcf}"
    script:
        "../scripts/add_multi_snv_in_codon.py"
