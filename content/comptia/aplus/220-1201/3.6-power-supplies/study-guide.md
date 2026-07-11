# Objective 3.6: Power Supplies

Objective 3.6 covers selecting and installing the appropriate power supply for
a system. The practical decisions are input voltage, DC output rails,
motherboard connector fit, redundancy, modular cabling, wattage sizing, and
energy efficiency.

## Safety and Conversion

Power supplies contain electrical risk. Disconnect the system from power before
working inside it, and follow system documentation for any device that can
store charge after being unplugged.

A computer power supply converts wall power from alternating current (AC) into
the direct current (DC) voltages used inside the computer. Common input ranges
are 110-120 VAC in the United States and Canada and 220-240 VAC in many other
regions. Some power supplies switch automatically across input ranges, while
others require the technician to set the correct input voltage before use.

## Output Voltages

The output side of the power supply provides several DC voltages for different
components. The main outputs in this objective are 3.3 V, 5 V, and 12 V.

The 12 V output is commonly associated with higher-power components such as
PCIe adapters, drive motors, cooling fans, and many modern components. The 5 V
output supports some motherboard components. Many motherboard logic circuits,
RAM slots, and M.2 slots use 3.3 V.

## Motherboard Power Connector

The main motherboard power connection is commonly a 24-pin ATX connector. The
older ATX connector was 20-pin, so many supplies use a 20+4-pin connector that
can fit either a 20-pin board or a 24-pin board when the extra four-pin section
is attached.

Do not confuse the main motherboard connector with PCIe auxiliary power
connectors for high-power add-on cards. Objective 3.6 focuses on choosing the
appropriate power supply and main power connection; Objective 3.5 covers
motherboard and add-on-card installation context.

## Redundant Power Supplies

Redundant power supplies use two or more power supply modules in the same
system, commonly in server hardware. Each supply should be able to handle the
load, so the system can continue running if one supply fails. Redundant
supplies are often hot-swappable, allowing replacement of a failed module
without powering down the system when the hardware supports it.

## Modular and Fixed Cabling

A fixed-cable power supply has cables permanently attached. It may be less
expensive, but unused cables can clutter the case and reduce airflow.

A modular power supply lets the technician add only the cables needed for the
build. This can improve cable management and airflow, but the supply is often
more expensive than a fixed-cable supply.

## Wattage Rating

Power supplies are rated in watts. The wattage must cover the system's
components, including CPU, storage, cooling, and especially video adapters when
present. Video adapter specifications often list a recommended power supply
wattage.

Oversizing is not automatically useful. A much larger supply does not make the
computer faster, may cost more, and may not run at the most efficient point.
Sizing should account for the total load, per-voltage requirements, and
reasonable room for future growth.

## Energy Efficiency

Converting AC to DC is not perfect. Some input power is lost as heat. A more
efficient power supply delivers more usable DC power for a given input and
generates less waste heat.

Efficiency is a selection factor, not a substitute for correct wattage,
connector compatibility, or input-voltage support. Choose an efficiency level
that fits the system requirements and operating environment.

## Scope Caveats

Do not memorize vendor-specific modular cable pinouts, proprietary power-supply
dimensions, exact efficiency certification marketing tiers, or a single wattage
number for every build. Use the objective concepts to select the right supply,
then verify exact requirements in the system, case, motherboard, and component
documentation.

## References

- CompTIA 220-1201 Exam Objectives v4.0, Objective 3.6
- Professor Messer 220-1201 v1.70 pp.40-41
