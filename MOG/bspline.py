from __future__ import annotations

from dataclasses import dataclass, field
from typing import Sequence

import numpy as np


DEFAULT_DEGREE = 4


def _as_points_array(control_points: Sequence[Sequence[float] | np.ndarray]) -> np.ndarray:
    points = np.asarray(control_points, dtype=float)
    if points.size == 0:
        return np.empty((0, 2), dtype=float)
    if points.ndim != 2 or points.shape[1] != 2:
        raise ValueError("Os pontos de controle devem ter formato (n, 2).")
    return points


def validar_knot_vector(knots: Sequence[float], n: int, p: int) -> np.ndarray:
    knot_array = np.asarray(knots, dtype=float)
    expected_size = n + p + 2

    if knot_array.ndim != 1 or knot_array.size != expected_size:
        raise ValueError(
            f"Vetor de nos invalido: esperado {expected_size} valores, recebido {knot_array.size}."
        )
    if np.any(np.diff(knot_array) < 0.0):
        raise ValueError("O vetor de nos deve ser nao decrescente.")

    start = knot_array[0]
    end = knot_array[-1]
    if not np.allclose(knot_array[: p + 1], start):
        raise ValueError("O vetor de nos deve ser aberto no inicio.")
    if not np.allclose(knot_array[-(p + 1) :], end):
        raise ValueError("O vetor de nos deve ser aberto no fim.")

    internal_knots = knot_array[p + 1 : -(p + 1)]
    if internal_knots.size > 0:
        if np.any(internal_knots <= start) or np.any(internal_knots >= end):
            raise ValueError("Os nos internos devem estar estritamente dentro do intervalo parametrico.")
        if internal_knots.size > 1 and np.any(np.diff(internal_knots) <= 0.0):
            raise ValueError("Os nos internos devem ser estritamente crescentes.")

    return knot_array


def gerar_knots_nao_uniformes(n: int, p: int) -> np.ndarray:
    if n < p:
        raise ValueError(f"Sao necessarios pelo menos {p + 1} pontos de controle.")

    internal_count = n - p
    if internal_count > 0:
        positions = np.arange(1, internal_count + 1, dtype=float) / (internal_count + 1)
        internal_knots = positions**1.35
    else:
        internal_knots = np.empty(0, dtype=float)

    knots = np.concatenate(
        [
            np.zeros(p + 1, dtype=float),
            internal_knots,
            np.ones(p + 1, dtype=float),
        ]
    )
    return validar_knot_vector(knots, n, p)


def intervalo_parametrico(knots: Sequence[float], degree: int) -> tuple[float, float]:
    knot_array = np.asarray(knots, dtype=float)
    return float(knot_array[degree]), float(knot_array[-degree - 1])


def base_bspline(
    i: int,
    p: int,
    t: float,
    knots: Sequence[float],
    _cache: dict[tuple[int, int], float] | None = None,
) -> float:
    if _cache is None:
        _cache = {}

    key = (i, p)
    if key in _cache:
        return _cache[key]

    knot_array = np.asarray(knots, dtype=float)

    if p == 0:
        value = 1.0 if knot_array[i] <= t < knot_array[i + 1] else 0.0
        _cache[key] = value
        return value

    denom1 = knot_array[i + p] - knot_array[i]
    denom2 = knot_array[i + p + 1] - knot_array[i + 1]

    left = 0.0
    if not np.isclose(denom1, 0.0):
        left = ((t - knot_array[i]) / denom1) * base_bspline(i, p - 1, t, knot_array, _cache)

    right = 0.0
    if not np.isclose(denom2, 0.0):
        right = ((knot_array[i + p + 1] - t) / denom2) * base_bspline(
            i + 1, p - 1, t, knot_array, _cache
        )

    value = left + right
    _cache[key] = value
    return value


