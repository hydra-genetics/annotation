import tempfile
import os
import unittest

from pysam import VariantFile


class TestUnitUtils(unittest.TestCase):
    def setUp(self):
        self.in_vcf_filename = ".tests/unit/vcf/sample.svdb_query.vcf"
        self.genes = open(".tests/unit/cnv_amp_genes.bed")

        self.tempdir = tempfile.mkdtemp()

    def tearDown(self):
        pass

    def _test_annotation(self, test_table, variants, field):
        for variant in variants:
            try:
                self.assertEqual(test_table["{}\t{}".format(variant.chrom, variant.start + 1)],
                                 variant.info.get(field, ''))
            except AssertionError as e:
                print("Failed to annotate of: " + str(variant))
                raise e

    def test_filter_variants(self):
        from annotate_cnv import filter_variants

        out_vcf_filename = "sample.svdb_query.annotate_cnv.cnv_amp_genes.vcf"

        # Annotate some cnv variants with gene info
        filter_variants(self.in_vcf_filename, out_vcf_filename, self.genes)

        # Make sure header has been updated
        result = VariantFile(out_vcf_filename)
        self.assertTrue("Genes" in result.header.info)

        test_table = {
            "chr1\t150500": "PHEW", # Variant overlapping one gene
            "chr1\t934169": ('MTOR', 'PHEW'), # Variant overlapping two genes
            "chr1\t3683619": "MTOR", # Variant overlapping one gene
            "chr1\t142388550": "", # Variant not overlapping any gene
        }

        self._test_annotation(test_table, result, "Genes")
