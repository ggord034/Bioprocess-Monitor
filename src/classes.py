import os
import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

class BioprocessMonitor:

    def __init__(self, filepath, ph_lims, temperature_lims):
        
        for limits in (ph_lims, temperature_lims):
            if len(limits) != 2 or limits[0] > limits[1]:
                raise ValueError("Limits must be (lower, upper), with lower <= upper.")
        self.filepath = filepath
        self.ph_lims = ph_lims
        self.temperature_lims = temperature_lims
        self.df = pd.read_csv(filepath)
        required = {'batch_id', 'time_h', 'temperature_C', 'pH', 'DO_percent',
                    'C_glucose_g_L^-1', 'C_biomass_g_L^-1', 'C_product_g_L^-1'}
        missing = required.difference(self.df.columns)
        if missing:
            raise ValueError(f"Missing dataset columns: {sorted(missing)}")
        if self.df.empty:
            raise ValueError("Dataset must contain measurements.")

    
    def extract_batch(self, batch_id):
        
        return self.df.loc[self.df['batch_id'] == batch_id].sort_values(
            'time_h', kind='stable').copy()
        

    def optimal_ph_mask(self, df_batch):
       
        return df_batch['pH'].between(*self.ph_lims, inclusive='both')

    
    def optimal_temperature_mask(self, df_batch):
        
        return df_batch['temperature_C'].between(*self.temperature_lims, inclusive='both')

        
    def get_n_batches(self):
        
        return int(self.df['batch_id'].nunique())

        
    def export_dashboard(self, batch_id, filepath):
        batch = self.extract_batch(batch_id)
        if batch.empty:
            raise ValueError(f"Batch {batch_id} has no measurements.")
        Path(filepath).parent.mkdir(parents=True, exist_ok=True)
        fig, axes = plt.subplots(2, 2, figsize=(13, 9), constrained_layout=True)
        try:
            fig.suptitle(f'Bioprocess Monitor | Batch {batch_id:03d}', fontsize=18)
            for substance, color, marker in [('glucose', '#2864ad', 'o'),
                                             ('biomass', '#e89828', 's'),
                                             ('product', '#8056a6', '^')]:
                axes[0, 0].scatter(batch['time_h'], batch[f'C_{substance}_g_L^-1'],
                                   color=color, marker=marker, s=25,
                                   label=substance.capitalize())
            axes[0, 0].set(title='Concentration profiles', ylabel='Concentration (g/L)')
            axes[0, 0].legend()
            for ax, column, limits, mask, title, ylabel in [
                (axes[0, 1], 'temperature_C', self.temperature_lims,
                 self.optimal_temperature_mask(batch), 'Temperature', 'Temperature (°C)'),
                (axes[1, 0], 'pH', self.ph_lims,
                 self.optimal_ph_mask(batch), 'pH', 'pH')]:
                ax.axhspan(*limits, color='green', alpha=0.08,
                           label=f'Acceptable range: {limits[0]}–{limits[1]}')
                ax.scatter(batch.loc[mask, 'time_h'], batch.loc[mask, column],
                           color='green', marker='o', s=25, label='Within range')
                ax.scatter(batch.loc[~mask, 'time_h'], batch.loc[~mask, column],
                           color='red', marker='x', s=35, label='Outside range')
                ax.set(title=title, ylabel=ylabel)
                ax.legend(fontsize=9)
            axes[1, 1].scatter(batch['time_h'], batch['DO_percent'],
                               color='#237f89', marker='o', s=25)
            axes[1, 1].set(title='Dissolved oxygen', ylabel='Dissolved oxygen (%)')
            for ax in axes.flat:
                ax.set_xlabel('Time (h)')
                ax.xaxis.set_major_locator(MultipleLocator(6))
                ax.grid(True, alpha=0.25)
                ax.set_axisbelow(True)
                ax.spines[['top', 'right']].set_visible(False)
            fig.savefig(filepath, dpi=180)
        finally:
            plt.close(fig)

    def export_summary(self, filepath):
        rows = []

        for batch_id in sorted(self.df["batch_id"].unique()):
            batch = self.extract_batch(batch_id)
            batch = batch.sort_values("time_h")

            rows.append({
                "batch_id": batch_id,
                "ph_optimal_percent": round(
                    self.optimal_ph_mask(batch).mean() * 100, 2
                ),
                "temperature_optimal_percent": round(
                    self.optimal_temperature_mask(batch).mean() * 100, 2
                ),
                "C_product_g_L^-1_final":
                    batch["C_product_g_L^-1"].iloc[-1]
            })

        Path(filepath).parent.mkdir(parents=True, exist_ok=True)
        pd.DataFrame(rows).to_csv(filepath, index=False)
