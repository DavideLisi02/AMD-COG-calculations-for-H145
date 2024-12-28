import matplotlib.pyplot as plt

######################################
# Mass and coordinates for original points
H145_to_mass = 3300
H145_ld_mass = 2914
H145_zf_mass = 2844

H145_zf_BL = -5
H145_ld_BL = -5
H145_to_BL = -5
H145_zf_STA = 4490
H145_ld_STA = 4460
H145_to_STA = 4470

######################################
# Mass and coordinates for rail and box
rail_mass = 75
rail_BL = -650
rail_STA = 2510

box_mass = 150
box_BL = -1100
box_STA = 2510

######################################
# Define points for Station Line (STA)
sta_points = {
    "A": (4380, 3700),
    "B": (4535, 3700),
    "C": (4700, 2000),
    "D": (4347, 2400),
    "A'": (4250, 3700),
    "D'": (4250, 3000)
}

# Define points for Buttock Line (BL)
bl_points = {
    "A": (-80, 3700),
    "B": (80, 3700),
    "F'": (80, 3000),
    "F": (100, 3000),
    "C": (100, 2000),
    "D": (-100, 2000),
    "E": (-100, 3000),
    "E'": (-80, 3000)
}

# Define polygons for STA
sta_polygon1 = ["A", "B", "C", "D", "A"]  # Closed polygon (ABCD)
sta_polygon2 = ["A'", "B", "C", "D", "D'", "A'"]  # Closed polygon (A'BCDD')
sta_polygon1_coords = [sta_points[point] for point in sta_polygon1]
sta_polygon2_coords = [sta_points[point] for point in sta_polygon2]

# Define the single polygon for BL
bl_polygon = ["A", "B", "F'", "F", "C", "D", "E", "E'", "A"]  # Single polygon A-B-F'-F-C-D-E-E'-A
bl_polygon_coords = [bl_points[point] for point in bl_polygon]

# Additional points for STA and BL
h145_points_sta = {
    "TO": (H145_to_STA, H145_to_mass),
    "LD": (H145_ld_STA, H145_ld_mass),
    "ZF": (H145_zf_STA, H145_zf_mass)
}

h145_points_bl = {
    "TO": (H145_to_BL, H145_to_mass),
    "LD": (H145_ld_BL, H145_ld_mass),
    "ZF": (H145_zf_BL, H145_zf_mass)
}

# New points considering rail and box
to_tot_mass = H145_to_mass + box_mass + rail_mass
ld_tot_mass = H145_ld_mass + box_mass + rail_mass
zf_tot_mass = H145_zf_mass + box_mass + rail_mass

h145_new_points_sta = {
    "TO'": ((H145_to_STA * H145_to_mass + box_mass * box_STA + rail_mass * rail_STA) / to_tot_mass, to_tot_mass),
    "LD'": ((H145_ld_STA * H145_ld_mass + box_mass * box_STA + rail_mass * rail_STA) / ld_tot_mass, ld_tot_mass),
    "ZF'": ((H145_zf_STA * H145_zf_mass + box_mass * box_STA + rail_mass * rail_STA) / zf_tot_mass, zf_tot_mass)
}

h145_new_points_bl = {
    "TO'": ((H145_to_BL * H145_to_mass + box_mass * box_BL + rail_mass * rail_BL) / to_tot_mass, to_tot_mass),
    "LD'": ((H145_ld_BL * H145_ld_mass + box_mass * box_BL + rail_mass * rail_BL) / ld_tot_mass, ld_tot_mass),
    "ZF'": ((H145_zf_BL * H145_zf_mass + box_mass * box_BL + rail_mass * rail_BL) / zf_tot_mass, zf_tot_mass)
}

# Plotting
fig, axes = plt.subplots(1, 2, figsize=(16, 8))

# First graph: STA polygons and additional points
axes[0].plot(*zip(*sta_polygon1_coords), marker="o", color="red", label="Polygon ABCD")
axes[0].plot(*zip(*sta_polygon2_coords), marker="o", color="red", label="Polygon A'BCDD'")
axes[0].scatter(*zip(*h145_points_sta.values()), color="blue", label="Original Points (TO, LD, ZF)", zorder=5)
axes[0].scatter(*zip(*h145_new_points_sta.values()), color="green", label="With our system (TO', LD', ZF')", zorder=6)
axes[0].set_title(f"Box: {box_mass}kg | Rail: {rail_mass}kg | (STA)")
axes[0].set_xlabel("Station Line (STA) (mm)")
axes[0].set_ylabel("Mass (kg)")
axes[0].grid(True)
axes[0].legend()

# Annotate points for STA
for point, coord in sta_points.items():
    axes[0].text(coord[0], coord[1], f" {point}", fontsize=10, color="blue")
for label, coord in h145_points_sta.items():
    axes[0].text(coord[0], coord[1], f" {label}", fontsize=10, color="black")
for label, coord in h145_new_points_sta.items():
    axes[0].text(coord[0], coord[1], f" {label}", fontsize=10, color="green")

# Adjust x-axis limits for better visibility
axes[0].set_xlim(4200, 4800)  # Scaled x-axis for STA polygons

# Second graph: Single BL polygon and additional points
axes[1].plot(*zip(*bl_polygon_coords), marker="o", color="red", label="Polygon A-B-F'-F-C-D-E-E'-A")
axes[1].scatter(*zip(*h145_points_bl.values()), color="blue", label="Original Points (TO, LD, ZF)", zorder=5)
axes[1].scatter(*zip(*h145_new_points_bl.values()), color="green", label="With our system (TO', LD', ZF')", zorder=6)
axes[1].set_title(f"Box: {box_mass}kg | Rail: {rail_mass}kg | (BL)")
axes[1].set_xlabel("Buttock Line (BL) (mm)")
axes[1].set_ylabel("Mass (kg)")
axes[1].grid(True)
axes[1].legend()

# Annotate points for BL
for point, coord in bl_points.items():
    axes[1].text(coord[0], coord[1], f" {point}", fontsize=10, color="purple")
for label, coord in h145_points_bl.items():
    axes[1].text(coord[0], coord[1], f" {label}", fontsize=10, color="black")
for label, coord in h145_new_points_bl.items():
    axes[1].text(coord[0], coord[1], f" {label}", fontsize=10, color="green")

# Adjust x-axis limits for better visibility
axes[1].set_xlim(-120, 120)  # Scaled x-axis for BL polygon

# Show both plots
plt.tight_layout()
plt.show()
