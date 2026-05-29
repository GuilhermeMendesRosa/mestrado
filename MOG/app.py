from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt

from bspline import CurvaBSpline
from continuidade import aplicar_c0, aplicar_c1, aplicar_c2, relatorio_continuidade


class BSplineEditor:
    def __init__(self, degree: int = 4) -> None:
        self.degree = degree
        self.curves = [
            CurvaBSpline(name="Curva 1", color="#1f77b4", degree=degree),
            CurvaBSpline(name="Curva 2", color="#d62728", degree=degree),
        ]
        self.active_curve_index = 0
        self.dragging_point: tuple[int, int] | None = None
        self.status_message = (
            "Curva 1 ativa. Clique para inserir pontos ou clique sobre um ponto existente para arrastar."
        )

        self.fig, self.ax = plt.subplots(figsize=(12, 8))
        self.ax.set_title("B-spline grau 4 nao uniforme com continuidade C0/C1/C2", fontsize=13)
        self.ax.set_xlabel("X")
        self.ax.set_ylabel("Y")
        self.ax.grid(True, alpha=0.35)
        self.ax.set_aspect("equal", adjustable="box")
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(0, 10)

        self.curve_artists = []
        self.polygon_artists = []
        self.point_artists = []
        for curve in self.curves:
            spline_artist, = self.ax.plot([], [], color=curve.color, linewidth=2.8, label=curve.name)
            polygon_artist, = self.ax.plot([], [], "--", color=curve.color, linewidth=1.2, alpha=0.55)
            point_artist, = self.ax.plot(
                [],
                [],
                linestyle="",
                marker="o",
                color=curve.color,
                markeredgecolor="black",
                markersize=8,
                zorder=5,
            )
            self.curve_artists.append(spline_artist)
            self.polygon_artists.append(polygon_artist)
            self.point_artists.append(point_artist)

        self.selected_artist, = self.ax.plot(
            [],
            [],
            linestyle="",
            marker="o",
            markerfacecolor="none",
            markeredgecolor="black",
            markeredgewidth=2.0,
            markersize=14,
            zorder=6,
        )

        self.help_text = self.ax.text(
            0.02,
            0.98,
            "",
            transform=self.ax.transAxes,
            va="top",
            ha="left",
            fontsize=9,
            family="monospace",
            bbox=dict(boxstyle="round", facecolor="white", alpha=0.9),
        )
        self.status_text = self.ax.text(
            0.02,
            0.02,
            "",
            transform=self.ax.transAxes,
            va="bottom",
            ha="left",
            fontsize=9,
            family="monospace",
            bbox=dict(boxstyle="round", facecolor="white", alpha=0.9),
        )

        self.ax.legend(loc="upper right")

        self.fig.canvas.mpl_connect("button_press_event", self.on_button_press)
        self.fig.canvas.mpl_connect("button_release_event", self.on_button_release)
        self.fig.canvas.mpl_connect("motion_notify_event", self.on_mouse_move)
        self.fig.canvas.mpl_connect("key_press_event", self.on_key_press)

        self.redraw()

    @property
    def active_curve(self) -> CurvaBSpline:
        return self.curves[self.active_curve_index]

    def on_button_press(self, event) -> None:
        if event.inaxes != self.ax or event.xdata is None or event.ydata is None:
            return
        if event.button != 1:
            return

        selection = self.find_nearest_point(event)
        if selection is not None:
            self.dragging_point = selection
            self.active_curve_index = selection[0]
            self.status_message = (
                f"Arrastando P{selection[1]} da Curva {selection[0] + 1}."
            )
            self.redraw()
            return

        self.active_curve.add_control_point((event.xdata, event.ydata))
        self.status_message = (
            f"Ponto adicionado na Curva {self.active_curve_index + 1}. "
            f"Total: {self.active_curve.point_count}."
        )
        self.redraw()

    def on_button_release(self, event) -> None:
        if event.button != 1 or self.dragging_point is None:
            return
        curve_index, point_index = self.dragging_point
        self.dragging_point = None
        self.status_message = f"P{point_index} da Curva {curve_index + 1} atualizado."
        self.redraw()

    def on_mouse_move(self, event) -> None:
        if self.dragging_point is None:
            return
        if event.inaxes != self.ax or event.xdata is None or event.ydata is None:
            return

        curve_index, point_index = self.dragging_point
        self.curves[curve_index].set_control_point(point_index, (event.xdata, event.ydata))
        self.status_message = (
            f"Movendo P{point_index} da Curva {curve_index + 1} para "
            f"({event.xdata:.2f}, {event.ydata:.2f})."
        )
        self.redraw()

    def on_key_press(self, event) -> None:
        if event.key is None:
            return

        key = event.key.lower()

        if key in {"1", "2"}:
            self.active_curve_index = int(key) - 1
            self.status_message = f"Curva {key} ativada para insercao de pontos."
        elif key == "c":
            self.apply_continuity("C0", aplicar_c0)
            return
        elif key == "v":
            self.apply_continuity("C1", aplicar_c1)
            return
        elif key == "b":
            self.apply_continuity("C2", aplicar_c2)
            return
        elif key == "r":
            current = self.active_curve
            current.reset()
            self.status_message = f"{current.name} foi resetada."
        elif key == "k":
            knots = self.active_curve.regenerate_knots()
            if knots is None:
                self.status_message = (
                    f"{self.active_curve.name} ainda precisa de {self.degree + 1} pontos para gerar knots."
                )
            else:
                self.status_message = f"Knots nao uniformes regenerados para {self.active_curve.name}."
        elif key == "t":
            self.print_state()
            self.status_message = "Dados das curvas impressos no terminal."
        elif key == "escape":
            plt.close(self.fig)
            return
        else:
            self.status_message = f"Comando '{event.key}' nao mapeado."

        self.redraw()

    def apply_continuity(self, label: str, operation) -> None:
        try:
            report = operation(self.curves[0], self.curves[1])
            self.status_message = (
                f"{label} aplicada entre o fim da Curva 1 e o inicio da Curva 2. "
                f"Erros: C0={report['c0_error']:.2e}, C1={report['c1_error']:.2e}, C2={report['c2_error']:.2e}."
            )
        except ValueError as exc:
            self.status_message = str(exc)
        self.redraw()

    def find_nearest_point(self, event, pixel_threshold: float = 12.0) -> tuple[int, int] | None:
        nearest: tuple[int, int] | None = None
        best_distance = pixel_threshold

        for curve_index, curve in enumerate(self.curves):
            points = curve.points_array()
            for point_index, point in enumerate(points):
                point_x, point_y = self.ax.transData.transform(point)
                distance = float(np.hypot(point_x - event.x, point_y - event.y))
                if distance <= best_distance:
                    best_distance = distance
                    nearest = (curve_index, point_index)

        return nearest

    def continuity_summary(self) -> str:
        report = relatorio_continuidade(self.curves[0], self.curves[1])
        if not report.get("ready"):
            return str(report["message"])

        return (
            f"C0={'OK' if report['c0'] else 'NAO'} ({report['c0_error']:.2e}) | "
            f"C1={'OK' if report['c1'] else 'NAO'} ({report['c1_error']:.2e}) | "
            f"C2={'OK' if report['c2'] else 'NAO'} ({report['c2_error']:.2e})"
        )

    def update_texts(self) -> None:
        help_lines = [
            "Clique esquerdo: adiciona ponto na curva ativa",
            "Clique e arraste: move ponto existente",
            "1/2: ativa curva | c: C0 | v: C1 | b: C2",
            "r: reset curva ativa | k: novos knots | t: imprimir dados | esc: sair",
            "Continuidade aplicada sempre do fim da Curva 1 para o inicio da Curva 2",
        ]
        self.help_text.set_text("\n".join(help_lines))

        active = self.active_curve
        knot_state = "nao uniforme" if active.ready else "aguardando pontos"
        status_lines = [
            (
                f"Curva ativa: {self.active_curve_index + 1} | "
                f"Pontos C1: {self.curves[0].point_count} | "
                f"Pontos C2: {self.curves[1].point_count} | "
                f"Knots ativos: {knot_state}"
            ),
            self.continuity_summary(),
            f"Status: {self.status_message}",
        ]
        self.status_text.set_text("\n".join(status_lines))

    def autoscale_view(self) -> None:
        all_points = [curve.points_array() for curve in self.curves if curve.point_count > 0]
        if not all_points:
            self.ax.set_xlim(0, 10)
            self.ax.set_ylim(0, 10)
            return

        points = np.vstack(all_points)
        min_x, min_y = points.min(axis=0)
        max_x, max_y = points.max(axis=0)

        span_x = max(max_x - min_x, 1.0)
        span_y = max(max_y - min_y, 1.0)
        span = max(span_x, span_y)
        margin = max(1.0, span * 0.15)
        center_x = (min_x + max_x) / 2.0
        center_y = (min_y + max_y) / 2.0
        half_span = span / 2.0 + margin

        self.ax.set_xlim(center_x - half_span, center_x + half_span)
        self.ax.set_ylim(center_y - half_span, center_y + half_span)

    def update_artists(self) -> None:
        for index, curve in enumerate(self.curves):
            points = curve.points_array()
            is_active = index == self.active_curve_index

            if points.size == 0:
                self.polygon_artists[index].set_data([], [])
                self.point_artists[index].set_data([], [])
                self.curve_artists[index].set_data([], [])
            else:
                self.polygon_artists[index].set_data(points[:, 0], points[:, 1])
                self.point_artists[index].set_data(points[:, 0], points[:, 1])
                self.polygon_artists[index].set_linewidth(2.0 if is_active else 1.2)
                self.polygon_artists[index].set_alpha(0.85 if is_active else 0.45)
                self.point_artists[index].set_markersize(9 if is_active else 7)

                sampled_curve = curve.sample_curve(num_samples=450)
                if sampled_curve is None:
                    self.curve_artists[index].set_data([], [])
                else:
                    self.curve_artists[index].set_data(sampled_curve[:, 0], sampled_curve[:, 1])
                    self.curve_artists[index].set_linewidth(3.0 if is_active else 2.3)

        if self.dragging_point is None:
            self.selected_artist.set_data([], [])
        else:
            curve_index, point_index = self.dragging_point
            point = self.curves[curve_index].control_points[point_index]
            self.selected_artist.set_data([point[0]], [point[1]])

    def redraw(self) -> None:
        self.update_artists()
        self.update_texts()
        self.autoscale_view()
        self.fig.canvas.draw_idle()

    def print_state(self) -> None:
        print("\n" + "=" * 72)
        print("B-SPLINE GRAU 4 - ESTADO ATUAL")
        print("=" * 72)
        for curve in self.curves:
            print(curve.info_text())
            print("-" * 72)

        report = relatorio_continuidade(self.curves[0], self.curves[1])
        if not report.get("ready"):
            print(f"Continuidade: {report['message']}")
        else:
            print(
                "Continuidade C0/C1/C2 entre Curva 1 -> Curva 2:\n"
                f"  C0: {'OK' if report['c0'] else 'NAO'} | erro = {report['c0_error']:.6e}\n"
                f"  C1: {'OK' if report['c1'] else 'NAO'} | erro = {report['c1_error']:.6e}\n"
                f"  C2: {'OK' if report['c2'] else 'NAO'} | erro = {report['c2_error']:.6e}"
            )
        print("=" * 72 + "\n")


def main() -> None:
    print("\n" + "=" * 72)
    print("B-SPLINE GRAU 4 (ORDEM 5) - DUAS CURVAS NO MESMO CANVAS")
    print("=" * 72)
    print("Comandos:")
    print("  Clique esquerdo  -> adiciona ponto de controle")
    print("  Clique/arraste   -> move ponto de controle")
    print("  1 / 2            -> ativa curva 1 ou curva 2")
    print("  c / v / b        -> aplica C0 / C1 / C2")
    print("  r                -> reseta a curva ativa")
    print("  k                -> regenera knots nao uniformes da curva ativa")
    print("  t                -> imprime pontos, knots e derivadas")
    print("  esc              -> fecha a janela")
    print("=" * 72 + "\n")

    editor = BSplineEditor(degree=4)
    plt.show()


if __name__ == "__main__":
    main()
