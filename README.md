##  Project Structure
### **Data**
- `data/Amberd.xlsx` → Visualization data for hydropower analysis.
- `data/HP_Energy_Production.csv` → Energy production data for the HP model.
- `data/STL_Energy_Production.csv` → Energy production data for the STL model.
- `data/Water_Flow_Calculations.csv` → Processed water flow data used in the analysis.
- `data/hp_energy_production_with_water_flow.csv` → HP energy data combined with water flow.
- `data/hp_energy_production_with_weather.csv` → HP energy data merged with weather conditions.
- `data/stl_energy_production_with_water_flow.csv` → STL energy data combined with water flow.
- `data/stl_energy_production_with_weather.csv` → STL energy data merged with weather conditions.

### **Processed Data**

- `processed_data/energy_production_with_engineered_features.csv` → HP energy data with engineered features.

### **Notebooks**
- `notebooks/calculate_water_flow.ipynb` → Jupyter notebook for calculating water flow.
- `notebooks/ts_forecast.ipynb` → Time-series forecasting analysis.
-` notebooks/ts_decomp.ipynb`→ Seasonal decomposition using STL and HP filters.
- `notebooks/experiments_1.ipynb`→ ML/DL  experiments on Station 1.
- `notebooks/experiments_2.ipynb`→ ML/DL  experiments on Station 2.
- `notebooks/experiments_3.ipynb`→ ML/DL  experiments on Station 3.
- `notebooks/experiments_global.ipynb`→  Combined forecasting experiments using data from all stations
- `notebooks/feature_engineering.ipynb` → Notebook for generating and testing new features.
- `notebooks/save_experiments.py` → Notebook for a saving function.


### **R Scripts**
- `r_scripts/Visualizations.Rmd` → R Markdown file for generating visualizations.
- `r_scripts/Capstone.Rproj` → Initial project setup for R-based analysis.

### **Visualizations**
- `visualizations/Visualizations.pdf` → Pre-generated visualizations from the R Markdown file, including feature importance and correlation plots.

### **Other Files**
- `requirements.txt` → Dependencies needed to run the project.
- `.gitignore` → Files and folders ignored by Git.
