#!/usr/bin/env python3
"""
Quick verification script for RAFAELIA/ZRF mathematics library.
Tests a sample of the 69 mathematical operations.
"""

import math
import sys
from pathlib import Path

# Resolve src relative to this repository instead of a provider-specific runner path.
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from mathematics import (
    derivative_sine, derivative_cosine, derivative_power, derivative_exponential,
    antiderivative_sine, antiderivative_power, antiderivative_exponential,
    inverse_linear, inverse_exponential, inverse_sine,
    get_all_operations,
)


def test_derivatives():
    """Test derivative operations."""
    print("Testing Derivatives:")
    print("-" * 50)

    result = derivative_sine(math.pi / 4)
    expected = math.cos(math.pi / 4)
    assert abs(result - expected) < 1e-10, f"Failed: sin'(π/4) = {result}, expected {expected}"
    print(f"✓ sin'(π/4) = {result:.6f} (expected {expected:.6f})")

    result = derivative_power(3, 2)
    expected = 6
    assert abs(result - expected) < 1e-10, f"Failed: (3²)' = {result}, expected {expected}"
    print(f"✓ (x²)' at x=3 = {result:.6f} (expected {expected})")

    result = math.exp(1)
    from mathematics import derivative_natural_exp
    calc_result = derivative_natural_exp(1)
    assert abs(calc_result - result) < 1e-10, f"Failed: (e^1)' = {calc_result}, expected {result}"
    print(f"✓ (e^x)' at x=1 = {calc_result:.6f} (expected e ≈ {result:.6f})")
    print()


def test_antiderivatives():
    """Test antiderivative operations."""
    print("Testing Antiderivatives:")
    print("-" * 50)

    result = antiderivative_sine(math.pi)
    expected = -math.cos(math.pi)
    assert abs(result - expected) < 1e-10, f"Failed: ∫sin(π) = {result}, expected {expected}"
    print(f"✓ ∫sin(x)dx at x=π = {result:.6f} (expected {expected:.6f})")

    result = antiderivative_power(3, 2)
    expected = 9
    assert abs(result - expected) < 1e-10, f"Failed: ∫3² = {result}, expected {expected}"
    print(f"✓ ∫x²dx at x=3 = {result:.6f} (expected {expected})")

    result = antiderivative_exponential(0)
    expected = 1
    assert abs(result - expected) < 1e-10, f"Failed: ∫e^0 = {result}, expected {expected}"
    print(f"✓ ∫e^x dx at x=0 = {result:.6f} (expected {expected})")
    print()


def test_inverses():
    """Test inverse operations."""
    print("Testing Inverse Operations:")
    print("-" * 50)

    result = inverse_linear(7, 2, 1)
    expected = 3
    assert abs(result - expected) < 1e-10, f"Failed: inverse_linear(7,2,1) = {result}, expected {expected}"
    print(f"✓ Inverse of y=2x+1 at y=7: x = {result:.6f} (expected {expected})")

    result = inverse_exponential(math.e)
    expected = 1
    assert abs(result - expected) < 1e-10, f"Failed: inverse_exponential(e) = {result}, expected {expected}"
    print(f"✓ Inverse of e^x at y=e: x = {result:.6f} (expected {expected})")

    result = inverse_sine(0.5)
    expected = math.pi / 6
    assert abs(result - expected) < 1e-10, f"Failed: inverse_sine(0.5) = {result}, expected {expected}"
    print(f"✓ Inverse of sin(x) at y=0.5: x = {result:.6f} (expected π/6 ≈ {expected:.6f})")
    print()


def test_operations_count():
    """Verify all 69 operation slots exist."""
    print("Verifying Operation Count:")
    print("-" * 50)

    ops = get_all_operations()
    count = len(ops)
    assert count == 69, f"Expected 69 operations, found {count}"
    print("✓ All 69 mathematical operations are available")

    derivatives = list(range(1, 24))
    antiderivatives = list(range(24, 47))
    inverses = list(range(47, 70))
    assert all(i in ops for i in derivatives), "Missing some derivatives"
    assert all(i in ops for i in antiderivatives), "Missing some antiderivatives"
    assert all(i in ops for i in inverses), "Missing some inverses"

    print(f"✓ Derivatives (1-23): {len(derivatives)} operations")
    print(f"✓ Antiderivatives (24-46): {len(antiderivatives)} operations")
    print(f"✓ Inverses (47-69): {len(inverses)} operations")
    print()


def main():
    """Run all tests."""
    print("=" * 70)
    print("RAFAELIA/ZRF Mathematics Library Verification")
    print("=" * 70)
    print()

    try:
        test_operations_count()
        test_derivatives()
        test_antiderivatives()
        test_inverses()

        print("=" * 70)
        print("✅ ALL TESTS PASSED!")
        print("=" * 70)
        print()
        print("Summary:")
        print("- All 69 mathematical operation slots are implemented")
        print("- Sample derivatives passed")
        print("- Sample antiderivatives passed")
        print("- Sample inverse operations passed")
        print()
        return 0

    except AssertionError as exc:
        print(f"❌ TEST FAILED: {exc}")
        return 1
    except Exception as exc:
        print(f"❌ ERROR: {exc}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
