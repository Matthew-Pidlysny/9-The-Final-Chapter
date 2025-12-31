"""
ZeroHex Tredecim Structure Validation
Validates code structure without GUI dependencies
"""

import ast
import os
import sys

def validate_python_syntax(file_path):
    """Validate Python syntax"""
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        ast.parse(content)
        return True, "Syntax OK"
    except SyntaxError as e:
        return False, f"Syntax Error: {e}"
    except Exception as e:
        return False, f"Error: {e}"

def validate_imports(file_path):
    """Check imports structure"""
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        
        tree = ast.parse(content)
        imports = []
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.append(alias.name)
            elif isinstance(node, ast.ImportFrom):
                module = node.module or ""
                for alias in node.names:
                    imports.append(f"{module}.{alias.name}")
                    
        return True, imports
    except Exception as e:
        return False, [f"Error: {e}"]

def validate_class_structure(file_path):
    """Validate class definitions"""
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        
        tree = ast.parse(content)
        classes = []
        
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                methods = []
                for item in node.body:
                    if isinstance(item, ast.FunctionDef):
                        methods.append(item.name)
                classes.append({
                    'name': node.name,
                    'methods': methods,
                    'method_count': len(methods)
                })
                
        return True, classes
    except Exception as e:
        return False, [f"Error: {e}"]

def main():
    """Main validation"""
    print("🔍 ZeroHex Tredecim Structure Validation")
    print("=" * 50)
    
    # Files to validate
    files_to_check = [
        'zerohex_tredecim_final_complete.py',
        'zerohex_tredecim_workshop_14.py',
        'test_zerohex_bug_free.py'
    ]
    
    total_files = 0
    passed_files = 0
    
    for file_path in files_to_check:
        if os.path.exists(file_path):
            total_files += 1
            print(f"\n📁 Validating: {file_path}")
            
            # Check syntax
            syntax_ok, syntax_msg = validate_python_syntax(file_path)
            print(f"   Syntax: {'✅' if syntax_ok else '❌'} {syntax_msg}")
            
            if syntax_ok:
                # Check imports
                imports_ok, imports = validate_imports(file_path)
                print(f"   Imports: {'✅' if imports_ok else '❌'} {len(imports)} imports found")
                
                # Check classes
                classes_ok, classes = validate_class_structure(file_path)
                if classes_ok:
                    print(f"   Classes: ✅ {len(classes)} classes found")
                    for cls in classes:
                        print(f"      - {cls['name']}: {cls['method_count']} methods")
                        
                        # Check for required methods in main classes
                        if 'Widget' in cls['name'] or 'App' in cls['name']:
                            if 'init_ui' in cls['methods']:
                                print(f"        ✅ Has init_ui method")
                            if 'add_module_content' in cls['methods']:
                                print(f"        ✅ Has add_module_content method")
                
                passed_files += 1
            else:
                print(f"   ❌ Failed validation")
        else:
            print(f"\n❌ File not found: {file_path}")
    
    print(f"\n📊 Validation Summary:")
    print(f"   Total files: {total_files}")
    print(f"   Passed: {passed_files}")
    print(f"   Success rate: {(passed_files/total_files*100):.1f}%" if total_files > 0 else "0%")
    
    # Check for specific ZeroHex requirements
    print(f"\n🎯 ZeroHex Requirements Check:")
    
    main_file = 'zerohex_tredecim_final_complete.py'
    if os.path.exists(main_file):
        with open(main_file, 'r') as f:
            content = f.read()
        
        requirements = {
            '14 workshops': 'class.*Widget.*14' or 'Module 14',
            'Beta Sequence': 'BetaSequenceExplorer',
            '13-Heartbeat': 'HeartbeatStudio', 
            'Hexagonal': 'HexagonalConstantLab',
            'Base-13': 'Base13Calculator',
            'Riemann': 'RiemannThirteenBridge',
            'OPGS': 'OPGSConvergenceAnalyzer',
            'Dimensions': 'DimensionalEmergenceStudio',
            'U-V Duality': 'UVDualityWorkbench',
            'Sequinor': 'SequinorAxiomNavigator',
            'Pi Judgment': 'PiJudgmentFramework',
            '137-Displacement': 'DisplacementLaboratory',
            'RCO': 'RCOCitizenshipVerifier',
            'Unified': 'UnifiedPatternSynthesizer',
            'Academy': 'Ultimate13StudyAcademy'
        }
        
        for req, pattern in requirements.items():
            if pattern in content:
                print(f"   ✅ {req}: Found")
            else:
                print(f"   ❌ {req}: Not found")
    
    # Check workshop 14 for 5000 features
    workshop_14 = 'zerohex_tredecim_workshop_14.py'
    if os.path.exists(workshop_14):
        with open(workshop_14, 'r') as f:
            content = f.read()
        
        if '5000' in content:
            print(f"   ✅ 5000 features: Found")
        else:
            print(f"   ❌ 5000 features: Not found")
            
        feature_categories = [
            'Algebra Detection',
            'Number Theory', 
            'Geometry',
            'Calculus',
            'Statistics',
            'Combinatorics',
            'Pattern Recognition',
            'Problem Solving',
            'Research Tools'
        ]
        
        found_categories = 0
        for category in feature_categories:
            if category in content:
                found_categories += 1
                
        print(f"   📊 Feature categories: {found_categories}/9 found")
    
    print(f"\n🎉 Validation Complete!")
    return passed_files == total_files

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)