# Procedural-Fluid-Engine

This is an SPH based fluid engine written for maya users to easily simulate particle
based fluid dynamics for small scale simulations. It supports up to 2500 particles, 
with basic bounding box and cylinder type collisions. The defining characteristic of
this tool is giving more artistic control to users over initial particle configurations,
also allowing users to art direct particular particle based fluid attributes easily 
within the maya interface.

## Key algorithm

Smooth Particle Hydrodynamics is a field of research of particle based fluid dynamics that
deals with simulating particle behaviours by calculating local particle neighbourhoods and
finding aggregate forces that apply to particles within the same neighbourhood. Different
weighting kernels are applied to particles within common neighbourhoods which can 
approximate physical forces such as viscosity, pressure, density, buoyancy and surface 
tension. 

## Using the tool
Documentation on tool specific algorithms and approaches to developing the tool 
can be found within the documentation folder in this repo. Instructions on using the
tool can be found below:

### Instructions for loading the tool:
- Extract all subfolders src, docs and artefacts into one project location on your
  local machine
- Within the maya interface open the python shell editor
- run the script entitled main.py within the src subdirectory
- this will prompt you with a file location field.
- Paste the location to the directory containing all the subfolders i.e src, docs
  and artefacts.
- This should then open up as the Coffee Works interface

### Instructions on using the tool
- To understand default physical parameters for specific fluid types, there are information
  tabs within the tools interface enlisting default liquid values
- The main interface is defaulted to 3 types of liquids which automatically reset the
  physical attributes to the right values.
- Clicking simulate will run the simulation with those values, in which case further changes
  cannot be applied until the simulation pop-up is complete

### Further improvements
- The tool can be optimized by using points instead of primitive representatives for particles.
- Using multithreading and parallelization techniques can drastically improve simulation times
- Re-writing some of the code in either OpenMaya or C++ libraries can boost performance
- using compute shaders/ CUDA frameworks to integrate faster simulation times with more particles.


