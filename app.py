from rocketpy import Environment, SolidMotor, Rocket, Flight
from rocketpy.plots.environment_plots import _EnvironmentPlots
from rocketpy.plots.solid_motor_plots import _SolidMotorPlots
from rocketpy.plots.rocket_plots import _RocketPlots
from rocketpy.plots.flight_plots import _FlightPlots
import streamlit as st
import leafmap.foliumap as lfm
tab1,tab2 = st.tabs(['About','Simulation'])
with tab1:
    st.header("About the simulator")
    
env = Environment(latitude=32.990254, longitude=-106.974998, elevation=1400)
import datetime
motor = SolidMotor(
    thrust_source="Cesaroni_M1670.eng",
    dry_mass=1.815,
    dry_inertia=(0.125, 0.125, 0.002),
    nozzle_radius=33 / 1000,
    grain_number=5,
    grain_density=1815,
    grain_outer_radius=33 / 1000,
    grain_initial_inner_radius=15 / 1000,
    grain_initial_height=120 / 1000,
    grain_separation=5 / 1000,
    grains_center_of_mass_position=0.397,
    center_of_dry_mass_position=0.317,
    nozzle_position=0,
    burn_time=3.9,
    throat_radius=11 / 1000,
    coordinate_system_orientation="nozzle_to_combustion_chamber",
)
tomorrow = datetime.date.today() + datetime.timedelta(days=1)

#ROCKET
calisto_radius = 127/2000

calisto = Rocket(
    radius=calisto_radius, #variable
    mass=14.426,
    inertia=(6.321, 6.321, 0.034),
    power_off_drag="powerOffDragCurve.csv",
    power_on_drag="powerOnDragCurve.csv",
    center_of_mass_without_motor=0,
    coordinate_system_orientation="tail_to_nose",
)
rail_buttons = calisto.set_rail_buttons(
    upper_button_position=0.0818,
    lower_button_position=-0.618,
    angular_position=45,)
calisto.add_motor(motor, position=-1.255)
nose_cone = calisto.add_nose(
    length=0.55829, kind="vonKarman", position=1.278 #variable
)

fin_set = calisto.add_trapezoidal_fins(
    n=4,
    root_chord=0.120,
    tip_chord=0.060,
    span=0.110,
    position=-1.04956,
    cant_angle=0.5,
    airfoil=("NACA0012-radians.csv","radians"),
)

tail = calisto.add_tail(
    top_radius=0.0635, bottom_radius=0.0435, length=0.060, position=-1.194656 #variable
)
main = calisto.add_parachute(
        "Main",
        cd_s=10.0,
        trigger=800,
        sampling_rate=105,
        lag=1.5,
        noise=(0, 8.3, 0.5),
    )
    
drogue = calisto.add_parachute(
        "Drogue",
        cd_s=1.0,
        trigger="apogee",
        sampling_rate=105,
        lag=1.5,
        noise=(0, 8.3, 0.5),
    )
test_flight = Flight(rocket = calisto, environment=env, rail_length=5.2, inclination=85,heading = 0)
if st.button("press me"):
    env.set_date((tomorrow.year, tomorrow.month, tomorrow.day, 12))  # Hour give in UTC time
    env.set_atmospheric_model(type="Forecast", file="GFS")
    envp = _EnvironmentPlots(env)
    motorp = _SolidMotorPlots(motor)
    rocketp = _RocketPlots(calisto)
    flightp = _FlightPlots(test_flight)
    motorp.draw()
    envp.info()
    rocketp.draw()
    flightp.trajectory_3d()
    flightp.angular_kinematics_data()
    flightp.aerodynamic_forces()
    st.image('info.jpg')
    st.image('motor.jpg')
    st.image('rocket.jpg')
    st.image('flight1.jpg')
    st.image('vital.png')
    st.image('flight3.jpg')
    m = lfm.Map()
    in_kml = 'test_flight.kml'
    m.add_kml(in_kml, layer_name="KML")
    m.to_streamlit()
