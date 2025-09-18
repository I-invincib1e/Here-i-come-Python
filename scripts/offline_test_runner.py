#!/usr/bin/env python3
"""
Offline Test Runner for Python Practice Projects

This script runs all tests in the project without requiring internet access.
It provides detailed output and supports various test formats.

Usage:
    python scripts/offline_test_runner.py
    python scripts/offline_test_runner.py --verbose
    python scripts/offline_test_runner.py --coverage
"""

import os
import sys
import time
import importlib.util
import traceback
from pathlib import Path
from typing import List, Tuple, Dict
import argparse


class TestRunner:
    """Offline test runner for Python projects."""

    def __init__(self, verbose: bool = False, show_coverage: bool = False):
        self.verbose = verbose
        self.show_coverage = show_coverage
        self.results = {
            'passed': 0,
            'failed': 0,
            'errors': 0,
            'total': 0,
            'duration': 0
        }
        self.start_time = time.time()

    def find_test_files(self) -> List[Path]:
        """Find all test files in the project."""
        test_files = []

        # Common test directories
        test_dirs = ['tests', 'test']

        for root, dirs, files in os.walk('.'):
            # Skip common non-test directories
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['__pycache__', 'node_modules']]

            for file in files:
                if file.startswith('test_') and file.endswith('.py'):
                    test_files.append(Path(root) / file)

        return test_files

    def run_single_test_file(self, test_file: Path) -> Tuple[int, int, int]:
        """Run all tests in a single test file."""
        passed = 0
        failed = 0
        errors = 0

        try:
            # Import the test module
            spec = importlib.util.spec_from_file_location(
                test_file.stem, str(test_file)
            )
            if spec is None or spec.loader is None:
                print(f"❌ Could not load {test_file}")
                return 0, 0, 1

            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            # Find and run test functions
            test_functions = [
                attr for attr in dir(module)
                if attr.startswith('test_') and callable(getattr(module, attr))
            ]

            if not test_functions:
                if self.verbose:
                    print(f"⚠️  No test functions found in {test_file}")
                return 0, 0, 0

            print(f"\\n📋 Running {test_file.name} ({len(test_functions)} tests)")

            for test_func_name in test_functions:
                try:
                    test_func = getattr(module, test_func_name)
                    test_func()
                    print(f"  ✅ {test_func_name}")
                    passed += 1
                except Exception as e:
                    print(f"  ❌ {test_func_name}: {e}")
                    if self.verbose:
                        traceback.print_exc()
                    failed += 1

        except Exception as e:
            print(f"❌ Error loading {test_file}: {e}")
            if self.verbose:
                traceback.print_exc()
            errors += 1

        return passed, failed, errors

    def calculate_coverage(self) -> Dict[str, float]:
        """Calculate basic test coverage metrics."""
        # This is a simple implementation - in a real scenario you'd use coverage.py
        coverage_data = {
            'lines_covered': 0,
            'total_lines': 0,
            'functions_tested': 0,
            'total_functions': 0
        }

        # Count Python files and functions
        for root, dirs, files in os.walk('.'):
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['__pycache__']]

            for file in files:
                if file.endswith('.py') and not file.startswith('test_'):
                    file_path = Path(root) / file
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()

                        lines = len([line for line in content.split('\\n') if line.strip()])
                        functions = len([line for line in content.split('\\n') if line.strip().startswith('def ')])

                        coverage_data['total_lines'] += lines
                        coverage_data['total_functions'] += functions

                    except Exception:
                        continue

        return coverage_data

    def run_all_tests(self) -> Dict[str, int]:
        """Run all tests in the project."""
        print("🚀 Starting Offline Test Runner")
        print("=" * 50)

        test_files = self.find_test_files()

        if not test_files:
            print("❌ No test files found!")
            return self.results

        print(f"📁 Found {len(test_files)} test files")

        for test_file in test_files:
            passed, failed, errors = self.run_single_test_file(test_file)
            self.results['passed'] += passed
            self.results['failed'] += failed
            self.results['errors'] += errors
            self.results['total'] += passed + failed + errors

        # Calculate duration
        self.results['duration'] = time.time() - self.start_time

        return self.results

    def print_summary(self):
        """Print test results summary."""
        print("\\n" + "=" * 50)
        print("📊 TEST RESULTS SUMMARY")
        print("=" * 50)

        results = self.results
        total_tests = results['total']
        passed = results['passed']
        failed = results['failed']
        errors = results['errors']

        print(f"Total Tests: {total_tests}")
        print(f"✅ Passed: {passed}")
        print(f"❌ Failed: {failed}")
        print(f"⚠️  Errors: {errors}")
        print(".2f")
        print(".2f")

        if self.show_coverage:
            print("\\n📈 CODE COVERAGE (Estimated)")
            coverage = self.calculate_coverage()
            if coverage['total_lines'] > 0:
                line_coverage = (coverage['lines_covered'] / coverage['total_lines']) * 100
                print(".1f")
            if coverage['total_functions'] > 0:
                func_coverage = (coverage['functions_tested'] / coverage['total_functions']) * 100
                print(".1f")

        # Success message
        if failed == 0 and errors == 0:
            print("\\n🎉 All tests passed! Your code is working correctly.")
        else:
            print(f"\\n⚠️  {failed + errors} tests need attention.")

        print(".2f")


def main():
    parser = argparse.ArgumentParser(description='Offline Test Runner for Python Projects')
    parser.add_argument('-v', '--verbose', action='store_true', help='Show detailed output')
    parser.add_argument('-c', '--coverage', action='store_true', help='Show coverage information')
    parser.add_argument('-f', '--file', help='Run specific test file')

    args = parser.parse_args()

    runner = TestRunner(verbose=args.verbose, show_coverage=args.coverage)

    if args.file:
        # Run specific test file
        test_file = Path(args.file)
        if test_file.exists():
            passed, failed, errors = runner.run_single_test_file(test_file)
            runner.results['passed'] = passed
            runner.results['failed'] = failed
            runner.results['errors'] = errors
            runner.results['total'] = passed + failed + errors
            runner.print_summary()
        else:
            print(f"❌ Test file not found: {args.file}")
    else:
        # Run all tests
        runner.run_all_tests()
        runner.print_summary()


if __name__ == "__main__":
    main()
