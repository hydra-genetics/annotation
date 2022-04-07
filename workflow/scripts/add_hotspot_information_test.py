import tempfile
import os
import unittest

from pysam import VariantFile


class TestUnitUtils(unittest.TestCase):
    def setUp(self):
        self.in_vcf = ".tests/unit/vcf/sample.vcf"
        self.in_hotspot_report = ".tests/unit/hotspot_report.tsv"
        self.in_chr_mapping = ".tests/unit/chr_mapping.tsv"

        self.tempdir = tempfile.mkdtemp()

    def tearDown(self):
        pass

    def _test_annotation(self, test_table, variants, field):
        for variant in variants:
            try:
                self.assertEqual(test_table["{}:{}-{}".format(variant.chrom, variant.start + 1, variant.stop)],
                                 variant.info.get(field, ''))
            except AssertionError as e:
                print("Failed annotation of: " + str(variant))
                raise e

    def test_annotate_vcf_with_hotspot(self):
        from add_hotspot_information import annotate_vcf_with_hotspot_data

        out_vcf = os.path.join(self.tempdir, "sample.annotated.vcf")
        annotate_vcf_with_hotspot_data(self.in_vcf, out_vcf, self.in_hotspot_report, self.in_chr_mapping, True)

        # Make sure header has been updated
        result = VariantFile(out_vcf)
        self.assertTrue("Hotspot" in result.header.info)

        # Only annotate overlapping variants
        test_table = {
            "chr12:25398281-25398281": '1-hotspot',  # SNV overlapping a hotspot
            "chr7:55242464-55242479": '2-indel',  # indel that overlap a hotspot
            "chrX:149667834-149667834": '',  # Not verlapping a hotspot
            "chr17:41245466-41245466": '3-check'  # SNV/indel overlapping region/region_all"
        }

        self._test_annotation(test_table, result, "Hotspot")

        # Annotate all variants
        annotate_vcf_with_hotspot_data(self.in_vcf, out_vcf, self.in_hotspot_report, self.in_chr_mapping)

        test_table = {
            "chr12:25398281-25398281": '1-hotspot',  # SNV overlapping a hotspot
            "chr7:55242464-55242479": '2-indel',  # indel that overlap a hotspot
            "chrX:149667834-149667834": '4-other',  # Not verlapping a hotspot
            "chr17:41245466-41245466": '3-check'  # SNV/indel overlapping region/region_all"
        }

        self._test_annotation(test_table, result, "Hotspot")
