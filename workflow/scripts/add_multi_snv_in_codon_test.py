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
            "chr1\t12646": "Asn1100Pro",  # Added variant
            "chr1\t12645": "",  # Additional variant in another codon
        }

        self._test_annotation(test_table, result, "AA")

    def test_add_multi_snv_in_codon_negative_strand(self):
        from add_multi_snv_in_codon import add_multi_snv_in_codon

        fasta_path = os.path.join(self.tempdir, "test.fasta")
        with open(fasta_path, "w") as f:
            # chrTest: 1=G, 2=T, 3=T
            # Negative strand:
            # G3 (pos 3) = T -> c.1 = A
            # G2 (pos 2) = T -> c.2 = A
            # G1 (pos 1) = G -> c.3 = C
            # Coding codon: AAC (Asn)
            f.write(">chrTest\nGTT\n")
        import pysam
        pysam.faidx(fasta_path)

        in_vcf_path = os.path.join(self.tempdir, "test.vcf")
        with open(in_vcf_path, "w") as f:
            f.write("##fileformat=VCFv4.2\n")
            csq_desc = '##INFO=<ID=CSQ,Number=.,Type=String,Description="Format: Allele|...|HGVSc|...|CDS_position|...">'
            f.write(csq_desc + "\n")
            f.write('##INFO=<ID=AF,Number=A,Type=Float,Description="Allele Frequency">\n')
            f.write('##INFO=<ID=Artifact,Number=1,Type=String,Description="Artifact">\n')
            f.write("#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\tSAMPLE\n")

            csq_1 = "G|missense|MOD|GENE|1|Transcript|T1|pc|1/1||GENE:c.1A>G||1|1|1||Acc/Gcc||-1||||||"
            csq_2 = "G|missense|MOD|GENE|1|Transcript|T1|pc|1/1||GENE:c.2A>G||2|2|1||aAc/gAc||-1||||||"

            f.write(f"chrTest\t2\t.\tT\tC\t100\tPASS\tAF=0.5;Artifact=0,;CSQ={csq_2}\tGT\t0/1\n")
            f.write(f"chrTest\t3\t.\tT\tC\t100\tPASS\tAF=0.5;Artifact=0,;CSQ={csq_1}\tGT\t0/1\n")

        out_vcf_path = os.path.join(self.tempdir, "out.vcf")
        artifacts_path = os.path.join(self.tempdir, "artifacts.tsv")
        with open(artifacts_path, "w") as f:
            f.write("chrTest\t1\tA\t0\t0\t0\n")

        add_multi_snv_in_codon(
            fasta_path,
            open(in_vcf_path),
            open(out_vcf_path, "w"),
            0.0,
            1000,
            artifacts_path
        )

        # Verify the result
        result = VariantFile(out_vcf_path)
        found_multi = False
        for variant in result:
            if variant.start == 0 and variant.ref == "GTT":  # Genomic pos 1 (0-based)
                # AA info should be Asn1Gly
                # Asn (AAC) -> Gly (GGC)
                self.assertEqual(variant.info.get("AA"), "Asn1Gly")
                found_multi = True
        self.assertTrue(found_multi)

    def test_add_multi_snv_in_codon_phasing(self):
        from add_multi_snv_in_codon import add_multi_snv_in_codon

        fasta_path = os.path.join(self.tempdir, "phasing.fasta")
        with open(fasta_path, "w") as f:
            f.write(">chrPhase\nATGGGCTGAGGC\n")  # Met (ATG), Gly (GGC), * (TGA), Gly (GGC)
        import pysam
        pysam.faidx(fasta_path)

        in_vcf_path = os.path.join(self.tempdir, "phasing.vcf")
        with open(in_vcf_path, "w") as f:
            f.write("##fileformat=VCFv4.2\n")
            f.write('##INFO=<ID=CSQ,Number=.,Type=String,Description="Format: Allele|...|HGVSc|...|CDS_position|...">\n')
            f.write('##INFO=<ID=AF,Number=A,Type=Float,Description="Allele Frequency">\n')
            f.write('##INFO=<ID=Artifact,Number=1,Type=String,Description="Artifact">\n')
            f.write('##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">\n')
            f.write('##FORMAT=<ID=PS,Number=1,Type=Integer,Description="Phase set">\n')
            f.write("#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\tSAMPLE\n")

            # Codon 2: GGC (pos 4,5,6)
            # Variant 1: G4>A (c.4G>A)
            # Variant 2: G5>A (c.5G>A)
            # Variant 3: G4>T (c.4G>T) - different PS
            # Variant 4: G5>T (c.5G>T) - different phase

            csq_v1 = "A|missense|MOD|G|1|T|T1|pc|1/1||G:c.4G>A||4|4|2||Ggc/Agc||-1||||||"
            csq_v2 = "A|missense|MOD|G|1|T|T1|pc|1/1||G:c.5G>A||5|5|2||gGc/gAc||-1||||||"
            csq_v3 = "T|missense|MOD|G|1|T|T1|pc|1/1||G:c.4G>T||4|4|2||Ggc/Tgc||-1||||||"
            csq_v4 = "T|missense|MOD|G|1|T|T1|pc|1/1||G:c.5G>T||5|5|2||gGc/gTc||-1||||||"

            # Phased together (should combine)
            f.write(f"chrPhase\t4\t.\tG\tA\t100\tPASS\tAF=0.5;Artifact=0,;CSQ={csq_v1}\tGT:PS\t0|1:100\n")
            f.write(f"chrPhase\t5\t.\tG\tA\t100\tPASS\tAF=0.5;Artifact=0,;CSQ={csq_v2}\tGT:PS\t0|1:100\n")

            # Phased differently (should NOT combine)
            csq_v_diff_p1 = "A|missense|MOD|G|1|T|T1|pc|1/1||G:c.7T>A||7|7|3||Tga/Aga||-1||||||"
            f.write(f"chrPhase\t7\t.\tT\tA\t100\tPASS\tAF=0.5;Artifact=0,;CSQ={csq_v_diff_p1}\tGT:PS\t0|1:100\n")
            csq_v_diff_p2 = "T|missense|MOD|G|1|T|T1|pc|1/1||G:c.8G>T||8|8|3||tGa/tTa||-1||||||"
            f.write(f"chrPhase\t8\t.\tG\tT\t100\tPASS\tAF=0.5;Artifact=0,;CSQ={csq_v_diff_p2}\tGT:PS\t1|0:100\n")

            # Different Phase Set (should NOT combine)
            csq_v_diff_ps1 = "T|missense|MOD|G|1|T|T1|pc|1/1||G:c.10G>T||10|10|4||||-1||||||"
            f.write(f"chrPhase\t10\t.\tG\tT\t100\tPASS\tAF=0.5;Artifact=0,;CSQ={csq_v_diff_ps1}\tGT:PS\t0|1:100\n")
            csq_v_diff_ps2 = "T|missense|MOD|G|1|T|T1|pc|1/1||G:c.11G>T||11|11|4||||-1||||||"
            f.write(f"chrPhase\t11\t.\tG\tT\t100\tPASS\tAF=0.5;Artifact=0,;CSQ={csq_v_diff_ps2}\tGT:PS\t0|1:200\n")

        out_vcf_path = os.path.join(self.tempdir, "phased_out.vcf")
        add_multi_snv_in_codon(fasta_path, open(in_vcf_path), open(out_vcf_path, "w"), 0.0, 1000, "")

        # Verify results
        result = VariantFile(out_vcf_path)
        combined_positions = []
        for v in result:
            if "AA" in v.info:
                combined_positions.append(v.start + 1)

        # Should only have combined variant at position 4 (from pos 4 and 5)
        # Positions 7/8 (opposing phase) and 10/11 (different PS) should NOT be here
        self.assertIn(4, combined_positions)
        self.assertNotIn(7, combined_positions)
        self.assertNotIn(10, combined_positions)