def avaliar_ponto_bspline(
    control_points: Sequence[Sequence[float] | np.ndarray],
    degree: int,
    knots: Sequence[float],
    t: float,
) -> np.ndarray:
    points = _as_points_array(control_points)
    if points.shape[0] < degree + 1:
        raise ValueError(f"Sao necessarios pelo menos {degree + 1} pontos de controle.")

    knot_array = validar_knot_vector(knots, points.shape[0] - 1, degree)
    start, end = intervalo_parametrico(knot_array, degree)

    if t < start and not np.isclose(t, start):
        raise ValueError("Parametro fora do intervalo valido da curva.")
    if t > end and not np.isclose(t, end):
        raise ValueError("Parametro fora do intervalo valido da curva.")
    if np.isclose(t, start):
        return points[0].copy()
    if np.isclose(t, end):
        return points[-1].copy()

    cache: dict[tuple[int, int], float] = {}
    point = np.zeros(points.shape[1], dtype=float)
    for i in range(points.shape[0]):
        point += base_bspline(i, degree, t, knot_array, cache) * points[i]
    return point


def avaliar_bspline(
    control_points: Sequence[Sequence[float] | np.ndarray],
    degree: int,
    knots: Sequence[float],
    num_samples: int = 400,
) -> np.ndarray:
    points = _as_points_array(control_points)
    if points.shape[0] < degree + 1:
        raise ValueError(f"Sao necessarios pelo menos {degree + 1} pontos de controle.")

    knot_array = validar_knot_vector(knots, points.shape[0] - 1, degree)
    start, end = intervalo_parametrico(knot_array, degree)
    sample_count = max(2, int(num_samples))
    t_values = np.linspace(start, end, sample_count)
    return np.vstack([avaliar_ponto_bspline(points, degree, knot_array, t) for t in t_values])


def derivar_pontos_controle(
    control_points: Sequence[Sequence[float] | np.ndarray],
    degree: int,
    knots: Sequence[float],
    ordem: int = 1,
) -> tuple[np.ndarray, int, np.ndarray]:
    if ordem < 0:
        raise ValueError("A ordem da derivada deve ser nao negativa.")

    points = _as_points_array(control_points)
    knot_array = validar_knot_vector(knots, points.shape[0] - 1, degree)

    if ordem == 0:
        return points.copy(), degree, knot_array.copy()
    if ordem > degree:
        return np.zeros((1, points.shape[1]), dtype=float), 0, np.array([knot_array[0], knot_array[-1]])

    derived_points = points.copy()
    derived_knots = knot_array.copy()
    derived_degree = degree

    for _ in range(ordem):
        next_points = np.zeros((derived_points.shape[0] - 1, derived_points.shape[1]), dtype=float)
        for i in range(next_points.shape[0]):
            denom = derived_knots[i + derived_degree + 1] - derived_knots[i + 1]
            if np.isclose(denom, 0.0):
                continue
            next_points[i] = (derived_degree / denom) * (derived_points[i + 1] - derived_points[i])

        derived_points = next_points
        derived_knots = derived_knots[1:-1]
        derived_degree -= 1

    return derived_points, derived_degree, derived_knots


def avaliar_derivada_bspline(
    control_points: Sequence[Sequence[float] | np.ndarray],
    degree: int,
    knots: Sequence[float],
    t: float,
    ordem: int = 1,
) -> np.ndarray:
    points = _as_points_array(control_points)
    if ordem < 0:
        raise ValueError("A ordem da derivada deve ser nao negativa.")
    if ordem == 0:
        return avaliar_ponto_bspline(points, degree, knots, t)
    if ordem > degree:
        return np.zeros(points.shape[1], dtype=float)

    derived_points, derived_degree, derived_knots = derivar_pontos_controle(
        points, degree, knots, ordem=ordem
    )
    return avaliar_ponto_bspline(derived_points, derived_degree, derived_knots, t)


