import tempfile
import os
import unittest

from pysam import VariantFile


class TestUnitUtils(unittest.TestCase):
    def setUp(self):

        self.tempdir = tempfile.mkdtemp()

    def tearDown(self):
        pass

    def _test_annotation(self, test_table, variants, analysis_type):
        if analysis_type == "seqrun":
            for variant in variants:
                try:
                    self.assertEqual(test_table["{}\t{}".format(variant[0], variant[1])], variant[2])
                except AssertionError as e:
                    print("Failed calculate background of: " + str(variant))
                    raise e
        elif analysis_type == "panel":
            for variant in variants:
                try:
                    self.assertEqual(test_table["{}\t{}".format(variant[0], variant[1])], [variant[2], variant[3]])
                except AssertionError as e:
                    print("Failed calculate background of: " + str(variant))
                    raise e

    def test_calculate_run_background(self):
        from calculate_background import calculate_run_background

        out_background_filename = os.path.join(self.tempdir, "flowcell.seqrun_background.tsv")
        out_background = open(out_background_filename, "w")

        # Calculate background for all positions in seqrun mode
        gvcfs = [
            ".tests/unit/vcf/sample.g.vcf.gz",
            ".tests/unit/vcf/sample2.g.vcf.gz",
            ".tests/unit/vcf/sample3.g.vcf.gz",
            ".tests/unit/vcf/sample4.g.vcf.gz",
        ]
        calculate_run_background(gvcfs, out_background, "seqrun")

        result_file = open(out_background_filename)
        result = []
        next(result_file)
        for line in result_file:
            result.append(line.strip().split("\t"))
        result_file.close()

        test_table = {
            "1\t934419": "0.0014534883720930232", # Position1
            "1\t934420": "0.0017852055398810782", # Position2
        }

        self._test_annotation(test_table, result, "seqrun")

        out_background = open(out_background_filename, "w")

        # Calculate background for all positions in panel mode
        gvcfs = ".tests/unit/gvcf_files.txt"
        calculate_run_background(gvcfs, out_background, "panel")

        result_file = open(out_background_filename)
        result = []
        next(result_file)
        for line in result_file:
            result.append(line.strip().split("\t"))
        result_file.close()

        test_table = {
            "1\t934419": ["0.0014534883720930232", "0.0012548022188792567"], # Position1
            "1\t934420": ["0.0017852055398810782", "0.0031975927425936467"], # Position2
        }

        self._test_annotation(test_table, result, "panel")
