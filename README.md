This repository contains scripts and analysis materials for the study of white LED spectra using a Michelson Interferometer. The primary objective is to analyze the color properties of a white LED based on the CIE 1931 color spaces, measuring critical parameters such as Correlated Color Temperature (CCT) and Color Rendering Index (CRI). The experiment uses Fourier Transform Spectroscopy principles to derive the spectrum from interferogram data.


Simulation.py: Simulates Michelson Interferometer interferograms for various light sources, allowing parameter adjustments to optimize interferogram quality.

global_calibration.py: Script for performing global calibration of the interferometer, ensuring that all system components are aligned to a universal reference.

local_calibration.py: Complements global_calibration.py by fine-tuning calibration for specific experimental conditions, adjusting for local variances in components or environmental factors.

crossing_points.py: Analyzes crossing points in He-Ne laser interferograms to refine motor movement accuracy.

quick_plot.py: Utility for visualizing interferograms from experimental data files.

RGB_analysis.py: My extention work to investigate the LED RGB values.

A 4-page conference-style [report](https://github.com/ZZZiyao/Year2-Interferometry-Lab/blob/main/Interferometry_Report.pdf) was written.

This repository is intended for academic and personal use ONLY. 
