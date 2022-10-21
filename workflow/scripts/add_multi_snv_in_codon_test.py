import tempfile
import os
import unittest

from pysam import VariantFile


class TestUnitUtils(unittest.TestCase):
    def setUp(self):
        self.reference = ".tests/integration/reference/WASH7P.fna"
        self.in_vcf = open(".tests/unit/vcf/sample.background_annotation.include.exon.filter.snv_hard_filter.vcf")
        self.af_limit = 0.0
        self.artifact_limit = 1000
        self.artifacts = ".tests/integration/reference/artifact_panel_chr1.tsv"

        self.tempdir = tempfile.mkdtemp()

    def tearDown(self):
        pass

    def _test_annotation(self, test_table, variants, field):
        for variant in variants:
            try:
                self.assertEqual(test_table["{}\t{}".format(variant.chrom, variant.start + 1)],
                                 variant.info.get(field, ''))
            except AssertionError as e:
                print("Failed to add multi snv of: " + str(variant))
                raise e

    def test_add_multi_snv_in_codon(self):
        from add_multi_snv_in_codon import add_multi_snv_in_codon

        out_vcf_filename = os.path.join(
            self.tempdir,
            "sample.background_annotation.include.exon.filter.snv_hard_filter.codon_snvs.vcf",
        )
        out_vcf = open(out_vcf_filename, "w")

        # Annotate all variants with multi snv in codon info
        add_multi_snv_in_codon(
            self.reference, self.in_vcf, out_vcf, self.af_limit, self.artifact_limit, self.artifacts
        )
        out_vcf.close()

        # Make sure header has been updated
        result = VariantFile(out_vcf_filename)
        self.assertTrue("AA" in result.header.info)

        test_table = {
            "chr1\t12647": "",  # Original variant1
            "chr1\t12648": "",  # Original variant2
            "chr1\t12646": "Lys1100Pro",  # Added variant
            "chr1\t12645": "",  # Additional variant in another codon
        }

        self._test_annotation(test_table, result, "AA")
