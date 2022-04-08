from collections import OrderedDict
import gzip
import logging
from pysam import VariantFile

from hydra_genetics.utils.io.chr import ChrTranslater
from hydra_genetics.utils.models.hotspot import MultiBpVariantData
from hydra_genetics.utils.models.hotspot import ReportClass
from hydra_genetics.utils.io.hotspot import Reader as HotspotReader
from hydra_genetics.utils.io import utils


def annotate_vcf_with_hotspot_data(in_vcf, out_vcf, hotspot_report, chr_mapping, annotate_only_overlapping=False):
    """
    function used to annotate variants with hotspot information

    The diffent type of hotspot are:
    - hotspot: SNV overlapping this will be annotated as 1-hotspot, Indels as 2-indel
    - region/region_all: any variant overlapping these regions are annotated as 3-check
    - any variant that doesn't overlap any hotspot/region/region_all will be annotated as 4-other

    :param in_vcf: input vcf path
    :type in_vcf: string
    :param out_vcf: input vcf path
    :type out_vcf: string
    :param hotspot_report: path to file with hotspot information
    :type hotspot_report: string
    :param chr_mapping: path to file with chr and NC information used to map chr to NC
    :type chr_mapping: string
    :param annotate_only_overlapping: set to true if only overlapping variants should be annotated
    :type annotate_only_overlapping: boolean

    :return: None
    """
    log = logging.getLogger()
    log.info("Opening input vcf: {}".format(str(in_vcf)))
    variants = VariantFile(in_vcf, "r")

    # Add new info field to header used to create output vcf
    new_header = variants.header
    new_header.add_meta('INFO', items=[('ID', "Hotspot"),
                                       ('Number', '1'),
                                       ('Type', 'String'),
                                       ('Description', 'Hotspot classification')])

    # Create output vcf with new header
    log.info("Opening output vcf: {}".format(out_vcf))
    with VariantFile(out_vcf, 'w', header=new_header) as out_vcf:
        # Import hotspot file and put them in a dict according to chromosome
        hotspots = {}
        try:
            log.info("Parsing hotspot report: {}".format(hotspot_report))
            hotspot_reader = HotspotReader(hotspot_report)
            for hotspot in iter(hotspot_reader):
                if hotspot.CHROMOSOME not in hotspots:
                    hotspots[hotspot.CHROMOSOME] = OrderedDict(((ReportClass.hotspot, []),
                                                                (ReportClass.region_all, []),
                                                                (ReportClass.region, []),
                                                                (ReportClass.indel, [])))
                hotspots[hotspot.CHROMOSOME][hotspot.REPORT].append(hotspot)
        except ValueError as e:
            logging.error(e)
            exit(1)

        # Open file used to translate from chr to NC id
        log.info("Parsing reference chr translater: {}".format(chr_mapping))
        chr_translater = ChrTranslater(chr_mapping)

        log.info("Processing variants")
        for variant in variants:
            log.debug("Variant: {}".format(str(variant).rstrip()))
            # Error handling
            if variant is None:
                raise Exception("Empty allele found: " + str(variant))
            if not len(variant.alts) == 1:
                raise Exception("Multiple allele found: " + str(variant.alts))
            annotated = False
            nc_id = chr_translater.get_nc_value(variant.chrom)
            report_type = "4-other"
            if nc_id in hotspots:
                for hotspot_class in hotspots[nc_id]:
                    for hotspot in hotspots[nc_id][hotspot_class]:
                        if len(variant.ref) == 1 and len(variant.alts[0]) == 1 and hotspot.REPORT == ReportClass.indel:
                            continue
                        v_start = variant.start + 1
                        v_stop = variant.stop + 1
                        if hotspot.check_overlap(nc_id, hotspot.START, hotspot.END, v_start, v_stop):
                            report_type = utils.get_report_type(variant, hotspot)
                            log.debug("Annotating variant with: {}".format(report_type))
                            annotated = True
                            variant.info.update({'Hotspot': report_type})
                            break
            if not annotated and not annotate_only_overlapping:
                log.debug("Annotating variant with: {}".format(report_type))
                variant.info.update({'Hotspot': report_type})
            out_vcf.write(variant)


if __name__ == "__main__":
    log = snakemake.log_fmt_shell(stdout=False, stderr=True)

    annotate_vcf_with_hotspot_data(snakemake.input.vcf,
                                   snakemake.output.vcf,
                                   snakemake.input.hotspot,
                                   snakemake.input.chr_mapping)
