# Design Explanation

The `VariantQualityAssessor` class encapsulates the core functionality, separating concerns into well-defined methods:
- `load_vcf` handles file reading.
- `assess_variant` evaluates each variant based on the provided criteria.
- `process_variants` coordinates the overall assessment process.

A helper function, `parse_vcf_line`, is responsible for extracting relevant fields from each VCF line. This modular approach ensures that the parsing logic can be tested independently, improving maintainability.

The use of `pytest` allows for comprehensive test coverage, ensuring the reliability of the code. Docker provides an isolated environment for testing, making it easy to replicate results across different systems. GitHub Actions automates the CI process, promoting seamless integration and quality assurance.
