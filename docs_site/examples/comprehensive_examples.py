#!/usr/bin/env python3
"""
Comprehensive Examples for boot_dw Package
==========================================

This script demonstrates all features of the boot_dw package using real economic data
from the Federal Reserve Economic Data (FRED) database.

Author: Dr. Merwan Roudane
Email: merwanroudane920@gmail.com
"""

import numpy as np
import pandas as pd
from datetime import datetime

# Try to import plotting libraries
try:
    import matplotlib.pyplot as plt
    PLOT_AVAILABLE = True
except ImportError:
    print("Warning: matplotlib not available. Skipping plots.")
    PLOT_AVAILABLE = False

# Try to import data reader
try:
    from pandas_datareader import data as pdr
    FRED_AVAILABLE = True
except ImportError:
    print("Warning: pandas-datareader not available. Using simulated data.")
    FRED_AVAILABLE = False

# Import boot_dw functions
from boot_dw import (
    dw_test,
    bdw_test,
    b_rho_test,
    bca_rho_test,
    autocorrelation_test,
    durbin_watson,
    ols_regression,
    estimate_rho
)


def print_section(title):
    """Print a formatted section header."""
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80 + "\n")


def example_1_phillips_curve():
    """
    Example 1: Phillips Curve - Inflation vs Unemployment
    
    Tests for autocorrelation in the classic Phillips curve relationship.
    """
    print_section("EXAMPLE 1: Phillips Curve - Inflation vs Unemployment")
    
    if FRED_AVAILABLE:
        try:
            # Download real data from FRED
            start_date = datetime(1960, 1, 1)
            end_date = datetime(2023, 12, 31)
            
            print("Downloading data from FRED...")
            unemployment = pdr.DataReader('UNRATE', 'fred', start_date, end_date)
            cpi = pdr.DataReader('CPIAUCSL', 'fred', start_date, end_date)
            inflation = cpi.pct_change(12) * 100  # 12-month percent change
            
            # Merge datasets
            data = pd.concat([unemployment, inflation], axis=1)
            data.columns = ['unemployment', 'inflation']
            data = data.dropna()
            
            print(f"✓ Downloaded {len(data)} observations from {data.index[0]} to {data.index[-1]}")
            
            # Prepare data
            y = data['inflation'].values
            X = data['unemployment'].values.reshape(-1, 1)
            
        except Exception as e:
            print(f"Could not download FRED data: {e}")
            print("Using simulated data instead...")
            FRED_AVAILABLE = False
    
    if not FRED_AVAILABLE:
        # Simulate Phillips curve data
        np.random.seed(42)
        n = 500
        
        # Simulate unemployment rate
        X = 4 + 2 * np.random.randn(n)  # Mean unemployment ~ 4%
        
        # Simulate inflation with autocorrelated errors
        rho_true = 0.7
        errors = np.zeros(n)
        errors[0] = np.random.randn()
        for t in range(1, n):
            errors[t] = rho_true * errors[t-1] + np.random.randn() * 0.5
        
        # Phillips curve: π = 8 - 0.5*U + errors
        y = 8 - 0.5 * X + errors
        X = X.reshape(-1, 1)
        
        print(f"✓ Generated {n} simulated observations")
    
    # Run OLS regression
    print("\nRunning OLS regression...")
    beta, residuals, fitted = ols_regression(y, X, add_constant=True)
    
    print(f"\nRegression Results:")
    print(f"  Intercept: {beta[0]:.4f}")
    print(f"  Slope (unemployment): {beta[1]:.4f}")
    
    # Calculate statistics
    dw_stat = durbin_watson(residuals)
    rho_hat = estimate_rho(residuals)
    
    print(f"\nDiagnostic Statistics:")
    print(f"  Durbin-Watson statistic: {dw_stat:.4f}")
    print(f"  Estimated ρ: {rho_hat:.4f}")
    print(f"  R-squared: {1 - np.var(residuals)/np.var(y):.4f}")
    
    # Test for autocorrelation using BCa-ρ test
    print("\n" + "-" * 80)
    print("Testing for Autocorrelation using BCa-ρ Test")
    print("-" * 80)
    
    result = bca_rho_test(y, X, n_bootstrap=200, random_state=42)
    
    print(f"\nTest Results:")
    print(f"  Method: {result.method}")
    print(f"  ρ̂ = {result.statistic:.4f}")
    print(f"  P-value = {result.pvalue:.4f}")
    print(f"  95% BCa CI: [{result.additional_info['bca_interval'][0]:.4f}, "
          f"{result.additional_info['bca_interval'][1]:.4f}]")
    print(f"  Bias constant (z₀): {result.additional_info['bias_constant_z0']:.4f}")
    print(f"  Acceleration (a₀): {result.additional_info['acceleration_constant_a0']:.4f}")
    
    if result.pvalue < 0.05:
        print("\n⚠ WARNING: Significant autocorrelation detected!")
        print("  → Standard errors in OLS are biased")
        print("  → Consider using robust standard errors or GLS")
    else:
        print("\n✓ No significant autocorrelation detected")
        print("  → OLS estimates are reliable")
    
    # Plot if available
    if PLOT_AVAILABLE:
        fig, axes = plt.subplots(2, 2, figsize=(12, 10))
        
        # Scatter plot
        axes[0, 0].scatter(X, y, alpha=0.5)
        axes[0, 0].plot(X, fitted, 'r-', linewidth=2)
        axes[0, 0].set_xlabel('Unemployment Rate (%)')
        axes[0, 0].set_ylabel('Inflation Rate (%)')
        axes[0, 0].set_title('Phillips Curve')
        axes[0, 0].grid(True, alpha=0.3)
        
        # Residuals over time
        axes[0, 1].plot(residuals, alpha=0.7)
        axes[0, 1].axhline(y=0, color='r', linestyle='--')
        axes[0, 1].set_xlabel('Time')
        axes[0, 1].set_ylabel('Residuals')
        axes[0, 1].set_title('Residuals Over Time')
        axes[0, 1].grid(True, alpha=0.3)
        
        # Autocorrelation plot
        axes[1, 0].scatter(residuals[:-1], residuals[1:], alpha=0.5)
        axes[1, 0].set_xlabel('Residual(t-1)')
        axes[1, 0].set_ylabel('Residual(t)')
        axes[1, 0].set_title(f'Residual Autocorrelation (ρ̂ = {rho_hat:.4f})')
        axes[1, 0].grid(True, alpha=0.3)
        
        # Histogram
        axes[1, 1].hist(residuals, bins=30, edgecolor='black', alpha=0.7)
        axes[1, 1].set_xlabel('Residuals')
        axes[1, 1].set_ylabel('Frequency')
        axes[1, 1].set_title('Distribution of Residuals')
        axes[1, 1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('phillips_curve_diagnostics.png', dpi=300)
        print("\n✓ Plots saved to 'phillips_curve_diagnostics.png'")


def example_2_method_comparison():
    """
    Example 2: Comparing All Four Test Methods
    
    Demonstrates the differences between DW, BDW, B-ρ, and BCa-ρ tests.
    """
    print_section("EXAMPLE 2: Comparing All Four Test Methods")
    
    # Generate data with known autocorrelation
    np.random.seed(42)
    n = 100
    X = np.random.randn(n, 2)
    
    # Generate AR(1) errors with ρ = 0.6
    rho_true = 0.6
    errors = np.zeros(n)
    errors[0] = np.random.randn() / np.sqrt(1 - rho_true**2)
    for t in range(1, n):
        errors[t] = rho_true * errors[t-1] + np.random.randn()
    
    y = 2 + 3*X[:, 0] - 1.5*X[:, 1] + errors
    
    print(f"Generated data with true ρ = {rho_true}")
    print(f"Sample size: n = {n}\n")
    
    # Test using all four methods
    methods = {
        'Classical DW': ('dw', None),
        'Bootstrapped DW': ('bdw', bdw_test),
        'Bootstrapped ρ': ('b_rho', b_rho_test),
        'BCa-ρ': ('bca_rho', bca_rho_test)
    }
    
    results = {}
    
    for name, (method_code, func) in methods.items():
        print(f"{name} Test:")
        print("-" * 60)
        
        if method_code == 'dw':
            result = dw_test(y, X)
        else:
            result = func(y, X, n_bootstrap=200, random_state=42)
        
        results[name] = result
        
        print(f"  Statistic: {result.statistic:.4f}")
        if result.pvalue is not None:
            print(f"  P-value: {result.pvalue:.4f}")
            decision = "Reject H₀" if result.pvalue < 0.05 else "Fail to reject H₀"
            print(f"  Decision: {decision}")
        else:
            print(f"  P-value: Not available (use DW tables)")
        
        print()
    
    # Summary table
    print("\n" + "=" * 80)
    print("SUMMARY TABLE")
    print("=" * 80)
    print(f"{'Method':<20} {'Statistic':<12} {'P-value':<12} {'Decision':<20}")
    print("-" * 80)
    
    for name, result in results.items():
        stat = f"{result.statistic:.4f}"
        pval = f"{result.pvalue:.4f}" if result.pvalue else "N/A"
        decision = "Reject H₀" if result.pvalue and result.pvalue < 0.05 else "Fail to reject"
        if result.pvalue is None:
            decision = "Use DW tables"
        
        print(f"{name:<20} {stat:<12} {pval:<12} {decision:<20}")
    
    print("\n💡 Recommendation: Use BCa-ρ test for best performance!")


def example_3_multiple_models():
    """
    Example 3: Testing Multiple Model Specifications
    
    Shows how to test autocorrelation across different models.
    """
    print_section("EXAMPLE 3: Testing Multiple Model Specifications")
    
    np.random.seed(42)
    n = 100
    
    # Generate different models with varying autocorrelation
    models = {
        'Model 1 (No autocorrelation)': {
            'X': np.random.randn(n, 1),
            'rho': 0.0
        },
        'Model 2 (Moderate autocorrelation)': {
            'X': np.random.randn(n, 2),
            'rho': 0.4
        },
        'Model 3 (Strong autocorrelation)': {
            'X': np.random.randn(n, 3),
            'rho': 0.7
        }
    }
    
    results_summary = []
    
    for model_name, spec in models.items():
        print(f"\n{model_name} (true ρ = {spec['rho']}):")
        print("-" * 60)
        
        # Generate errors
        errors = np.zeros(n)
        if spec['rho'] > 0:
            errors[0] = np.random.randn() / np.sqrt(1 - spec['rho']**2)
            for t in range(1, n):
                errors[t] = spec['rho'] * errors[t-1] + np.random.randn()
        else:
            errors = np.random.randn(n)
        
        # Generate y
        X = spec['X']
        beta_true = np.random.randn(X.shape[1])
        y = X @ beta_true + errors
        
        # Test using BCa-ρ
        result = bca_rho_test(y, X, n_bootstrap=200, random_state=42)
        
        print(f"  ρ̂ = {result.statistic:.4f}")
        print(f"  P-value = {result.pvalue:.4f}")
        print(f"  95% CI: [{result.additional_info['bca_interval'][0]:.4f}, "
              f"{result.additional_info['bca_interval'][1]:.4f}]")
        
        if result.pvalue < 0.05:
            print(f"  ✗ Autocorrelation detected")
        else:
            print(f"  ✓ No autocorrelation")
        
        results_summary.append({
            'Model': model_name,
            'True ρ': spec['rho'],
            'ρ̂': result.statistic,
            'P-value': result.pvalue,
            'CI Lower': result.additional_info['bca_interval'][0],
            'CI Upper': result.additional_info['bca_interval'][1]
        })
    
    # Create summary DataFrame
    df = pd.DataFrame(results_summary)
    print("\n" + "=" * 80)
    print("SUMMARY OF ALL MODELS")
    print("=" * 80)
    print(df.to_string(index=False))
    
    # Plot comparison if available
    if PLOT_AVAILABLE:
        fig, ax = plt.subplots(figsize=(10, 6))
        
        models_list = [r['Model'] for r in results_summary]
        rhos = [r['ρ̂'] for r in results_summary]
        ci_lowers = [r['CI Lower'] for r in results_summary]
        ci_uppers = [r['CI Upper'] for r in results_summary]
        pvalues = [r['P-value'] for r in results_summary]
        
        y_pos = np.arange(len(models_list))
        
        # Colors based on significance
        colors = ['green' if p >= 0.05 else 'red' for p in pvalues]
        
        # Plot estimates
        ax.barh(y_pos, rhos, color=colors, alpha=0.6)
        
        # Add confidence intervals
        for i in range(len(models_list)):
            ax.plot([ci_lowers[i], ci_uppers[i]], [i, i], 'k-', linewidth=2)
            ax.plot([ci_lowers[i], ci_lowers[i]], [i-0.2, i+0.2], 'k-', linewidth=2)
            ax.plot([ci_uppers[i], ci_uppers[i]], [i-0.2, i+0.2], 'k-', linewidth=2)
        
        ax.axvline(x=0, color='blue', linestyle='--', label='H₀: ρ=0')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(models_list)
        ax.set_xlabel('Autocorrelation Coefficient (ρ)')
        ax.set_title('Autocorrelation Estimates with 95% BCa Confidence Intervals')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('model_comparison.png', dpi=300)
        print("\n✓ Plot saved to 'model_comparison.png'")


def main():
    """Run all examples."""
    print("\n" + "=" * 80)
    print("BOOT_DW PACKAGE - COMPREHENSIVE EXAMPLES")
    print("=" * 80)
    print("\nAuthor: Dr. Merwan Roudane")
    print("Email: merwanroudane920@gmail.com")
    print("Based on: Jeong & Chung (2001), Computational Statistics & Data Analysis\n")
    
    # Run examples
    example_1_phillips_curve()
    example_2_method_comparison()
    example_3_multiple_models()
    
    print("\n" + "=" * 80)
    print("ALL EXAMPLES COMPLETED SUCCESSFULLY!")
    print("=" * 80)
    print("\nFor more information, visit the documentation:")
    print("https://your-username.github.io/boot_dw/")
    print("\n")


if __name__ == "__main__":
    main()