@dataclass
class CurvaBSpline:
    name: str
    color: str
    degree: int = DEFAULT_DEGREE
    control_points: list[np.ndarray] = field(default_factory=list)
    knots: np.ndarray | None = None

    def __post_init__(self) -> None:
        self.control_points = [np.asarray(point, dtype=float).reshape(2) for point in self.control_points]
        if self.knots is not None:
            self.knots = np.asarray(self.knots, dtype=float)

    @property
    def ready(self) -> bool:
        return len(self.control_points) >= self.degree + 1

    @property
    def point_count(self) -> int:
        return len(self.control_points)

    def points_array(self) -> np.ndarray:
        return _as_points_array(self.control_points)

    def ensure_knots(self) -> np.ndarray | None:
        if not self.ready:
            self.knots = None
            return None

        n = self.point_count - 1
        try:
            if self.knots is None:
                raise ValueError("Knot vector ausente.")
            self.knots = validar_knot_vector(self.knots, n, self.degree)
        except ValueError:
            self.knots = gerar_knots_nao_uniformes(n, self.degree)
        return self.knots

    def regenerate_knots(self) -> np.ndarray | None:
        if not self.ready:
            self.knots = None
            return None
        self.knots = gerar_knots_nao_uniformes(self.point_count - 1, self.degree)
        return self.knots

    def add_control_point(self, point: Sequence[float] | np.ndarray) -> None:
        self.control_points.append(np.asarray(point, dtype=float).reshape(2))
        self.ensure_knots()

    def set_control_point(self, index: int, point: Sequence[float] | np.ndarray) -> None:
        self.control_points[index] = np.asarray(point, dtype=float).reshape(2)

    def translate(self, delta: Sequence[float] | np.ndarray) -> None:
        offset = np.asarray(delta, dtype=float).reshape(2)
        self.control_points = [point + offset for point in self.control_points]

    def reset(self) -> None:
        self.control_points.clear()
        self.knots = None

    def parameter_range(self) -> tuple[float, float]:
        knots = self.ensure_knots()
        if knots is None:
            raise ValueError(f"A curva {self.name} ainda nao possui pontos suficientes.")
        return intervalo_parametrico(knots, self.degree)

    def evaluate(self, t: float) -> np.ndarray:
        knots = self.ensure_knots()
        if knots is None:
            raise ValueError(f"A curva {self.name} ainda nao possui pontos suficientes.")
        return avaliar_ponto_bspline(self.points_array(), self.degree, knots, t)

    def derivative(self, t: float, ordem: int = 1) -> np.ndarray:
        knots = self.ensure_knots()
        if knots is None:
            raise ValueError(f"A curva {self.name} ainda nao possui pontos suficientes.")
        return avaliar_derivada_bspline(self.points_array(), self.degree, knots, t, ordem=ordem)

    def sample_curve(self, num_samples: int = 400) -> np.ndarray | None:
        knots = self.ensure_knots()
        if knots is None:
            return None
        return avaliar_bspline(self.points_array(), self.degree, knots, num_samples=num_samples)

    def start_point(self) -> np.ndarray:
        start, _ = self.parameter_range()
        return self.evaluate(start)

    def end_point(self) -> np.ndarray:
        _, end = self.parameter_range()
        return self.evaluate(end)

    def info_text(self) -> str:
        lines = [
            f"{self.name}",
            f"  grau: {self.degree}",
            f"  pontos: {self.point_count}",
        ]

        for index, point in enumerate(self.control_points):
            lines.append(f"  P{index}: ({point[0]:.3f}, {point[1]:.3f})")

        if self.ready:
            knots = self.ensure_knots()
            assert knots is not None
            lines.append(f"  knots: {np.array2string(knots, precision=4, separator=', ')}")
            start, end = self.parameter_range()
            lines.append(
                f"  derivada inicio: {np.array2string(self.derivative(start, 1), precision=4, separator=', ')}"
            )
            lines.append(
                f"  derivada fim: {np.array2string(self.derivative(end, 1), precision=4, separator=', ')}"
            )
            lines.append(
                f"  segunda derivada inicio: {np.array2string(self.derivative(start, 2), precision=4, separator=', ')}"
            )
            lines.append(
                f"  segunda derivada fim: {np.array2string(self.derivative(end, 2), precision=4, separator=', ')}"
            )
        else:
            lines.append(f"  faltam {self.degree + 1 - self.point_count} pontos para ativar a curva")

        return "\n".join(lines)
