import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("physical_properties.csv")
filtered_data = data[(data['temperature_K'] > 3000) & (data['temperature_K'] < 10000) & 
                     (data['luminosity'] > 0) & (data['luminosity'] < 0.5)]

plt.figure(figsize=(8, 6)) 
sc = plt.scatter(
    filtered_data['temperature_K'],
    filtered_data['luminosity'],
    c=filtered_data['B-V'],
    cmap='plasma',
    s=20, 
    edgecolor='k',
    alpha=0.8 
)
plt.gca().invert_xaxis()
cbar = plt.colorbar(sc)
cbar.set_label("B-V (Color Index)", fontsize=12)
cbar.ax.set_ylabel("Star's Color Index (B-V)", fontsize=10, rotation=270, labelpad=15)

# HR DIAGRAM, TEMPERATURE VS LUMINOSITY
plt.title("Hertzsprung-Russell Diagram (Zoomed-In)", fontsize=14)
plt.xlabel("Effective Temperature (K)", fontsize=12)
plt.ylabel("Luminosity (Solar Units)", fontsize=12)
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
plt.tight_layout()  
plt.savefig("hr_diagram_zoomed.png")
plt.show()

#PARALLAX VS LUMINOSITY
plt.figure(figsize=(8, 6))
plt.scatter(data['PLX_VALUE'], data['FLUX_V'], alpha=0.7, edgecolor='k')
plt.xlabel('Parallax (milliarcseconds)', fontsize=12)
plt.ylabel('Flux (V band)', fontsize=12)
plt.title('Parallax vs. V-Band Flux', fontsize=14)
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
plt.tight_layout()
plt.show()

#FLUX B VS FLUX V
plt.figure(figsize=(8, 6))
plt.scatter(data['FLUX_B'], data['FLUX_V'], alpha=0.7, edgecolor='k')
plt.xlabel('Flux (B Band)', fontsize=12)
plt.ylabel('Flux (V Band)', fontsize=12)
plt.title('B-Band Flux vs. V-Band Flux', fontsize=14)
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
plt.tight_layout()
plt.show()

# HISTOGRAM OF PARALLAX VALUES
filtered_parallax = data['PLX_VALUE'][(data['PLX_VALUE'] > 0) & (data['PLX_VALUE'] < 30)]
plt.figure(figsize=(8, 6))
plt.hist(filtered_parallax, bins=50, color='blue', alpha=0.7, edgecolor='black')
plt.xlabel('Parallax (milliarcseconds)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.title('Distribution of Parallax Values (Filtered)', fontsize=14)
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
plt.tight_layout()
plt.show()



