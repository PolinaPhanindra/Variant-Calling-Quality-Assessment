import pytest
from src.variant_quality_assessor import VariantQualityAssessor, parse_vcf_line


@pytest.fixture
def sample_vcf_data():
    return """##fileformat=VCFv4.2
##INFO=<ID=DP,Number=1,Type=Integer,Description="Read Depth">
##INFO=<ID=AF,Number=A,Type=Float,Description="Allele Frequency">
#CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO	FORMAT	SAMPLE
1	12345	rs1234	A	C	50	PASS	.	GT:AD:AF:DP	0/1:20,30:0.1:500
1	12346	rs5678	T	G	50	PASS	.	GT:AD:AF:DP	0/1:5,10:0.25:100
"""


def test_parse_vcf_line():
    line = "1\t12345\trs1234\tA\tC\t50\tPASS\t.\tGT:AD:AF:DP\t0/1:20,30:0.1:500"
    result = parse_vcf_line(line)
    assert result["ID"] == "rs1234"
    assert result["DP"] == 500
    assert result["AF"] == 0.1


def test_assess_variant_pass():
    assessor = VariantQualityAssessor()
    variant = {"ID": "rs1234", "DP": 500, "AF": 0.1}
    assert assessor.assess_variant(variant) == "PASS"


def test_assess_variant_fail():
    assessor = VariantQualityAssessor()
    variant = {"ID": "rs5678", "DP": 100, "AF": 0.25}
    assert assessor.assess_variant(variant) == "FAIL"


def test_process_variants(sample_vcf_data, tmp_path):
    file_path = tmp_path / "sample.vcf"
    with open(file_path, "w") as f:
        f.write(sample_vcf_data)

    assessor = VariantQualityAssessor()
    assessor.load_vcf(file_path)
    results = assessor.process_variants()
    assert len(results) == 2
    assert results[0] == ("rs1234", "PASS")
    assert results[1] == ("rs5678", "FAIL")
