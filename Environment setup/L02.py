import os
import matplotlib.pyplot as plt
import pandas as pd

print(os.getcwd())




# import os
# import pandas as pd
# import numpy as np
#
# pd.set_option('display.max_rows', 500)
# pd.set_option('display.max_columns', 500)
# pd.set_option('display.width', 1000)
#
# # path_import = os.path.join("datasets","dataset_wine.csv")
# # df = pd.read_csv(path_import)
#
# n_samples = 101
#
# mu_max = 0.5
# k_s = 100
# s = np.linspace(0, 1000, n_samples)
# mu = mu_max * s / (k_s + s)
#
# records = []
# for i in range(n_samples):
#     record = (s[i], k_s, mu[i], mu_max)
#     records.append(record)
#
# column_names = ("s[i]", "k(s)", "mu[i]", "mu_max")
# df_export = pd.DataFrame(records, columns=column_names)
# df_export.to_csv(os.path.join("tables", "table_monod_kinetics.csv"))
# print(df_export)
#=======================================================
# import numpy as np
#
# ph_vals = np.linspace(6,8,11)
#
# mask_acidic = ph_vals < 7
# print(f"{mask_acidic = }")
#
# ph_vals_acidic = ph_vals[mask_acidic]
# print(f"{ph_vals_acidic = }")
#
# mask_neutral_or_basic = ~mask_acidic
# print(f"{mask_neutral_or_basic = }")
#
# ph_lims = (7.1, 7.5)
# mask_ph_low = ph_vals < ph_lims[0]
# mask_ph_high = ph_vals > ph_lims[1]
# mask_ph_notok = mask_ph_low+mask_ph_high
#
# print(f"{list(mask_ph_low)}")
# print(f"{list(mask_ph_high)}")
# print(f"{list(mask_ph_notok)}")
#
# mask_ph_ok = (ph_vals >= ph_lims[0]) * (ph_vals <= ph_lims[1])
# print(f"{ph_vals[mask_ph_ok]}")
#===========================================================
# class Bioreactor:
#
#     def __init__(self, process_name, pH_lims, pH_chg, temp_lims, temp_chg):
#       self.process_name = process_name
#       self.pH_min = pH_lims[0]
#       self.pH_max = pH_lims[1]
#       self.pH_chg = pH_chg
#       self.temp_min = temp_lims[0]
#       self.temp_max = temp_lims[1]
#       self.temp_chg = temp_chg
#
#
#
#     def in_optimal_range(self,pH, temperature):
#             ph_ok = (self.pH_min <= pH <= self.pH_max)
#             T_ok = (self.temp_min <= temperature <= self.temp_max)
#             process_ok = (ph_ok and T_ok)
#
#             print(f"====({pH = :.2f}, {temperature = :.1f})====")
#             return process_ok
#
#
#     def simulate_process(self, initial_pH, initial_temp):
#         pH = initial_pH
#         temperature = initial_temp
#
#         process_ok = self.in_optimal_range(pH, temperature)
#         while not process_ok:
#             if pH > self.pH_max:
#                 print("pH is too high, injecting HCl")
#                 pH -= self.pH_chg
#             elif pH < self.pH_min:
#                 print("pH is too low, injecting caustic")
#                 pH += self.pH_chg
#
#             else:
#                 print("pH is ok")
#
#             if temperature > self.temp_max:
#                 print("Temperature is too high, increasing cooling water flow")
#                 temperature -= self.temp_chg
#
#             elif temperature < self.temp_min:
#                 print("Temperature too low, decreasing cooling water flow")
#                 temperature += self.temp_chg
#
#             else:
#                 print("Temperature is ok")
#
#             process_ok = self.in_optimal_range(pH, temperature)
#
#
#
# bioreactor_1 = Bioreactor(process_name="Ethanol fermentation",
#                           pH_lims=[4.0, 5.0], pH_chg = 0.1,
#                           temp_lims=(28,32), temp_chg=0.4)
#
# bioreactor_2 = Bioreactor(process_name="diddly",
#                           pH_lims=[2.0, 3.0], pH_chg = 0.1,
#                           temp_lims=(80,100), temp_chg=0.3)
#
# bioreactor_1.simulate_process(initial_pH = 5.15, initial_temp=20.0)
#
# bioreactor_2.simulate_process(initial_pH = 3.2, initial_temp=75)
