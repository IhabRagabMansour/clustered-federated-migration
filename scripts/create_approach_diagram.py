"""
Create an architecture-focused diagram for clustered FL with migration.

Outputs:
    figures/approach_diagram.png
    figures/approach_diagram.svg
    figures/approach_diagram.pdf
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch, Rectangle


OUT_DIR = Path("figures")


COLORS = {
    "ink": "#172033",
    "muted": "#52667d",
    "line": "#40546b",
    "blue": "#4d89c7",
    "blue_fill": "#edf5fd",
    "green": "#5e9a68",
    "green_fill": "#eff9f1",
    "orange": "#bd7d24",
    "orange_fill": "#fff8ed",
    "red": "#a34848",
    "red_fill": "#fff2f2",
    "gray": "#8c95a6",
    "gray_fill": "#f7f8fb",
    "yellow": "#fff1bd",
    "yellow_edge": "#b88700",
    "purple": "#7567b0",
    "purple_fill": "#f3f0ff",
}


BOX_LW = 1.75
ARROW_LW = 1.55
RADIUS = 0.13


def text(ax, x, y, value, size=10, color=None, weight="normal",
         ha="center", va="center", linespacing=1.12):
    ax.text(
        x,
        y,
        value,
        ha=ha,
        va=va,
        fontsize=size,
        fontweight=weight,
        color=color or COLORS["ink"],
        linespacing=linespacing,
    )


def rounded_box(ax, x, y, w, h, face, edge, radius=RADIUS, lw=BOX_LW):
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle=f"round,pad=0.025,rounding_size={radius}",
        linewidth=lw,
        edgecolor=edge,
        facecolor=face,
    )
    ax.add_patch(patch)
    return patch


def arrow(ax, start, end, color=None, lw=ARROW_LW, scale=14, curve=0.0,
          alpha=1.0, shrink_a=4, shrink_b=4):
    patch = FancyArrowPatch(
        start,
        end,
        connectionstyle=f"arc3,rad={curve}",
        arrowstyle="-|>",
        mutation_scale=scale,
        linewidth=lw,
        color=color or COLORS["line"],
        alpha=alpha,
        shrinkA=shrink_a,
        shrinkB=shrink_b,
    )
    ax.add_patch(patch)
    return patch


def routed_arrow(ax, points, color, lw=ARROW_LW, scale=14, alpha=1.0):
    for start, end in zip(points[:-2], points[1:-1]):
        ax.plot([start[0], end[0]], [start[1], end[1]],
                color=color, linewidth=lw, alpha=alpha, solid_capstyle="round")
    arrow(ax, points[-2], points[-1], color=color, lw=lw, scale=scale,
          alpha=alpha, shrink_a=0, shrink_b=3)


def layer_band(ax, y, h, label):
    ax.add_patch(Rectangle((0.12, y), 15.74, h, facecolor=COLORS["gray_fill"],
                           edgecolor="#d8dee8", linewidth=0.95, zorder=-3))
    text(ax, 1.18, y + h / 2, label, size=8.4, color=COLORS["muted"],
         weight="bold", ha="right")


def client(ax, x, y, label, migrated=False):
    face = COLORS["yellow"] if migrated else "white"
    edge = COLORS["yellow_edge"] if migrated else "#647a94"
    lw = 1.45 if migrated else 1.25
    ax.add_patch(Circle((x, y), 0.17, facecolor=face, edgecolor=edge, linewidth=lw))
    text(ax, x, y, label, size=7.4)


def client_cluster(ax, x, y, w, h, title, subtitle, edge, face, clients, migrated=None):
    migrated = set(migrated or [])
    rounded_box(ax, x, y, w, h, face, edge, radius=RADIUS, lw=BOX_LW)
    text(ax, x + 0.36, y + h - 0.34, title, size=11.0, weight="bold", ha="left")
    text(ax, x + 0.36, y + h - 0.72, subtitle, size=8.4, color=COLORS["muted"], ha="left")

    xs = np.linspace(x + 0.74, x + w - 0.74, len(clients))
    for xpos, label in zip(xs, clients):
        client(ax, xpos, y + 0.62, label, migrated=label in migrated)


def coordinator(ax, x, y, w, h, title, model_label, edge, face):
    rounded_box(ax, x, y, w, h, face, edge, radius=RADIUS, lw=BOX_LW)
    text(ax, x + 0.36, y + h - 0.30, title, size=10.5, weight="bold", ha="left")
    text(ax, x + 0.36, y + h - 0.67, "cluster FedAvg", size=8.3,
         color=COLORS["muted"], ha="left")
    ax.add_patch(Circle((x + w - 0.60, y + h / 2), 0.34,
                        facecolor="white", edgecolor=edge, linewidth=1.9))
    text(ax, x + w - 0.60, y + h / 2, model_label, size=9.8,
         weight="bold", color=edge)


def sharing_module(ax, x, y, w, h):
    rounded_box(ax, x, y, w, h, COLORS["orange_fill"], COLORS["orange"],
                radius=RADIUS, lw=BOX_LW)
    text(ax, x + 0.40, y + h - 0.25, "Inter-cluster sharing module",
         size=11.0, weight="bold", ha="left")
    text(ax, x + 0.40, y + 0.20, "optional weighted mixing of cluster models",
         size=8.3, color=COLORS["muted"], ha="left")

    badge_w = 0.86
    badge_h = 0.30
    rounded_box(ax, x + w - badge_w - 0.36, y + h - badge_h - 0.20,
                badge_w, badge_h, "white", COLORS["orange"], radius=0.07, lw=1.15)
    text(ax, x + w - badge_w / 2 - 0.36, y + h - badge_h / 2 - 0.20,
         "Case B", size=8.2, color=COLORS["orange"], weight="bold")


def migration_controller(ax, x, y, w, h):
    rounded_box(ax, x, y, w, h, COLORS["red_fill"], COLORS["red"],
                radius=RADIUS, lw=BOX_LW)
    text(ax, x + w / 2, y + h - 0.34, "Migration controller", size=9.8, weight="bold")
    text(ax, x + w / 2, y + 0.34, "reassigns selected clients",
         size=7.6, color=COLORS["muted"])


def mode_chip(ax, x, y, w, label, edge, face):
    rounded_box(ax, x, y, w, 0.34, face, edge, radius=0.075, lw=1.15)
    text(ax, x + w / 2, y + 0.17, label, size=7.8, weight="bold", color=edge)


def evaluator(ax, x, y, w, h):
    rounded_box(ax, x, y, w, h, COLORS["purple_fill"], COLORS["purple"],
                radius=RADIUS, lw=BOX_LW)
    text(ax, x + 0.36, y + h - 0.34, "Evaluation logger", size=10.3,
         weight="bold", ha="left")
    text(ax, x + 0.36, y + h - 0.72, "records impact", size=7.8,
         color=COLORS["muted"], ha="left")

    chart_x = x + 0.36
    chart_y = y + 0.34
    chart_w = 1.22
    chart_h = 0.62
    ax.add_patch(Rectangle((chart_x, chart_y), chart_w, chart_h,
                           facecolor="white", edgecolor="#b6bfd0", linewidth=0.9))
    xs = np.linspace(chart_x + 0.10, chart_x + chart_w - 0.10, 8)
    ys = np.array([0.62, 0.63, 0.61, 0.28, 0.42, 0.52, 0.58, 0.61])
    ax.plot(xs, chart_y + chart_h * ys, color=COLORS["red"], linewidth=1.8)
    ax.plot([chart_x + 0.10, chart_x + chart_w - 0.10],
            [chart_y + chart_h * 0.62] * 2,
            color=COLORS["gray"], linewidth=0.85, linestyle="--")

    pill_x = x + 1.90
    for idx, label in enumerate(["accuracy", "drop", "recovery"]):
        pill_y = y + 0.34 + idx * 0.43
        rounded_box(ax, pill_x, pill_y, 0.98, 0.29, "white", COLORS["purple"],
                    radius=0.055, lw=1.05)
        text(ax, pill_x + 0.49, pill_y + 0.145, label, size=6.5,
             color=COLORS["ink"], weight="bold")


def legend_item(ax, x, y, label, edge, face):
    rounded_box(ax, x, y, 0.32, 0.21, face, edge, radius=0.045, lw=1.05)
    text(ax, x + 0.43, y + 0.105, label, size=7.4, color=COLORS["muted"], ha="left")


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(16.0, 8.8))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 8.8)
    ax.axis("off")
    fig.patch.set_facecolor("white")

    text(ax, 8.0, 8.46, "Architecture of Clustered Federated Learning with Migration",
         size=18.4, weight="bold")
    text(ax, 8.0, 8.08,
         "Model updates stay inside clusters, optional sharing connects cluster models, and migration changes client ownership.",
         size=10.2, color=COLORS["muted"])

    layer_band(ax, 6.55, 1.05, "sharing layer")
    layer_band(ax, 4.42, 1.62, "aggregation layer")
    layer_band(ax, 1.34, 2.76, "client layer")

    # Major architecture blocks.
    sharing_module(ax, 5.10, 6.72, 6.20, 0.76)

    src_coord = (2.28, 4.72, 3.52, 1.04)
    dst_coord = (8.44, 4.72, 3.52, 1.04)
    coordinator(ax, *src_coord, "Source coordinator", "Ws", COLORS["blue"], COLORS["blue_fill"])
    coordinator(ax, *dst_coord, "Destination coordinator", "Wd", COLORS["green"], COLORS["green_fill"])

    evaluator(ax, 12.46, 4.24, 3.04, 1.94)

    client_cluster(ax, 1.36, 1.92, 5.00, 1.82, "Source cluster",
                   "clients train on local data", COLORS["blue"], COLORS["blue_fill"],
                   ["c1", "c2", "c3", "c4"], migrated=["c2", "c3"])
    client_cluster(ax, 9.42, 1.92, 5.00, 1.82, "Destination cluster",
                   "receives migrated clients", COLORS["green"], COLORS["green_fill"],
                   ["d1", "d2", "d3", "m"], migrated=["m"])

    migration_controller(ax, 6.72, 2.60, 2.40, 1.04)

    # Symmetric client <-> coordinator update flow.
    source_up_x, source_down_x = 3.52, 4.50
    dest_up_x, dest_down_x = 10.42, 11.40
    arrow(ax, (source_up_x, 3.80), (source_up_x, 4.68),
          color=COLORS["blue"], lw=ARROW_LW, scale=14)
    arrow(ax, (source_down_x, 4.68), (source_down_x, 3.80),
          color=COLORS["blue"], lw=ARROW_LW, scale=14)
    text(ax, source_up_x - 0.40, 4.26, "local\nupdates", size=7.3,
         color=COLORS["blue"])
    text(ax, source_down_x + 0.48, 4.26, "model\nbroadcast", size=7.2,
         color=COLORS["blue"])

    arrow(ax, (dest_up_x, 3.80), (dest_up_x, 4.68),
          color=COLORS["green"], lw=ARROW_LW, scale=14)
    arrow(ax, (dest_down_x, 4.68), (dest_down_x, 3.80),
          color=COLORS["green"], lw=ARROW_LW, scale=14)
    text(ax, dest_up_x - 0.40, 4.26, "local\nupdates", size=7.3,
         color=COLORS["green"])
    text(ax, dest_down_x + 0.48, 4.26, "model\nbroadcast", size=7.2,
         color=COLORS["green"])

    # Clean two-lane sharing connectors. Upward arrows send cluster models to
    # the sharing module; downward arrows return mixed models to coordinators.
    arrow(ax, (4.38, 5.80), (6.10, 6.68), color=COLORS["orange"],
          lw=ARROW_LW, scale=14)
    arrow(ax, (6.48, 6.68), (4.78, 5.80), color=COLORS["orange"],
          lw=ARROW_LW, scale=14)
    arrow(ax, (9.78, 5.80), (9.92, 6.68), color=COLORS["orange"],
          lw=ARROW_LW, scale=14)
    arrow(ax, (10.42, 6.68), (10.28, 5.80), color=COLORS["orange"],
          lw=ARROW_LW, scale=14)

    # Client migration flow.
    text(ax, 7.92, 3.88, "client movement", size=8.1,
         color=COLORS["red"], weight="bold")
    arrow(ax, (6.10, 2.80), (6.70, 3.02), color=COLORS["red"],
          lw=1.9, scale=17)
    arrow(ax, (9.14, 3.02), (9.44, 2.80), color=COLORS["red"],
          lw=1.9, scale=17)
    mode_chip(ax, 6.72, 1.86, 2.40, "membership only", COLORS["red"], COLORS["red_fill"])
    mode_chip(ax, 6.72, 1.44, 2.40, "data-changing", COLORS["green"], COLORS["green_fill"])

    # Evaluation flow. The source signal is routed around the destination
    # coordinator so it does not cut through the main aggregation block.
    routed_arrow(
        ax,
        [(5.82, 5.62), (6.22, 6.18), (12.18, 6.18), (12.44, 5.84)],
        COLORS["purple"],
        lw=1.10,
        scale=12,
        alpha=0.56,
    )
    arrow(ax, (11.98, 5.28), (12.44, 5.28), color=COLORS["purple"],
          lw=1.30, scale=12, alpha=0.85)

    # Legend and takeaway.
    legend_y = 0.86
    legend_item(ax, 1.32, legend_y, "source side", COLORS["blue"], COLORS["blue_fill"])
    legend_item(ax, 3.72, legend_y, "destination side", COLORS["green"], COLORS["green_fill"])
    legend_item(ax, 6.54, legend_y, "migrated client", COLORS["yellow_edge"], COLORS["yellow"])
    legend_item(ax, 9.18, legend_y, "sharing path", COLORS["orange"], COLORS["orange_fill"])
    legend_item(ax, 11.62, legend_y, "migration path", COLORS["red"], COLORS["red_fill"])

    rounded_box(ax, 1.18, 0.24, 13.64, 0.42, COLORS["gray_fill"], COLORS["gray"],
                radius=0.10, lw=1.15)
    text(ax, 8.00, 0.45,
         "The architecture separates model sharing between clusters from client migration between clusters.",
         size=8.8, weight="bold")

    for ext in ["png", "svg", "pdf"]:
        fig.savefig(OUT_DIR / f"approach_diagram.{ext}", dpi=300, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
