import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Object:
    def __init__(self, name, mass, BL, STA):
        self.name = name
        self.mass = mass
        self.BL = BL
        self.STA = STA

def calculate_cog(objects):
    total_mass = sum(obj.mass for obj in objects)
    if total_mass == 0:
        return None, None
    cog_sta = sum(obj.mass * obj.STA for obj in objects) / total_mass
    cog_bl = sum(obj.mass * obj.BL for obj in objects) / total_mass
    return (cog_sta, cog_bl), total_mass

########################################################################################

# Mass and coordinates for original points
H145_to_mass = 3440
H145_ld_mass = 2914
H145_zf_mass = 2844

H145_zf_BL = -5
H145_ld_BL = -5
H145_to_BL = -5
H145_zf_STA = 4490
H145_ld_STA = 4460
H145_to_STA = 4470

rail_mass = 70
box_mass = 30
support_mass = 50

human_mass = 70

########################################################################################

# STEP 1
#   H145 TAKE OFF
rail_BL_1 = -420
rail_STA_1 = 2510
box_BL_1 = -1100
box_STA_1 = 2510
kart_BL_1 = -1100
kart_STA_1 = 2510
support_BL_1 = +25
support_STA_1 = 2400
#   Set up the objects
h145_to = Object("H145_to", H145_to_mass, H145_to_BL, H145_to_STA)
doctor_1 = Object("Doctor_1", human_mass, -330, 4004)
copilot_1 = Object("Copilot_1", human_mass, +330, 1380)
pilot_1 = Object("Pilot_1", human_mass, -330, 1380)
rail_1 = Object("Rail_1", rail_mass, rail_BL_1, rail_STA_1)
box_1 = Object("Box_1", box_mass, box_BL_1, box_STA_1)
support_1 = Object("Support_1", support_mass, support_BL_1, support_STA_1)
#   Calculate the CoG
cog_1 = [h145_to, rail_1, box_1, support_1]


# STEP 2
rail_BL_2 = -420
rail_STA_2 = 2510
box_BL_2 = -1150
box_STA_2 = 2650
kart_BL_2 = -1150
kart_STA_2 = 2650
support_BL_2 = +25
support_STA_2 = 2400
#   H145 lowering doctor
#   Set up the objects
h145_to = Object("H145_TO", H145_to_mass, H145_to_BL, H145_to_STA)
doctor_2 = Object("Doctor_2", human_mass, -1150, 2650)
copilot_2 = Object("Copilot_2", human_mass, -330, 4010)
pilot_2 = Object("Pilot_2", human_mass, +330, 1380)
rail_2 = Object("Rail_2", rail_mass, rail_BL_2, rail_STA_2)
box_2 = Object("Box_2", box_mass, box_BL_2, box_STA_2)
support_2 = Object("Support_2", support_mass, support_BL_2, support_STA_2)
#   Calculate the CoG
cog_2 = [h145_to, rail_2, box_2, support_2]

# STEP 3
rail_BL_3 = -420
rail_STA_3 = 2510
box_BL_3 = -1150
box_STA_3 = 2650
kart_BL_3 = -1150
kart_STA_3 = 2650
support_BL_3 = +25
support_STA_3 = 2400
#   H145 rising doctor & patient
#   Set up the objects
h145_to = Object("h145_to", H145_to_mass, H145_to_BL, H145_to_STA)
doctor_3 = Object("Doctor_3", human_mass, -1150, 2650)
copilot_3 = Object("Copilot_3", human_mass, -330, 4010)
pilot_3 = Object("Pilot_3", human_mass, +330, 1380)
patient_3 = Object("Patient_3", human_mass, -1150, 2650)
rail_3 = Object("Rail_3", rail_mass, rail_BL_3, rail_STA_3)
box_3 = Object("Box_3", box_mass, box_BL_3, box_STA_3)
support_3 = Object("Support_3", support_mass, support_BL_3, support_STA_3)
#   Calculate the CoG
cog_3 = [h145_to, rail_3, box_3, support_3, patient_3]


# STEP 4
rail_BL_4 = -570
rail_STA_4 = 2510
box_BL_4 = -1100
box_STA_4 = 2510
kart_BL_4 = -1100
kart_STA_4 = 2510
support_BL_4 = +25
support_STA_4 = 2400
#   H145 moving rail
#   Set up the objects
h145_to = Object("h145_to", H145_to_mass, H145_to_BL, H145_to_STA)
doctor_4 = Object("Doctor_4", human_mass, -420, 2510)
copilot_4 = Object("Copilot_4", human_mass, -330, 4010)
pilot_4 = Object("Pilot_4", human_mass, +330, 1380)
patient_4 = Object("Patient_4", human_mass, -1150, 2510)
rail_4 = Object("Rail_4", rail_mass, rail_BL_4, rail_STA_4)
box_4 = Object("Box_4", box_mass, box_BL_4, box_STA_4)
support_4 = Object("Support_4", support_mass, support_BL_4, support_STA_4)
#   Calculate the CoG
cog_4 = [h145_to, rail_4, box_4, support_4, patient_4]


