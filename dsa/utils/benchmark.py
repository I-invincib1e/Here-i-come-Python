"""
Benchmarking utilities for DSA algorithm comparisons.
Provides timing and performance analysis tools.
"""

import time
from typing import Any, Callable, Dict, List, Tuple
from functools import wraps


def time_function(func: Callable) -> Callable:
    """Decorator to time function execution.

    Args:
        func: Function to time

    Returns:
        Wrapped function that returns (result, execution_time)
    """
    @wraps(func)
    def wrapper(*args, **kwargs) -> Tuple[Any, float]:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        return result, execution_time
    return wrapper


def benchmark_algorithms(algorithms: Dict[str, Callable],
                        test_cases: List[Tuple],
                        iterations: int = 5) -> Dict[str, Dict]:
    """Benchmark multiple algorithms against the same test cases.

    Runs each algorithm on each test case multiple times to get reliable
    performance measurements, handling both successful runs and failures.

    Args:
        algorithms: Dict mapping algorithm names to functions
        test_cases: List of argument tuples to test with
        iterations: Number of times to run each test for averaging

    Returns:
        Dict with algorithm names as keys and performance stats as values
    """
    results = {}

    for name, func in algorithms.items():
        # Initialize tracking structure for this algorithm
        algorithm_results = {
            'total_time': 0.0,
            'avg_time': 0.0,
            'min_time': float('inf'),
            'max_time': 0.0,
            'test_results': [],
            'success_rate': 0.0
        }

        successful_runs = 0

        # Test this algorithm against each test case
        for test_case in test_cases:
            case_times = []
            case_success = False

            # Run multiple iterations for statistical reliability
            for _ in range(iterations):
                try:
                    # Time the function execution
                    timed_func = time_function(func)
                    result, exec_time = timed_func(*test_case)

                    # Record timing data
                    case_times.append(exec_time)
                    algorithm_results['total_time'] += exec_time
                    algorithm_results['min_time'] = min(algorithm_results['min_time'], exec_time)
                    algorithm_results['max_time'] = max(algorithm_results['max_time'], exec_time)

                    # Count successful test case completion (not per iteration)
                    if not case_success:
                        case_success = True
                        successful_runs += 1

                except Exception as e:
                    # Handle algorithm failures gracefully
                    case_times.append(float('inf'))
                    continue

            # Store detailed results for this test case
            algorithm_results['test_results'].append({
                'args': test_case,
                'times': case_times,
                'avg_time': sum(t for t in case_times if t != float('inf')) / len([t for t in case_times if t != float('inf')]) if case_times else 0
            })

        # Calculate final statistics across all test cases
        total_test_cases = len(test_cases)
        algorithm_results['success_rate'] = successful_runs / total_test_cases if total_test_cases > 0 else 0
        algorithm_results['avg_time'] = algorithm_results['total_time'] / (successful_runs * iterations) if successful_runs > 0 else 0

        results[name] = algorithm_results

    return results


def print_performance_comparison(results: Dict[str, Dict]) -> None:
    """Print a formatted performance comparison table.

    Args:
        results: Benchmark results from benchmark_algorithms
    """
    print("\n" + "="*80)
    print("ALGORITHM PERFORMANCE COMPARISON")
    print("="*80)

    # Header
    print(f"{'Algorithm':<25} {'Avg Time (ms)':<15} {'Min Time (ms)':<15} {'Max Time (ms)':<15} {'Success Rate':<12}")
    print("-" * 80)

    # Results
    for name, stats in results.items():
        avg_ms = stats['avg_time'] * 1000  # Convert to milliseconds
        min_ms = stats['min_time'] * 1000
        max_ms = stats['max_time'] * 1000
        success_pct = stats['success_rate'] * 100

        print(f"{name:<25} {avg_ms:<15.4f} {min_ms:<15.4f} {max_ms:<15.4f} {success_pct:<12.1f}%")

    print("="*80)


def compare_two_sum_algorithms() -> None:
    """Demonstrate performance comparison between two_sum approaches."""
    from dsa.problems.arrays import two_sum, two_sum_brute_force

    # Test cases of different sizes
    test_cases = [
        ([2, 7, 11, 15], 9),      # Small case
        ([3, 2, 4], 6),            # Another small case
        ([1, 2, 3, 4, 5] * 20, 9), # Medium case (100 elements)
        ([1, 2, 3, 4, 5] * 40, 9), # Large case (200 elements)
    ]

    algorithms = {
        'Brute Force O(n²)': two_sum_brute_force,
        'Hash Map O(n)': two_sum
    }

    print("Benchmarking Two Sum Algorithms...")
    print("Test cases range from 4 to 200 elements")

    results = benchmark_algorithms(algorithms, test_cases, iterations=3)
    print_performance_comparison(results)

    # Show theoretical complexity
    print("\nTheoretical Complexity Analysis:")
    print("• Brute Force: O(n²) - Checks every pair, scales poorly")
    print("• Hash Map: O(n) - Single pass with constant-time lookups")
    print("• Break-even point: Around n=1000 for most practical purposes")
    print("\n💡 Learning Takeaway:")
    print("The hash map approach demonstrates the power of space-time tradeoffs.")
    print("While it uses O(n) extra space, it achieves O(n) time complexity,")
    print("making it suitable for large datasets where performance matters.")


if __name__ == "__main__":
    compare_two_sum_algorithms()
