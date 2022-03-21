
from pysam import VariantFile

in_vcf_filename = snakemake.input.vcf
background_panel_filename = snakemake.input.background
out_vcf_filename = snakemake.output.vcf
nr_min_sd = snakemake.params.nr_min_sd


in_vcf = VariantFile(in_vcf_filename)
new_header = in_vcf.header
new_header.filters.add("LownrSD", None, None, "Variant is close to background median in background panel")
new_header.info.add("PanelMedian", "1", "Float", "Background median MAF in panel")
new_header.info.add("PositionNrSD", "1", "Float", "Number of Standard Deviations from background panel median")
out_vcf = VariantFile(out_vcf_filename, 'w', header=new_header)
out_vcf.close()
in_vcf.close()


background_panel_dict = {}
if background_panel_filename != "":
    background_panel = open(background_panel_filename)
    next(background_panel)
    for line in background_panel:
        lline = line.strip().split("\t")
        chrom = "chr" + lline[0]
        pos = lline[1]
        median = float(lline[2])
        sd = float(lline[3])
        background_panel_dict[chrom + "_" + pos] = [median, sd]


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
    key = chrom + "_" + pos
    ref = lline[3]
    alt = lline[4]
    filter = lline[6]
    INFO = lline[7]
    INFO_list = INFO.split(";")
    AF_index = 0
    Caller_index = 0
    i = 0
    for info in INFO_list:
        if info[:3] == "AF=":
            AF_index = i
        if info[:8] == "CALLERS=":
            Caller_index = i
        i += 1
    AF = float(INFO_list[AF_index][3:])
    nr_SD = 1000
    if len(ref) == 1 and len(alt) == 1:
        if key in background_panel_dict:
            panel_median = background_panel_dict[key][0]
            if panel_median > 0.0:
                nr_SD = (AF - panel_median) / background_panel_dict[key][1]
            INFO = "PanelMedian=" + "{:.4f}".format(panel_median) + ";" + INFO
            INFO = "PositionNrSD=" + "{:.2f}".format(nr_SD) + ";" + INFO
            lline[7] = INFO
    if nr_SD < nr_min_sd:
        if filter == "PASS":
            filter = "LownrSD"
        else:
            filter += ";LownrSD"
        lline[6] = filter
    out_vcf.write(lline[0])
    for column in lline[1:]:
        out_vcf.write("\t" + column)
    out_vcf.write("\n")
out_vcf.close()
