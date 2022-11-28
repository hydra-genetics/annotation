
from pysam import VariantFile


def add_artifact_annotation_data(in_vcf_filename, artifacts, out_vcf_filename):

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
        medians = []
        sds = []
        i = 0
        for data in lline[3:]:
            if i % 3 == 0:
                observations.append(data)
            if i % 3 == 1:
                medians.append(data)
            if i % 3 == 2:
                sds.append(data)
            i += 1
        for obs in observations:
            if int(obs) > max_nr_observations:
                max_nr_observations = int(obs)
        artifact_dict[chrom + "_" + pos + "_" + type] = [type, observations, medians, sds]

    in_vcf = VariantFile(in_vcf_filename)
    new_header = in_vcf.header
    new_header.info.add(
        "Artifact",
        "1",
        "String",
        "Number of observations of SNV or INDEL in panel samples per caller and finally panel size: %s,Total" %
        ",".join(caller_list)
    )
    new_header.info.add("ArtifactMedian", "1", "String", "Artifact median MAFs in normal panel")
    new_header.info.add("ArtifactNrSD", "1", "String", "Number of Standard Deviations from artifacts in panel median")
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
        ref = lline[3]
        alt = lline[4]
        if len(ref) == 1 and len(alt) == 1:
            type = "SNV"
        key = chrom + "_" + pos + "_" + type
        filter = lline[6]
        format_list = lline[8].split(":")
        format_data = lline[9].split(":")
        AF_index = 0
        i = 0
        for f in format_list:
            if f == "AF":
                AF_index = i
            i += 1
        AF = float(format_data[AF_index])
        Observations = Empty_observation
        Medians = Empty_observation
        SDs = Empty_observation
        if key in artifact_dict:
            Observations = artifact_dict[key][1]
            Medians = artifact_dict[key][2]
            SDs = artifact_dict[key][3]
        INFO = lline[7]
        Artifact_string = "Artifact=" + Observations[0]
        if len(Observations) > 1:
            for obs in Observations[1:]:
                Artifact_string += "," + obs
            Artifact_string += "," + str(max_nr_observations)
        Artifact_string += ";ArtifactMedian=" + Medians[0]
        if len(Medians) > 1:
            for median in Medians[1:]:
                Artifact_string += "," + median
        Artifact_string += ";ArtifactNrSD="
        i = 0
        nrsd = 1000
        for sd in SDs:
            if sd == "0":
                nrsd = 1000
            elif float(sd) == 1000.0 or float(sd) == 0.0:
                if float(Medians[i]) > AF:
                    nrsd = 0.0
                else:
                    nrsd = 1000
            else:
                nrsd = (AF - float(Medians[i])) / float(sd)
            if i == 0:
                Artifact_string += str(nrsd)
            else:
                Artifact_string += "," + str(nrsd)
            i += 1
        INFO = Artifact_string + ";" + INFO
        lline[7] = INFO
        out_vcf.write(lline[0])
        for column in lline[1:]:
            out_vcf.write("\t" + column)
        out_vcf.write("\n")
    out_vcf.close()


if __name__ == "__main__":
    log = snakemake.log_fmt_shell(stdout=False, stderr=True)

    add_artifact_annotation_data(
        snakemake.input.vcf,
        open(snakemake.input.artifacts),
        snakemake.output.vcf,
    )
