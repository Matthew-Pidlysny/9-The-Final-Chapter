#!/usr/bin/env python3
"""
Debug version of the universal number tester
"""

import json
from fractions import Fraction

def delta_t_function(value):
    """Simplified ΔT function for debugging"""
    try:
        # Handle different input types
        if isinstance(value, str):
            if '.' in value:
                # Decimal string
                decimal_part = value.split('.')[1]
                if len(decimal_part) > 1:
                    # Multi-digit decimal
                    return len(decimal_part) * 10
                else:
                    # Single digit decimal
                    return 50
            else:
                # Integer string
                return int(value) * 10 if int(value) <= 9 else 0
        elif isinstance(value, (int, float)):
            if isinstance(value, float) and not value.is_integer():
                # Convert to string for processing
                return delta_t_function(str(value))
            else:
                # Integer
                return int(value) * 10 if int(value) <= 9 else 0
        else:
            raise ValueError(f"Unsupported type: {type(value)}")
            
    except Exception as e:
        print(f"ΔT function error for {value}: {str(e)}")
        return 0

def construct_number(target):
    """Simple number construction"""
    try:
        print(f"Constructing: {target}")
        
        construction = {
            'target': target,
            'success': False,
            'method': None,
            'components': [],
            'delta_t_values': [],
            'formula_application': None
        }
        
        # Validate range
        if target < 0 or target > 100:
            raise ValueError(f"Target {target} out of range [0, 100]")
        
        # Construction method based on target type
        if target == int(target):
            # Integer construction
            construction['method'] = 'integer'
            
            if target <= 9:
                # Direct single-digit integer
                delta_t = delta_t_function(target)
                construction['components'] = [target]
                construction['delta_t_values'] = [delta_t]
                construction['formula_application'] = f"ΔT({target}) = {delta_t}"
            else:
                # Multi-digit integer using digit decomposition
                digits = [int(d) for d in str(target)]
                delta_ts = []
                
                for digit in digits:
                    delta_t = delta_t_function(digit)
                    delta_ts.append(delta_t)
                
                construction['components'] = digits
                construction['delta_t_values'] = delta_ts
                construction['formula_application'] = f"Digit decomposition: {digits} → {delta_ts}"
        else:
            # Decimal construction
            construction['method'] = 'decimal'
            delta_t = delta_t_function(str(target))
            construction['components'] = [target]
            construction['delta_t_values'] = [delta_t]
            construction['formula_application'] = f"ΔT({target}) = {delta_t}"
        
        construction['success'] = True
        print(f"Success: {construction}")
        return construction
        
    except Exception as e:
        print(f"Construction failed for {target}: {str(e)}")
        return {'target': target, 'success': False, 'error': str(e)}

def main():
    """Test some sample numbers"""
    print("=== Debug Testing ===")
    
    test_values = [0, 1, 2, 5, 10, 15, 0.5, 1.5, 2.5, 3.14]
    results = []
    
    for target in test_values:
        result = construct_number(target)
        results.append(result)
        print(f"Result for {target}: {result['success']}")
        print()
    
    success_count = sum(1 for r in results if r['success'])
    print(f"Success rate: {success_count}/{len(results)} = {success_count/len(results):.2%}")

if __name__ == "__main__":
    main()