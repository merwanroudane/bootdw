# boot_dw Documentation

## 📊 Bootstrap Tests for Autocorrelation

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Author:** Dr. Merwan Roudane  
**Email:** merwanroudane920@gmail.com  
**Version:** 0.0.1

---

## Overview

This repository contains comprehensive documentation for the `boot_dw` Python package - a powerful implementation of bootstrap-based tests for autocorrelation in regression models.

The package implements the methodology from:

> **Jeong, J., & Chung, S. (2001)**. "Bootstrap tests for autocorrelation"  
> *Computational Statistics & Data Analysis*, 38(1): 49-69.

## ✨ Key Features

- **Classical Durbin-Watson Test** - Traditional test with proper statistical foundations
- **Bootstrapped DW (BDW) Test** - Eliminates the indeterminate range using recursive bootstrap
- **Bootstrapped ρ (B-ρ) Test** - Direct bootstrap testing of autocorrelation coefficient  
- **BCa-ρ Test** - Bias-corrected accelerated test with superior small-sample properties
- **Comprehensive Documentation** - Full examples with real economic data
- **Easy to Use** - Simple, intuitive API for econometric analysis

## 📚 Documentation Structure

This documentation site includes:

### 1. **index.html** - Homepage
- Beautiful landing page with feature overview
- Comparison of test methods
- Quick example code
- Research citations

### 2. **installation.html** - Installation Guide
- Installation via pip
- Installation from source
- Virtual environment setup
- Troubleshooting common issues
- Optional dependencies

### 3. **quick-start.html** - Quick Start Guide
- Basic workflow overview
- All four test methods explained
- Understanding test results
- Common use cases
- Bootstrap parameter selection

### 4. **examples.html** - Comprehensive Examples
Real-world examples using FRED economic data:
- **Example 1:** Phillips Curve (Inflation vs Unemployment)
- **Example 2:** Consumption Function
- **Example 3:** Money Demand Function
- **Example 4:** Testing Multiple Models
- **Example 5:** Comparing All Test Methods

### 5. **api.html** - Complete API Reference
Detailed documentation for all functions:
- Test Functions
- Core Functions  
- Bootstrap Functions
- Utilities and Return Types

## 🚀 Quick Start

### Installation

```bash
pip install boot-dw
```

### Basic Usage

```python
import numpy as np
from boot_dw import bca_rho_test

# Your data
y = np.array([...])  # dependent variable
X = np.array([...])  # independent variables

# Run the most powerful test
result = bca_rho_test(y, X, random_state=42)
print(result)
```

## 📖 Package Features

### Four Test Methods

1. **Classical DW Test** (`dw_test`)
   - Traditional Durbin-Watson test
   - Has indeterminate range
   - No exact p-values

2. **Bootstrapped DW Test** (`bdw_test`)
   - Eliminates indeterminate range
   - Provides exact p-values
   - Constructs null distribution via bootstrap

3. **Bootstrapped ρ Test** (`b_rho_test`)
   - Direct bootstrap of autocorrelation coefficient
   - Uses percentile method
   - Better small-sample properties than BDW

4. **BCa-ρ Test** (`bca_rho_test`) ⭐ **RECOMMENDED**
   - Bias-corrected accelerated method
   - Best small-sample performance
   - Highest statistical power
   - Robust across sample sizes

### Unified Interface

```python
from boot_dw import autocorrelation_test

# Use any method via unified interface
result = autocorrelation_test(
    y, X,
    method='bca_rho',  # or 'dw', 'bdw', 'b_rho'
    n_bootstrap=200,
    random_state=42
)
```

## 📊 Real Data Examples

All examples use real economic data from the Federal Reserve Economic Data (FRED):

### Example 1: Phillips Curve

