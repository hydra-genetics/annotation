__author__ = "Pádraic Corcoran"
__copyright__ = "Copyright 2026, Pádraic Corcoran"
__email__ = "padraic.corcoran@scilifelab.uu.se"
__license__ = "GPL-3"


rule echtvar_anno:
    input:
        vcf="{file}.bcftools_norm.vcf.gz",
    output:
        vcf="{file}.bcftools_norm.echtvar_annotated.vcf.gz",
    params:
        echtvar_files=lambda wildcards: " ".join([f"-e {db}" for db in config.get("echtvar_anno", {}).get("databases", [])]),
        extra=config.get("echtvar_anno", {}).get("extra", ""),
    log:
        "{file}.bcftools_norm.echtvar_annotated.vcf.gz.log",
    benchmark:
        repeat(
            "{file}.bcftools_norm.echtvar_annotated.vcf.gz.benchmark.tsv",
            config.get("echtvar_anno", {}).get("benchmark_repeats", 1),
        )
    threads: config.get("echtvar_anno", {}).get("threads", config["default_resources"]["threads"])
    resources:
        mem_mb=config.get("echtvar_anno", {}).get("mem_mb", config["default_resources"]["mem_mb"]),
        mem_per_cpu=config.get("echtvar_anno", {}).get("mem_per_cpu", config["default_resources"]["mem_per_cpu"]),
        partition=config.get("echtvar_anno", {}).get("partition", config["default_resources"]["partition"]),
        threads=config.get("echtvar_anno", {}).get("threads", config["default_resources"]["threads"]),
        time=config.get("echtvar_anno", {}).get("time", config["default_resources"]["time"]),
    container:
        config.get("echtvar_anno", {}).get("container", config["default_container"])
    message:
        "{rule}: Anotate variants in {input.vcf} with echtvar"
    shell:
        "echtvar anno "
        "{params.echtvar_files} "
        "{input.vcf} "
        "{output.vcf} &> {log}"
