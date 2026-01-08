"""
COMPOSER STATISTICAL VALIDATOR
=============================

Provides rigorous statistical analysis for Composer framework validation.
Implements chi-square tests, t-tests, confidence intervals, and significance testing.
"""

import math
import json
import statistics
from typing import List, Dict, Tuple
import random
from scipy import stats
import numpy as np

class ComposerStatisticalValidator:
    """Rigorous statistical validation of Composer framework."""
    
    def __init__(self):
        self.significance_level = 0.05
        self.confidence_level = 0.95
        
    def chi_square_goodness_of_fit(self, observed_counts: List[int], expected_counts: List[int]) -> Dict:
        """Perform chi-square goodness of fit test."""
        
        if len(observed_counts) != len(expected_counts):
            raise ValueError("Observed and expected counts must have same length")
        
        # Calculate chi-square statistic
        chi_square = 0.0
        for obs, exp in zip(observed_counts, expected_counts):
            if exp > 0:
                chi_square += ((obs - exp) ** 2) / exp
        
        # Degrees of freedom
        df = len(observed_counts) - 1
        
        # p-value (using scipy if available, otherwise approximation)
        try:
            p_value = 1 - stats.chi2.cdf(chi_square, df)
        except:
            # Simplified approximation for large chi-square
            p_value = 0.05 if chi_square > stats.chi2.ppf(0.95, df) else 0.1
        
        # Critical value
        critical_value = stats.chi2.ppf(1 - self.significance_level, df)
        
        return {
            'chi_square_statistic': chi_square,
            'degrees_of_freedom': df,
            'p_value': p_value,
            'critical_value': critical_value,
            'significant': p_value < self.significance_level,
            'effect_size': math.sqrt(chi_square / (len(observed_counts) * df))  # Cohen's w
        }
    
    def two_sample_t_test(self, sample1: List[float], sample2: List[float]) -> Dict:
        """Perform two-sample t-test."""
        
        n1, n2 = len(sample1), len(sample2)
        if n1 < 2 or n2 < 2:
            return {'error': 'Samples must have at least 2 observations each'}
        
        mean1, mean2 = statistics.mean(sample1), statistics.mean(sample2)
        var1, var2 = statistics.variance(sample1), statistics.variance(sample2)
        
        # Pooled standard error
        pooled_se = math.sqrt(((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2))
        standard_error = pooled_se * math.sqrt(1/n1 + 1/n2)
        
        # t-statistic
        t_statistic = (mean1 - mean2) / standard_error if standard_error > 0 else 0
        
        # Degrees of freedom
        df = n1 + n2 - 2
        
        # p-value (two-tailed)
        try:
            p_value = 2 * (1 - stats.t.cdf(abs(t_statistic), df))
        except:
            p_value = 0.05 if abs(t_statistic) > 2.0 else 0.1
        
        # Effect size (Cohen's d)
        pooled_sd = math.sqrt(((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2))
        cohens_d = (mean1 - mean2) / pooled_sd if pooled_sd > 0 else 0
        
        # Confidence interval for difference
        t_critical = stats.t.ppf(1 - self.significance_level/2, df)
        margin_error = t_critical * standard_error
        ci_lower = (mean1 - mean2) - margin_error
        ci_upper = (mean1 - mean2) + margin_error
        
        return {
            't_statistic': t_statistic,
            'degrees_of_freedom': df,
            'p_value': p_value,
            'significant': p_value < self.significance_level,
            'effect_size_cohens_d': cohens_d,
            'mean_difference': mean1 - mean2,
            'confidence_interval': (ci_lower, ci_upper),
            'sample1_stats': {'n': n1, 'mean': mean1, 'std': math.sqrt(var1)},
            'sample2_stats': {'n': n2, 'mean': mean2, 'std': math.sqrt(var2)}
        }
    
    def confidence_interval_proportion(self, successes: int, trials: int) -> Dict:
        """Calculate confidence interval for proportion."""
        
        if trials == 0:
            return {'error': 'Number of trials must be greater than 0'}
        
        proportion = successes / trials
        
        # Standard error
        se = math.sqrt(proportion * (1 - proportion) / trials)
        
        # Z-score for confidence level
        z_score = stats.norm.ppf(1 - (1 - self.confidence_level) / 2)
        
        # Confidence interval
        margin_error = z_score * se
        ci_lower = max(0, proportion - margin_error)
        ci_upper = min(1, proportion + margin_error)
        
        return {
            'proportion': proportion,
            'standard_error': se,
            'confidence_level': self.confidence_level,
            'confidence_interval': (ci_lower, ci_upper),
            'margin_of_error': margin_error,
            'sample_size': trials,
            'successes': successes
        }
    
    def correlation_analysis(self, x_values: List[float], y_values: List[float]) -> Dict:
        """Analyze correlation between two variables."""
        
        if len(x_values) != len(y_values):
            raise ValueError("x_values and y_values must have same length")
        
        if len(x_values) < 3:
            return {'error': 'Need at least 3 data points for correlation analysis'}
        
        n = len(x_values)
        
        # Calculate correlation coefficient
        mean_x, mean_y = statistics.mean(x_values), statistics.mean(y_values)
        
        numerator = sum((x - mean_x) * (y - mean_y) for x, y in zip(x_values, y_values))
        sum_xx = sum((x - mean_x) ** 2 for x in x_values)
        sum_yy = sum((y - mean_y) ** 2 for y in y_values)
        
        denominator = math.sqrt(sum_xx * sum_yy)
        
        if denominator == 0:
            correlation = 0.0
        else:
            correlation = numerator / denominator
        
        # Test significance of correlation
        if abs(correlation) == 1.0:
            t_statistic = float('inf')
            p_value = 0.0
        else:
            t_statistic = correlation * math.sqrt((n - 2) / (1 - correlation ** 2))
            p_value = 2 * (1 - stats.t.cdf(abs(t_statistic), n - 2))
        
        # Confidence interval for correlation
        fisher_z = 0.5 * math.log((1 + correlation) / (1 - correlation)) if abs(correlation) < 1 else 0
        se_z = 1 / math.sqrt(n - 3)
        z_critical = stats.norm.ppf(1 - (1 - self.confidence_level) / 2)
        
        ci_lower_z = fisher_z - z_critical * se_z
        ci_upper_z = fisher_z + z_critical * se_z
        
        ci_lower = (math.exp(2 * ci_lower_z) - 1) / (math.exp(2 * ci_lower_z) + 1)
        ci_upper = (math.exp(2 * ci_upper_z) - 1) / (math.exp(2 * ci_upper_z) + 1)
        
        return {
            'correlation_coefficient': correlation,
            'sample_size': n,
            't_statistic': t_statistic,
            'p_value': p_value,
            'significant': p_value < self.significance_level,
            'confidence_interval': (ci_lower, ci_upper),
            'effect_size': abs(correlation)  # Correlation is itself an effect size
        }
    
    def monte_carlo_validation(self, observed_data: List[float], null_distribution_generator, iterations: int = 10000) -> Dict:
        """Monte Carlo simulation for validation."""
        
        observed_mean = statistics.mean(observed_data)
        observed_std = statistics.stdev(observed_data) if len(observed_data) > 1 else 0.0
        
        # Generate null distribution
        null_means = []
        for _ in range(iterations):
            null_sample = null_distribution_generator(len(observed_data))
            null_means.append(statistics.mean(null_sample))
        
        # Calculate p-value
        extreme_count = sum(1 for mean_val in null_means if abs(mean_val) >= abs(observed_mean))
        monte_carlo_p = extreme_count / iterations
        
        # Effect size (Cohen's d against null)
        null_mean_of_means = statistics.mean(null_means)
        null_std_of_means = statistics.stdev(null_means) if len(null_means) > 1 else 0.0
        
        if null_std_of_means > 0:
            cohens_d = (observed_mean - null_mean_of_means) / null_std_of_means
        else:
            cohens_d = 0.0
        
        return {
            'observed_mean': observed_mean,
            'observed_std': observed_std,
            'null_mean': null_mean_of_means,
            'null_std': null_std_of_means,
            'monte_carlo_p_value': monte_carlo_p,
            'effect_size_cohens_d': cohens_d,
            'iterations': iterations,
            'significant': monte_carlo_p < self.significance_level
        }
    
    def power_analysis(self, effect_size: float, sample_size: int, alpha: float = 0.05) -> Dict:
        """Calculate statistical power for given effect size and sample size."""
        
        # Simplified power calculation for two-sample t-test
        # This is an approximation
        
        # Critical t-value
        df = 2 * sample_size - 2
        t_critical = stats.t.ppf(1 - alpha/2, df)
        
        # Non-central t parameter
        ncp = effect_size * math.sqrt(sample_size / 2)
        
        # Power calculation (approximation)
        try:
            power = 1 - stats.nct.cdf(t_critical, df, ncp) + stats.nct.cdf(-t_critical, df, ncp)
        except:
            # Fallback approximation
            power = 0.8 if effect_size > 0.5 else 0.5 if effect_size > 0.2 else 0.2
        
        return {
            'effect_size': effect_size,
            'sample_size_per_group': sample_size,
            'alpha': alpha,
            'power': power,
            'adequate_power': power >= 0.8,
            'recommended_sample_size': self.calculate_sample_size(effect_size, desired_power=0.8, alpha=alpha)
        }
    
    def calculate_sample_size(self, effect_size: float, desired_power: float = 0.8, alpha: float = 0.05) -> int:
        """Calculate required sample size for given effect size and desired power."""
        
        # Simplified calculation for two-sample t-test
        # This is an approximation
        
        # Z-values
        z_alpha = stats.norm.ppf(1 - alpha/2)
        z_beta = stats.norm.ppf(desired_power)
        
        # Required sample size per group
        n_per_group = 2 * ((z_alpha + z_beta) / effect_size) ** 2
        
        return int(math.ceil(n_per_group))
    
    def multiple_comparison_correction(self, p_values: List[float], method: str = 'bonferroni') -> Dict:
        """Correct for multiple comparisons."""
        
        n_tests = len(p_values)
        
        if method == 'bonferroni':
            corrected_p = [min(p * n_tests, 1.0) for p in p_values]
            significant_corrected = [p < self.significance_level for p in corrected_p]
        
        elif method == 'holm_bonferroni':
            # Sort p-values
            sorted_indices = sorted(range(len(p_values)), key=lambda i: p_values[i])
            corrected_p = [0.0] * len(p_values)
            
            for i, idx in enumerate(sorted_indices):
                corrected_p[idx] = min(p_values[idx] * (n_tests - i), 1.0)
            
            significant_corrected = [p < self.significance_level for p in corrected_p]
        
        else:
            raise ValueError(f"Unknown correction method: {method}")
        
        return {
            'original_p_values': p_values,
            'corrected_p_values': corrected_p,
            'significant_original': [p < self.significance_level for p in p_values],
            'significant_corrected': significant_corrected,
            'correction_method': method,
            'num_tests': n_tests
        }

def main():
    """Demonstrate statistical validation capabilities."""
    
    print("================================================================================")
    print("COMPOSER STATISTICAL VALIDATOR")
    print("Rigorous statistical analysis for Composer framework validation")
    print("================================================================================")
    
    validator = ComposerStatisticalValidator()
    
    # Example: Test C* pattern significance
    print("\n📊 Example: C* Pattern Significance Test")
    
    # Simulated data (in real use, this would come from actual Composer results)
    observed_c_star_patterns = [450, 230, 180, 140]  # Categories of pattern strength
    expected_random = [250, 250, 250, 250]  # Expected under null hypothesis
    
    chi_square_result = validator.chi_square_goodness_of_fit(observed_c_star_patterns, expected_random)
    
    print(f"   Chi-square statistic: {chi_square_result['chi_square_statistic']:.4f}")
    print(f"   p-value: {chi_square_result['p_value']:.6f}")
    print(f"   Significant: {chi_square_result['significant']}")
    print(f"   Effect size: {chi_square_result['effect_size']:.4f}")
    
    # Example: Hardness difference test
    print("\n🔬 Example: Hardness Difference T-Test")
    
    # Simulated hardness scores
    reptend_hardness = [0.95, 0.97, 0.96, 0.98, 0.94, 0.99, 0.97, 0.96, 0.98, 0.95]
    non_reptend_hardness = [0.65, 0.68, 0.62, 0.70, 0.64, 0.66, 0.69, 0.63, 0.67, 0.65]
    
    t_test_result = validator.two_sample_t_test(reptend_hardness, non_reptend_hardness)
    
    print(f"   t-statistic: {t_test_result['t_statistic']:.4f}")
    print(f"   p-value: {t_test_result['p_value']:.6f}")
    print(f"   Significant: {t_test_result['significant']}")
    print(f"   Effect size (Cohen's d): {t_test_result['effect_size_cohens_d']:.4f}")
    print(f"   95% CI for difference: ({t_test_result['confidence_interval'][0]:.4f}, {t_test_result['confidence_interval'][1]:.4f})")
    
    # Example: Correlation analysis
    print("\n📈 Example: Pattern Correlation Analysis")
    
    # Simulated correlation between C* accuracy and 0.6 pattern presence
    c_star_accuracy = [0.98, 0.95, 0.97, 0.99, 0.96, 0.94, 0.97, 0.95, 0.98, 0.96]
    point_six_strength = [0.85, 0.82, 0.88, 0.90, 0.83, 0.80, 0.87, 0.84, 0.89, 0.86]
    
    correlation_result = validator.correlation_analysis(c_star_accuracy, point_six_strength)
    
    print(f"   Correlation coefficient: {correlation_result['correlation_coefficient']:.4f}")
    print(f"   p-value: {correlation_result['p_value']:.6f}")
    print(f"   Significant: {correlation_result['significant']}")
    print(f"   95% CI: ({correlation_result['confidence_interval'][0]:.4f}, {correlation_result['confidence_interval'][1]:.4f})")
    
    # Example: Power analysis
    print("\n⚡ Example: Power Analysis")
    
    power_result = validator.power_analysis(effect_size=0.8, sample_size=25)
    
    print(f"   Effect size: {power_result['effect_size']:.2f}")
    print(f"   Sample size per group: {power_result['sample_size_per_group']}")
    print(f"   Statistical power: {power_result['power']:.3f}")
    print(f"   Adequate power: {power_result['adequate_power']}")
    print(f"   Recommended sample size: {power_result['recommended_sample_size']}")
    
    print(f"\n✅ Statistical validator ready for Composer framework analysis!")
    
    return {
        'chi_square_example': chi_square_result,
        't_test_example': t_test_result,
        'correlation_example': correlation_result,
        'power_analysis_example': power_result
    }

if __name__ == "__main__":
    main()