# FireScapeRx-release
Release repository for FireScape Rx

<html>
<body>
FireScape Rx is a simple interactive user interface that allows users to quickly and  easily import, interact with, 
simulate and view geospatial data of any resolution.<br><br>

One key aspect of FireScape Rx is that it integrates the Wildland-Urban Interface Fire Dynamics Simulation(WFDS) simulation engine and smokeview(SMV) visualisation tool into it's interface.

As such, we felt that it is important to specify what versions of WFDS and SMV FireScape-Rx has been tested with.

FireScape Rx is known to work with the following WFDS and SMV versions, respectively.

WFDS:
<li> FDS version: 6.0.0(Subversion revision number: 9977)

SMV:

<li> Smokeview Revision: SMV6.7.5-0-g92555b8-dirty

</body>
</html>

Quickstart:
Because WFDS and SMV are written in compiled languages(Fortran, C) FireScape-Rx does not provide a pre-packaged versions of either.

However, once one has access to compiled versions, users may point FireScape-Rx to the respective executables.
This may be achieved via the user settings, found under the 'settings' menu in the main menu bar.