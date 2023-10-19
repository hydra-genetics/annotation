# [Annotation module](https://github.com/hydra-genetics/annotation)
The annotation module consists of annotation steps, such as annotation of vcf files using VEP or SnpEff or adding artifact and background noise information. There are also simple tools for CNV and SV annotations in vcf files. Annotated output files will be tagged with the annotation tools but otherwise be identical to the input file, meaning that the annotation tools used are driven by the tags found in the final output files.

# [Hydra-genetics](https://hydra-genetics.readthedocs.io/en/latest/)

We are an organization/community with the goal of making [snakemake](https://snakemake.readthedocs.io/en/stable/index.html) pipeline development easier, faster, a bit more structured and of higher quality.

We do this by providing [snakemake modules](https://snakemake.readthedocs.io/en/stable/snakefiles/modularization.html#modules) that can be combined to create a complete analysis or included in already existing pipelines. All modules are subjected to extensive testing to make sure that new releases doesn't unexpectedly break existing pipeline or deviate from guidelines and best practices on how to write code.
<p align="center" width="100%">
    <img width="10%" src="images/hydragenetics.png">
</p>