# STEP 5
rail_BL_5 = -570
rail_STA_5 = 2510
box_BL_5 = -1100
box_STA_5 = 2510
kart_BL_5 = -420
kart_STA_5 = 2510
support_BL_5 = +25
support_STA_5 = 2400
#   H145 moving kart
#   Set up the objects
h145_to = Object("h145_to", H145_to_mass, H145_to_BL, H145_to_STA)
doctor_5 = Object("Doctor_5", human_mass, +50, 2510)
copilot_5 = Object("Copilot_5", human_mass, -330, 4010)
pilot_5 = Object("Pilot_5", human_mass, +330, 1380)
patient_5 = Object("Patient_5", human_mass, -420, 2510)
rail_5 = Object("Rail_5", rail_mass, rail_BL_5, rail_STA_5)
box_5 = Object("Box_5", box_mass, box_BL_5, box_STA_5)
support_5 = Object("Support_5", support_mass, support_BL_5, support_STA_5)
#   Calculate the CoG
cog_5 = [h145_to, rail_5, box_5, support_5, patient_5]

# STEP 6
rail_BL_6 = -570
rail_STA_6 = 2510
box_BL_6 = -1100
box_STA_6 = 2510
kart_BL_6 = -420
kart_STA_6 = 2510
support_BL_6 = +25
support_STA_6 = 2400
#   H145 moving kart
#   Set up the objects
h145_to = Object("h145_to", H145_to_mass, H145_to_BL, H145_to_STA)
doctor_6 = Object("Doctor_6", human_mass, +50, 2510)
copilot_6 = Object("Copilot_6", human_mass, -330, 4010)
pilot_6 = Object("Pilot_6", human_mass, +330, 1380)
patient_6 = Object("Patient_6", human_mass, -420, 4400)
rail_6 = Object("Rail_6", rail_mass, rail_BL_6, rail_STA_6)
box_6 = Object("Box_6", box_mass, box_BL_6, box_STA_6)
support_6 = Object("Support_6", support_mass, support_BL_6, support_STA_6)
#   Calculate the CoG
cog_6 = [h145_to, rail_6, box_6, support_6, patient_6]


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

# Calculate COG for each step
cogs = [cog_1, cog_2, cog_3, cog_4, cog_5, cog_6]
cog_coords = [calculate_cog(cog) for cog in cogs]


# Set up the figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
# Plot STA polygon
ax1.plot(*zip(*sta_polygon1_coords), color='blue')
ax1.plot(*zip(*sta_polygon2_coords), color='blue')
ax1.set_title('STA View')
ax1.set_xlabel('Station Line (STA) (mm)')
ax1.set_ylabel('Mass (kg)')
ax1.grid(True)
ax1.set_xlim(4200, 4800)
ax1.set_ylim(2000, 4000)

# Plot BL polygon
ax2.plot(*zip(*bl_polygon_coords), color='green')
ax2.set_title('BL View')
ax2.set_xlabel('Buttock Line (BL) (mm)')
ax2.set_ylabel('Mass (kg)')
ax2.grid(True)
ax2.set_xlim(-120, 120)
ax2.set_ylim(2000, 4000)

# Extract COG coordinates for plotting
cog_sta_coords = [cog[0][0] for cog in cog_coords]
cog_bl_coords = [cog[0][1] for cog in cog_coords]
total_masses = [cog[1] for cog in cog_coords]

# Plot the trajectory of the COG
ax1.plot(cog_sta_coords, total_masses, color='red', marker='o')
ax2.plot(cog_bl_coords, total_masses, color='red', marker='o')

# Plot the start point in green and the end point in blue
ax1.plot(cog_sta_coords[0], total_masses[0], color='green', marker='o', markersize=10)
ax1.plot(cog_sta_coords[-1], total_masses[-1], color='blue', marker='o', markersize=10)
ax2.plot(cog_bl_coords[0], total_masses[0], color='green', marker='o', markersize=10)
ax2.plot(cog_bl_coords[-1], total_masses[-1], color='blue', marker='o', markersize=10)

plt.tight_layout()
plt.show()

# Save the figure as a PNG file
fig.savefig('cog_trajectory.png')