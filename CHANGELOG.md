# Changelog

All notable changes to the boot_dw package will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.1] - 2024-12-07

### Added
- Initial release of boot_dw package
- Implementation of classical Durbin-Watson (DW) test
- Implementation of Bootstrapped Durbin-Watson (BDW) test
- Implementation of Bootstrapped ρ (B-ρ) test with percentile method
- Implementation of Bias-corrected accelerated ρ (BCa-ρ) test
- Core functions:
  - `durbin_watson()`: Calculate DW statistic
  - `ols_regression()`: OLS regression with residuals
  - `estimate_rho()`: Estimate AR(1) coefficient
  - `recursive_ar1_errors()`: Generate AR(1) errors recursively
- Bootstrap procedures:
  - `recursive_bootstrap_dw()`: Bootstrap DW distribution
  - `recursive_bootstrap_rho()`: Bootstrap ρ distribution
  - `bca_confidence_interval()`: BCa confidence intervals
- Utility functions:
  - `TestResult` class for standardized output
  - `format_test_output()`: Publication-ready formatting
  - `format_latex_table()`: LaTeX table generation
  - `significance_stars()`: Significance level markers
- Comprehensive documentation with examples
- Unit tests with >90% code coverage
- Examples:
  - Quick start example
  - Comprehensive examples with all tests
  - Monte Carlo power simulation
  - LaTeX table generation
- Full API documentation with mathematical formulas
- Citation information (BibTeX format)

### Features
- Publication-ready output formatting
- Support for different alternative hypotheses (greater, less, two-sided)
- Reproducible results via random_state parameter
- Comprehensive error handling and input validation
- Type hints for better code documentation
- Follows Jeong & Chung (2001) methodology exactly
- Optimized for small sample performance

### Documentation
- Detailed README with usage examples
- API reference documentation
- Theoretical background on bootstrap methods
- Comparison with classical DW test
- Monte Carlo simulation guidelines
- Citation instructions

### Testing
- Unit tests for all core functions
- Integration tests for all test procedures
- Reproducibility tests
- Input validation tests
- Edge case handling tests

## [Unreleased]

### Planned Features
- Additional bootstrap methods (block bootstrap, wild bootstrap)
- Support for higher-order AR processes (AR(p))
- Panel data autocorrelation tests
- Parallel processing for faster bootstrap
- Visualization tools for power curves
- R interface (reticulate)
- Stata interface

---

For more information, see the [full documentation](README.md).