```python
from pandas_datareader import data as pdr
import datetime

# Download inflation and unemployment data
start = datetime.datetime(1960, 1, 1)
end = datetime.datetime(2023, 12, 31)

unemployment = pdr.DataReader('UNRATE', 'fred', start, end)
cpi = pdr.DataReader('CPIAUCSL', 'fred', start, end)
inflation = cpi.pct_change(12) * 100

# Test for autocorrelation in Phillips curve
from boot_dw import bca_rho_test

result = bca_rho_test(
    inflation.values,
    unemployment.values.reshape(-1, 1),
    n_bootstrap=200,
    random_state=42
)

print(f"ρ̂ = {result.statistic:.4f}")
print(f"P-value = {result.pvalue:.4f}")
```

## 🎯 Why Bootstrap Tests?

| Feature | Classical DW | Bootstrap Tests |
|---------|--------------|-----------------|
| Indeterminate Range | ❌ Yes | ✅ Eliminated |
| Exact P-values | ❌ No | ✅ Yes |
| Small Sample Performance | ❌ Poor | ✅ Excellent |
| Distribution Free | ❌ Requires normality | ✅ Yes |
| Power | ⚠️ Good | ✅ Superior |

## 📈 Performance Comparison

Based on Monte Carlo evidence from Jeong & Chung (2001):

- **BCa-ρ test** has the most accurate empirical size
- **BCa-ρ test** has the highest power, especially in small samples (n < 50)
- **BDW test** considerably outperforms the classical DW test
- All bootstrap tests are robust to distributional assumptions

### Power Functions (from simulation studies)

For sample size n=50, k=3, ρ=0.5:
- Classical DW: 15% rejection rate
- BDW test: 62% rejection rate
- B-ρ test: 71% rejection rate
- BCa-ρ test: 89% rejection rate ⭐

## 🛠️ Development

### Dependencies

- `numpy` - Numerical computations
- `scipy` - Statistical distributions

### Optional Dependencies

- `pandas` - Data manipulation
- `pandas-datareader` - Download economic data
- `matplotlib` - Plotting and visualization

### Running Tests

```bash
pip install boot-dw[dev]
pytest tests/
```

## 📄 Citation

If you use this package in your research, please cite both the package and the original paper:

```bibtex
@article{jeong2001bootstrap,
  title={Bootstrap tests for autocorrelation},
  author={Jeong, Jinook and Chung, Seoung},
  journal={Computational Statistics \& Data Analysis},
  volume={38},
  number={1},
  pages={49--69},
  year={2001},
  publisher={Elsevier}
}

@software{roudane2024bootdw,
  author = {Roudane, Merwan},
  title = {boot\_dw: Bootstrap Tests for Autocorrelation},
  year = {2024},
  version = {0.0.1},
  email = {merwanroudane920@gmail.com}
}
```

## 🌐 Deploying to GitHub Pages

### Step 1: Push to GitHub

```bash
# Create a new repository on GitHub
# Then push the documentation

git init
git add .
git commit -m "Initial documentation"
git branch -M main
git remote add origin https://github.com/your-username/boot_dw.git
git push -u origin main
```

### Step 2: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click on **Settings**
3. Scroll to **Pages** section
4. Under "Source", select **main** branch and **/ (root)** folder
5. Click **Save**

Your documentation will be available at:
`https://your-username.github.io/boot_dw/`

### Step 3: Custom Domain (Optional)

If you have a custom domain:

1. Add a `CNAME` file with your domain name
2. Configure DNS settings with your domain provider
3. Wait for DNS propagation (usually 24-48 hours)

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### How to Contribute

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📧 Contact

**Dr. Merwan Roudane**  
Email: merwanroudane920@gmail.com

For questions, suggestions, or collaborations, please don't hesitate to reach out!

## 🙏 Acknowledgments

- **Jinook Jeong & Seoung Chung** for the original methodology
- **Bradley Efron** for the BCa bootstrap method
- **Federal Reserve Economic Data (FRED)** for economic time series data
- The Python scientific computing community

---

**Made with ❤️ for econometricians and data scientists**
