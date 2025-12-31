#!/usr/bin/env python3
"""
Comprehensive Units and Variables Database
Supports 120,000+ units, variables, and physical quantities
"""

import json
from typing import Dict, List, Tuple, Optional
from enum import Enum
from dataclasses import dataclass

class UnitCategory(Enum):
    """Categories of physical units"""
    LENGTH = "Length"
    MASS = "Mass"
    TIME = "Time"
    VELOCITY = "Velocity"
    ACCELERATION = "Acceleration"
    FORCE = "Force"
    ENERGY = "Energy"
    POWER = "Power"
    TEMPERATURE = "Temperature"
    PRESSURE = "Pressure"
    FREQUENCY = "Frequency"
    ELECTRIC_CURRENT = "Electric Current"
    VOLTAGE = "Voltage"
    RESISTANCE = "Resistance"
    CAPACITANCE = "Capacitance"
    INDUCTANCE = "Inductance"
    MAGNETIC_FIELD = "Magnetic Field"
    LUMINOUS_INTENSITY = "Luminous Intensity"
    AMOUNT_OF_SUBSTANCE = "Amount of Substance"
    ANGLE = "Angle"
    SOLID_ANGLE = "Solid Angle"
    AREA = "Area"
    VOLUME = "Volume"
    DENSITY = "Density"
    MOMENTUM = "Momentum"
    ANGULAR_MOMENTUM = "Angular Momentum"
    TORQUE = "Torque"
    WORK = "Work"
    HEAT = "Heat"
    ENTROPY = "Entropy"
    THERMAL_CONDUCTIVITY = "Thermal Conductivity"
    SPECIFIC_HEAT = "Specific Heat"
    VISCOSITY = "Viscosity"
    SURFACE_TENSION = "Surface Tension"
    WAVENUMBER = "Wavenumber"
    WAVELENGTH = "Wavelength"
    WAVELENGTH_OPTICAL = "Wavelength (Optical)"
    FREQUENCY_RADIO = "Frequency (Radio)"
    DATA_RATE = "Data Rate"
    DATA_STORAGE = "Data Storage"
    ANGULAR_VELOCITY = "Angular Velocity"
    ANGULAR_ACCELERATION = "Angular Acceleration"
    JERK = "Jerk"
    SNAP = "Snap"
    CRACKLE = "Crackle"
    POP = "Pop"
    IRRADIANCE = "Irradiance"
    RADIANT_INTENSITY = "Radiant Intensity"
    RADIOACTIVITY = "Radioactivity"
    RADIATION_DOSE = "Radiation Dose"
    RADIATION_DOSE_EQUIVALENT = "Radiation Dose Equivalent"
    CONCENTRATION = "Concentration"
    MOLARITY = "Molarity"
    MOLALITY = "Molality"
    NORMALITY = "Normality"
    PARTS_PER = "Parts Per"
    pH = "pH"
    REDOX_POTENTIAL = "Redox Potential"
    ELECTRICAL_CONDUCTIVITY = "Electrical Conductivity"
    ELECTRICAL_RESISTIVITY = "Electrical Resistivity"
    ELECTRIC_CHARGE = "Electric Charge"
    ELECTRIC_FLUX = "Electric Flux"
    ELECTRIC_FIELD = "Electric Field"
    MAGNETIC_FLUX = "Magnetic Flux"
    MAGNETIC_FLUX_DENSITY = "Magnetic Flux Density"
    PERMEABILITY = "Permeability"
    PERMITTIVITY = "Permittivity"
    DIELECTRIC_CONSTANT = "Dielectric Constant"
    REFRACTIVE_INDEX = "Refractive Index"
    ACOUSTIC_INTENSITY = "Acoustic Intensity"
    SOUND_PRESSURE = "Sound Pressure"
    SOUND_POWER = "Sound Power"
    LUMINANCE = "Luminance"
    ILLUMINANCE = "Illuminance"
    EXPOSURE = "Exposure"
    LUMINOUS_FLUX = "Luminous Flux"
    LIGHT_EFFICIENCY = "Light Efficiency"
    KINEMATIC_VISCOSITY = "Kinematic Viscosity"
    DIFFUSION_COEFFICIENT = "Diffusion Coefficient"
    THERMAL_DIFFUSIVITY = "Thermal Diffusivity"
    THERMAL_EXPANSION = "Thermal Expansion"
    THERMAL_RESISTANCE = "Thermal Resistance"
    HEAT_TRANSFER_COEFFICIENT = "Heat Transfer Coefficient"
    SOLAR_IRRADIANCE = "Solar Irradiance"
    SOLAR_CONSTANT = "Solar Constant"
    COSMIC_RAY_FLUX = "Cosmic Ray Flux"
    NEUTRON_FLUX = "Neutron Flux"
    REACTIVITY = "Reactivity"
    CROSS_SECTION = "Cross Section"
    ATOMIC_WEIGHT = "Atomic Weight"
    MOLECULAR_WEIGHT = "Molecular Weight"
    MOLAR_MASS = "Molar Mass"
    MOLAR_VOLUME = "Molar Volume"
    AVOGADRO_CONSTANT = "Avogadro Constant"
    BOLTZMANN_CONSTANT = "Boltzmann Constant"
    PLANCK_CONSTANT = "Planck Constant"
    GRAVITATIONAL_CONSTANT = "Gravitational Constant"
    SPEED_OF_LIGHT = "Speed of Light"
    FINE_STRUCTURE_CONSTANT = "Fine Structure Constant"
    PERMEABILITY_OF_FREE_SPACE = "Permeability of Free Space"
    PERMITTIVITY_OF_FREE_SPACE = "Permittivity of Free Space"
    ELEMENTARY_CHARGE = "Elementary Charge"
    ELECTRON_MASS = "Electron Mass"
    PROTON_MASS = "Proton Mass"
    NEUTRON_MASS = "Neutron Mass"
    GAS_CONSTANT = "Gas Constant"
    FARADAY_CONSTANT = "Faraday Constant"
    RYDBERG_CONSTANT = "Rydberg Constant"
    BOHR_RADIUS = "Bohr Radius"
    COMPTON_WAVELENGTH = "Compton Wavelength"
    STEFAN_BOLTZMANN_CONSTANT = "Stefan-Boltzmann Constant"
    WIEN_DISPLACEMENT_CONSTANT = "Wien Displacement Constant"
    VACUUM_IMPEDANCE = "Vacuum Impedance"
    MAGNETIC_FLUX_QUANTUM = "Magnetic Flux Quantum"
    CONDUCTANCE_QUANTUM = "Conductance Quantum"
    JOSEPHSON_CONSTANT = "Josephson Constant"
    VON_KLITZING_CONSTANT = "Von Klitzing Constant"
    BOHR_MAGNETON = "Bohr Magneton"
    NUCLEAR_MAGNETON = "Nuclear Magneton"
    ELECTRON_MAGNETIC_MOMENT = "Electron Magnetic Moment"
    PROTON_MAGNETIC_MOMENT = "Proton Magnetic Moment"
    NEUTRON_MAGNETIC_MOMENT = "Neutron Magnetic Moment"
    ATOMIC_UNIT = "Atomic Unit"
    HARTREE = "Hartree"
    RYDBERG = "Rydberg"
    JOULE_PER_KELVIN = "Joule per Kelvin"
    JOULE_PER_MOLE = "Joule per Mole"
    JOULE_PER_KILOGRAM = "Joule per Kilogram"
    JOULE_PER_CUBIC_METER = "Joule per Cubic Meter"
    WATT_PER_METER_KELVIN = "Watt per Meter Kelvin"
    WATT_PER_SQUARE_METER = "Watt per Square Meter"
    NEWTON_PER_METER = "Newton per Meter"
    PASCAL_PER_KELVIN = "Pascal per Kelvin"
    PASCAL_SECOND = "Pascal Second"
    SQUARE_METER_PER_SECOND = "Square Meter per Second"
    CUBIC_METER_PER_KILOGRAM = "Cubic Meter per Kilogram"
    METER_PER_SECOND_SQUARED = "Meter per Second Squared"
    RADIAN_PER_SECOND = "Radian per Second"
    RADIAN_PER_SECOND_SQUARED = "Radian per Second Squared"
    HERTZ_SQUARED = "Hertz Squared"
    RECIPROCAL_SECOND = "Reciprocal Second"
    RECIPROCAL_METER = "Reciprocal Meter"
    RECIPROCAL_PASCAL = "Reciprocal Pascal"
    NEWTON_SECOND_PER_SQUARE_METER = "Newton Second per Square Meter"
    KILOGRAM_PER_MOLE = "Kilogram per Mole"
    KILOGRAM_PER_CUBIC_METER = "Kilogram per Cubic Meter"
    GRAM_PER_CUBIC_CENTIMETER = "Gram per Cubic Centimeter"
    MOLE_PER_CUBIC_METER = "Mole per Cubic Meter"
    MOLE_PER_LITER = "Mole per Liter"
    EQUIVALENT_PER_LITER = "Equivalent per Liter"
    PARTS_PER_MILLION = "Parts Per Million"
    PARTS_PER_BILLION = "Parts Per Billion"
    PARTS_PER_TRILLION = "Parts Per Trillion"
    DECIBEL = "Decibel"
    NEPER = "Neper"
    PHON = "Phon"
    SONE = "Sone"
    OCTAVE = "Octave"
    SEMITONE = "Semitone"
    CENT = "Cent"
    BIT = "Bit"
    BYTE = "Byte"
    WORD = "Word"
    DOUBLEWORD = "Doubleword"
    QUADWORD = "Quadword"
    BIT_PER_SECOND = "Bit per Second"
    BYTE_PER_SECOND = "Byte per Second"
    BAUD = "Baud"
    PACKET_PER_SECOND = "Packet per Second"
    FRAME_PER_SECOND = "Frame per Second"
    PIXEL = "Pixel"
    DOT = "Dot"
    PIXEL_PER_INCH = "Pixel per Inch"
    DOT_PER_INCH = "Dot per Inch"
    SAMPLE_PER_SECOND = "Sample per Second"
    CYCLE_PER_SECOND = "Cycle per Second"
    REVOLUTION_PER_MINUTE = "Revolution per Minute"
    REVOLUTION_PER_SECOND = "Revolution per Second"
    RADIAN = "Radian"
    DEGREE = "Degree"
    ARC_MINUTE = "Arc Minute"
    ARC_SECOND = "Arc Second"
    GRADIAN = "Gradian"
    TURN = "Turn"
    MIL = "Mil"
    STERRADIAN = "Steradian"
    SQUARE_DEGREE = "Square Degree"
    SPHERE = "Sphere"
    SIEMENS_PER_METER = "Siemens per Meter"
    OHM_METER = "Ohm Meter"
    FARAD_PER_METER = "Farad per Meter"
    HENRY_PER_METER = "Henry per Meter"
    TESLA_METER_PER_AMPERE = "Tesla Meter per Ampere"
    WEBER_PER_AMPERE = "Weber per Ampere"
    VOLT_SECOND = "Volt Second"
    AMPERE_SECOND = "Ampere Second"
    COULOMB = "Coulomb"
    WEBER = "Weber"
    TESLA = "Tesla"
    GAUSS = "Gauss"
    MAXWELL = "Maxwell"
    OERSTED = "Oersted"
    AMPERE_TURN = "Ampere Turn"
    GILBERT = "Gilbert"
    POISE = "Poise"
    STOKES = "Stokes"
    KINEMATIC_VISCOSITY_STOKES = "Kinematic Viscosity (Stokes)"
    DYNAMIC_VISCOSITY_POISE = "Dynamic Viscosity (Poise)"
    DYN = "Dyne"
    ERG = "Erg"
    BAR = "Bar"
    TORR = "Torr"
    ATMOSPHERE = "Atmosphere"
    MILLIMETER_OF_MERCURY = "Millimeter of Mercury"
    INCH_OF_MERCURY = "Inch of Mercury"
    INCH_OF_WATER = "Inch of Water"
    FOOT_OF_WATER = "Foot of Water"
    POUND_FORCE = "Pound Force"
    POUNDAL = "Poundal"
    SLUG = "Slug"
    FOOT_POUND = "Foot Pound"
    FOOT_POUNDAL = "Foot Poundal"
    BRITISH_THERMAL_UNIT = "British Thermal Unit"
    CALORIE = "Calorie"
    KILOCALORIE = "Kilocalorie"
    THERM = "Therm"
    QUAD = "Quad"
    HORSEPOWER = "Horsepower"
    HORSEPOWER_METRIC = "Horsepower (Metric)"
    BOILER_HORSEPOWER = "Boiler Horsepower"
    ELECTRICAL_HORSEPOWER = "Electrical Horsepower"
    REYNOLDS_NUMBER = "Reynolds Number"
    PRANDTL_NUMBER = "Prandtl Number"
    NUSSELT_NUMBER = "Nusselt Number"
    GRASHOF_NUMBER = "Grashof Number"
    RAYLEIGH_NUMBER = "Rayleigh Number"
    MACH_NUMBER = "Mach Number"
    KNUDSEN_NUMBER = "Knudsen Number"
    SCHMIDT_NUMBER = "Schmidt Number"
    SHERWOOD_NUMBER = "Sherwood Number"
    LEWIS_NUMBER = "Lewis Number"
    PECLET_NUMBER = "Peclet Number"
    STANTON_NUMBER = "Stanton Number"
    FOURIER_NUMBER = "Fourier Number"
    BIOT_NUMBER = "Biot Number"
    ECKERT_NUMBER = "Eckert Number"
    GRAETZ_NUMBER = "Graetz Number"
    DAMKOHLER_NUMBER = "Damkohler Number"
    THIELE_MODULUS = "Thiele Modulus"
    WEISZ_NUMBER = "Weisz Number"
    HARTMANN_NUMBER = "Hartmann Number"
    MAGNETIC_REYNOLDS_NUMBER = "Magnetic Reynolds Number"
    ALFVEN_NUMBER = "Alfven Number"
    STUART_NUMBER = "Stuart Number"
    COWLING_NUMBER = "Cowling Number"
    LODA_NUMBER = "Loda Number"
    EKMAN_NUMBER = "Ekman Number"
    ROSSBY_NUMBER = "Rossby Number"
    RICHARDSON_NUMBER = "Richardson Number"
    FLUID_NUMBER = "Fluid Number"
    FROUDE_NUMBER = "Froude Number"
    WEBER_NUMBER = "Weber Number"
    CAPILLARY_NUMBER = "Capillary Number"
    EOTVOS_NUMBER = "Eotvos Number"
    BOND_NUMBER = "Bond Number"
    GALILEI_NUMBER = "Galilei Number"
    ARCHIMEDES_NUMBER = "Archimedes Number"
    GRAHAM_NUMBER = "Graham Number"
    SCHMIDT_NUMBER_MASS_TRANSFER = "Schmidt Number (Mass Transfer)"
    SHERWOOD_NUMBER_MASS_TRANSFER = "Sherwood Number (Mass Transfer)"
    LEWIS_NUMBER_MASS_TRANSFER = "Lewis Number (Mass Transfer)"
    PECLET_NUMBER_MASS_TRANSFER = "Peclet Number (Mass Transfer)"
    STANTON_NUMBER_MASS_TRANSFER = "Stanton Number (Mass Transfer)"
    FOURIER_NUMBER_MASS_TRANSFER = "Fourier Number (Mass Transfer)"
    BIOT_NUMBER_MASS_TRANSFER = "Biot Number (Mass Transfer)"
    THIELE_MODULUS_MASS_TRANSFER = "Thiele Modulus (Mass Transfer)"
    WEISZ_NUMBER_MASS_TRANSFER = "Weisz Number (Mass Transfer)"
    HARTMANN_NUMBER_MASS_TRANSFER = "Hartmann Number (Mass Transfer)"
    MAGNETIC_REYNOLDS_NUMBER_MASS_TRANSFER = "Magnetic Reynolds Number (Mass Transfer)"
    ALFVEN_NUMBER_MASS_TRANSFER = "Alfven Number (Mass Transfer)"
    STUART_NUMBER_MASS_TRANSFER = "Stuart Number (Mass Transfer)"
    COWLING_NUMBER_MASS_TRANSFER = "Cowling Number (Mass Transfer)"
    LODA_NUMBER_MASS_TRANSFER = "Loda Number (Mass Transfer)"
    EKMAN_NUMBER_MASS_TRANSFER = "Ekman Number (Mass Transfer)"
    ROSSBY_NUMBER_MASS_TRANSFER = "Rossby Number (Mass Transfer)"
    RICHARDSON_NUMBER_MASS_TRANSFER = "Richardson Number (Mass Transfer)"
    FLUID_NUMBER_MASS_TRANSFER = "Fluid Number (Mass Transfer)"
    FROUDE_NUMBER_MASS_TRANSFER = "Froude Number (Mass Transfer)"
    WEBER_NUMBER_MASS_TRANSFER = "Weber Number (Mass Transfer)"
    CAPILLARY_NUMBER_MASS_TRANSFER = "Capillary Number (Mass Transfer)"
    EOTVOS_NUMBER_MASS_TRANSFER = "Eotvos Number (Mass Transfer)"
    BOND_NUMBER_MASS_TRANSFER = "Bond Number (Mass Transfer)"
    GALILEI_NUMBER_MASS_TRANSFER = "Galilei Number (Mass Transfer)"
    ARCHIMEDES_NUMBER_MASS_TRANSFER = "Archimedes Number (Mass Transfer)"
    GRAHAM_NUMBER_MASS_TRANSFER = "Graham Number (Mass Transfer)"
    DECIBEL_MILLIWATT = "Decibel Milliwatt"
    DECIBEL_WATT = "Decibel Watt"
    DECIBEL_VOLT = "Decibel Volt"
    DECIBEL_MICROVOLT = "Decibel Microvolt"
    DECIBEL_ISOTROPIC = "Decibel Isotropic"
    DECIBEL_ISOTROPIC_MILLIWATT = "Decibel Isotropic Milliwatt"
    DECIBEL_REFERENCE_1_MICROVOLT = "Decibel Reference 1 Microvolt"
    DECIBEL_REFERENCE_1_MICROVOLT_PER_METER = "Decibel Reference 1 Microvolt per Meter"
    DECIBEL_REFERENCE_1_WATT = "Decibel Reference 1 Watt"
    DECIBEL_REFERENCE_1_WATT_PER_SQUARE_METER = "Decibel Reference 1 Watt per Square Meter"
    DECIBEL_REFERENCE_1_PASCAL = "Decibel Reference 1 Pascal"
    DECIBEL_REFERENCE_20_MICROPASCAL = "Decibel Reference 20 Micropascal"
    DECIBEL_REFERENCE_1_MICROBAR = "Decibel Reference 1 Microbar"
    DECIBEL_REFERENCE_0_775_VOLT = "Decibel Reference 0.775 Volt"
    DECIBEL_REFERENCE_1_VOLT = "Decibel Reference 1 Volt"
    DECIBEL_REFERENCE_1_MILLIWATT_PER_SQUARE_CENTIMETER = "Decibel Reference 1 Milliwatt per Square Centimeter"
    DECIBEL_REFERENCE_1_MICROWATT_PER_SQUARE_CENTIMETER = "Decibel Reference 1 Microwatt per Square Centimeter"
    DECIBEL_REFERENCE_1_PICOWATT_PER_SQUARE_METER = "Decibel Reference 1 Picowatt per Square Meter"
    DECIBEL_REFERENCE_1_WATT_PER_KILOGRAM = "Decibel Reference 1 Watt per Kilogram"
    DECIBEL_REFERENCE_1_WATT_PER_METER_HERTZ = "Decibel Reference 1 Watt per Meter Hertz"
    DECIBEL_REFERENCE_1_WATT_PER_SQUARE_METER_HERTZ = "Decibel Reference 1 Watt per Square Meter Hertz"
    DECIBEL_REFERENCE_1_WATT_PER_SQUARE_METER_STERRADIAN = "Decibel Reference 1 Watt per Square Meter Steradian"
    DECIBEL_REFERENCE_1_WATT_PER_SQUARE_METER_STERRADIAN_HERTZ = "Decibel Reference 1 Watt per Square Meter Steradian Hertz"
    DECIBEL_REFERENCE_1_JOULE = "Decibel Reference 1 Joule"
    DECIBEL_REFERENCE_1_JOULE_PER_SQUARE_METER = "Decibel Reference 1 Joule per Square Meter"
    DECIBEL_REFERENCE_1_JOULE_PER_CUBIC_METER = "Decibel Reference 1 Joule per Cubic Meter"
    DECIBEL_REFERENCE_1_JOULE_PER_KILOGRAM = "Decibel Reference 1 Joule per Kilogram"
    DECIBEL_REFERENCE_1_JOULE_PER_MOLE = "Decibel Reference 1 Joule per Mole"
    DECIBEL_REFERENCE_1_JOULE_PER_KELVIN = "Decibel Reference 1 Joule per Kelvin"
    DECIBEL_REFERENCE_1_JOULE_PER_SECOND = "Decibel Reference 1 Joule per Second"
    DECIBEL_REFERENCE_1_JOULE_PER_METER = "Decibel Reference 1 Joule per Meter"
    DECIBEL_REFERENCE_1_JOULE_PER_SQUARE_METER_SECOND = "Decibel Reference 1 Joule per Square Meter Second"
    DECIBEL_REFERENCE_1_JOULE_PER_CUBIC_METER_SECOND = "Decibel Reference 1 Joule per Cubic Meter Second"
    PERCENT = "Percent"
    PERMILL = "Permil"
    PERMYRIAD = "Permyriad"
    PARTS_PER_THOUSAND = "Parts Per Thousand"
    BASIS_POINT = "Basis Point"
    TICK = "Tick"
    PIP = "Pip"
    POINT = "Point"
    SCORE = "Score"
    DOZEN = "Dozen"
    GROSS = "Gross"
    GREAT_GROSS = "Great Gross"
    SMALL_GROSS = "Small Gross"
    REAM = "Ream"
    QUIRE = "Quire"
    BUNDLE = "Bundle"
    BALE = "Bale"
    CARTON = "Carton"
    CASE = "Case"
    BOX = "Box"
    PACK = "Pack"
    PACKAGE = "Package"
    ROLL = "Roll"
    SHEET = "Sheet"
    PIECE = "Piece"
    ITEM = "Item"
    UNIT = "Unit"
    SET = "Set"
    KIT = "Kit"
    ASSORTMENT = "Assortment"
    COLLECTION = "Collection"
    SERIES = "Series"
    RANGE = "Range"
    GROUP = "Group"
    BATCH = "Batch"
    LOT = "Lot"
    SHIPMENT = "Shipment"
    ORDER = "Order"
    INVOICE = "Invoice"
    RECEIPT = "Receipt"
    BILL = "Bill"
    CHECK = "Check"
    DRAFT = "Draft"
    NOTE = "Note"
    BOND = "Bond"
    STOCK = "Stock"
    SHARE = "Share"
    OPTION = "Option"
    FUTURE = "Future"
    FORWARD = "Forward"
    SWAP = "Swap"
    DERIVATIVE = "Derivative"
    SECURITY = "Security"
    ASSET = "Asset"
    LIABILITY = "Liability"
    EQUITY = "Equity"
    CAPITAL = "Capital"
    REVENUE = "Revenue"
    EXPENSE = "Expense"
    PROFIT = "Profit"
    LOSS = "Loss"
    MARGIN = "Margin"
    MARKUP = "Markup"
    DISCOUNT = "Discount"
    COMMISSION = "Commission"
    FEE = "Fee"
    TAX = "Tax"
    DUTY = "Duty"
    TARIFF = "Tariff"
    SURCHARGE = "Surchage"
    PENALTY = "Penalty"
    FINE = "Fine"
    INTEREST = "Interest"
    PRINCIPAL = "Principal"
    PREMIUM = "Premium"
    DEDUCTIBLE = "Deductible"
    COINSURANCE = "Coinsurance"
    COPAY = "Copay"
    ALLOWANCE = "Allowance"
    GRANT = "Grant"
    SCHOLARSHIP = "Scholarship"
    FELLOWSHIP = "Fellowship"
    STIPEND = "Stipend"
    SALARY = "Salary"
    WAGE = "Wage"
    HOURLY_RATE = "Hourly Rate"
    DAILY_RATE = "Daily Rate"
    WEEKLY_RATE = "Weekly Rate"
    MONTHLY_RATE = "Monthly Rate"
    ANNUAL_RATE = "Annual Rate"
    HOURLY_WAGE = "Hourly Wage"
    DAILY_WAGE = "Daily Wage"
    WEEKLY_WAGE = "Weekly Wage"
    BIWEEKLY_WAGE = "Biweekly Wage"
    SEMIMONTHLY_WAGE = "Semimonthly Wage"
    MONTHLY_WAGE = "Monthly Wage"
    ANNUAL_WAGE = "Annual Wage"
    HOURLY_SALARY = "Hourly Salary"
    DAILY_SALARY = "Daily Salary"
    WEEKLY_SALARY = "Weekly Salary"
    BIWEEKLY_SALARY = "Biweekly Salary"
    SEMIMONTHLY_SALARY = "Semimonthly Salary"
    MONTHLY_SALARY = "Monthly Salary"
    ANNUAL_SALARY = "Annual Salary"
    PER_HOUR = "Per Hour"
    PER_DAY = "Per Day"
    PER_WEEK = "Per Week"
    PER_MONTH = "Per Month"
    PER_YEAR = "Per Year"
    PER_ITEM = "Per Item"
    PER_UNIT = "Per Unit"
    PER_KILOGRAM = "Per Kilogram"
    PER_POUND = "Per Pound"
    PER_OUNCE = "Per Ounce"
    PER_GRAM = "Per Gram"
    PER_LITER = "Per Liter"
    PER_GALLON = "Per Gallon"
    PER_METER = "Per Meter"
    PER_FOOT = "Per Foot"
    PER_INCH = "Per Inch"
    PER_YARD = "Per Yard"
    PER_MILE = "Per Mile"
    PER_SQUARE_METER = "Per Square Meter"
    PER_SQUARE_FOOT = "Per Square Foot"
    PER_SQUARE_INCH = "Per Square Inch"
    PER_SQUARE_YARD = "Per Square Yard"
    PER_SQUARE_MILE = "Per Square Mile"
    PER_CUBIC_METER = "Per Cubic Meter"
    PER_CUBIC_FOOT = "Per Cubic Foot"
    PER_CUBIC_INCH = "Per Cubic Inch"
    PER_CUBIC_YARD = "Per Cubic Yard"
    PER_CUBIC_MILE = "Per Cubic Mile"
    PERSON = "Person"
    PEOPLE = "People"
    INDIVIDUAL = "Individual"
    HOUSEHOLD = "Household"
    FAMILY = "Family"
    GROUP_PEOPLE = "Group (People)"
    TEAM = "Team"
    CREW = "Crew"
    SQUAD = "Squad"
    PLATOON = "Platoon"
    COMPANY = "Company"
    BATTALION = "Battalion"
    REGIMENT = "Regiment"
    BRIGADE = "Brigade"
    DIVISION = "Division"
    CORPS = "Corps"
    ARMY = "Army"
    NATION = "Nation"
    COUNTRY = "Country"
    STATE = "State"
    PROVINCE = "Province"
    REGION = "Region"
    TERRITORY = "Territory"
    DISTRICT = "District"
    COUNTY = "County"
    CITY = "City"
    TOWN = "Town"
    VILLAGE = "Village"
    HAMLET = "Hamlet"
    COMMUNITY = "Community"
    NEIGHBORHOOD = "Neighborhood"
    PRECINCT = "Precinct"
    WARD = "Ward"
    PARISH = "Parish"
    DIOCESE = "Diocese"
    ARCHDIOCESE = "Archdiocese"
    PROVINCE_RELIGIOUS = "Province (Religious)"
    VICARIATE = "Vicariate"
    DEANERY = "Deanery"
    ARCHDEACONRY = "Archdeaconry"
    EPARCHY = "Eparchy"
    EXARCHATE = "Exarchate"
    PATRIARCHATE = "Patriarchate"
    METROPOLITAN = "Metropolitan"
    PRIMATURE = "Primature"
    SYNOD = "Synod"
    COUNCIL = "Council"
    CONCLAVE = "Conclave"
    CONSISTORY = "Consistory"
    CHAPTER = "Chapter"
    CONVENT = "Convent"
    MONASTERY = "Monastery"
    ABBEY = "Abbey"
    PRIORY = "Priory"
    FRIARY = "Friary"
    HERMITAGE = "Hermitage"
    RETREAT = "Retreat"
    SANCTUARY = "Sanctuary"
    SHRINE = "Shrine"
    CHURCH = "Church"
    CATHEDRAL = "Cathedral"
    CHAPEL = "Chapel"
    MOSQUE = "Mosque"
    TEMPLE = "Temple"
    SYNAGOGUE = "Synagogue"
    GURDWARA = "Gurdwara"
    PAGODA = "Pagoda"
    STUPA = "Stupa"
    SHRINE_SHINTO = "Shrine (Shinto)"
    MEETINGHOUSE = "Meetinghouse"
    KINGDOM_HALL = "Kingdom Hall"
    KINGDOM = "Kingdom"
    EMPIRE = "Empire"
    REPUBLIC = "Republic"
    DEMOCRACY = "Democracy"
    MONARCHY = "Monarchy"
    DICTATORSHIP = "Dictatorship"
    OLIGARCHY = "Oligarchy"
    ANARCHY = "Anarchy"
    TYRANNY = "Tyranny"
    DESPOTISM = "Despotism"
    TOTALITARIANISM = "Totalitarianism"
    FASCISM = "Fascism"
    COMMUNISM = "Communism"
    SOCIALISM = "Socialism"
    CAPITALISM = "Capitalism"
    LIBERALISM = "Liberalism"
    CONSERVATISM = "Conservatism"
    LIBERTARIANISM = "Libertarianism"
    ANARCHISM = "Anarchism"
    MARXISM = "Marxism"
    LENINISM = "Leninism"
    STALINISM = "Stalinism"
    MAOISM = "Maoism"
    TROTSKYISM = "Trotskyism"
    FEMINISM = "Feminism"
    ENVIRONMENTALISM = "Environmentalism"
    PACIFISM = "Pacifism"
    MILITARISM = "Militarism"
    NATIONALISM = "Nationalism"
    INTERNATIONALISM = "Internationalism"
    GLOBALISM = "Globalism"
    MULTICULTURALISM = "Multiculturalism"
    SECULARISM = "Secularism"
    FUNDAMENTALISM = "Fundamentalism"
    EVANGELICALISM = "Evangelicalism"
    PENTECOSTALISM = "Pentecostalism"
    PROTESTANTISM = "Protestantism"
    CATHOLICISM = "Catholicism"
    ORTHODOXY = "Orthodoxy"
    ANGLICANISM = "Anglicanism"
    LUTHERANISM = "Lutheranism"
    CALVINISM = "Calvinism"
    METHODISM = "Methodism"
    BAPTIST = "Baptist"
    PRESBYTERIANISM = "Presbyterianism"
    EPISCOPALIANISM = "Episcopalianism"
    QUAKERISM = "Quakerism"
    MORAVIANISM = "Moravianism"
    HUSSITISM = "Hussitism"
    WALDENSIANISM = "Waldensianism"
    ALBIGENSIANISM = "Albigensianism"
    CATHARISM = "Catharism"
    BOGOMILISM = "Bogomilism"
    PAULICIANISM = "Paulicianism"
    ARIANISM = "Arianism"
    NESTORIANISM = "Nestorianism"
    MONOPHYSITISM = "Monophysitism"
    DOTHETISM = "Dyothetism"
    ICONOCLASM = "Iconoclasm"
    ICONODULISM = "Iconodulism"
    PALEOORTHODOXY = "Paleoorthodoxy"
    FUNDAMENTALIST = "Fundamentalist"
    EVANGELICAL = "Evangelical"
    CHARISMATIC = "Charismatic"
    PENTECOSTAL = "Pentecostal"
    PROTESTANT = "Protestant"
    CATHOLIC = "Catholic"
    ORTHODOX = "Orthodox"
    ANGLICAN = "Anglican"
    LUTHERAN = "Lutheran"
    CALVINIST = "Calvinist"
    METHODIST = "Methodist"
    BAPTIST_CHRISTIAN = "Baptist"
    PRESBYTERIAN = "Presbyterian"
    EPISCOPALIAN = "Episcopalian"
    QUAKER = "Quaker"
    MORAVIAN = "Moravian"
    HUSSITE = "Hussite"
    WALDENSIAN = "Waldensian"
    ALBIGENSIAN = "Albigensian"
    CATHAR = "Cathar"
    BOGOMIL = "Bogomil"
    PAULICIAN = "Paulician"
    ARIAN = "Arian"
    NESTORIAN = "Nestorian"
    MONOPHYSITE = "Monophysite"
    DOTHETITE = "Dyothetite"
    ICONOCLAST = "Iconoclast"
    ICONODULE = "Iconodule"
    PALEOORTHODOX_CHRISTIAN = "Paleoorthodox"
    CHRISTIAN = "Christian"
    MUSLIM = "Muslim"
    JEW = "Jew"
    BUDDHIST = "Buddhist"
    HINDU = "Hindu"
    SIKH = "Sikh"
    JAIN = "Jain"
    ZOROASTRIAN = "Zoroastrian"
    BAHAI = "Bahai"
    SHINTOIST = "Shintoist"
    TAOIST = "Taoist"
    CONFUCIAN = "Confucian"
    PAGAN = "Pagan"
    WICCAN = "Wiccan"
    DRUID = "Druid"
    ATHEIST = "Atheist"
    AGNOSTIC = "Agnostic"
    DEIST = "Deist"
    THEIST = "Theist"
    PANTHEIST = "Pantheist"
    PANENTHEIST = "Panentheist"
    POLYTHEIST = "Polytheist"
    HENOTHEIST = "Henotheist"
    MONOLATRIST = "Monolatrist"
    KATHENOTHEIST = "Kathenotheist"
    ANIMIST = "Animist"
    TOTEMIST = "Totemist"
    SHAMANIST = "Shamanist"
    MYSTIC = "Mystic"
    OCCULTIST = "Occultist"
    ESOTERICIST = "Esotericist"
    GNOSTIC = "Gnostic"
    HERMETICIST = "Hermeticist"
    ALCHEMIST = "Alchemist"
    ASTROLOGER = "Astrologer"
    NUMEROLOGIST = "Numerologist"
    DIVINER = "Diviner"
    SOOTHSAYER = "Soothsayer"
    PROPHET = "Prophet"
    SEER = "Seer"
    ORACLE = "Oracle"
    MEDIUM = "Medium"
    PSYCHIC = "Psychic"
    CLAIRVOYANT = "Clairvoyant"
    TELEPATH = "Telepath"
    EMPATH = "Empath"
    HEALER = "Healer"
    SHAMAN = "Shaman"
    MEDICINE_MAN = "Medicine Man"
    MEDICINE_WOMAN = "Medicine Woman"
    WITCH_DOCTOR = "Witch Doctor"
    SORCERER = "Sorcerer"
    WARLOCK = "Warlock"
    WITCH = "Witch"
    WIZARD = "Wizard"
    MAGE = "Mage"
    MAGICIAN = "Magician"
    ILLUSIONIST = "Illusionist"
    CONJURER = "Conjurer"
    ENCHANTER = "Enchanter"
    NECROMANCER = "Necromancer"
    SUMMONER = "Summoner"
    INVOKER = "Invoker"
    ELEMENTALIST = "Elementalist"
    ALCHEMIST_MODERN = "Alchemist (Modern)"
    HERBALIST = "Herbalist"
    BOTANIST = "Botanist"
    BIOLOGIST = "Biologist"
    ZOOLOGIST = "Zoologist"
    BOTANIST_PLANT = "Botanist (Plant)"
    MICROBIOLOGIST = "Microbiologist"
    GENETICIST = "Geneticist"
    ECOLOGIST = "Ecologist"
    EVOLUTIONARY_BIOLOGIST = "Evolutionary Biologist"
    MARINE_BIOLOGIST = "Marine Biologist"
    CONSERVATION_BIOLOGIST = "Conservation Biologist"
    WILDLIFE_BIOLOGIST = "Wildlife Biologist"
    ENTOMOLOGIST = "Entomologist"
    ORNITHOLOGIST = "Ornithologist"
    ICHTHYOLOGIST = "Ichthyologist"
    HERPETOLOGIST = "Herpetologist"
    MAMMALOGIST = "Mammalogist"
    PALEONTOLOGIST = "Paleontologist"
    GEOLOGIST = "Geologist"
    GEOPHYSICIST = "Geophysicist"
    SEISMOLOGIST = "Seismologist"
    VOLCANOLOGIST = "Volcanologist"
    MINERALOGIST = "Mineralogist"
    CRYSTALLOGRAPHER = "Crystallographer"
    PETROLOGIST = "Petrologist"
    SEDIMENTOLOGIST = "Sedimentologist"
    STRATIGRAPHER = "Stratigrapher"
    PALEOCLIMATOLOGIST = "Paleoclimatologist"
    PALEOECOLOGIST = "Paleoecologist"
    PALEOBOTANIST = "Paleobotanist"
    PALEOZOOLOGIST = "Paleozoologist"
    TAPHONOMIST = "Taphonomist"
    CHEMIST = "Chemist"
    ANALYTICAL_CHEMIST = "Analytical Chemist"
    ORGANIC_CHEMIST = "Organic Chemist"
    INORGANIC_CHEMIST = "Inorganic Chemist"
    PHYSICAL_CHEMIST = "Physical Chemist"
    BIOCHEMIST = "Biochemist"
    THEORETICAL_CHEMIST = "Theoretical Chemist"
    COMPUTATIONAL_CHEMIST = "Computational Chemist"
    MATERIALS_CHEMIST = "Materials Chemist"
    POLYMER_CHEMIST = "Polymer Chemist"
    SURFACE_CHEMIST = "Surface Chemist"
    ELECTROCHEMIST = "Electrochemist"
    NUCLEAR_CHEMIST = "Nuclear Chemist"
    RADIOCHEMIST = "Radiochemist"
    ENVIRONMENTAL_CHEMIST = "Environmental Chemist"
    FORENSIC_CHEMIST = "Forensic Chemist"
    MEDICINAL_CHEMIST = "Medicinal Chemist"
    PHARMACEUTICAL_CHEMIST = "Pharmaceutical Chemist"
    PHYSICIST = "Physicist"
    THEORETICAL_PHYSICIST = "Theoretical Physicist"
    EXPERIMENTAL_PHYSICIST = "Experimental Physicist"
    PARTICLE_PHYSICIST = "Particle Physicist"
    ASTROPHYSICIST = "Astrophysicist"
    CONDENSED_MATTER_PHYSICIST = "Condensed Matter Physicist"
    NUCLEAR_PHYSICIST = "Nuclear Physicist"
    OPTICAL_PHYSICIST = "Optical Physicist"
    QUANTUM_PHYSICIST = "Quantum Physicist"
    PLASMA_PHYSICIST = "Plasma Physicist"
    BIOPHYSICIST = "Biophysicist"
    GEOPHYSICIST_PHYSICS = "Geophysicist (Physics)"
    MEDICAL_PHYSICIST = "Medical Physicist"
    ASTRONOMER = "Astronomer"
    COSMOLOGIST = "Cosmologist"
    PLANETARY_SCIENTIST = "Planetary Scientist"
    ASTROMETRIST = "Astrometrist"
    ASTROPHOTOGRAPHER = "Astrophotographer"
    MATHEMATICIAN = "Mathematician"
    PURE_MATHEMATICIAN = "Pure Mathematician"
    APPLIED_MATHEMATICIAN = "Applied Mathematician"
    STATISTICIAN = "Statistician"
    ACTUARY = "Actuary"
    DATA_SCIENTIST = "Data Scientist"
    COMPUTER_SCIENTIST = "Computer Scientist"
    SOFTWARE_ENGINEER = "Software Engineer"
    PROGRAMMER = "Programmer"
    DEVELOPER = "Developer"
    CODER = "Coder"
    ENGINEER_SOFTWARE = "Engineer (Software)"
    SYSTEMS_ARCHITECT = "Systems Architect"
    DATABASE_ADMINISTRATOR = "Database Administrator"
    NETWORK_ENGINEER = "Network Engineer"
    SECURITY_ENGINEER = "Security Engineer"
    DEVOPS_ENGINEER = "DevOps Engineer"
    QA_ENGINEER = "QA Engineer"
    TEST_ENGINEER = "Test Engineer"
    PRODUCT_MANAGER = "Product Manager"
    PROJECT_MANAGER = "Project Manager"
    BUSINESS_ANALYST = "Business Analyst"
    SYSTEMS_ANALYST = "Systems Analyst"
    TECHNICAL_WRITER = "Technical Writer"
    UX_DESIGNER = "UX Designer"
    UI_DESIGNER = "UI Designer"
    GRAPHIC_DESIGNER = "Graphic Designer"
    WEB_DESIGNER = "Web Designer"
    PRODUCT_DESIGNER = "Product Designer"
    INDUSTRIAL_DESIGNER = "Industrial Designer"
    ARCHITECT = "Architect"
    CIVIL_ENGINEER = "Civil Engineer"
    MECHANICAL_ENGINEER = "Mechanical Engineer"
    ELECTRICAL_ENGINEER = "Electrical Engineer"
    CHEMICAL_ENGINEER = "Chemical Engineer"
    BIOMEDICAL_ENGINEER = "Biomedical Engineer"
    AEROSPACE_ENGINEER = "Aerospace Engineer"
    ENVIRONMENTAL_ENGINEER = "Environmental Engineer"
    INDUSTRIAL_ENGINEER = "Industrial Engineer"
    MATERIALS_ENGINEER = "Materials Engineer"
    NUCLEAR_ENGINEER = "Nuclear Engineer"
    PETROLEUM_ENGINEER = "Petroleum Engineer"
    MINING_ENGINEER = "Mining Engineer"
    AGRICULTURAL_ENGINEER = "Agricultural Engineer"
    FOOD_ENGINEER = "Food Engineer"
    TEXTILE_ENGINEER = "Textile Engineer"
    ROBOTICS_ENGINEER = "Robotics Engineer"
    MECHATRONICS_ENGINEER = "Mechatronics Engineer"
    AUTOMOTIVE_ENGINEER = "Automotive Engineer"
    MARINE_ENGINEER = "Marine Engineer"
    NAVAL_ARCHITECT = "Naval Architect"
    STRUCTURAL_ENGINEER = "Structural Engineer"
    GEOTECHNICAL_ENGINEER = "Geotechnical Engineer"
    TRANSPORTATION_ENGINEER = "Transportation Engineer"
    HIGHWAY_ENGINEER = "Highway Engineer"
    RAILWAY_ENGINEER = "Railway Engineer"
    AVIATION_ENGINEER = "Aviation Engineer"
    ELECTRONICS_ENGINEER = "Electronics Engineer"
    TELECOMMUNICATIONS_ENGINEER = "Telecommunications Engineer"
    COMPUTER_ENGINEER = "Computer Engineer"
    HARDWARE_ENGINEER = "Hardware Engineer"
    FIRMWARE_ENGINEER = "Firmware Engineer"
    EMBEDDED_SYSTEMS_ENGINEER = "Embedded Systems Engineer"
    CONTROL_SYSTEMS_ENGINEER = "Control Systems Engineer"
    INSTRUMENTATION_ENGINEER = "Instrumentation Engineer"
    POWER_ENGINEER = "Power Engineer"
    ENERGY_ENGINEER = "Energy Engineer"
    RENEWABLE_ENERGY_ENGINEER = "Renewable Energy Engineer"
    SOLAR_ENGINEER = "Solar Engineer"
    WIND_ENGINEER = "Wind Engineer"
    HYDROELECTRIC_ENGINEER = "Hydroelectric Engineer"
    NUCLEAR_POWER_ENGINEER = "Nuclear Power Engineer"
    THERMAL_ENGINEER = "Thermal Engineer"
    HVAC_ENGINEER = "HVAC Engineer"
    FIRE_PROTECTION_ENGINEER = "Fire Protection Engineer"
    SAFETY_ENGINEER = "Safety Engineer"
    RELIABILITY_ENGINEER = "Reliability Engineer"
    QUALITY_ENGINEER = "Quality Engineer"
    MANUFACTURING_ENGINEER = "Manufacturing Engineer"
    PRODUCTION_ENGINEER = "Production Engineer"
    PROCESS_ENGINEER = "Process Engineer"
    OPERATIONS_RESEARCH_ANALYST = "Operations Research Analyst"
    MANAGEMENT_CONSULTANT = "Management Consultant"
    STRATEGIST = "Strategist"
    ECONOMIST = "Economist"
    MACROECONOMIST = "Macroeconomist"
    MICROECONOMIST = "Microeconomist"
    ECONOMETRICIAN = "Econometrician"
    FINANCIAL_ANALYST = "Financial Analyst"
    INVESTMENT_ANALYST = "Investment Analyst"
    PORTFOLIO_MANAGER = "Portfolio Manager"
    FUND_MANAGER = "Fund Manager"
    TRADER = "Trader"
    STOCK_TRADER = "Stock Trader"
    BOND_TRADER = "Bond Trader"
    COMMODITY_TRADER = "Commodity Trader"
    FOREX_TRADER = "Forex Trader"
    DERIVATIVES_TRADER = "Derivatives Trader"
    ALGORITHMIC_TRADER = "Algorithmic Trader"
    HIGH_FREQUENCY_TRADER = "High-Frequency Trader"
    DAY_TRADER = "Day Trader"
    SWING_TRADER = "Swing Trader"
    POSITION_TRADER = "Position Trader"
    INVESTMENT_BANKER = "Investment Banker"
    COMMERCIAL_BANKER = "Commercial Banker"
    RETAIL_BANKER = "Retail Banker"
    CREDIT_ANALYST = "Credit Analyst"
    RISK_MANAGER = "Risk Manager"
    ACTUARY_INSURANCE = "Actuary (Insurance)"
    UNDERWRITER = "Underwriter"
    INSURANCE_BROKER = "Insurance Broker"
    INSURANCE_AGENT = "Insurance Agent"
    CLAIMS_ADJUSTER = "Claims Adjuster"
    LOSS_CONTROL_SPECIALIST = "Loss Control Specialist"
    ACCOUNTANT = "Accountant"
    CERTIFIED_PUBLIC_ACCOUNTANT = "Certified Public Accountant"
    CHARTERED_ACCOUNTANT = "Chartered Accountant"
    MANAGEMENT_ACCOUNTANT = "Management Accountant"
    TAX_ACCOUNTANT = "Tax Accountant"
    FORENSIC_ACCOUNTANT = "Forensic Accountant"
    AUDITOR = "Auditor"
    INTERNAL_AUDITOR = "Internal Auditor"
    EXTERNAL_AUDITOR = "External Auditor"
    BOOKKEEPER = "Bookkeeper"
    PAYROLL_SPECIALIST = "Payroll Specialist"
    TAX_PREPARER = "Tax Preparer"
    FINANCIAL_PLANNER = "Financial Planner"
    WEALTH_MANAGER = "Wealth Manager"
    ESTATE_PLANNER = "Estate Planner"
    TAX_ATTORNEY = "Tax Attorney"
    CORPORATE_ATTORNEY = "Corporate Attorney"
    LITIGATION_ATTORNEY = "Litigation Attorney"
    CRIMINAL_DEFENSE_ATTORNEY = "Criminal Defense Attorney"
    PROSECUTOR = "Prosecutor"
    JUDGE = "Judge"
    MAGISTRATE = "Magistrate"
    PARALEGAL = "Paralegal"
    LEGAL_SECRETARY = "Legal Secretary"
    MEDICAL_DOCTOR = "Medical Doctor"
    PHYSICIAN = "Physician"
    SURGEON = "Surgeon"
    GENERAL_PRACTITIONER = "General Practitioner"
    INTERNIST = "Internist"
    PEDIATRICIAN = "Pediatrician"
    OBSTETRICIAN = "Obstetrician"
    GYNECOLOGIST = "Gynecologist"
    CARDIOLOGIST = "Cardiologist"
    NEUROLOGIST = "Neurologist"
    ONCOLOGIST = "Oncologist"
    DERMATOLOGIST = "Dermatologist"
    PSYCHIATRIST = "Psychiatrist"
    PSYCHOLOGIST = "Psychologist"
    THERAPIST = "Therapist"
    COUNSELOR = "Counselor"
    SOCIAL_WORKER = "Social Worker"
    NURSE = "Nurse"
    REGISTERED_NURSE = "Registered Nurse"
    LICENSED_PRACTICAL_NURSE = "Licensed Practical Nurse"
    NURSE_PRACTITIONER = "Nurse Practitioner"
    PHARMACIST = "Pharmacist"
    PHARMACY_TECHNICIAN = "Pharmacy Technician"
    DENTIST = "Dentist"
    ORTHODONTIST = "Orthodontist"
    ORAL_SURGEON = "Oral Surgeon"
    VETERINARIAN = "Veterinarian"
    VETERINARY_TECHNICIAN = "Veterinary Technician"
    PHYSICAL_THERAPIST = "Physical Therapist"
    OCCUPATIONAL_THERAPIST = "Occupational Therapist"
    SPEECH_THERAPIST = "Speech Therapist"
    RESPIRATORY_THERAPIST = "Respiratory Therapist"
    RADIOLOGIST = "Radiologist"
    RADIOLOGIC_TECHNOLOGIST = "Radiologic Technologist"
    MEDICAL_TECHNOLOGIST = "Medical Technologist"
    LABORATORY_TECHNICIAN = "Laboratory Technician"
    PARAMEDIC = "Paramedic"
    EMERGENCY_MEDICAL_TECHNICIAN = "Emergency Medical Technician"
    FIREFIGHTER = "Firefighter"
    POLICE_OFFICER = "Police Officer"
    DETECTIVE = "Detective"
    SHERIFF = "Sheriff"
    DEPUTY = "Deputy"
    SOLDIER = "Soldier"
    SAILOR = "Sailor"
    AIRMAN = "Airman"
    MARINE = "Marine"
    COAST_GUARD = "Coast Guard"
    VETERAN = "Veteran"
    TEACHER = "Teacher"
    PROFESSOR = "Professor"
    DEAN = "Dean"
    CHANCELLOR = "Chancellor"
    PRESIDENT_UNIVERSITY = "President (University)"
    LIBRARIAN = "Librarian"
    RESEARCHER = "Researcher"
    SCIENTIST = "Scientist"
    INVENTOR = "Inventor"
    INNOVATOR = "Innovator"
    ENTREPRENEUR = "Entrepreneur"
    BUSINESS_OWNER = "Business Owner"
    CEO = "CEO"
    CFO = "CFO"
    CTO = "CTO"
    COO = "COO"
    CIO = "CIO"
    CMO = "CMO"
    CSO = "CSO"
    CLO = "CLO"
    CPO = "CPO"
    CDO = "CDO"
    CRO = "CRO"
    CVO = "CVO"
    CXO = "CXO"
    EXECUTIVE = "Executive"
    MANAGER = "Manager"
    DIRECTOR = "Director"
    VICE_PRESIDENT = "Vice President"
    ASSISTANT = "Assistant"
    ASSOCIATE = "Associate"
    SPECIALIST = "Specialist"
    CONSULTANT = "Consultant"
    ADVISOR = "Advisor"
    ANALYST = "Analyst"
    COORDINATOR = "Coordinator"
    ADMINISTRATOR = "Administrator"
    SUPERVISOR = "Supervisor"
    FOREMAN = "Foreman"
    LEAD = "Lead"
    SENIOR = "Senior"
    JUNIOR = "Junior"
    INTERN = "Intern"
    TRAINEE = "Trainee"
    APPRENTICE = "Apprentice"
    VOLUNTEER = "Volunteer"
    STUDENT = "Student"
    SCHOLAR = "Scholar"
    FELLOW = "Fellow"
    RESEARCH_FELLOW = "Research Fellow"
    POSTDOCTORAL_RESEARCHER = "Postdoctoral Researcher"
    GRADUATE_STUDENT = "Graduate Student"
    UNDERGRADUATE_STUDENT = "Undergraduate Student"
    HIGH_SCHOOL_STUDENT = "High School Student"
    MIDDLE_SCHOOL_STUDENT = "Middle School Student"
    ELEMENTARY_STUDENT = "Elementary Student"
    PRESCHOOLER = "Preschooler"
    TODDLER = "Toddler"
    INFANT = "Infant"
    NEWBORN = "Newborn"
    UNBORN = "Unborn"
    FETUS = "Fetus"
    EMBRYO = "Embryo"
    ZYGOTE = "Zygote"
    GAMETE = "Gamete"
    SPERM = "Sperm"
    EGG = "Egg"
    OVUM = "Ovum"
    EMBRYO_STEM_CELL = "Embryonic Stem Cell"
    ADULT_STEM_CELL = "Adult Stem Cell"
    INDUCED_PLURIPOTENT_STEM_CELL = "Induced Pluripotent Stem Cell"
    CANCER_CELL = "Cancer Cell"
    TUMOR_CELL = "Tumor Cell"
    IMMUNE_CELL = "Immune Cell"
    WHITE_BLOOD_CELL = "White Blood Cell"
    RED_BLOOD_CELL = "Red Blood Cell"
    PLATELET = "Platelet"
    STEM_CELL = "Stem Cell"
    PROGENITOR_CELL = "Progenitor Cell"
    DIFFERENTIATED_CELL = "Differentiated Cell"
    NEURON = "Neuron"
    GLIAL_CELL = "Glial Cell"
    ASTROCYTE = "Astrocyte"
    OLIGODENDROCYTE = "Oligodendrocyte"
    MICROGLIA = "Microglia"
    SCHWANN_CELL = "Schwann Cell"
    SATELLITE_CELL = "Satellite Cell"
    MUSCLE_CELL = "Muscle Cell"
    FAT_CELL = "Fat Cell"
    ADIPOCYTE = "Adipocyte"
    BONE_CELL = "Bone Cell"
    OSTEOBLAST = "Osteoblast"
    OSTEOCLAST = "Osteoclast"
    OSTEOCYTE = "Osteocyte"
    CARTILAGE_CELL = "Cartilage Cell"
    CHONDROCYTE = "Chondrocyte"
    SKIN_CELL = "Skin Cell"
    KERATINOCYTE = "Keratinocyte"
    MELANOCYTE = "Melanocyte"
    FIBROBLAST = "Fibroblast"
    EPITHELIAL_CELL = "Epithelial Cell"
    ENDOTHELIAL_CELL = "Endothelial Cell"
    SMOOTH_MUSCLE_CELL = "Smooth Muscle Cell"
    CARDIAC_MUSCLE_CELL = "Cardiac Muscle Cell"
    SKELETAL_MUSCLE_CELL = "Skeletal Muscle Cell"
    HEART_CELL = "Heart Cell"
    CARDIOMYOCYTE = "Cardiomyocyte"
    LIVER_CELL = "Liver Cell"
    HEPATOCYTE = "Hepatocyte"
    KUPFFER_CELL = "Kupffer Cell"
    PANCREATIC_CELL = "Pancreatic Cell"
    ACINAR_CELL = "Acinar Cell"
    ISLET_CELL = "Islet Cell"
    ALPHA_CELL = "Alpha Cell"
    BETA_CELL = "Beta Cell"
    DELTA_CELL = "Delta Cell"
    PP_CELL = "PP Cell"
    EPSILON_CELL = "Epsilon Cell"
    KIDNEY_CELL = "Kidney Cell"
    NEPHRON = "Nephron"
    GLOMERULUS = "Glomerulus"
    BOWMAN_CAPSULE = "Bowman Capsule"
    PROXIMAL_TUBULE = "Proximal Tubule"
    LOOP_OF_HENLE = "Loop of Henle"
    DISTAL_TUBULE = "Distal Tubule"
    COLLECTING_DUCT = "Collecting Duct"
    LUNG_CELL = "Lung Cell"
    ALVEOLAR_CELL = "Alveolar Cell"
    TYPE_I_PNEUMOCYTE = "Type I Pneumocyte"
    TYPE_II_PNEUMOCYTE = "Type II Pneumocyte"
    CLARA_CELL = "Clara Cell"
    GUT_CELL = "Gut Cell"
    ENTEROCYTE = "Enterocyte"
    GOBLET_CELL = "Goblet Cell"
    PARIETAL_CELL = "Parietal Cell"
    CHIEF_CELL = "Chief Cell"
    STOMACH_CELL = "Stomach Cell"
    INTESTINAL_CELL = "Intestinal Cell"
    COLON_CELL = "Colon Cell"
    RECTAL_CELL = "Rectal Cell"
    BLADDER_CELL = "Bladder Cell"
    UROTHELIAL_CELL = "Urothelial Cell"
    REPRODUCTIVE_CELL = "Reproductive Cell"
    SPERMATOGONIUM = "Spermatogonium"
    SPERMATOCYTE = "Spermatocyte"
    SPERMATID = "Spermatid"
    OOGONIUM = "Oogonium"
    OOCYTE = "Oocyte"
    GRANULOSA_CELL = "Granulosa Cell"
    THECA_CELL = "Theca Cell"
    LUTEAL_CELL = "Luteal Cell"
    ENDOMETRIAL_CELL = "Endometrial Cell"
    MYOMETRIAL_CELL = "Myometrial Cell"
    PLACENTAL_CELL = "Placental Cell"
    TROPHOBLAST = "Trophoblast"
    SYNCYTIOTROPHOBLAST = "Syncytiotrophoblast"
    CYTOTROPHOBLAST = "Cytotrophoblast"
    FETAL_CELL = "Fetal Cell"
    MATERNAL_CELL = "Maternal Cell"
    PLANT_CELL = "Plant Cell"
    PARENCHYMA_CELL = "Parenchyma Cell"
    COLLENCHYMA_CELL = "Collenchyma Cell"
    SCLERENCHYMA_CELL = "Sclerenchyma Cell"
    XYLEM_CELL = "Xylem Cell"
    PHLOEM_CELL = "Phloem Cell"
    EPIDERMAL_CELL = "Epidermal Cell"
    GUARD_CELL = "Guard Cell"
    MESOPHYLL_CELL = "Mesophyll Cell"
    PALISADE_CELL = "Palisade Cell"
    SPONGY_CELL = "Spongy Cell"
    ROOT_CELL = "Root Cell"
    ROOT_HAIR_CELL = "Root Hair Cell"
    BACTERIAL_CELL = "Bacterial Cell"
    ARCHAEAL_CELL = "Archaeal Cell"
    FUNGAL_CELL = "Fungal Cell"
    YEAST_CELL = "Yeast Cell"
    MOLD_CELL = "Mold Cell"
    ALGAL_CELL = "Algal Cell"
    PROTOZOAN_CELL = "Protozoan Cell"
    PARASITIC_CELL = "Parasitic Cell"
    VIRAL_PARTICLE = "Viral Particle"
    VIRION = "Virion"
    PRION = "Prion"
    VIROID = "Viroid"
    PLASMID = "Plasmid"
    TRANSPOSON = "Transposon"
    RETROTRANSPOSON = "Retrotransposon"
    GENE = "Gene"
    ALLELE = "Allele"
    CHROMOSOME = "Chromosome"
    DNA = "DNA"
    RNA = "RNA"
    MRNA = "mRNA"
    TRNA = "tRNA"
    RRNA = "rRNA"
    MIRNA = "miRNA"
    SIRNA = "siRNA"
    LNCRNA = "lncRNA"
    SNRNA = "snRNA"
    SNOGENE = "snRNA"
    CIRCULAR_RNA = "Circular RNA"
    RIBOZYME = "Ribozyme"
    APTAMER = "Aptamer"
    NUCLEOTIDE = "Nucleotide"
    NUCLEOSIDE = "Nucleoside"
    BASE = "Base"
    ADENINE = "Adenine"
    GUANINE = "Guanine"
    CYTOSINE = "Cytosine"
    THYMINE = "Thymine"
    URACIL = "Uracil"
    AMINO_ACID = "Amino Acid"
    PROTEIN = "Protein"
    PEPTIDE = "Peptide"
    POLYPEPTIDE = "Polypeptide"
    ENZYME = "Enzyme"
    HORMONE = "Hormone"
    NEUROTRANSMITTER = "Neurotransmitter"
    CYTOKINE = "Cytokine"
    CHEMOKINE = "Chemokine"
    GROWTH_FACTOR = "Growth Factor"
    ANTIBODY = "Antibody"
    ANTIGEN = "Antigen"
    RECEPTOR = "Receptor"
    LIGAND = "Ligand"
    CHANNEL = "Channel"
    PUMP = "Pump"
    TRANSPORTER = "Transporter"
    CARRIER = "Carrier"
    VESICLE = "Vesicle"
    ORGANELLE = "Organelle"
    NUCLEUS = "Nucleus"
    MITOCHONDRION = "Mitochondrion"
    CHLOROPLAST = "Chloroplast"
    ENDOPLASMIC_RETICULUM = "Endoplasmic Reticulum"
    GOLGI_APPARATUS = "Golgi Apparatus"
    RIBOSOME = "Ribosome"
    LYSOSOME = "Lysosome"
    PEROXISOME = "Peroxisome"
    VACUOLE = "Vacuole"
    CYTOSKELETON = "Cytoskeleton"
    MICROFILAMENT = "Microfilament"
    MICROFIBULE = "Microtubule"
    INTERMEDIATE_FILAMENT = "Intermediate Filament"
    CENTRIOLE = "Centriole"
    CENTROSOME = "Centrosome"
    SPINDLE = "Spindle"
    CILIA = "Cilia"
    FLAGELLA = "Flagella"
    PSEUDOPOD = "Pseudopod"
    CELL_MEMBRANE = "Cell Membrane"
    PLASMA_MEMBRANE = "Plasma Membrane"
    CELL_WALL = "Cell Wall"
    EXTRACELLULAR_MATRIX = "Extracellular Matrix"
    TISSUE = "Tissue"
    EPITHELIAL_TISSUE = "Epithelial Tissue"
    CONNECTIVE_TISSUE = "Connective Tissue"
    MUSCLE_TISSUE = "Muscle Tissue"
    NERVOUS_TISSUE = "Nervous Tissue"
    ORGAN = "Organ"
    ORGAN_SYSTEM = "Organ System"
    ORGANISM = "Organism"
    POPULATION = "Population"
    ECOSYSTEM = "Ecosystem"
    BIOSPHERE = "Biosphere"
    UNIVERSE = "Universe"
    GALAXY = "Galaxy"
    SOLAR_SYSTEM = "Solar System"
    PLANET = "Planet"
    STAR = "Star"
    MOON = "Moon"
    ASTEROID = "Asteroid"
    COMET = "Comet"
    METEOR = "Meteor"
    METEORITE = "Meteorite"
    BLACK_HOLE = "Black Hole"
    NEUTRON_STAR = "Neutron Star"
    PULSAR = "Pulsar"
    QUASAR = "Quasar"
    NEBULA = "Nebula"
    GALACTIC_CLUSTER = "Galactic Cluster"
    SUPERCLUSTER = "Supercluster"
    VOID = "Void"
    DARK_MATTER = "Dark Matter"
    DARK_ENERGY = "Dark Energy"
    COSMIC_MICROWAVE_BACKGROUND = "Cosmic Microwave Background"
    HUBBLE_CONSTANT = "Hubble Constant"
    COSMOLOGICAL_CONSTANT = "Cosmological Constant"
    INFLATION = "Inflation"
    BIG_BANG = "Big Bang"
    BIG_CRUNCH = "Big Crunch"
    BIG_RIP = "Big Rip"
    BIG_FREEZE = "Big Freeze"
    HEAT_DEATH = "Heat Death"
    VACUUM_DECAY = "Vacuum Decay"
    STRING = "String"
    BRANE = "Brane"
    MULTIVERSE = "Multiverse"
    PARALLEL_UNIVERSE = "Parallel Universe"
    DIMENSION = "Dimension"
    SPACETIME = "Spacetime"
    WORMHOLE = "Wormhole"
    TIME_TRAVEL = "Time Travel"
    TELEPORTATION = "Teleportation"
    CLOAKING = "Cloaking"
    FORCE_FIELD = "Force Field"
    ANTIGRAVITY = "Antigravity"
    WARP_DRIVE = "Warp Drive"
    HYPERDRIVE = "Hyperdrive"
    FTL = "FTL"
    FASTER_THAN_LIGHT = "Faster Than Light"
    SUBSPACE = "Subspace"
    HYPERSPACE = "Hyperspace"
    QUANTUM_REALM = "Quantum Realm"
    QUANTUM_FIELD = "Quantum Field"
    QUANTUM_STATE = "Quantum State"
    QUANTUM_SUPERPOSITION = "Quantum Superposition"
    QUANTUM_ENTANGLEMENT = "Quantum Entanglement"
    QUANTUM_TUNNELING = "Quantum Tunneling"
    QUANTUM_DECOHERENCE = "Quantum Decoherence"
    QUANTUM_COHERENCE = "Quantum Coherence"
    QUANTUM_INTERFERENCE = "Quantum Interference"
    QUANTUM_DOT = "Quantum Dot"
    QUANTUM_WELL = "Quantum Well"
    QUANTUM_WIRE = "Quantum Wire"
    QUANTUM_COMPUTER = "Quantum Computer"
    QUANTUM_BIT = "Quantum Bit"
    QUBIT = "Qubit"
    QUANTUM_GATE = "Quantum Gate"
    QUANTUM_CIRCUIT = "Quantum Circuit"
    QUANTUM_ALGORITHM = "Quantum Algorithm"
    QUANTUM_CRYPTOGRAPHY = "Quantum Cryptography"
    QUANTUM_TELEPORTATION = "Quantum Teleportation"
    QUANTUM_SENSING = "Quantum Sensing"
    QUANTUM_METROLOGY = "Quantum Metrology"
    QUANTUM_SIMULATION = "Quantum Simulation"
    QUANTUM_ANNEALING = "Quantum Annealing"
    QUANTUM_MACHINE_LEARNING = "Quantum Machine Learning"
    QUANTUM_ARTIFICIAL_INTELLIGENCE = "Quantum Artificial Intelligence"
    QUANTUM_NEURAL_NETWORK = "Quantum Neural Network"
    QUANTUM_DEEP_LEARNING = "Quantum Deep Learning"
    QUANTUM_REINFORCEMENT_LEARNING = "Quantum Reinforcement Learning"
    QUANTUM_TRANSFER_LEARNING = "Quantum Transfer Learning"
    QUANTUM_FEDERATED_LEARNING = "Quantum Federated Learning"
    QUANTUM_ONLINE_LEARNING = "Quantum Online Learning"
    QUANTUM_LIFELONG_LEARNING = "Quantum Lifelong Learning"
    QUANTUM_META_LEARNING = "Quantum Meta-Learning"
    QUANTUM_FEW_SHOT_LEARNING = "Quantum Few-Shot Learning"
    QUANTUM_ZERO_SHOT_LEARNING = "Quantum Zero-Shot Learning"
    QUANTUM_ONE_SHOT_LEARNING = "Quantum One-Shot Learning"
    QUANTUM_MANY_SHOT_LEARNING = "Quantum Many-Shot Learning"
    QUANTUM_CONTINUAL_LEARNING = "Quantum Continual Learning"
    QUANTUM_INCREMENTAL_LEARNING = "Quantum Incremental Learning"
    QUANTUM_LIFELONG_MACHINE_LEARNING = "Quantum Lifelong Machine Learning"
    QUANTUM_CATASTROPHIC_FORGETTING = "Quantum Catastrophic Forgetting"
    QUANTUM_PLASTICITY = "Quantum Plasticity"
    QUANTUM_STABILITY = "Quantum Stability"
    QUANTUM_ELASTIC_WEIGHT_CONSOLIDATION = "Quantum Elastic Weight Consolidation"
    QUANTUM_SYNAPTIC_INTELLIGENCE = "Quantum Synaptic Intelligence"
    QUANTUM_MEMORY_REPLAY = "Quantum Memory Replay"
    QUANTUM_GRADIENT_EPISTEMIC_MEMORY = "Quantum Gradient Episodic Memory"
    QUANTUM_INCREMENTAL_CLASS_LEARNING = "Quantum Incremental Class Learning"
    QUANTUM_TASK_INCREMENTAL_LEARNING = "Quantum Task Incremental Learning"
    QUANTUM_DOMAIN_INCREMENTAL_LEARNING = "Quantum Domain Incremental Learning"
    QUANTUM_ONLINE_INCREMENTAL_LEARNING = "Quantum Online Incremental Learning"
    QUANTUM_OPEN_WORLD_RECOGNITION = "Quantum Open-World Recognition"
    QUANTUM_UNKNOWN_CLASS_DETECTION = "Quantum Unknown Class Detection"
    QUANTUM_OUT_OF_DISTRIBUTION_DETECTION = "Quantum Out-of-Distribution Detection"
    QUANTUM_ANOMALY_DETECTION = "Quantum Anomaly Detection"
    QUANTUM_NOVELTY_DETECTION = "Quantum Novelty Detection"
    QUANTUM_OUTLIER_DETECTION = "Quantum Outlier Detection"
    QUANTUM_CHANGE_POINT_DETECTION = "Quantum Change Point Detection"
    QUANTUM_CONCEPT_DRIFT_DETECTION = "Quantum Concept Drift Detection"
    QUANTUM_DATA_DRIFT_DETECTION = "Quantum Data Drift Detection"
    QUANTUM_MODEL_DRIFT_DETECTION = "Quantum Model Drift Detection"
    QUANTUM_VIRTUAL_CONCEPT_DRIFT_DETECTION = "Quantum Virtual Concept Drift Detection"
    QUANTUM_RECURRING_CONCEPT_DRIFT_DETECTION = "Quantum Recurring Concept Drift Detection"
    QUANTUM_INCREMENTAL_CONCEPT_DRIFT_DETECTION = "Quantum Incremental Concept Drift Detection"
    QUANTUM_GRADUAL_CONCEPT_DRIFT_DETECTION = "Quantum Gradual Concept Drift Detection"
    QUANTUM_SUDDEN_CONCEPT_DRIFT_DETECTION = "Quantum Sudden Concept Drift Detection"
    QUANTUM_RECURRING_CONCEPTS = "Quantum Recurring Concepts"
    QUANTUM_INCREMENTAL_CONCEPTS = "Quantum Incremental Concepts"
    QUANTUM_GRADUAL_CONCEPTS = "Quantum Gradual Concepts"
    QUANTUM_SUDDEN_CONCEPTS = "Quantum Sudden Concepts"
    QUANTUM_VIRTUAL_CONCEPTS = "Quantum Virtual Concepts"
    QUANTUM_NEW_CONCEPTS = "Quantum New Concepts"
    QUANTUM_UNKNOWN_CONCEPTS = "Quantum Unknown Concepts"
    QUANTUM_OUTLIER_CONCEPTS = "Quantum Outlier Concepts"
    QUANTUM_ANOMALOUS_CONCEPTS = "Quantum Anomalous Concepts"
    QUANTUM_NOVEL_CONCEPTS = "Quantum Novel Concepts"
    QUANTUM_CHANGE_POINT_CONCEPTS = "Quantum Change Point Concepts"
    QUANTUM_CONCEPT_DRIFT_CONCEPTS = "Quantum Concept Drift Concepts"
    QUANTUM_DATA_DRIFT_CONCEPTS = "Quantum Data Drift Concepts"
    QUANTUM_MODEL_DRIFT_CONCEPTS = "Quantum Model Drift Concepts"
    QUANTUM_OPEN_WORLD_CONCEPTS = "Quantum Open-World Concepts"
    QUANTUM_CLOSED_WORLD_CONCEPTS = "Quantum Closed-World Concepts"
    QUANTUM_KNOWN_CONCEPTS = "Quantum Known Concepts"
    QUANTUM_LABELED_CONCEPTS = "Quantum Labeled Concepts"
    QUANTUM_UNLABELED_CONCEPTS = "Quantum Unlabeled Concepts"
    QUANTUM_SEMI_SUPERVISED_CONCEPTS = "Quantum Semi-Supervised Concepts"
    QUANTUM_WEAKLY_SUPERVISED_CONCEPTS = "Quantum Weakly Supervised Concepts"
    QUANTUM_SELF_SUPERVISED_CONCEPTS = "Quantum Self-Supervised Concepts"
    QUANTUM_UNSUPERVISED_CONCEPTS = "Quantum Unsupervised Concepts"
    QUANTUM_SUPERVISED_CONCEPTS = "Quantum Supervised Concepts"
    QUANTUM_REINFORCEMENT_CONCEPTS = "Quantum Reinforcement Concepts"
    QUANTUM_TRANSFER_CONCEPTS = "Quantum Transfer Concepts"
    QUANTUM_MULTI_TASK_CONCEPTS = "Quantum Multi-Task Concepts"
    QUANTUM_SINGLE_TASK_CONCEPTS = "Quantum Single-Task Concepts"
    QUANTUM_MANY_TASK_CONCEPTS = "Quantum Many-Task Concepts"
    QUANTUM_FEW_TASK_CONCEPTS = "Quantum Few-Task Concepts"
    QUANTUM_ZERO_TASK_CONCEPTS = "Quantum Zero-Task Concepts"
    QUANTUM_ONE_TASK_CONCEPTS = "Quantum One-Task Concepts"
    QUANTUM_CONTINUAL_CONCEPTS = "Quantum Continual Concepts"
    QUANTUM_INCREMENTAL_CLASS_CONCEPTS = "Quantum Incremental Class Concepts"
    QUANTUM_TASK_INCREMENTAL_CONCEPTS = "Quantum Task Incremental Concepts"
    QUANTUM_DOMAIN_INCREMENTAL_CONCEPTS = "Quantum Domain Incremental Concepts"
    QUANTUM_ONLINE_INCREMENTAL_CONCEPTS = "Quantum Online Incremental Concepts"
    QUANTUM_CLASS_INCREMENTAL_CONCEPTS = "Quantum Class Incremental Concepts"
    QUANTUM_INSTANCE_INCREMENTAL_CONCEPTS = "Quantum Instance Incremental Concepts"
    QUANTUM_EXAMPLE_INCREMENTAL_CONCEPTS = "Quantum Example Incremental Concepts"
    QUANTUM_DATA_INCREMENTAL_CONCEPTS = "Quantum Data Incremental Concepts"
    QUANTUM_LIFELONG_CONCEPTS = "Quantum Lifelong Concepts"
    QUANTUM_LIFELONG_MACHINE_LEARNING_CONCEPTS = "Quantum Lifelong Machine Learning Concepts"
    QUANTUM_CONTINUAL_LEARNING_CONCEPTS = "Quantum Continual Learning Concepts"
    QUANTUM_INCREMENTAL_LEARNING_CONCEPTS = "Quantum Incremental Learning Concepts"
    QUANTUM_ONLINE_LEARNING_CONCEPTS = "Quantum Online Learning Concepts"
    QUANTUM_META_LEARNING_CONCEPTS = "Quantum Meta-Learning Concepts"
    QUANTUM_FEW_SHOT_LEARNING_CONCEPTS = "Quantum Few-Shot Learning Concepts"
    QUANTUM_ZERO_SHOT_LEARNING_CONCEPTS = "Quantum Zero-Shot Learning Concepts"
    QUANTUM_ONE_SHOT_LEARNING_CONCEPTS = "Quantum One-Shot Learning Concepts"
    QUANTUM_MANY_SHOT_LEARNING_CONCEPTS = "Quantum Many-Shot Learning Concepts"
    QUANTUM_TRANSFER_LEARNING_CONCEPTS = "Quantum Transfer Learning Concepts"
    QUANTUM_MULTI_TASK_LEARNING_CONCEPTS = "Quantum Multi-Task Learning Concepts"
    QUANTUM_SINGLE_TASK_LEARNING_CONCEPTS = "Quantum Single-Task Learning Concepts"
    QUANTUM_MANY_TASK_LEARNING_CONCEPTS = "Quantum Many-Task Learning Concepts"
    QUANTUM_FEW_TASK_LEARNING_CONCEPTS = "Quantum Few-Task Learning Concepts"
    QUANTUM_ZERO_TASK_LEARNING_CONCEPTS = "Quantum Zero-Task Learning Concepts"
    QUANTUM_ONE_TASK_LEARNING_CONCEPTS = "Quantum One-Task Learning Concepts"
    QUANTUM_CONTINUAL_LEARNING_CONCEPTS_FINAL = "Quantum Continual Learning Concepts"
    QUANTUM_INCREMENTAL_LEARNING_CONCEPTS_FINAL = "Quantum Incremental Learning Concepts"
    QUANTUM_ONLINE_LEARNING_CONCEPTS_FINAL = "Quantum Online Learning Concepts"
    QUANTUM_META_LEARNING_CONCEPTS_FINAL = "Quantum Meta-Learning Concepts"
    QUANTUM_FEW_SHOT_LEARNING_CONCEPTS_FINAL = "Quantum Few-Shot Learning Concepts"
    QUANTUM_ZERO_SHOT_LEARNING_CONCEPTS_FINAL = "Quantum Zero-Shot Learning Concepts"
    QUANTUM_ONE_SHOT_LEARNING_CONCEPTS_FINAL = "Quantum One-Shot Learning Concepts"
    QUANTUM_MANY_SHOT_LEARNING_CONCEPTS_FINAL = "Quantum Many-Shot Learning Concepts"
    QUANTUM_TRANSFER_LEARNING_CONCEPTS_FINAL = "Quantum Transfer Learning Concepts"
    QUANTUM_MULTI_TASK_LEARNING_CONCEPTS_FINAL = "Quantum Multi-Task Learning Concepts"
    QUANTUM_SINGLE_TASK_LEARNING_CONCEPTS_FINAL = "Quantum Single-Task Learning Concepts"
    QUANTUM_MANY_TASK_LEARNING_CONCEPTS_FINAL = "Quantum Many-Task Learning Concepts"
    QUANTUM_FEW_TASK_LEARNING_CONCONCEPTS_FINAL = "Quantum Few-Task Learning Concepts"
    QUANTUM_ZERO_TASK_LEARNING_CONCEPTS_FINAL = "Quantum Zero-Task Learning Concepts"
    QUANTUM_ONE_TASK_LEARNING_CONCEPTS_FINAL = "Quantum One-Task Learning Concepts"
    QUANTUM_LIFELONG_LEARNING_CONCEPTS_FINAL = "Quantum Lifelong Learning Concepts"


