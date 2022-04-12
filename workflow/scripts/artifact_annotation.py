
from pysam import VariantFile

in_vcf_filename = snakemake.input.vcf
artifacts = open(snakemake.input.artifacts)
out_vcf_filename = snakemake.output.vcf


artifact_dict = {}
header = True
caller_list = []
Empty_observation = ["0"]
max_nr_observations = 0
for line in artifacts:
    lline = line.strip().split("\t")
    if header:
        caller_list = []
        i = 0
        for column in lline[3:]:
            if i % 3 == 0:
                caller_list.append(column)
            i += 1
        if len(caller_list) > 1:
            for caller in caller_list[1:]:
                Empty_observation.append("0")
        header = False
        continue
    chrom = lline[0]
    pos = lline[1]
    type = lline[2]
    observations = []
    i = 0
    for observation in lline[3:]:
        if i % 3 == 0:
            observations.append(observation)
        i += 1
    for obs in observations:
        if int(obs) > max_nr_observations:
            max_nr_observations = int(obs)
    artifact_dict[chrom + "_" + pos + "_" + type] = [type, observations]


in_vcf = VariantFile(in_vcf_filename)
new_header = in_vcf.header
new_header.info.add(
    "Artifact",
    "1",
    "String",
    "Number of observations of SNV or INDEL in panel samples per caller and finally panel size: %s,Total" % ",".join(caller_list)
)
out_vcf = VariantFile(out_vcf_filename, 'w', header=new_header)
out_vcf.close()
in_vcf.close()


out_vcf = open(out_vcf_filename, "a")
in_vcf = open(in_vcf_filename)
header = True
for line in in_vcf:
    if header:
        # out_vcf.write(line)
        if line[:6] == "#CHROM":
            header = False
        continue
    lline = line.strip().split("\t")
    chrom = lline[0]
    pos = lline[1]
    type = "INDEL"
    if len(ref) == 1 and len(alt) == 1:
        type = "SNV"
    key = chrom + "_" + pos + "_" + type
    ref = lline[3]
    alt = lline[4]
    filter = lline[6]
    Observations = Empty_observation
    if key in artifact_dict:
        Observations = artifact_dict[key][1]
    max_observations = 0
    for obs in Observations:
        if int(obs) > max_observations:
            max_observations = int(obs)
    INFO = lline[7]
    Artifact_string = "Artifact=" + Observations[0]
    if len(Observations) > 1:
        for obs in Observations[1:]:
            Artifact_string += "," + obs
        Artifact_string += "," + str(max_nr_observations)
    INFO = Artifact_string + ";" + INFO
    lline[7] = INFO
    out_vcf.write(lline[0])
    for column in lline[1:]:
        out_vcf.write("\t" + column)
    out_vcf.write("\n")
out_vcf.close()
