
import gzip
import statistics
import sys


def calculate_run_background(gvcf_files, background_file, analysis_type):
    gvcf_filenames = []
    if analysis_type == "panel":
        gvcf_file = open(gvcf_files)
        for line in gvcf_file:
            gvcf_filenames.append(line.strip())
    elif analysis_type == "seqrun":
        gvcf_filenames = gvcf_files
    else:
        print("Wrong analysis type. Should be panel or run")
        sys.exit(1)

    background_dict = {}
    for file_name in gvcf_filenames:
        with gzip.open(file_name, 'rt') as infile:
            file_content = infile.read().split("\n")
            header = True
            for line in file_content:
                if header:
                    if line[:6] == "#CHROM":
                        header = False
                    continue
                columns = line.strip().split("\t")
                if len(columns) <= 1:
                    continue
                chrom = columns[0][3:]
                pos = columns[1]
                key = chrom + "_" + pos
                format = columns[8].split(":")
                data = columns[9].split(":")
                AD_id = 0
                for f in format:
                    if f == "AD":
                        break
                    AD_id += 1
                AD_info = data[AD_id].split(",")
                ref_AD = int(AD_info[0])
                alt_AD = 0
                for AD in AD_info[1:]:
                    alt_AD += int(AD)
                DP = ref_AD + alt_AD
                alt_AF = 0.0
                if DP > 50:
                    alt_AF = alt_AD / float(DP)
                if alt_AF > 0.95:
                    alt_AF = 1.0 - alt_AF
                if alt_AF > 0.05:
                    continue
                if key in background_dict:
                    background_dict[key].append(alt_AF)
                else:
                    background_dict[key] = [alt_AF]

    if analysis_type == "panel":
        background_file.write("Chrom\tPos\tMedian\tSD\n")
        for key in background_dict:
            background_dict[key].sort()
            nr_obs = len(background_dict[key])
            if nr_obs > 3:
                median_background = statistics.median(background_dict[key])
                '''This is the sample variance s² with Bessel’s correction, also known as variance with N-1 degrees of freedom.
                Provided that the data points are representative (e.g. independent and identically distributed),
                the result should be an unbiased estimate of the true population variance.'''
                stdev_background = statistics.stdev(background_dict[key])
                background_file.write(
                    key.split("_")[0] + "\t" + key.split("_")[1] + "\t" + str(median_background) + "\t" + str(stdev_background) + "\n"
                )
    else:
        background_file.write("Chrom\tPos\tMedian\n")
        for key in background_dict:
            background_dict[key].sort()
            nr_obs = len(background_dict[key])
            if nr_obs >= 1:
                median_background = statistics.median(background_dict[key])
                background_file.write(
                    key.split("_")[0] + "\t" + key.split("_")[1] + "\t" + str(median_background) + "\n"
                )
    background_file.close()

if __name__ == "__main__":
    gvcf_files = snakemake.input.gvcfs
    background_file = open(snakemake.output.background, "w")
    analysis_type = snakemake.params.type

    calculate_run_background(gvcf_files, background_file, analysis_type)
