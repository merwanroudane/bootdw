# Contributing to boot_dw

Thank you for your interest in contributing to boot_dw! This document provides guidelines for contributing to the project.

## Development Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/merwanroudane/bootdw.git
   cd bootdw
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install in development mode:**
   ```bash
   pip install -e ".[dev]"
   ```

## Code Style

- Follow PEP 8 style guidelines
- Use type hints for function signatures
- Write comprehensive docstrings (NumPy style)
- Keep functions focused and modular
- Maximum line length: 100 characters

## Testing

Run the test suite before submitting:

```bash
pytest tests/ -v --cov=boot_dw --cov-report=html
```

All tests must pass, and code coverage should remain above 90%.

## Adding New Features

1. **Create a new branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Implement your feature:**
   - Add new functions to appropriate modules
   - Write comprehensive docstrings
   - Add type hints
   - Include examples in docstrings

3. **Add tests:**
   - Create test cases in `tests/test_boot_dw.py`
   - Ensure >90% code coverage
   - Test edge cases and error handling

4. **Update documentation:**
   - Update README.md if needed
   - Add examples if applicable
   - Update CHANGELOG.md

5. **Submit a pull request:**
   - Provide clear description of changes
   - Reference any related issues
   - Ensure all tests pass

## Reporting Bugs

When reporting bugs, please include:

1. Python version
2. boot_dw version
3. Operating system
4. Minimal reproducible example
5. Expected behavior
6. Actual behavior
7. Full error traceback

## Feature Requests

Feature requests are welcome! Please provide:

1. Clear description of the feature
2. Use case and motivation
3. Proposed API (if applicable)
4. References to relevant literature

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on what is best for the community
- Show empathy towards other contributors

## Questions?

If you have questions, please:

1. Check existing documentation
2. Search existing issues
3. Open a new issue if needed
4. Email: merwanroudane920@gmail.com

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Acknowledgments

Thank you for helping improve boot_dw!
