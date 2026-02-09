# Changelog

## [1.3.0](https://www.github.com/hydra-genetics/annotation/compare/v1.2.0...v1.3.0) (2026-02-09)


### Features

* add echtvar anno ([14d51d0](https://www.github.com/hydra-genetics/annotation/commit/14d51d055479d95f536c7d4b543ff5a0502119ff))

## [1.2.0](https://www.github.com/hydra-genetics/annotation/compare/v1.1.0...v1.2.0) (2025-09-04)



### Bug Fixes

* add all required/change names of inputs in whatshap_haplotag (as per wrapper) ([c11061d](https://www.github.com/hydra-genetics/annotation/commit/c11061df706a39ccb17b1fbe4d2ad239eeff033f))
* add bai input ([fd70524](https://www.github.com/hydra-genetics/annotation/commit/fd70524252b46241da548ee6cbb2da5393a52206))
* add extra to whatshap_phase command ([f87731c](https://www.github.com/hydra-genetics/annotation/commit/f87731c15b88435e0955e4bf749997baadc2de37))
* add separate whatshap phase and whatshap haplotag entries ([32517ea](https://www.github.com/hydra-genetics/annotation/commit/32517ea695d90d0352f27c60628e530a2c975cab))
* correct benchmark filename in whatshap_haplotag ([8e57e8d](https://www.github.com/hydra-genetics/annotation/commit/8e57e8dcf4a500bee171b477a0f4bc446081976a))
* correct benchmark filename in whatshap_phase ([ba3e873](https://www.github.com/hydra-genetics/annotation/commit/ba3e873e4a1a48e99e658b04f6eeabb5ba02a2bd))
* correct log filename in whatshap_haplotag ([2c3a81d](https://www.github.com/hydra-genetics/annotation/commit/2c3a81df649f5cb5ba5816ad770e0d9df7a2243f))
* correct log filename in whatshap_phase ([fda07bf](https://www.github.com/hydra-genetics/annotation/commit/fda07bf872458f8e9ebba5c7f70e9e871ecbac76))
* make SAMPLE to SAMPLES more precise ([71ee702](https://www.github.com/hydra-genetics/annotation/commit/71ee702553cd4df11a56f2fc6495bf692bcdf86b))
* remove special output name/handle (bam) ([74f0ee5](https://www.github.com/hydra-genetics/annotation/commit/74f0ee5710fd6d10fd8508a3eccb9959cd2bc530))
* remove whatshap rules ([de1dea7](https://www.github.com/hydra-genetics/annotation/commit/de1dea791a9e0cdc20fc3179f647f78e4b376a1c))


### Documentation

* Update README.md ([d46d415](https://www.github.com/hydra-genetics/annotation/commit/d46d41545138c509a0a4014bb19bfa8f51e59531))
* update workflow/schemas/rules.schema.yaml ([9fe7834](https://www.github.com/hydra-genetics/annotation/commit/9fe7834e5adfed8edbe3da3929756885012aba53))
* update workflow/schemas/rules.schema.yaml ([113abc4](https://www.github.com/hydra-genetics/annotation/commit/113abc48095f81badbf1886c7b6ff41fa3c45b25))

## [1.1.0](https://www.github.com/hydra-genetics/annotation/compare/v1.0.1...v1.1.0) (2024-10-02)


### Features

* bgzipped output ([271c2f9](https://www.github.com/hydra-genetics/annotation/commit/271c2f9e63a1e6718851ade7a69ed3bd31c8a82c))
* make background_annotation be able to handel vcf.gz-files ([20608dc](https://www.github.com/hydra-genetics/annotation/commit/20608dcd4844516b4d22b1f242a029f764d8a3bd))
* output bgzipped vcf ([9378b16](https://www.github.com/hydra-genetics/annotation/commit/9378b16a923b587904974ac496a0c8d6157b930d))
* write gzipped outputfile ([138518c](https://www.github.com/hydra-genetics/annotation/commit/138518c2c8c5964bdd655cfa2117c4fe78e2de54))


### Bug Fixes

* adapt vcf header to new svdb ([c897dbb](https://www.github.com/hydra-genetics/annotation/commit/c897dbbe5099d48e69a842a77e8d6ab5f99c4298))
* add biopython ([d5c7c9f](https://www.github.com/hydra-genetics/annotation/commit/d5c7c9f276a4515339b847eed05c993e33e35838))
* add S to SAMPLE in vcf header ([00c4524](https://www.github.com/hydra-genetics/annotation/commit/00c4524ff4987f8da11594c5edff771f1a98b0de))
* bugfix ([2730ebf](https://www.github.com/hydra-genetics/annotation/commit/2730ebfdd141559ede77cc6efe34c9a560d3994b))
* bugfix ([171d978](https://www.github.com/hydra-genetics/annotation/commit/171d9789c26ae24f567bfc2a7d0082f53987eed8))
* bugfix ([1e78a3a](https://www.github.com/hydra-genetics/annotation/commit/1e78a3a6ae83a05914d27b8e2e6bc28d86a183bc))
* integration test using apptainer ([9b402b4](https://www.github.com/hydra-genetics/annotation/commit/9b402b43a0ce03c2ad51a42e3697e6187173732d))
* output bgzipped ([a9137df](https://www.github.com/hydra-genetics/annotation/commit/a9137dfa08db0cefe2174c7b28bf0fa2398b2823))
* pulp ([8dea2cc](https://www.github.com/hydra-genetics/annotation/commit/8dea2cc33430452660caf93d7407e7222b69e19b))
* remove missing module for bgzip ([75d82df](https://www.github.com/hydra-genetics/annotation/commit/75d82df8a9012761e6a46523ed64705b74d9e35b))
* rm gzipped output ([046c7c3](https://www.github.com/hydra-genetics/annotation/commit/046c7c39a380446097a2fc9446acd1166b7e3dd2))
* rm non-installed module ([e5a21ce](https://www.github.com/hydra-genetics/annotation/commit/e5a21ceb490533113c11b74ac3afc6680df38811))
* rm old svdb header fix ([779efe6](https://www.github.com/hydra-genetics/annotation/commit/779efe6d3a3f37a256a4f50d42ffd50934ac6210))
* rm req field that is now in data config ([af26eed](https://www.github.com/hydra-genetics/annotation/commit/af26eedc2f8a6b1d243e35346e911860d157231d))
* rule all with gz ([838131b](https://www.github.com/hydra-genetics/annotation/commit/838131b4722801b2239f411d49498e21f3f2927a))
* **stranger:** access extra in the shell command ([5fb7bed](https://www.github.com/hydra-genetics/annotation/commit/5fb7bed3b2639edcd126afea33c2db300ee0e819))
* trying to close closed file ([2b2805e](https://www.github.com/hydra-genetics/annotation/commit/2b2805e3e1984db402244369e1f884f316012ed0))
* Update requirements.txt (pulp) ([a535a56](https://www.github.com/hydra-genetics/annotation/commit/a535a56262accc060edcf2551b21d22df3d0bc2e))
* update rule all to gz ([4b77e37](https://www.github.com/hydra-genetics/annotation/commit/4b77e3730d6db355efa0bcda0b62180aac84eb8c))
* update test file with gz ([fcd18db](https://www.github.com/hydra-genetics/annotation/commit/fcd18dbd7ef5fe477d6a49e28dab8e04e4f5edd1))

### [1.0.1](https://www.github.com/hydra-genetics/annotation/compare/v1.0.0...v1.0.1) (2023-10-24)


### Bug Fixes

* include bgzip smk file and change wildcard/filename for bcftools_sort ([1cd7f15](https://www.github.com/hydra-genetics/annotation/commit/1cd7f158ab041a49ac7d96487256d2992b83b9cc))
* reinstate tabix and bgzip rules ([c1c00c7](https://www.github.com/hydra-genetics/annotation/commit/c1c00c7e304375bb86112f6114db2aad09b0ead0))
* remove conda env files entry for bgzip rule ([11d9c65](https://www.github.com/hydra-genetics/annotation/commit/11d9c65e7a3adcafa2a97f3f3f25f29311cf0802))
* revert to unaltered version of script ([be2e85d](https://www.github.com/hydra-genetics/annotation/commit/be2e85de5d05cc4554af9ac74d810edc793089ca))
* update output file from pipeline ([2ebc961](https://www.github.com/hydra-genetics/annotation/commit/2ebc961236b15916a153cae9d4e86e10441a035b))

## [1.0.0](https://www.github.com/hydra-genetics/annotation/compare/v0.3.0...v1.0.0) (2023-10-19)


### ⚠ BREAKING CHANGES

* renamed sort_vcf to bcftools_sort
* make annotation rule order independent where possible
* move --refseq option from shell to params.mode

### Features

* drop conda support and testing ([062002b](https://www.github.com/hydra-genetics/annotation/commit/062002b6b9fa891f89d4b91ac5f42342299d6888))
* make annotation rule order independent where possible ([9bbefcc](https://www.github.com/hydra-genetics/annotation/commit/9bbefcc92b27e0492389a951f97f445895aa34da))
* move --refseq option from shell to params.mode ([4d4a4a8](https://www.github.com/hydra-genetics/annotation/commit/4d4a4a8f9eec280817d20762098a19e8dfe7a955))
* update snakemake version, allow range up to version 8 ([5b48038](https://www.github.com/hydra-genetics/annotation/commit/5b48038d75dda2766cbb578edce60eb314bf11f5))


### Bug Fixes

* handle edge case correctly ([52eff4b](https://www.github.com/hydra-genetics/annotation/commit/52eff4bfb00897c48d1c6db6d7b5d2207fd1fef9))
* renamed sort_vcf to bcftools_sort ([14a2733](https://www.github.com/hydra-genetics/annotation/commit/14a2733dcdf256db9bafe3ebc24dd43225b7b5be))


### Documentation

* added read the docs for all rules in the annotation module ([9fa5f54](https://www.github.com/hydra-genetics/annotation/commit/9fa5f54b29ac81bd32e61d225a5582ed98dede13))
* Update config.schema.yaml ([eb1756a](https://www.github.com/hydra-genetics/annotation/commit/eb1756afcd6a0d3fa7559f270e11c57ffb210004))
* Update rules.schema.yaml ([eb12bcf](https://www.github.com/hydra-genetics/annotation/commit/eb12bcfe83a65936196d5f1bf0d13cac97b52e9b))

## [0.3.0](https://www.github.com/hydra-genetics/annotation/compare/v0.2.0...v0.3.0) (2023-01-27)


### Features

* added bcftools annotate rule ([0af9134](https://www.github.com/hydra-genetics/annotation/commit/0af9134b86f0bf16d25985c825ee283cbac8766d))


### Bug Fixes

* annotate missing positions in background ([25ca244](https://www.github.com/hydra-genetics/annotation/commit/25ca24461aa6833662931bcc0d688af0350aa65c))
* correct nrsd for median = 0 ([08fe2f9](https://www.github.com/hydra-genetics/annotation/commit/08fe2f9e15070d110222055ff037338c3eb6e875))
* float division by 0 ([6659ca3](https://www.github.com/hydra-genetics/annotation/commit/6659ca345d5852e4d85b1f23f422f7a790aa8490))
* **script:** homozygous normal variants should be filtered ([6245853](https://www.github.com/hydra-genetics/annotation/commit/62458539d115ec10c59a72b8688806c87c26d5f9))
* update bcltools version to fi dep issues ([0865bc6](https://www.github.com/hydra-genetics/annotation/commit/0865bc69fbce2c6367d0b65d7fcc2f555c6b6e9f))

## [0.2.0](https://www.github.com/hydra-genetics/annotation/compare/v0.1.2...v0.2.0) (2022-11-14)


### Features

* added additional artifact annotation to vcf file. Add temp on stranger rule ([21bb0e1](https://www.github.com/hydra-genetics/annotation/commit/21bb0e11e420c5079364061c4fd3109b731df320))


### Bug Fixes

* return correct reference base and not always C ([1bcc50e](https://www.github.com/hydra-genetics/annotation/commit/1bcc50e1b0ce35cf58d6474c8d993e4ab05b563f))


### Documentation

* update release versions ([5268635](https://www.github.com/hydra-genetics/annotation/commit/52686350d91651e847b0588acbecd76ed24e62c4))
* update release versions ([120e0a1](https://www.github.com/hydra-genetics/annotation/commit/120e0a1fc55cc3489537fe5dcf990447d668f83c))
* update versions ([87c1de4](https://www.github.com/hydra-genetics/annotation/commit/87c1de4534b072c9a277c01ab2308a449e881593))

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
