import os

class VariantQualityAssessor:
    def __init__(self):
        self.variants = []

    def load_vcf(self, file_path: str):
        """Loads variants from a VCF file."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File {file_path} not found")
        with open(file_path, "r") as file:
            self.variants = [
                parse_vcf_line(line)
                for line in file if not line.startswith("#")
            ]

    def assess_variant(self, variant: dict) -> str:
        """Assess a single variant for PASS or FAIL based on DP and AF."""
        dp = variant.get("DP", 0)
        af = variant.get("AF", 0.0)
        if dp >= 400 and 0.001 <= af <= 0.2:
            return "PASS"
        return "FAIL"

    def process_variants(self):
        """Process all variants and return a list of (variant_id, status)."""
        results = []
        for variant in self.variants:
            variant_id = variant["ID"]
            status = self.assess_variant(variant)
            results.append((variant_id, status))
        return results


def parse_vcf_line(line: str) -> dict:
    """Parses a line from a VCF file into a dictionary with relevant fields."""
    fields = line.strip().split("\t")
    info = fields[-1].split(":")
    return {
        "CHROM": fields[0],
        "POS": fields[1],
        "ID": fields[2],
        "REF": fields[3],
        "ALT": fields[4],
        "DP": int(info[3]),  # Depth
        "AF": float(info[2]),  # Allele Frequency
    }
