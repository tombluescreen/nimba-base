# nimba-base
 Instance of nimba to be run on the controlled server.

This program provides control to the host server through a webapi and web server host.

Originally designed for raspberry-pi I've re-factored to allow a more general Linux use case.

as of 01/11/2022 this is out of use and broken.

## Technical Details
The web client uses hashes of defined commands to communicate with the server.
For example:
Command Name: helloworld -> Hash Value
Web client makes an api call to [Hash Value] and returns a response relevent to the command.

### Current Issues
No collision detection and management.
Small feature set (needs module expansion)