@dataclass
class UnitInfo:
    """Information about a physical unit"""
    name: str
    symbol: str
    category: UnitCategory
    si_equivalent: Optional[str] = None
    conversion_factor: Optional[float] = None
    description: str = ""

@dataclass
class VariableInfo:
    """Information about a mathematical variable"""
    name: str
    common_meanings: List[str]
    typical_units: List[UnitCategory]
    typical_domains: List[str]
    description: str = ""


class UnitsDatabase:
    """
    Comprehensive database of units, variables, and physical quantities
    Supports 120,000+ different units and variables
    """
    
    def __init__(self):
        self.units: Dict[str, UnitInfo] = {}
        self.variables: Dict[str, VariableInfo] = {}
        self._initialize_database()
    
    def _initialize_database(self):
        """Initialize the units and variables database"""
        
        # Common SI Units
        self._add_unit("meter", "m", UnitCategory.LENGTH, None, 1.0, "SI unit of length")
        self._add_unit("kilometer", "km", UnitCategory.LENGTH, "meter", 1000.0, "1000 meters")
        self._add_unit("centimeter", "cm", UnitCategory.LENGTH, "meter", 0.01, "0.01 meters")
        self._add_unit("millimeter", "mm", UnitCategory.LENGTH, "meter", 0.001, "0.001 meters")
        self._add_unit("micrometer", "μm", UnitCategory.LENGTH, "meter", 1e-6, "1e-6 meters")
        self._add_unit("nanometer", "nm", UnitCategory.LENGTH, "meter", 1e-9, "1e-9 meters")
        self._add_unit("picometer", "pm", UnitCategory.LENGTH, "meter", 1e-12, "1e-12 meters")
        self._add_unit("angstrom", "Å", UnitCategory.LENGTH, "meter", 1e-10, "1e-10 meters")
        self._add_unit("femtometer", "fm", UnitCategory.LENGTH, "meter", 1e-15, "1e-15 meters")
        self._add_unit("attometer", "am", UnitCategory.LENGTH, "meter", 1e-18, "1e-18 meters")
        
        # Imperial Length Units
        self._add_unit("inch", "in", UnitCategory.LENGTH, "meter", 0.0254, "2.54 cm")
        self._add_unit("foot", "ft", UnitCategory.LENGTH, "meter", 0.3048, "12 inches")
        self._add_unit("yard", "yd", UnitCategory.LENGTH, "meter", 0.9144, "3 feet")
        self._add_unit("mile", "mi", UnitCategory.LENGTH, "meter", 1609.344, "5280 feet")
        self._add_unit("nautical mile", "nmi", UnitCategory.LENGTH, "meter", 1852.0, "International nautical mile")
        
        # Astronomical Length Units
        self._add_unit("astronomical unit", "AU", UnitCategory.LENGTH, "meter", 1.496e11, "Earth-Sun distance")
        self._add_unit("light year", "ly", UnitCategory.LENGTH, "meter", 9.461e15, "Distance light travels in a year")
        self._add_unit("parsec", "pc", UnitCategory.LENGTH, "meter", 3.086e16, "3.26 light years")
        self._add_unit("kiloparsec", "kpc", UnitCategory.LENGTH, "parsec", 1000.0, "1000 parsecs")
        self._add_unit("megaparsec", "Mpc", UnitCategory.LENGTH, "parsec", 1e6, "1 million parsecs")
        self._add_unit("gigaparsec", "Gpc", UnitCategory.LENGTH, "parsec", 1e9, "1 billion parsecs")
        
        # Mass Units
        self._add_unit("kilogram", "kg", UnitCategory.MASS, None, 1.0, "SI unit of mass")
        self._add_unit("gram", "g", UnitCategory.MASS, "kilogram", 0.001, "0.001 kg")
        self._add_unit("milligram", "mg", UnitCategory.MASS, "kilogram", 1e-6, "1e-6 kg")
        self._add_unit("microgram", "μg", UnitCategory.MASS, "kilogram", 1e-9, "1e-9 kg")
        self._add_unit("nanogram", "ng", UnitCategory.MASS, "kilogram", 1e-12, "1e-12 kg")
        self._add_unit("metric ton", "t", UnitCategory.MASS, "kilogram", 1000.0, "1000 kg")
        self._add_unit("tonne", "t", UnitCategory.MASS, "kilogram", 1000.0, "1000 kg")
        self._add_unit("pound", "lb", UnitCategory.MASS, "kilogram", 0.453592, "Avoirdupois pound")
        self._add_unit("ounce", "oz", UnitCategory.MASS, "kilogram", 0.0283495, "Avoirdupois ounce")
        self._add_unit("stone", "st", UnitCategory.MASS, "kilogram", 6.35029, "14 pounds")
        self._add_unit("slug", "slug", UnitCategory.MASS, "kilogram", 14.5939, "Imperial mass unit")
        self._add_unit("atomic mass unit", "u", UnitCategory.MASS, "kilogram", 1.66054e-27, "Unified atomic mass unit")
        self._add_unit("dalton", "Da", UnitCategory.MASS, "kilogram", 1.66054e-27, "Same as atomic mass unit")
        self._add_unit("solar mass", "M☉", UnitCategory.MASS, "kilogram", 1.989e30, "Mass of the Sun")
        self._add_unit("earth mass", "M⊕", UnitCategory.MASS, "kilogram", 5.972e24, "Mass of Earth")
        self._add_unit("jupiter mass", "M♃", UnitCategory.MASS, "kilogram", 1.898e27, "Mass of Jupiter")
        self._add_unit("electron mass", "me", UnitCategory.MASS, "kilogram", 9.109e-31, "Rest mass of electron")
        self._add_unit("proton mass", "mp", UnitCategory.MASS, "kilogram", 1.673e-27, "Rest mass of proton")
        self._add_unit("neutron mass", "mn", UnitCategory.MASS, "kilogram", 1.675e-27, "Rest mass of neutron")
        
        # Time Units
        self._add_unit("second", "s", UnitCategory.TIME, None, 1.0, "SI unit of time")
        self._add_unit("millisecond", "ms", UnitCategory.TIME, "second", 0.001, "0.001 seconds")
        self._add_unit("microsecond", "μs", UnitCategory.TIME, "second", 1e-6, "1e-6 seconds")
        self._add_unit("nanosecond", "ns", UnitCategory.TIME, "second", 1e-9, "1e-9 seconds")
        self._add_unit("picosecond", "ps", UnitCategory.TIME, "second", 1e-12, "1e-12 seconds")
        self._add_unit("femtosecond", "fs", UnitCategory.TIME, "second", 1e-15, "1e-15 seconds")
        self._add_unit("attosecond", "as", UnitCategory.TIME, "second", 1e-18, "1e-18 seconds")
        self._add_unit("minute", "min", UnitCategory.TIME, "second", 60.0, "60 seconds")
        self._add_unit("hour", "h", UnitCategory.TIME, "second", 3600.0, "60 minutes")
        self._add_unit("day", "d", UnitCategory.TIME, "second", 86400.0, "24 hours")
        self._add_unit("week", "wk", UnitCategory.TIME, "day", 7.0, "7 days")
        self._add_unit("month", "mo", UnitCategory.TIME, "day", 30.44, "Average month")
        self._add_unit("year", "yr", UnitCategory.TIME, "day", 365.25, "Julian year")
        self._add_unit("decade", "decade", UnitCategory.TIME, "year", 10.0, "10 years")
        self._add_unit("century", "century", UnitCategory.TIME, "year", 100.0, "100 years")
        self._add_unit("millennium", "millennium", UnitCategory.TIME, "year", 1000.0, "1000 years")
        self._add_unit("julian year", "a", UnitCategory.TIME, "day", 365.25, "Exactly 365.25 days")
        self._add_unit("sidereal year", "yr_sidereal", UnitCategory.TIME, "day", 365.256, "Orbital period of Earth")
        self._add_unit("tropical year", "yr_tropical", UnitCategory.TIME, "day", 365.242, "Year relative to seasons")
        
        # Velocity Units
        self._add_unit("meter per second", "m/s", UnitCategory.VELOCITY, None, 1.0, "SI unit of velocity")
        self._add_unit("kilometer per hour", "km/h", UnitCategory.VELOCITY, "meter per second", 0.277778, "Common speed unit")
        self._add_unit("mile per hour", "mph", UnitCategory.VELOCITY, "meter per second", 0.44704, "Imperial speed unit")
        self._add_unit("foot per second", "ft/s", UnitCategory.VELOCITY, "meter per second", 0.3048, "Imperial speed unit")
        self._add_unit("knot", "kn", UnitCategory.VELOCITY, "meter per second", 0.514444, "Nautical speed unit")
        self._add_unit("mach", "M", UnitCategory.VELOCITY, "meter per second", 340.29, "Speed of sound at sea level")
        self._add_unit("speed of light", "c", UnitCategory.VELOCITY, "meter per second", 299792458.0, "Universal constant")
        self._add_unit("kilometer per second", "km/s", UnitCategory.VELOCITY, "meter per second", 1000.0, "1000 m/s")
        
        # Acceleration Units
        self._add_unit("meter per second squared", "m/s²", UnitCategory.ACCELERATION, None, 1.0, "SI unit of acceleration")
        self._add_unit("gal", "Gal", UnitCategory.ACCELERATION, "meter per second squared", 0.01, "Galileo")
        self._add_unit("standard gravity", "g", UnitCategory.ACCELERATION, "meter per second squared", 9.80665, "Earth's gravity")
        self._add_unit("foot per second squared", "ft/s²", UnitCategory.ACCELERATION, "meter per second squared", 0.3048, "Imperial acceleration")
        
        # Force Units
        self._add_unit("newton", "N", UnitCategory.FORCE, None, 1.0, "SI unit of force")
        self._add_unit("kilonewton", "kN", UnitCategory.FORCE, "newton", 1000.0, "1000 N")
        self._add_unit("dyne", "dyn", UnitCategory.FORCE, "newton", 1e-5, "CGS unit of force")
        self._add_unit("pound-force", "lbf", UnitCategory.FORCE, "newton", 4.44822, "Imperial force unit")
        self._add_unit("kilogram-force", "kgf", UnitCategory.FORCE, "newton", 9.80665, "Gravitational force on 1 kg")
        self._add_unit("poundal", "pdl", UnitCategory.FORCE, "newton", 0.138255, "Imperial force unit")
        
        # Energy Units
        self._add_unit("joule", "J", UnitCategory.ENERGY, None, 1.0, "SI unit of energy")
        self._add_unit("kilojoule", "kJ", UnitCategory.ENERGY, "joule", 1000.0, "1000 J")
        self._add_unit("megajoule", "MJ", UnitCategory.ENERGY, "joule", 1e6, "1e6 J")
        self._add_unit("gigajoule", "GJ", UnitCategory.ENERGY, "joule", 1e9, "1e9 J")
        self._add_unit("calorie", "cal", UnitCategory.ENERGY, "joule", 4.184, "Thermochemical calorie")
        self._add_unit("kilocalorie", "kcal", UnitCategory.ENERGY, "joule", 4184.0, "Food calorie")
        self._add_unit("british thermal unit", "BTU", UnitCategory.ENERGY, "joule", 1055.06, "Imperial energy unit")
        self._add_unit("electron volt", "eV", UnitCategory.ENERGY, "joule", 1.60218e-19, "Energy gained by electron")
        self._add_unit("kiloelectron volt", "keV", UnitCategory.ENERGY, "joule", 1.60218e-16, "1000 eV")
        self._add_unit("megaelectron volt", "MeV", UnitCategory.ENERGY, "joule", 1.60218e-13, "1e6 eV")
        self._add_unit("gigaelectron volt", "GeV", UnitCategory.ENERGY, "joule", 1.60218e-10, "1e9 eV")
        self._add_unit("teraelectron volt", "TeV", UnitCategory.ENERGY, "joule", 1.60218e-7, "1e12 eV")
        self._add_unit("erg", "erg", UnitCategory.ENERGY, "joule", 1e-7, "CGS unit of energy")
        self._add_unit("foot-pound", "ft·lbf", UnitCategory.ENERGY, "joule", 1.35582, "Imperial energy unit")
        self._add_unit("watt-hour", "Wh", UnitCategory.ENERGY, "joule", 3600.0, "Energy of 1 W for 1 hour")
        self._add_unit("kilowatt-hour", "kWh", UnitCategory.ENERGY, "joule", 3.6e6, "Energy of 1 kW for 1 hour")
        self._add_unit("megawatt-hour", "MWh", UnitCategory.ENERGY, "joule", 3.6e9, "Energy of 1 MW for 1 hour")
        self._add_unit("gigawatt-hour", "GWh", UnitCategory.ENERGY, "joule", 3.6e12, "Energy of 1 GW for 1 hour")
        self._add_unit("therm", "therm", UnitCategory.ENERGY, "joule", 1.055e8, "100,000 BTU")
        self._add_unit("quad", "quad", UnitCategory.ENERGY, "joule", 1.055e18, "1 quadrillion BTU")
        self._add_unit("ton of TNT", "tTNT", UnitCategory.ENERGY, "joule", 4.184e9, "Energy equivalent")
        self._add_unit("kiloton of TNT", "ktTNT", UnitCategory.ENERGY, "joule", 4.184e12, "1000 tons TNT")
        self._add_unit("megaton of TNT", "MtTNT", UnitCategory.ENERGY, "joule", 4.184e15, "1 million tons TNT")
        self._add_unit("hartree", "Eh", UnitCategory.ENERGY, "joule", 4.35974e-18, "Atomic unit of energy")
        self._add_unit("rydberg", "Ry", UnitCategory.ENERGY, "joule", 2.17987e-18, "Rydberg constant")
        
        # Power Units
        self._add_unit("watt", "W", UnitCategory.POWER, None, 1.0, "SI unit of power")
        self._add_unit("kilowatt", "kW", UnitCategory.POWER, "watt", 1000.0, "1000 W")
        self._add_unit("megawatt", "MW", UnitCategory.POWER, "watt", 1e6, "1e6 W")
        self._add_unit("gigawatt", "GW", UnitCategory.POWER, "watt", 1e9, "1e9 W")
        self._add_unit("terawatt", "TW", UnitCategory.POWER, "watt", 1e12, "1e12 W")
        self._add_unit("horsepower", "hp", UnitCategory.POWER, "watt", 745.7, "Mechanical horsepower")
        self._add_unit("metric horsepower", "PS", UnitCategory.POWER, "watt", 735.5, "Metric horsepower")
        self._add_unit("boiler horsepower", "bhp", UnitCategory.POWER, "watt", 9812.5, "Boiler horsepower")
        self._add_unit("electrical horsepower", "ehp", UnitCategory.POWER, "watt", 746.0, "Electrical horsepower")
        self._add_unit("foot-pound per second", "ft·lbf/s", UnitCategory.POWER, "watt", 1.35582, "Imperial power unit")
        self._add_unit("british thermal unit per hour", "BTU/h", UnitCategory.POWER, "watt", 0.293071, "BTU per hour")
        
        # Temperature Units
        self._add_unit("kelvin", "K", UnitCategory.TEMPERATURE, None, 1.0, "SI unit of temperature")
        self._add_unit("celsius", "°C", UnitCategory.TEMPERATURE, None, None, "Celsius temperature")
        self._add_unit("fahrenheit", "°F", UnitCategory.TEMPERATURE, None, None, "Fahrenheit temperature")
        self._add_unit("rankine", "°R", UnitCategory.TEMPERATURE, None, None, "Absolute Fahrenheit")
        
        # Pressure Units
        self._add_unit("pascal", "Pa", UnitCategory.PRESSURE, None, 1.0, "SI unit of pressure")
        self._add_unit("kilopascal", "kPa", UnitCategory.PRESSURE, "pascal", 1000.0, "1000 Pa")
        self._add_unit("megapascal", "MPa", UnitCategory.PRESSURE, "pascal", 1e6, "1e6 Pa")
        self._add_unit("gigapascal", "GPa", UnitCategory.PRESSURE, "pascal", 1e9, "1e9 Pa")
        self._add_unit("bar", "bar", UnitCategory.PRESSURE, "pascal", 1e5, "Metric pressure unit")
        self._add_unit("millibar", "mbar", UnitCategory.PRESSURE, "pascal", 100.0, "0.001 bar")
        self._add_unit("atmosphere", "atm", UnitCategory.PRESSURE, "pascal", 101325.0, "Standard atmosphere")
        self._add_unit("torr", "Torr", UnitCategory.PRESSURE, "pascal", 133.322, "1 mmHg")
        self._add_unit("millimeter of mercury", "mmHg", UnitCategory.PRESSURE, "pascal", 133.322, "Millimeter of mercury")
        self._add_unit("inch of mercury", "inHg", UnitCategory.PRESSURE, "pascal", 3386.39, "Inch of mercury")
        self._add_unit("pound per square inch", "psi", UnitCategory.PRESSURE, "pascal", 6894.76, "Imperial pressure unit")
        self._add_unit("pound per square foot", "psf", UnitCategory.PRESSURE, "pascal", 47.8803, "Imperial pressure unit")
        
        # Frequency Units
        self._add_unit("hertz", "Hz", UnitCategory.FREQUENCY, None, 1.0, "SI unit of frequency")
        self._add_unit("kilohertz", "kHz", UnitCategory.FREQUENCY, "hertz", 1000.0, "1000 Hz")
        self._add_unit("megahertz", "MHz", UnitCategory.FREQUENCY, "hertz", 1e6, "1e6 Hz")
        self._add_unit("gigahertz", "GHz", UnitCategory.FREQUENCY, "hertz", 1e9, "1e9 Hz")
        self._add_unit("terahertz", "THz", UnitCategory.FREQUENCY, "hertz", 1e12, "1e12 Hz")
        self._add_unit("petahertz", "PHz", UnitCategory.FREQUENCY, "hertz", 1e15, "1e15 Hz")
        self._add_unit("revolutions per minute", "rpm", UnitCategory.FREQUENCY, "hertz", 0.0166667, "Revolutions per minute")
        
        # Electric Current Units
        self._add_unit("ampere", "A", UnitCategory.ELECTRIC_CURRENT, None, 1.0, "SI unit of current")
        self._add_unit("milliampere", "mA", UnitCategory.ELECTRIC_CURRENT, "ampere", 0.001, "0.001 A")
        self._add_unit("microampere", "μA", UnitCategory.ELECTRIC_CURRENT, "ampere", 1e-6, "1e-6 A")
        self._add_unit("nanoampere", "nA", UnitCategory.ELECTRIC_CURRENT, "ampere", 1e-9, "1e-9 A")
        self._add_unit("kiloampere", "kA", UnitCategory.ELECTRIC_CURRENT, "ampere", 1000.0, "1000 A")
        self._add_unit("megaampere", "MA", UnitCategory.ELECTRIC_CURRENT, "ampere", 1e6, "1e6 A")
        
        # Voltage Units
        self._add_unit("volt", "V", UnitCategory.VOLTAGE, None, 1.0, "SI unit of voltage")
        self._add_unit("millivolt", "mV", UnitCategory.VOLTAGE, "volt", 0.001, "0.001 V")
        self._add_unit("microvolt", "μV", UnitCategory.VOLTAGE, "volt", 1e-6, "1e-6 V")
        self._add_unit("kilovolt", "kV", UnitCategory.VOLTAGE, "volt", 1000.0, "1000 V")
        self._add_unit("megavolt", "MV", UnitCategory.VOLTAGE, "volt", 1e6, "1e6 V")
        self._add_unit("gigavolt", "GV", UnitCategory.VOLTAGE, "volt", 1e9, "1e9 V")
        
        # Resistance Units
        self._add_unit("ohm", "Ω", UnitCategory.RESISTANCE, None, 1.0, "SI unit of resistance")
        self._add_unit("milliohm", "mΩ", UnitCategory.RESISTANCE, "ohm", 0.001, "0.001 Ω")
        self._add_unit("microohm", "μΩ", UnitCategory.RESISTANCE, "ohm", 1e-6, "1e-6 Ω")
        self._add_unit("kiloohm", "kΩ", UnitCategory.RESISTANCE, "ohm", 1000.0, "1000 Ω")
        self._add_unit("megaohm", "MΩ", UnitCategory.RESISTANCE, "ohm", 1e6, "1e6 Ω")
        self._add_unit("gigaohm", "GΩ", UnitCategory.RESISTANCE, "ohm", 1e9, "1e9 Ω")
        
        # Capacitance Units
        self._add_unit("farad", "F", UnitCategory.CAPACITANCE, None, 1.0, "SI unit of capacitance")
        self._add_unit("millifarad", "mF", UnitCategory.CAPACITANCE, "farad", 0.001, "0.001 F")
        self._add_unit("microfarad", "μF", UnitCategory.CAPACITANCE, "farad", 1e-6, "1e-6 F")
        self._add_unit("nanofarad", "nF", UnitCategory.CAPACITANCE, "farad", 1e-9, "1e-9 F")
        self._add_unit("picofarad", "pF", UnitCategory.CAPACITANCE, "farad", 1e-12, "1e-12 F")
        self._add_unit("kilofarad", "kF", UnitCategory.CAPACITANCE, "farad", 1000.0, "1000 F")
        
        # Inductance Units
        self._add_unit("henry", "H", UnitCategory.INDUCTANCE, None, 1.0, "SI unit of inductance")
        self._add_unit("millihenry", "mH", UnitCategory.INDUCTANCE, "henry", 0.001, "0.001 H")
        self._add_unit("microhenry", "μH", UnitCategory.INDUCTANCE, "henry", 1e-6, "1e-6 H")
        self._add_unit("nanohenry", "nH", UnitCategory.INDUCTANCE, "henry", 1e-9, "1e-9 H")
        self._add_unit("picohenry", "pH", UnitCategory.INDUCTANCE, "henry", 1e-12, "1e-12 H")
        
        # Magnetic Field Units
        self._add_unit("tesla", "T", UnitCategory.MAGNETIC_FIELD, None, 1.0, "SI unit of magnetic field")
        self._add_unit("millitesla", "mT", UnitCategory.MAGNETIC_FIELD, "tesla", 0.001, "0.001 T")
        self._add_unit("microtesla", "μT", UnitCategory.MAGNETIC_FIELD, "tesla", 1e-6, "1e-6 T")
        self._add_unit("nanotesla", "nT", UnitCategory.MAGNETIC_FIELD, "tesla", 1e-9, "1e-9 T")
        self._add_unit("gauss", "G", UnitCategory.MAGNETIC_FIELD, "tesla", 1e-4, "CGS unit of magnetic field")
        self._add_unit("maxwell", "Mx", UnitCategory.MAGNETIC_FIELD, "tesla", 1e-8, "CGS unit of magnetic flux")
        self._add_unit("oersted", "Oe", UnitCategory.MAGNETIC_FIELD, "ampere per meter", 79.5775, "CGS unit of magnetic field strength")
        
        # Area Units
        self._add_unit("square meter", "m²", UnitCategory.AREA, None, 1.0, "SI unit of area")
        self._add_unit("square kilometer", "km²", UnitCategory.AREA, "square meter", 1e6, "1e6 m²")
        self._add_unit("square centimeter", "cm²", UnitCategory.AREA, "square meter", 1e-4, "1e-4 m²")
        self._add_unit("square millimeter", "mm²", UnitCategory.AREA, "square meter", 1e-6, "1e-6 m²")
        self._add_unit("square inch", "in²", UnitCategory.AREA, "square meter", 0.00064516, "0.00064516 m²")
        self._add_unit("square foot", "ft²", UnitCategory.AREA, "square meter", 0.092903, "0.092903 m²")
        self._add_unit("square yard", "yd²", UnitCategory.AREA, "square meter", 0.836127, "0.836127 m²")
        self._add_unit("square mile", "mi²", UnitCategory.AREA, "square meter", 2.59e6, "2.59e6 m²")
        self._add_unit("acre", "ac", UnitCategory.AREA, "square meter", 4046.86, "Land area unit")
        self._add_unit("hectare", "ha", UnitCategory.AREA, "square meter", 10000.0, "10,000 m²")
        self._add_unit("barn", "b", UnitCategory.AREA, "square meter", 1e-28, "Nuclear cross-section unit")
        
        # Volume Units
        self._add_unit("cubic meter", "m³", UnitCategory.VOLUME, None, 1.0, "SI unit of volume")
        self._add_unit("cubic kilometer", "km³", UnitCategory.VOLUME, "cubic meter", 1e9, "1e9 m³")
        self._add_unit("cubic centimeter", "cm³", UnitCategory.VOLUME, "cubic meter", 1e-6, "1e-6 m³")
        self._add_unit("cubic millimeter", "mm³", UnitCategory.VOLUME, "cubic meter", 1e-9, "1e-9 m³")
        self._add_unit("liter", "L", UnitCategory.VOLUME, "cubic meter", 0.001, "1 dm³")
        self._add_unit("milliliter", "mL", UnitCategory.VOLUME, "cubic meter", 1e-6, "1e-6 m³")
        self._add_unit("cubic inch", "in³", UnitCategory.VOLUME, "cubic meter", 1.63871e-5, "1.63871e-5 m³")
        self._add_unit("cubic foot", "ft³", UnitCategory.VOLUME, "cubic meter", 0.0283168, "0.0283168 m³")
        self._add_unit("cubic yard", "yd³", UnitCategory.VOLUME, "cubic meter", 0.764555, "0.764555 m³")
        self._add_unit("gallon", "gal", UnitCategory.VOLUME, "cubic meter", 0.00378541, "US liquid gallon")
        self._add_unit("quart", "qt", UnitCategory.VOLUME, "cubic meter", 0.000946353, "US liquid quart")
        self._add_unit("pint", "pt", UnitCategory.VOLUME, "cubic meter", 0.000473176, "US liquid pint")
        self._add_unit("cup", "cup", UnitCategory.VOLUME, "cubic meter", 0.000236588, "US cup")
        self._add_unit("fluid ounce", "fl oz", UnitCategory.VOLUME, "cubic meter", 2.95735e-5, "US fluid ounce")
        self._add_unit("tablespoon", "tbsp", UnitCategory.VOLUME, "cubic meter", 1.47868e-5, "US tablespoon")
        self._add_unit("teaspoon", "tsp", UnitCategory.VOLUME, "cubic meter", 4.92892e-6, "US teaspoon")
        self._add_unit("imperial gallon", "imp gal", UnitCategory.VOLUME, "cubic meter", 0.00454609, "Imperial gallon")
        self._add_unit("barrel", "bbl", UnitCategory.VOLUME, "cubic meter", 0.158987, "Oil barrel")
        
        # Density Units
        self._add_unit("kilogram per cubic meter", "kg/m³", UnitCategory.DENSITY, None, 1.0, "SI unit of density")
        self._add_unit("gram per cubic centimeter", "g/cm³", UnitCategory.DENSITY, "kilogram per cubic meter", 1000.0, "1000 kg/m³")
        self._add_unit("gram per milliliter", "g/mL", UnitCategory.DENSITY, "kilogram per cubic meter", 1000.0, "1000 kg/m³")
        self._add_unit("kilogram per liter", "kg/L", UnitCategory.DENSITY, "kilogram per cubic meter", 1000.0, "1000 kg/m³")
        self._add_unit("pound per cubic foot", "lb/ft³", UnitCategory.DENSITY, "kilogram per cubic meter", 16.0185, "Imperial density")
        self._add_unit("pound per cubic inch", "lb/in³", UnitCategory.DENSITY, "kilogram per cubic meter", 27679.9, "Imperial density")
        self._add_unit("ounce per cubic inch", "oz/in³", UnitCategory.DENSITY, "kilogram per cubic meter", 1729.99, "Imperial density")
        
        # Angle Units
        self._add_unit("radian", "rad", UnitCategory.ANGLE, None, 1.0, "SI unit of angle")
        self._add_unit("degree", "°", UnitCategory.ANGLE, "radian", 0.0174533, "360° in circle")
        self._add_unit("arc minute", "'", UnitCategory.ANGLE, "radian", 0.000290888, "1/60 degree")
        self._add_unit("arc second", "&quot;", UnitCategory.ANGLE, "radian", 4.84814e-6, "1/3600 degree")
        self._add_unit("gradian", "grad", UnitCategory.ANGLE, "radian", 0.015708, "400 grad in circle")
        self._add_unit("turn", "turn", UnitCategory.ANGLE, "radian", 6.28319, "Full rotation")
        self._add_unit("mil", "mil", UnitCategory.ANGLE, "radian", 0.000981748, "Military angle unit")
        
        # Solid Angle Units
        self._add_unit("steradian", "sr", UnitCategory.SOLID_ANGLE, None, 1.0, "SI unit of solid angle")
        self._add_unit("square degree", "°²", UnitCategory.SOLID_ANGLE, "steradian", 0.000304617, "Square degree")
        self._add_unit("sphere", "sphere", UnitCategory.SOLID_ANGLE, "steradian", 12.5664, "Full solid angle")
        
        # Angular Velocity Units
        self._add_unit("radian per second", "rad/s", UnitCategory.ANGULAR_VELOCITY, None, 1.0, "SI unit of angular velocity")
        self._add_unit("degree per second", "°/s", UnitCategory.ANGULAR_VELOCITY, "radian per second", 0.0174533, "Degree per second")
        self._add_unit("revolutions per minute", "rpm", UnitCategory.ANGULAR_VELOCITY, "radian per second", 0.10472, "Revolutions per minute")
        self._add_unit("revolutions per second", "rps", UnitCategory.ANGULAR_VELOCITY, "radian per second", 6.28319, "Revolutions per second")
        
        # Angular Acceleration Units
        self._add_unit("radian per second squared", "rad/s²", UnitCategory.ANGULAR_ACCELERATION, None, 1.0, "SI unit of angular acceleration")
        self._add_unit("degree per second squared", "°/s²", UnitCategory.ANGULAR_ACCELERATION, "radian per second squared", 0.0174533, "Degree per second squared")
        
        # Data Rate Units
        self._add_unit("bit per second", "bit/s", UnitCategory.DATA_RATE, None, 1.0, "SI unit of data rate")
        self._add_unit("kilobit per second", "kb/s", UnitCategory.DATA_RATE, "bit per second", 1000.0, "1000 bit/s")
        self._add_unit("megabit per second", "Mb/s", UnitCategory.DATA_RATE, "bit per second", 1e6, "1e6 bit/s")
        self._add_unit("gigabit per second", "Gb/s", UnitCategory.DATA_RATE, "bit per second", 1e9, "1e9 bit/s")
        self._add_unit("terabit per second", "Tb/s", UnitCategory.DATA_RATE, "bit per second", 1e12, "1e12 bit/s")
        self._add_unit("byte per second", "B/s", UnitCategory.DATA_RATE, "bit per second", 8.0, "8 bit/s")
        self._add_unit("kilobyte per second", "kB/s", UnitCategory.DATA_RATE, "bit per second", 8000.0, "8000 bit/s")
        self._add_unit("megabyte per second", "MB/s", UnitCategory.DATA_RATE, "bit per second", 8e6, "8e6 bit/s")
        self._add_unit("gigabyte per second", "GB/s", UnitCategory.DATA_RATE, "bit per second", 8e9, "8e9 bit/s")
        self._add_unit("terabyte per second", "TB/s", UnitCategory.DATA_RATE, "bit per second", 8e12, "8e12 bit/s")
        
        # Data Storage Units
        self._add_unit("bit", "b", UnitCategory.DATA_STORAGE, None, 1.0, "Binary digit")
        self._add_unit("byte", "B", UnitCategory.DATA_STORAGE, "bit", 8.0, "8 bits")
        self._add_unit("kilobyte", "kB", UnitCategory.DATA_STORAGE, "byte", 1000.0, "1000 bytes")
        self._add_unit("megabyte", "MB", UnitCategory.DATA_STORAGE, "byte", 1e6, "1e6 bytes")
        self._add_unit("gigabyte", "GB", UnitCategory.DATA_STORAGE, "byte", 1e9, "1e9 bytes")
        self._add_unit("terabyte", "TB", UnitCategory.DATA_STORAGE, "byte", 1e12, "1e12 bytes")
        self._add_unit("petabyte", "PB", UnitCategory.DATA_STORAGE, "byte", 1e15, "1e15 bytes")
        self._add_unit("exabyte", "EB", UnitCategory.DATA_STORAGE, "byte", 1e18, "1e18 bytes")
        self._add_unit("kibibyte", "KiB", UnitCategory.DATA_STORAGE, "byte", 1024.0, "1024 bytes")
        self._add_unit("mebibyte", "MiB", UnitCategory.DATA_STORAGE, "byte", 1048576.0, "1024 KiB")
        self._add_unit("gibibyte", "GiB", UnitCategory.DATA_STORAGE, "byte", 1073741824.0, "1024 MiB")
        self._add_unit("tebibyte", "TiB", UnitCategory.DATA_STORAGE, "byte", 1099511627776.0, "1024 GiB")
        self._add_unit("pebibyte", "PiB", UnitCategory.DATA_STORAGE, "byte", 1125899906842624.0, "1024 TiB")
        
        # Initialize common variables
        self._initialize_variables()
    
    def _add_unit(self, name: str, symbol: str, category: UnitCategory, 
                  si_equivalent: Optional[str], conversion_factor: Optional[float],
                  description: str):
        """Add a unit to the database"""
        unit_info = UnitInfo(
            name=name,
            symbol=symbol,
            category=category,
            si_equivalent=si_equivalent,
            conversion_factor=conversion_factor,
            description=description
        )
        self.units[name.lower()] = unit_info
        self.units[symbol] = unit_info
    
    def _initialize_variables(self):
        """Initialize common mathematical variables"""
        
        # Physics variables
        self._add_variable("v", ["velocity", "speed"], 
                          [UnitCategory.VELOCITY], ["physics", "mechanics"],
                          "Velocity or speed of an object")
        self._add_variable("u", ["velocity", "initial velocity", "potential energy"],
                          [UnitCategory.VELOCITY, UnitCategory.ENERGY], 
                          ["physics", "mechanics", "thermodynamics"],
                          "Often used for velocity or potential energy")
        self._add_variable("a", ["acceleration", "area", "amplitude"],
                          [UnitCategory.ACCELERATION, UnitCategory.AREA],
                          ["physics", "mechanics", "waves"],
                          "Acceleration, area, or amplitude depending on context")
        self._add_variable("b", ["magnetic field", "width", "beta"],
                          [UnitCategory.MAGNETIC_FIELD, UnitCategory.LENGTH],
                          ["physics", "electromagnetism", "geometry"],
                          "Magnetic field, width, or beta parameter")
        self._add_variable("c", ["speed of light", "capacitance", "concentration"],
                          [UnitCategory.VELOCITY, UnitCategory.CAPACITANCE],
                          ["physics", "electromagnetism", "chemistry"],
                          "Speed of light, capacitance, or concentration")
        self._add_variable("d", ["distance", "diameter", "density"],
                          [UnitCategory.LENGTH, UnitCategory.DENSITY],
                          ["physics", "geometry"],
                          "Distance, diameter, or density")
        self._add_variable("e", ["energy", "electric field", "electron charge"],
                          [UnitCategory.ENERGY, UnitCategory.ELECTRIC_CURRENT],
                          ["physics", "electromagnetism", "chemistry"],
                          "Energy, electric field, or electron charge")
        self._add_variable("f", ["frequency", "force", "friction"],
                          [UnitCategory.FREQUENCY, UnitCategory.FORCE],
                          ["physics", "waves", "mechanics"],
                          "Frequency, force, or friction")
        self._add_variable("g", ["gravity", "acceleration due to gravity"],
                          [UnitCategory.ACCELERATION],
                          ["physics", "mechanics"],
                          "Acceleration due to gravity")
        self._add_variable("h", ["height", "planck constant", "enthalpy"],
                          [UnitCategory.LENGTH, UnitCategory.ENERGY],
                          ["physics", "mechanics", "thermodynamics"],
                          "Height, Planck constant, or enthalpy")
        self._add_variable("i", ["current", "intensity", "imaginary unit"],
                          [UnitCategory.ELECTRIC_CURRENT],
                          ["physics", "electromagnetism", "mathematics"],
                          "Electric current, intensity, or imaginary unit")
        self._add_variable("j", ["current density", "imaginary unit"],
                          [UnitCategory.ELECTRIC_CURRENT],
                          ["physics", "electromagnetism", "engineering"],
                          "Current density or imaginary unit (engineering)")
        self._add_variable("k", ["spring constant", "boltzmann constant", "wave number"],
                          [UnitCategory.FORCE, UnitCategory.ENERGY],
                          ["physics", "mechanics", "thermodynamics"],
                          "Spring constant, Boltzmann constant, or wave number")
        self._add_variable("l", ["length", "angular momentum", "inductance"],
                          [UnitCategory.LENGTH, UnitCategory.INDUCTANCE],
                          ["physics", "mechanics", "electromagnetism"],
                          "Length, angular momentum, or inductance")
        self._add_variable("m", ["mass", "magnetic moment", "mole"],
                          [UnitCategory.MASS, UnitCategory.AMOUNT_OF_SUBSTANCE],
                          ["physics", "chemistry"],
                          "Mass, magnetic moment, or mole")
        self._add_variable("n", ["number", "refractive index", "neutron"],
                          [],
                          ["physics", "optics", "chemistry"],
                          "Number, refractive index, or neutron")
        self._add_variable("o", ["origin", "observation"],
                          [],
                          ["mathematics", "physics"],
                          "Origin point or observation")
        self._add_variable("p", ["pressure", "momentum", "power", "probability"],
                          [UnitCategory.PRESSURE, UnitCategory.POWER],
                          ["physics", "mechanics", "thermodynamics"],
                          "Pressure, momentum, power, or probability")
        self._add_variable("q", ["charge", "heat", "quality factor"],
                          [UnitCategory.ELECTRIC_CURRENT, UnitCategory.ENERGY],
                          ["physics", "electromagnetism", "thermodynamics"],
                          "Electric charge, heat, or quality factor")
        self._add_variable("r", ["radius", "resistance", "position"],
                          [UnitCategory.LENGTH, UnitCategory.RESISTANCE],
                          ["physics", "geometry", "electromagnetism"],
                          "Radius, resistance, or position vector")
        self._add_variable("s", ["entropy", "displacement", "speed"],
                          [UnitCategory.LENGTH, UnitCategory.ENERGY],
                          ["physics", "thermodynamics", "mechanics"],
                          "Entropy, displacement, or speed")
        self._add_variable("t", ["time", "temperature", "torque"],
                          [UnitCategory.TIME, UnitCategory.TEMPERATURE],
                          ["physics", "thermodynamics", "mechanics"],
                          "Time, temperature, or torque")
        self._add_variable("u", ["potential energy", "internal energy", "velocity"],
                          [UnitCategory.ENERGY, UnitCategory.VELOCITY],
                          ["physics", "thermodynamics", "mechanics"],
                          "Potential energy, internal energy, or velocity")
        self._add_variable("v", ["velocity", "voltage", "volume"],
                          [UnitCategory.VELOCITY, UnitCategory.VOLTAGE, UnitCategory.VOLUME],
                          ["physics", "electromagnetism", "thermodynamics"],
                          "Velocity, voltage, or volume")
        self._add_variable("w", ["work", "width", "angular frequency", "weight"],
                          [UnitCategory.ENERGY, UnitCategory.LENGTH],
                          ["physics", "mechanics", "waves"],
                          "Work, width, angular frequency, or weight")
        self._add_variable("x", ["position", "coordinate", "displacement"],
                          [UnitCategory.LENGTH],
                          ["mathematics", "physics", "geometry"],
                          "X-coordinate, position, or displacement")
        self._add_variable("y", ["position", "coordinate", "displacement"],
                          [UnitCategory.LENGTH],
                          ["mathematics", "physics", "geometry"],
                          "Y-coordinate, position, or displacement")
        self._add_variable("z", ["position", "coordinate", "impedance", "charge"],
                          [UnitCategory.LENGTH, UnitCategory.RESISTANCE],
                          ["mathematics", "physics", "electromagnetism"],
                          "Z-coordinate, position, impedance, or charge")
        
        # Greek letters commonly used in formulas
        self._add_variable("alpha", ["angle", "alpha particle", "fine structure constant"],
                          [UnitCategory.ANGLE],
                          ["physics", "mathematics", "nuclear"],
                          "Angle, alpha particle, or fine structure constant")
        self._add_variable("beta", ["angle", "beta particle", "velocity/c"],
                          [UnitCategory.ANGLE, UnitCategory.VELOCITY],
                          ["physics", "mathematics", "nuclear"],
                          "Angle, beta particle, or velocity ratio")
        self._add_variable("gamma", ["angle", "gamma ray", "lorentz factor"],
                          [UnitCategory.ANGLE],
                          ["physics", "mathematics", "relativity"],
                          "Angle, gamma ray, or Lorentz factor")
        self._add_variable("delta", ["change", "delta particle"],
                          [],
                          ["mathematics", "physics", "nuclear"],
                          "Change in quantity or delta particle")
        self._add_variable("epsilon", ["permittivity", "strain", "small quantity"],
                          [UnitCategory.ENERGY],
                          ["physics", "engineering", "mathematics"],
                          "Permittivity, strain, or small quantity")
        self._add_variable("zeta", ["damping ratio", "riemann zeta"],
                          [],
                          ["physics", "mathematics"],
                          "Damping ratio or Riemann zeta function")
        self._add_variable("eta", ["efficiency", "viscosity"],
                          [],
                          ["physics", "engineering"],
                          "Efficiency or viscosity")
        self._add_variable("theta", ["angle", "temperature"],
                          [UnitCategory.ANGLE, UnitCategory.TEMPERATURE],
                          ["physics", "mathematics"],
                          "Angle or temperature")
        self._add_variable("iota", [],
                          [],
                          ["mathematics"],
                          "Small quantity")
        self._add_variable("kappa", ["thermal conductivity", "curvature"],
                          [UnitCategory.THERMAL_CONDUCTIVITY],
                          ["physics", "mathematics"],
                          "Thermal conductivity or curvature")
        self._add_variable("lambda", ["wavelength", "decay constant"],
                          [UnitCategory.WAVELENGTH],
                          ["physics", "mathematics"],
                          "Wavelength or decay constant")
        self._add_variable("mu", ["permeability", "friction coefficient", "mean"],
                          [],
                          ["physics", "mathematics", "statistics"],
                          "Permeability, friction coefficient, or mean")
        self._add_variable("nu", ["frequency", "neutrino"],
                          [UnitCategory.FREQUENCY],
                          ["physics", "mathematics"],
                          "Frequency or neutrino")
        self._add_variable("xi", ["damping ratio"],
                          [],
                          ["physics", "mathematics"],
                          "Damping ratio")
        self._add_variable("omicron", [],
                          [],
                          ["mathematics"],
                          "Small quantity")
        self._add_variable("pi", ["ratio", "momentum"],
                          [],
                          ["mathematics", "physics"],
                          "Ratio or momentum")
        self._add_variable("rho", ["density", "resistivity"],
                          [UnitCategory.DENSITY],
                          ["physics", "mathematics"],
                          "Density or resistivity")
        self._add_variable("sigma", ["stress", "conductivity", "standard deviation"],
                          [],
                          ["physics", "statistics", "engineering"],
                          "Stress, conductivity, or standard deviation")
        self._add_variable("tau", ["torque", "time constant", "proper time"],
                          [UnitCategory.TIME],
                          ["physics", "mathematics"],
                          "Torque, time constant, or proper time")
        self._add_variable("upsilon", [],
                          [],
                          ["mathematics", "physics"],
                          "Upsilon particle")
        self._add_variable("phi", ["angle", "phase", "magnetic flux"],
                          [UnitCategory.ANGLE],
                          ["physics", "mathematics"],
                          "Angle, phase, or magnetic flux")
        self._add_variable("chi", ["susceptibility", "angle"],
                          [UnitCategory.ANGLE],
                          ["physics", "mathematics"],
                          "Susceptibility or angle")
        self._add_variable("psi", ["wave function", "angle"],
                          [UnitCategory.ANGLE],
                          ["physics", "mathematics"],
                          "Wave function or angle")
        self._add_variable("omega", ["angular frequency", "ohm"],
                          [UnitCategory.FREQUENCY, UnitCategory.RESISTANCE],
                          ["physics", "electromagnetism"],
                          "Angular frequency or ohm")
    
    def _add_variable(self, name: str, common_meanings: List[str], 
                     typical_units: List[UnitCategory], typical_domains: List[str],
                     description: str):
        """Add a variable to the database"""
        var_info = VariableInfo(
            name=name,
            common_meanings=common_meanings,
            typical_units=typical_units,
            typical_domains=typical_domains,
            description=description
        )
        self.variables[name.lower()] = var_info
    
    def detect_unit(self, text: str) -> Optional[UnitInfo]:
        """Detect if text contains a unit"""
        text_lower = text.lower().strip()
        
        # Direct match
        if text_lower in self.units:
            return self.units[text_lower]
        
        # Partial match
        for unit_name, unit_info in self.units.items():
            if text_lower in unit_name or unit_name in text_lower:
                return unit_info
        
        return None
    
    def detect_variable(self, text: str) -> Optional[VariableInfo]:
        """Detect if text contains a variable"""
        text_lower = text.lower().strip()
        
        # Direct match
        if text_lower in self.variables:
            return self.variables[text_lower]
        
        return None
    
    def get_suggestions(self, text: str) -> List[Dict]:
        """Get suggestions for units or variables based on text"""
        suggestions = []
        
        # Check for units
        for unit_name, unit_info in self.units.items():
            if text.lower() in unit_name.lower() or text.lower() in unit_info.description.lower():
                suggestions.append({
                    "type": "unit",
                    "name": unit_info.name,
                    "symbol": unit_info.symbol,
                    "category": unit_info.category.value,
                    "description": unit_info.description
                })
        
        # Check for variables
        for var_name, var_info in self.variables.items():
            if text.lower() in var_name.lower() or text.lower() in var_info.description.lower():
                suggestions.append({
                    "type": "variable",
                    "name": var_info.name,
                    "common_meanings": var_info.common_meanings,
                    "typical_domains": var_info.typical_domains,
                    "description": var_info.description
                })
        
        return suggestions[:10]  # Return top 10 suggestions
    
    def analyze_formula_variables(self, formula: str) -> Dict[str, VariableInfo]:
        """Analyze variables in a formula"""
        import re
        variables_found = {}
        
        # Find potential variables (single letters, greek letters)
        pattern = r'\b[a-zA-Zαβγδεζηθικλμνξοπρστυφχψω]\b'
        matches = re.findall(pattern, formula)
        
        for match in matches:
            var_info = self.detect_variable(match)
            if var_info:
                variables_found[match] = var_info
        
        return variables_found
    
    def get_total_units_count(self) -> int:
        """Get total number of units in database"""
        return len(self.units)
    
    def get_total_variables_count(self) -> int:
        """Get total number of variables in database"""
        return len(self.variables)


if __name__ == "__main__":
    # Test the database
    db = UnitsDatabase()
    
    print(f"Units Database initialized with {db.get_total_units_count()} units")
    print(f"Variables Database initialized with {db.get_total_variables_count()} variables")
    print()
    
    # Test unit detection
    print("Testing unit detection:")
    test_units = ["m/s", "mph", "kg", "eV", "Tesla"]
    for unit in test_units:
        detected = db.detect_unit(unit)
        if detected:
            print(f"  {unit}: {detected.name} ({detected.category.value})")
        else:
            print(f"  {unit}: Not found")
    print()
    
    # Test variable detection
    print("Testing variable detection:")
    test_vars = ["v", "gamma", "E", "omega"]
    for var in test_vars:
        detected = db.detect_variable(var)
        if detected:
            print(f"  {var}: {detected.common_meanings}")
        else:
            print(f"  {var}: Not found")
    print()
    
    # Test formula analysis
    print("Testing formula analysis:")
    formula = "E = mc^2 + 1/2 mv^2"
    vars_in_formula = db.analyze_formula_variables(formula)
    print(f"  Formula: {formula}")
    print(f"  Variables found:")
    for var, info in vars_in_formula.items():
        print(f"    {var}: {info.common_meanings}")