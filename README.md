## PyScripts

A collection of Python scripts/projects by KF:

1. **AutoRProj** - A simple Python script to automate the process of creating a new R Project folder with Input and Output sub-folders. At the moment, it relies on hard-coded coordinates. NewRProj is updated version.

2. **NewRProj** - Upgrade from AutoRProj, but uses images rather than hard-coded coordinates.
   - Coded for macOS retina screen resolutions. Non-macOS uses will need to tweak the `x_coord` and `y_coord` variables in the `moveToClick` function.
   - Reference images are for RStudio Dark Mode.



### AutoRProj vs NewRProj

| -         | Pros                             | Cons                     |
| --------- | -------------------------------- | ------------------------ |
| AutoRProj | - simple to setup                | - hard-coded coordinates |
| NewRProj  | - will work for all window sizes | - many more setup steps  |



### Citations:

1. [Python .gitignore](https://gist.github.com/GhostofGoes/94580e76cd251972b15b4821c8a06f59)
