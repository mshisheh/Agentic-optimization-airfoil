import pytest

from airfoil_opt.utils.geometry import default_geometry_params, mutate_geometry


def test_default_geometry_params_has_expected_baseline_values():
    params = default_geometry_params()

    assert params == {
        "camber": 0.02,
        "camber_pos": 0.4,
        "thickness": 0.12,
        "chord": 1.0,
    }


def test_mutate_geometry_scales_every_parameter_deterministically():
    params = {"camber": 0.02, "thickness": 0.1}

    mutated = mutate_geometry(params, scale=0.1)

    assert mutated["camber"] == pytest.approx(0.022)
    assert mutated["thickness"] == pytest.approx(0.11)
