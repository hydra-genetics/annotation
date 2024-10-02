import gzip
from pysam import VariantFile


def variant_in_genelist(chrom, start, end, gene_dict):
    genes = ""
    if chrom in gene_dict:
        for gene_region in gene_dict[chrom]:
            g_start = gene_region[0]
            g_end = gene_region[1]
            if (
                (start >= g_start and start <= g_end) or
                (end >= g_start and end <= g_end) or
                (start < g_start and end > g_end)
            ):
                if genes == "":
                    genes = gene_region[2]
                else:
                    genes = "%s,%s" % (genes, gene_region[2])
    return genes


def filter_variants(in_vcf, out_vcf, filter_bed_file):
    gene_dict = {}
    for line in filter_bed_file:
        columns = line.strip().split("\t")
        chrom = columns[0]
        start = int(columns[1])
        end = int(columns[2])
        gene = columns[3]
        if chrom not in gene_dict:
            gene_dict[chrom] = [[start, end, gene]]
        else:
            gene_dict[chrom].append([start, end, gene])

    vcf_out = open(out_vcf, "w")
    vcf_in = open(in_vcf) if not in_vcf.endswith(".gz") else gzip.open(in_vcf, "rt")
    header = True
    for line in vcf_in:
        if header:
            if line[:6] == "#CHROM":
                vcf_out.write("##INFO=<ID=Genes,Number=1,Type=String,Description=\"Gene names\">\n")
                vcf_out.write(line)
                header = False
            elif (
                line[:11] == "##INFO=<ID=" and
                line.find("SAMPLE") != -1 and
                line.find("pipe separated list of all details in the") != -1
            ):
                # Change SAMPLE to SAMPLES
                new_sample_header = f"{line.split('_')[0]}_{line.split(',')[0].split('_')[1]}S"
                for header_info in line.split(",")[1:]:
                    new_sample_header = f"{new_sample_header},{header_info}"
                vcf_out.write(new_sample_header)
            else:
                vcf_out.write(line)
            continue
        columns = line.strip().split("\t")
        chrom = columns[0]
        start = int(columns[1])
        INFO = columns[7]
        end = int(INFO.split("END=")[1].split(";")[0])
        genes = variant_in_genelist(chrom, start, end, gene_dict)
        if genes:
            INFO = "Genes=%s;%s" % (genes, INFO)
        columns[7] = INFO
        vcf_out.write(columns[0])
        for column in columns[1:]:
            vcf_out.write("\t" + column)
        vcf_out.write("\n")
    vcf_out.close()


if __name__ == "__main__":
    in_vcf = snakemake.input.vcf
    out_vcf = snakemake.output.vcf
    filter_bed_file = open(snakemake.params.bed)

    filter_variants(in_vcf, out_vcf, filter_bed_file)
