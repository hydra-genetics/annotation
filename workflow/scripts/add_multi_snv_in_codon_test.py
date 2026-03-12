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
