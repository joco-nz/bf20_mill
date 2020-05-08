 # BF20 Mill Gui

This is a GUI developed for an Optimum BF20 mill that has been converted
to cnc. I suspect this will work okay for similar machines or anything
that is not all decked out with an ATC of some form.

## Usage
This UI is intended to be used with a mill that does not have a repeatable
tool mounting system.  Where there is a need to remeasure tool changes after
the intial reference is set.   The general pattern being as follows:

a.  touch off with wobble of equivalent to get the x/y home point.
b.  touch off the z highet to the cnc models reference point with the first tool.
c.  start programme and all tool changes using M6 will move to a tool change location per ini file
d.  change tool and push acknowledge button on gui
e.  auto tool measuure happens against probe
f.  gcode prog continues

## Credits
There are some MASSIVE credits I need to and want to call out here:

[1] jethornton   https://github.com/jethornton/mill_touch_v6
I basiclly started as a tutorial a ground up build of his excellent gui.
In the end (under the MIT license) I re used a couple of his python code
files.  I could have rebuilt them but it was silly and my result would
have ended up looking almost exactly the same.
Also for the questions answered and the patience in answering them.

[2] hazzy for the support/questions answered on the most excellent qtpyvcp.
Also for the patience shown for what must have seemed like an endless
list statements that all summarise into "how does this work".

[3] kcjengr https://github.com/kcjengr/probe_basic
Used probe-basic to help understand how things work and also have made
temp use of some probe icons.Once I get more done I will assess if continued
use is the best option or not.

