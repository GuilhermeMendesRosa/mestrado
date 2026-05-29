from __future__ import annotations

import numpy as np

from bspline import CurvaBSpline


def _ensure_ready(curva_a: CurvaBSpline, curva_b: CurvaBSpline, ordem: int = 0) -> None:
    if not curva_a.ready or not curva_b.ready:
        required = max(curva_a.degree, curva_b.degree) + 1
        raise ValueError(f"As duas curvas precisam de pelo menos {required} pontos de controle.")
    if curva_b.degree < ordem:
        raise ValueError(f"A curva {curva_b.name} nao suporta derivada de ordem {ordem}.")


def relatorio_continuidade(
    curva_a: CurvaBSpline,
    curva_b: CurvaBSpline,
    tolerancia: float = 1e-6,
) -> dict[str, object]:
    if not curva_a.ready or not curva_b.ready:
        return {
            "ready": False,
            "message": "Cada curva precisa de pelo menos 5 pontos para medir continuidade.",
        }

    ponto_a = curva_a.end_point()
    ponto_b = curva_b.start_point()
    derivada_a = curva_a.derivative(curva_a.parameter_range()[1], 1)
    derivada_b = curva_b.derivative(curva_b.parameter_range()[0], 1)
    derivada2_a = curva_a.derivative(curva_a.parameter_range()[1], 2)
    derivada2_b = curva_b.derivative(curva_b.parameter_range()[0], 2)

    c0_error = float(np.linalg.norm(ponto_a - ponto_b))
    c1_error = float(np.linalg.norm(derivada_a - derivada_b))
    c2_error = float(np.linalg.norm(derivada2_a - derivada2_b))

    return {
        "ready": True,
        "c0": c0_error <= tolerancia,
        "c1": c0_error <= tolerancia and c1_error <= tolerancia,
        "c2": c0_error <= tolerancia and c1_error <= tolerancia and c2_error <= tolerancia,
        "c0_error": c0_error,
        "c1_error": c1_error,
        "c2_error": c2_error,
        "ponto_a": ponto_a,
        "ponto_b": ponto_b,
        "derivada_a": derivada_a,
        "derivada_b": derivada_b,
        "derivada2_a": derivada2_a,
        "derivada2_b": derivada2_b,
    }


def verificar_c0(curva_a: CurvaBSpline, curva_b: CurvaBSpline, tolerancia: float = 1e-6) -> bool:
    report = relatorio_continuidade(curva_a, curva_b, tolerancia=tolerancia)
    return bool(report.get("ready") and report.get("c0"))


def verificar_c1(curva_a: CurvaBSpline, curva_b: CurvaBSpline, tolerancia: float = 1e-6) -> bool:
    report = relatorio_continuidade(curva_a, curva_b, tolerancia=tolerancia)
    return bool(report.get("ready") and report.get("c1"))


def verificar_c2(curva_a: CurvaBSpline, curva_b: CurvaBSpline, tolerancia: float = 1e-6) -> bool:
    report = relatorio_continuidade(curva_a, curva_b, tolerancia=tolerancia)
    return bool(report.get("ready") and report.get("c2"))


def aplicar_c0(curva_a: CurvaBSpline, curva_b: CurvaBSpline) -> dict[str, object]:
    _ensure_ready(curva_a, curva_b, ordem=0)
    delta = curva_a.end_point() - curva_b.start_point()
    curva_b.translate(delta)
    return relatorio_continuidade(curva_a, curva_b)


def aplicar_c1(curva_a: CurvaBSpline, curva_b: CurvaBSpline) -> dict[str, object]:
    _ensure_ready(curva_a, curva_b, ordem=1)
    aplicar_c0(curva_a, curva_b)

    knots = curva_b.ensure_knots()
    assert knots is not None

    p = curva_b.degree
    denom = knots[p + 1] - knots[1]
    if np.isclose(denom, 0.0):
        raise ValueError("Nao foi possivel ajustar C1 com o vetor de nos atual.")

    target_d1 = curva_a.derivative(curva_a.parameter_range()[1], 1)
    first_step = p / denom

    p0 = curva_b.control_points[0]
    p1 = p0 + target_d1 / first_step
    curva_b.set_control_point(1, p1)

    return relatorio_continuidade(curva_a, curva_b)


def aplicar_c2(curva_a: CurvaBSpline, curva_b: CurvaBSpline) -> dict[str, object]:
    _ensure_ready(curva_a, curva_b, ordem=2)
    aplicar_c1(curva_a, curva_b)

    knots = curva_b.ensure_knots()
    assert knots is not None

    p = curva_b.degree
    target_d1 = curva_a.derivative(curva_a.parameter_range()[1], 1)
    target_d2 = curva_a.derivative(curva_a.parameter_range()[1], 2)

    denom_q1 = knots[p + 2] - knots[2]
    denom_r0 = knots[p + 1] - knots[2]
    if np.isclose(denom_q1, 0.0) or np.isclose(denom_r0, 0.0):
        raise ValueError("Nao foi possivel ajustar C2 com o vetor de nos atual.")

    q1_scale = p / denom_q1
    r0_scale = (p - 1) / denom_r0

    q0 = target_d1
    q1 = q0 + target_d2 / r0_scale

    p1 = curva_b.control_points[1]
    p2 = p1 + q1 / q1_scale
    curva_b.set_control_point(2, p2)

    return relatorio_continuidade(curva_a, curva_b)
