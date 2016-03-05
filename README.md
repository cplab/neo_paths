
neo_paths
==========================================================================

This is the code repository for neo_paths. This repository was created 
with the end goal of developing a query tool that will be able to provide
information regarding the data stored in a Neo object.

Neo objects are flexible in that they can store data from multiple file 
formats. Neo objects belong to the Python Neo package, whose documentation 
can be found at the link below:

  * https://pythonhosted.org/neo/

Their ability to load and store multiple data formats stems from the 
Neo io module. 
 
  * https://pythonhosted.org/neo/io.html

In the Computational Physiology Lab, the Neo objects are used to store 
electrophysiology data originating from several data formats, notably MCS 
and SMR (from Spike2 software). The code in this repository will
initally be tested on these formats, however the goal is to make it
functional for any data format that can be converted to a Neo object. 
In the end, we hope to provide a consistent user experience regardless
of the original file format for the electrophysiology data so that the
user can quickly determine what information they have in any given file. 

### Authors

This main contributors to this project will be Hannah Gallovic and Megan
Leszczynski, with assistance from Matt Einhorn. 
