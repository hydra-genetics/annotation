import tempfile
import os
import unittest

from pysam import VariantFile


class TestUnitUtils(unittest.TestCase):
    def setUp(self):
        self.in_vcf_filename = ".tests/unit/vcf/sample.hotspot_annotation.vcf"
        self.background_filename = ".tests/integration/reference/background_panel_HES45.tsv"
        self.nr_min_sd = 5

        self.tempdir = tempfile.mkdtemp()

    def tearDown(self):
        pass

    def _test_annotation(self, test_table, variants, field):
        for variant in variants:
            try:
                self.assertEqual(test_table["{}\t{}".format(variant.chrom, variant.start + 1)],
                                 variant.info.get(field, ''))
            except AssertionError as e:
                print("Failed background annotation of: " + str(variant))
                raise e

    def test_add_background_annotation_data(self):
        from background_annotation import add_background_annotation_data

        out_vcf_filename = os.path.join(self.tempdir, "sample.background_annotation.vcf")

        # Test PositionNrSD
        # Annotate all variants with background info
        add_background_annotation_data(self.in_vcf_filename, self.background_filename, out_vcf_filename, self.nr_min_sd)

        # Make sure header has been updated
        result = VariantFile(out_vcf_filename)
        self.assertTrue("PositionNrSD" in result.header.info)

        test_table_sd = {
            "chr1\t934487": 121.06999969482422, # Variant with SD
            "chr1\t935222": 1000.00, # Variant without SD
            "chr1\t2460944": "", # Indel variant that should not be annotated
            "chr1\t2491306": 21.270000457763672, # Variant with median > 0
        }

        self._test_annotation(test_table_sd, result, "PositionNrSD")

        # Test PanelMedian
        # Annotate all variants with background info
        add_background_annotation_data(self.in_vcf_filename, self.background_filename, out_vcf_filename, self.nr_min_sd)

        # Make sure header has been updated
        result = VariantFile(out_vcf_filename)
        self.assertTrue("PanelMedian" in result.header.info)

        test_table_median = {
            "chr1\t934487": 0.0000, # Variant with SD
            "chr1\t935222": 0.0000, # Variant without SD
            "chr1\t2460944": "", # Indel variant that should not be annotated
            "chr1\t2491306": 0.0008999999845400453, # Variant with median > 0
        }

        self._test_annotation(test_table_median, result, "PanelMedian")
