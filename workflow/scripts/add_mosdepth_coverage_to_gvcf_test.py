import tempfile
import os
import unittest
import gzip
from Bio import bgzf


class TestUnitUtils(unittest.TestCase):
    def setUp(self):
        self.in_coverage = gzip.open(".tests/unit/mosdepth/sample.bed.gz", "rt")
        self.in_gvcf = gzip.open(".tests/unit/vcf/sample.g.vcf.gz", "rt")

        self.tempdir = tempfile.mkdtemp()

    def tearDown(self):
        pass

    def _test_annotation(self, test_table, variants):
        for variant in variants:
            columns = variant.strip().split("\t")
            try:
                self.assertEqual(test_table["{}\t{}".format(columns[0], columns[1])], columns[9])
            except AssertionError as e:
                print("Failed mosdepth coverage annotation of: " + str(variant))
                raise e

    def test_annotate_gvcf_with_mosdepth_data(self):
        from add_mosdepth_coverage_to_gvcf import annotate_gvcf_with_mosdepth_data

        out_gvcf = bgzip.open(os.path.join(self.tempdir, "sample.mosdepth.g.vcf.gz"), "w")

        # Annotate all variants with depth from mosdepth (added last)
        annotate_gvcf_with_mosdepth_data(self.in_coverage, self.in_gvcf, out_gvcf)
        out_gvcf.close()

        result_file = gzip.open(os.path.join(self.tempdir, "sample.mosdepth.g.vcf.gz"))
        result = []
        for line in result_file:
            if line[0] != "#":
                result.append(line)

        test_table = {
            "chr1\t934419": '0/0:1374,2:1376:-5.652e+00:1111',
            "chr1\t934420": '0/0:1397,0:1397:-3.146e+00:1124',
        }
        print(result)

        self._test_annotation(test_table, result)
