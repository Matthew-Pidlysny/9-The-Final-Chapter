# CMake generated Testfile for 
# Source directory: /workspace
# Build directory: /workspace/build
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(UVOperatorsTest "unrh_tests")
set_tests_properties(UVOperatorsTest PROPERTIES  _BACKTRACE_TRIPLES "/workspace/CMakeLists.txt;74;add_test;/workspace/CMakeLists.txt;0;")
add_test(IntegrationTest "unrh_tests")
set_tests_properties(IntegrationTest PROPERTIES  _BACKTRACE_TRIPLES "/workspace/CMakeLists.txt;75;add_test;/workspace/CMakeLists.txt;0;")
add_test(PerformanceTest "/workspace/build/unrh_performance_test")
set_tests_properties(PerformanceTest PROPERTIES  _BACKTRACE_TRIPLES "/workspace/CMakeLists.txt;76;add_test;/workspace/CMakeLists.txt;0;")
