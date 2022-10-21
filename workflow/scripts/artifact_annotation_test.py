import tempfile
import os
import unittest

from pysam import VariantFile


class TestUnitUtils(unittest.TestCase):
    def setUp(self):
        self.in_vcf_filename = ".tests/unit/vcf/sample.ensembled.vep_annotated.vcf"
        self.artifacts = open(".tests/integration/reference/artifact_panel_chr1.tsv")

        self.tempdir = tempfile.mkdtemp()

    def tearDown(self):
        pass

    def _test_annotation(self, test_table, variants, field):
        for variant in variants:
            try:
                self.assertEqual(test_table["{}\t{}".format(variant.chrom, variant.start + 1)],
                                 variant.info.get(field, ''))
            except AssertionError as e:
                print("Failed artifact annotation of: " + str(variant))
                raise e

    def test_add_artifact_annotation_data(self):
        from artifact_annotation import add_artifact_annotation_data

        out_vcf_filename = os.path.join(self.tempdir, "sample.artifact_annotation.vcf")

        # Annotate all variants with artifact info
        add_artifact_annotation_data(self.in_vcf_filename, self.artifacts, out_vcf_filename)

        # Make sure header has been updated
        result = VariantFile(out_vcf_filename)
        self.assertTrue("Artifact" in result.header.info)

        test_table = {
            "chr1\t934487": ('0', '0', '36'),  # Variant without artifacts
            "chr1\t935222": ('33', '31', '36'),  # Variants with artifacts
        }

        self._test_annotation(test_table, result, "Artifact")
