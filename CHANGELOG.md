# Changelog

### [0.1.2](https://www.github.com/hydra-genetics/annotation/compare/v0.1.1...v0.1.2) (2022-11-07)


### Bug Fixes

* rename env file for bcftools.smk


### Documentation

* update README and compatibility ([e51c5ca](https://www.github.com/hydra-genetics/annotation/commit/e51c5cac6e434c20aff6435d50ebe116e7c68345))

### [0.1.1](https://www.github.com/hydra-genetics/annotation/compare/v0.1.0...v0.1.1) (2022-10-28)


### Bug Fixes

* change output path for stranger.smk ([c49f774](https://www.github.com/hydra-genetics/annotation/commit/c49f774faf033d8c19b4dedd1ba7692071413af6))
* Fixed message in bgzip. Added testrun of bgzip and tabix. ([9cf7676](https://www.github.com/hydra-genetics/annotation/commit/9cf7676211afce299fbb8d1b190d97afd31eaac9))
* update env ([33fb178](https://www.github.com/hydra-genetics/annotation/commit/33fb178ff8564068e1aea9f6b17193cbefeb16ac))


### Documentation

* new rulegraph ([4880e96](https://www.github.com/hydra-genetics/annotation/commit/4880e96ec070ef0f5caba026f80a632f262afda1))

## 0.1.0 (2022-10-24)


### Features

* adaption to new artifact file ([74f8c37](https://www.github.com/hydra-genetics/annotation/commit/74f8c37b0dbb06fe9344ea8c33a6d9a0b2c0409d))
* add background entry to schema ([8638430](https://www.github.com/hydra-genetics/annotation/commit/86384308146c8dd353f4265a188cde5a934dcf13))
* add conventional-prs workflow ([c6710f5](https://www.github.com/hydra-genetics/annotation/commit/c6710f569e3112fd7064c7a81e8d3018bf3fb35d))
* add hotspot annotation script and test. ([db7efd4](https://www.github.com/hydra-genetics/annotation/commit/db7efd4cbdd0f42fce873d0911f0a21bb14510aa))
* add resources to rule. ([c025d3c](https://www.github.com/hydra-genetics/annotation/commit/c025d3c03ffd92a3c7dad63beb35127d1cdcb443))
* Add simple_sv_annotation ([05daaf9](https://www.github.com/hydra-genetics/annotation/commit/05daaf91d662b82e408e7d9bef3298e042e5b19e))
* Add snpeff rule ([4b2f5aa](https://www.github.com/hydra-genetics/annotation/commit/4b2f5aa703c8b71ba07eddd5b277d9edb60ceda4))
* add_multi_snv_in_codon can now be run wo artifact file ([ab4466d](https://www.github.com/hydra-genetics/annotation/commit/ab4466ddfe6e6f8825374b2160c279d5dfc884be))
* added hotspot annotation rule ([14bc248](https://www.github.com/hydra-genetics/annotation/commit/14bc24899599b1bb0d9fdd84ad5fc4029cc82df2))
* Added rule add_mosdepth_coverage_to_gvcf ([358122f](https://www.github.com/hydra-genetics/annotation/commit/358122fb2db2e4966166656ca0b264a4e2feb4b3))
* Added rule: calculate_backround_run ([c0b357c](https://www.github.com/hydra-genetics/annotation/commit/c0b357c3c522751490ab292c96d1310436afe8a0))
* added rules to Snamkemake ([cef7146](https://www.github.com/hydra-genetics/annotation/commit/cef714627786fe10e148f51d1fb9847e2c0b0494))
* added schemas ([cb8b0e8](https://www.github.com/hydra-genetics/annotation/commit/cb8b0e8b50038e9210a834df788efc64b4d4959b))
* make config.yaml location more flexible ([20a3da0](https://www.github.com/hydra-genetics/annotation/commit/20a3da06249d9a8e984242126fc261a350e48b12))
* make configfile/confgilefiles argument mandatory ([a16ceb2](https://www.github.com/hydra-genetics/annotation/commit/a16ceb29708f15615aac42c5ca39ed1480f3ff83))
* moved codon to after filtering ([1cbea47](https://www.github.com/hydra-genetics/annotation/commit/1cbea47adf407b35b79f620c5837536553ce8360))
* Moved rule annotate to the annotation module and changed name to vep ([c3fa0ba](https://www.github.com/hydra-genetics/annotation/commit/c3fa0ba99016ee47d7de68e31dddb53cdd549289))
* Moved rule annotate to the annotation module and changed name to vep ([2690c54](https://www.github.com/hydra-genetics/annotation/commit/2690c541abd7ea6ef9aa289f7e37fa9ad573f33d))
* mutect2 rename ([f18a8b3](https://www.github.com/hydra-genetics/annotation/commit/f18a8b34ddd74fcb99b900a087ed7cee6b8fc4ca))
* script used to annotate cnv with gene and fix header. ([23fecb9](https://www.github.com/hydra-genetics/annotation/commit/23fecb96995e75ed569b24891a0b4091b0e3a3c4))
* separate conda and singularity test ([a2b87c2](https://www.github.com/hydra-genetics/annotation/commit/a2b87c2e7b5c1575867cb0029466d1f57185be88))
* Target SnpEff output in all rule ([59828b0](https://www.github.com/hydra-genetics/annotation/commit/59828b05a107776400155a957982709068521ace))
* update schema with information about artifact file ([8d85404](https://www.github.com/hydra-genetics/annotation/commit/8d85404dbed2b3e5961e0fb8b6bc9b6920d4b0a9))
* update snakemake version ([fdb0bbb](https://www.github.com/hydra-genetics/annotation/commit/fdb0bbbcfcb8d7061d23a5fd5142356feecbd0ab))
* update to work work with latest develop branch for snv_indels ([3c782f1](https://www.github.com/hydra-genetics/annotation/commit/3c782f12f6f96eb723a88f05f703ac1c047efbd4))
* use pysam instead calling samtools externally ([656a6ba](https://www.github.com/hydra-genetics/annotation/commit/656a6bafa401d9641b190b41e5bede351ce01903))


### Bug Fixes

* Add snakemake wrapper utils to snpeff env ([665b0ed](https://www.github.com/hydra-genetics/annotation/commit/665b0eda4fb974399da31ab91b62f3c51a8ffb89))
* annotation of standard deviation even if median is 0 ([e76d4f1](https://www.github.com/hydra-genetics/annotation/commit/e76d4f1689aa52bf9ded6d7b8feefc7924b23f6d))
* bugfix ([0ce2e7e](https://www.github.com/hydra-genetics/annotation/commit/0ce2e7e641068e980a004f8f90d7e9f3402c08b8))
* bugfix ([df9c821](https://www.github.com/hydra-genetics/annotation/commit/df9c821f9dbadf3b70373cfac1e57a404167aa94))
* bugfix ([900cfb5](https://www.github.com/hydra-genetics/annotation/commit/900cfb5f5ff452d05fea49a39f4205d41ee7b539))
* bugfix ([ad49cb0](https://www.github.com/hydra-genetics/annotation/commit/ad49cb0b59fcfbf1722656e9649b400bef97ed98))
* bugfix for INDELs ([8da4803](https://www.github.com/hydra-genetics/annotation/commit/8da4803e2252dbafff52feca892e8c8a922e229a))
* change run column name to flowcell in units. ([70f6c1a](https://www.github.com/hydra-genetics/annotation/commit/70f6c1aa69ff463b59b8fa661ae269a59ac405dd))
* change type from float to number ([e7e92ab](https://www.github.com/hydra-genetics/annotation/commit/e7e92abba5751cc4505ab469c2f57842aabb89eb))
* changed filename ([1cfdfbf](https://www.github.com/hydra-genetics/annotation/commit/1cfdfbfc75f624b69efa2f0d2f7c23df9a4f7930))
* changed rule name, added resources, changed container ([04caedf](https://www.github.com/hydra-genetics/annotation/commit/04caedface2e2033aa3c5345069059a45430aefa))
* **container:** missing environment for conda ([52b2f0b](https://www.github.com/hydra-genetics/annotation/commit/52b2f0b89518429765dae978f7037791e2b49571))
* correct gzip output file type ([1d16fae](https://www.github.com/hydra-genetics/annotation/commit/1d16fae3bb62188fa3693cb762714bdd05d50443))
* correct name of snakemake wrapper utils and downgrade bcftools ([48a77c0](https://www.github.com/hydra-genetics/annotation/commit/48a77c055af340f79ddd0aebcd8f8cf935e45c62))
* Correct simple sv annotation output suffix ([283904d](https://www.github.com/hydra-genetics/annotation/commit/283904d9720f0ad62d77e791e8a29fd58ba66f30))
* Fix snpeff rule - flag, wrapper path, genes file output ([584bf8c](https://www.github.com/hydra-genetics/annotation/commit/584bf8cd161339666a6a4b7390bc639808860862))
* fix stanza access ([4459516](https://www.github.com/hydra-genetics/annotation/commit/4459516a3896602c29d658c57140be2ef480b119))
* handle 0 SD ([e5d2b26](https://www.github.com/hydra-genetics/annotation/commit/e5d2b267fe6d901fdd0e5a857dd5171117def4e4))
* limit tag to not include dots ([0def461](https://www.github.com/hydra-genetics/annotation/commit/0def461a7143b46ffd51e7b08b38db8f753ced72))
* looping forever ([cc35fec](https://www.github.com/hydra-genetics/annotation/commit/cc35fecad65b289a76d51a2bfd8f66195da9f100))
* make artifacts key optional ([6af5efb](https://www.github.com/hydra-genetics/annotation/commit/6af5efb746723d8eae99e26fbfee847a857a6f46))
* make background key optional ([6fed3ee](https://www.github.com/hydra-genetics/annotation/commit/6fed3eecfe56b8f951e83aff8a24b93284093d77))
* missing annotation if both SNV and INDEL ([3fe28a2](https://www.github.com/hydra-genetics/annotation/commit/3fe28a2254f27c586b7975962881a8581b0628a9))
* more general regex for the tag constraint ([6f6d420](https://www.github.com/hydra-genetics/annotation/commit/6f6d4208b057decc22fac1a6f9cdfa6f6a0f4203))
* only add multivariants if not artifacts ([36cc0f7](https://www.github.com/hydra-genetics/annotation/commit/36cc0f7e739d15399fc8b14c9ef26c0557947556))
* output as unzipped vcf ([99d2740](https://www.github.com/hydra-genetics/annotation/commit/99d274099f4436811de763210fd5705cf943c882))
* output error ([284539f](https://www.github.com/hydra-genetics/annotation/commit/284539febb3947e72f0d35591d78ec5e41005cd4))
* remove parameter that isn't used ([c54dfb6](https://www.github.com/hydra-genetics/annotation/commit/c54dfb665880dd4ec7b293d45d1eb7550e4e4b93))
* set strict mode for conda ([fff5680](https://www.github.com/hydra-genetics/annotation/commit/fff568002b250dd7b7f5ff4a5c184200f5e64ab6))
* snpeff input order, calculate_background changed citatation marks ([10fe23f](https://www.github.com/hydra-genetics/annotation/commit/10fe23f92e9b396dc448d0311248660ab5aebf7a))
* test changes ([9942cf3](https://www.github.com/hydra-genetics/annotation/commit/9942cf3da8f12eca4c4b202f78f9c28a2e66df63))
* use samtools within container inside script ([625f504](https://www.github.com/hydra-genetics/annotation/commit/625f50413ac148ac8378a5fd4a13f27c9251553d))
* vep annotation of added lines in vcf file ([59a8a45](https://www.github.com/hydra-genetics/annotation/commit/59a8a454a41518f2f4a36d1631d247b37d935ef8))


### Documentation

* added dag graph ([a91895e](https://www.github.com/hydra-genetics/annotation/commit/a91895e04420286f69f93a9fef2c850abbbcce93))
* added module compatibility ([862fca5](https://www.github.com/hydra-genetics/annotation/commit/862fca5ba8ac7f5fc92d8a990fdde75b4b2dc84b))
* readme and hydra image ([b56c660](https://www.github.com/hydra-genetics/annotation/commit/b56c6604f6eaeda8c424b2b7007cc032e2b589d7))
* updated README ([fb4ea8e](https://www.github.com/hydra-genetics/annotation/commit/fb4ea8e9d380afd62f8e1b5cc00061b4d59fdcd0))