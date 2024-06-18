from rocketpy import Environment, SolidMotor, Rocket, Flight
from rocketpy.plots.environment_plots import _EnvironmentPlots
from rocketpy.plots.solid_motor_plots import _SolidMotorPlots
from rocketpy.plots.rocket_plots import _RocketPlots
from rocketpy.plots.flight_plots import _FlightPlots
import streamlit as st
import numpy as np
from PIL import Image

from rocketpy import *
import datetime

st.set_page_config(
        page_title = "StellarThrust",
        page_icon = Image.open("Logo1.jpg")
)

if 'SS' not in st.session_state:
        st.session_state['SS'] = 1
        st.session_state['nozzle_radius'] = 33/1000
        st.session_state['throat_radius'] = 11/1000
        st.session_state['nozzle_pos'] = 0
        st.session_state['grain_out_rad'] = 33/1000
        st.session_state['grain_in_rad'] = 15/1000
        grain_density = 1815
        st.session_state['grain_initial_height'] = 120 / 1000
        st.session_state['grain_separation'] = 5/1000
        st.session_state['calisto_radius'] = 127/2000
        st.session_state['calisto_mass'] = 14.4
        st.session_state['nosecone_length'] = 0.06
        st.session_state['tail_topradius'] = 0.06
        st.session_state['tail_bottomradius'] = 0.04
        st.session_state['upper_button_pos'] = 0.0818
        st.session_state['lower_button_pos'] = -0.618
        st.session_state['nose_cone_pos'] = 1.5



if st.session_state['SS'] == 1:
        # st.title("Rocket Simulation")
        # st.write("This is a rocket simulation aimed to educate high school students about the different factors that affect the launch of a rocket using an engaging and interactive way. In this app, users can learn about the variables that change different factors of a rocket, and are given the freedome to play with the values and look at the results of the launch first hand. This website's purpose is to give users a greater understanding of the complex task of launching a rocket and to be able to break down such a task into smaller, more comprehendable tasks.")
        with st.container(border = True):
                c1, c2 = st.columns(2)
                with c1:
                        st.write("")
                        st.write("")
                        st.title("StellarThrust")
                        st.subheader("A Rocket Launch Simulator")
                        # st.markdown(":orange[A Rocket Launch]")
                        # st.markdown(":orange[Simulator]")
                with c2:
                        st.image("Logo1.jpg")

        c1, c2 = st.columns(2)
        with c1:
                with st.container(border = True):
                        st.subheader("ABOUT THE SIMULATION")
                        st.write("This is a rocket simulation aimed to educate high school students about the different factors that affect the launch of a rocket using an engaging and interactive way. In this app, users can learn about the variables that change different factors of a rocket, and are given the freedome to play with the values and look at the results of the launch first hand. This website's purpose is to give users a greater understanding of the complex task of launching a rocket and to be able to break down such a task into smaller, more comprehendable tasks.")
        with c2:
                with st.container(border = True):
                        st.subheader("ABOUT THE AUTHOR")
                        st.write("I am a high school student passionate about the ")
                
                
                
        v1, v2, v3 = st.columns(3)
        with v2:
                if st.button("Start Simulation", key = 15):
                        st.session_state['SS'] = 2
                        st.rerun()
elif st.session_state['SS'] == 2:
        with st.sidebar:
                st.header("Rocket Details")
                
                with st.expander("Nozzle"):
                        @st.experimental_dialog("More Info About Nozzle")
                        def nozzleinfo():
                                st.image("NozzleImage.jpg")
                                st.write("Nozzle is located at the base of the rocket, controlling the amount of gas that flows out of the system. It's shape is vital in determining the mass flow rate as well as the speed of the fuel as it exits the chamber. The nozzle has 2 parts: the throat and the nozzle.")

                                st.write("The throat is the converging part of the rocket. Here, the gas's area reduces, increasing the pressure and temprature, in turn increasing the speed of the gas particles. In this part, the random motion of gas in the combusion chamber is essentially converted into one directional motion which towards the bottom of the rocket. Here, a smaller value will increase the speed of the gas particles but reduce the mass of the gas that escapes per second. On the other hand, a larger value will reduce the speed of the particles but increase the mass of the gas that exits the rocket per second.")
                                st.write("The nozzle is the diverging part of the rocket. Here, the the gas expands outward and accelerates further, and is then converted into thrust. A smaller value of nozzle radius will reduce the acceleration of the particles but will focus the thrust to a specifc point. On the other hand, a larger value will increase the acceleration of the gas but will be spread out across the cross section of the nozzle width.")

                        
                        if st.button("Click me for more info", key = 124):
                                nozzleinfo()
                        text_type_nozzle = st.radio(label = "Choose data type", options = ["Slider", "TextBox"], index = 0, key = 13)
                        if text_type_nozzle == "Slider":
                                st.session_state['nozzle_radius'] = st.select_slider(label = "Nozzle Radius/meters", options = np.arange(0.001,0.1,0.001), value = 0.033)
                                st.session_state['throat_radius'] = st.select_slider(label = "Throat Radius/meters", options = np.arange(0.001,0.1,0.001), value = 0.011)
                                st.session_state['nozzle_pos'] = st.select_slider(label = "Nozzle Postition/meters", options = np.arange(-1,1,0.01), value = 0.0)
                        else:
                                st.session_state['nozzle_radius'] = st.number_input(label = "Nozzle Radius/meters", min_value=0.001, max_value=0.1, step=0.001, value = 0.033)
                                st.session_state['throat_radius'] = st.number_input(label = "Throat Radius/meters", min_value=0.001, max_value=0.1, step=0.001, value = 0.011)
                                st.session_state['nozzle_pos'] = st.number_input(label = "Throat Position/meters", min_value=-1.0, max_value=1.0, step=0.01, value = 0.0)

                with st.expander("Grain"):
                        @st.experimental_dialog("More Info About Grain")
                        def graininfo():
                                st.image("GrainImage.jpg")
                                st.write("Grain refers to the solid propellent in the motor. It is the material that burns in the rocket. It is typically cylindrical in shape with a space for burning in the middle, allowing two cylinders to be in place: the inner radius and the outer radius. The burning of fuel starts from the inside, slowly making its way to the outer radius and expanding the inner radius and more fuel is burnt.")
                                st.write("A higher value for the inner radius will increase the inital surface area that is exposed to the burning propellent. A higher value for the grain outer radius would increase the total volume availible for the rocket to burn, therefore increasing burn time. ")
                                st.write("The height of the cylinder is controlled by the grain initial height variable. An increase in grain height will expand the length of the motor.")
                                st.write("The grain sepearation controls the distance between each grain particle. A lower value is preferred as high density fuel provides the most thrust, however a lower density (high value of seperation) would increase the burn time.")
                        if "graininfo" not in st.session_state:
                                if st.button("Click me for more info", key = 130):
                                        graininfo()

                        text_type_grain = st.radio(label = "Choose data type", options = ["Slider", "TextBox"], index = 0, key = 14)
                        if text_type_grain == "Slider":
                                st.session_state['grain_out_rad'] = st.select_slider(label = "Grain Outer Radius/meters", options = np.arange(0.01,0.1,0.001), value = 0.03)
                                st.session_state['grain_in_rad'] = st.select_slider(label = "Grain Inner Radius/meters", options = np.arange(0.001,0.08,0.001), value = 0.01)
                                st.session_state['grain_initial_height'] = st.select_slider(label = "Grain Initial Height/meters", options = np.arange(0.01,0.5,0.01), value = 0.12)
                                st.session_state['grain_separation'] = st.select_slider(label = "Grain Separation/meters", options = np.arange(0.001,0.5,0.001), value = 0.005)
                                
                        else:
                                st.session_state['grain_out_rad'] = st.number_input(label = "Grain Outer Radius/meters", min_value=0.01, max_value=0.1, step=0.001, value = 0.03)
                                st.session_state['grain_in_rad'] = st.number_input(label = "Grain Inner Radius/meters", min_value=0.001, max_value=0.08, step=0.001, value = 0.01)
                                st.session_state['grain_initial_height'] = st.number_input(label = "Grain Initial Height/meters", min_value=0.01, max_value=0.5, step=0.01, value = 0.12)
                                st.session_state['grain_separation'] = st.number_input(label = "Grain Separation/meters", min_value=0.001, max_value=0.5, step=0.001, value = 0.005)

                with st.expander("Rocket Size"):
                        @st.experimental_dialog("More Info About The Rocket Size")
                        def rocketsminfo():
                                st.write("The rocket's dimensions heavily affect the total thrust applied on the rocket. A larger radius will increase the drag force, slowling down the rocket. The rocket radius must be kept at a minimum to ensure and all the motor comfortably fits inside the body of the rocket.")
                        if "rocketsminfo" not in st.session_state:
                                if st.button("Click me for more info", key = 17):
                                        rocketsminfo()

                        text_type_rocketsm = st.radio(label = "Choose data type", options = ["Slider", "TextBox"], index = 0, key = 18)
                        if text_type_rocketsm == "Slider":
                                st.session_state['calisto_radius'] = st.select_slider(label = "Rocket Radius/meters", options = np.arange(0.001,0.5,0.001), value = 0.06)
                        else:
                                st.session_state['calisto_radius'] = st.number_input(label = "Rocket Radius/meters", min_value=0.001, max_value=0.5, step=0.001, value = 0.06)

                with st.expander("Flaps"):
                        @st.experimental_dialog("More Info About Flaps")
                        def flapinfo():
                                st.image("ImageFlaps.png")
                                st.write("Flaps ensure the stabilisation of the rocket with the large force of aerodynamic air pressure. The nose cone is placed at the top of the rocket, allowing air to curve around the tip of the rocket. The tail is placed at the bottom of the rocket, and contorls the angular veocity compoenent of the rocket. ")
                        if "flapinfo" not in st.session_state:
                                if st.button("Click me for more info", key = 190):
                                        flapinfo()

                        text_type_flap = st.radio(label = "Choose data type", options = ["Slider", "TextBox"], index = 0, key = 20)
                        if text_type_flap == "Slider":
                                st.session_state['nosecone_length'] = st.select_slider(label = "Nose Cone Length/meters", options = np.arange(0,1,0.01), value = 0.55)
                                st.session_state['nose_cone_pos'] = st.select_slider(label = "Nose Cone position/meters", options = np.arange(0.0,5.0,0.1), value = 1.5)
                                st.session_state['tail_topradius'] = st.select_slider(label = "Tail Top radius/meters", options = np.arange(0,0.5,0.001), value = 0.06)
                                st.session_state['tail_bottomradius'] = st.select_slider(label = "Tail Bottom radius/meters", options = np.arange(0.0,0.5,0.001), value = 0.04)
                        else:
                                st.session_state['nosecone_length'] = st.number_input(label = "Nose Cone Length/meters", min_value=0.0, max_value=1.0, step=0.01, value = 0.55)
                                st.session_state['nose_cone_pos'] = st.number_input(label = "Nose Cone position/meters", min_value=0.0, max_value=5.0, step=0.1, value = 1.5)
                                st.session_state['tail_topradius'] = st.number_input(label = "Tail Top radius/meters", min_value=0.0, max_value=0.5, step=0.001, value = 0.06)
                                st.session_state['tail_bottomradius'] = st.number_input(label = "Tail Bottom radius/meters", min_value=0.0, max_value=0.5, step=0.001, value = 0.04)


                with st.expander("Rail Buttons"):
                        @st.experimental_dialog("More Info About Rail Buttons")
                        def railinfo():
                                st.write("Rail buttons are placed for the launch of the rocket. It keeps the rocket aligned during the launch and stabilises it while in the air. There are two rail buttons, an upper button and a lower puttons whose postion can be changed.")
                        if "railinfo" not in st.session_state:
                                if st.button("Click me for more info", key = 21):
                                        railinfo()

                        text_type_rail = st.radio(label = "Choose data type", options = ["Slider", "TextBox"], index = 0, key = 22)
                        if text_type_rail == "Slider":
                                st.session_state['upper_button_pos'] = st.select_slider(label = "Upper Button Position/meters", options = np.arange(-0.5,0.5,0.001), value = 0.081)
                                st.session_state['lower_button_pos'] = st.select_slider(label = "Lower Button Postion/meters", options = np.arange(-1.0,1.0,0.001), value = -0.618)
                        else:
                                st.session_state['upper_button_pos'] = st.number_input(label = "Upper Button Position/meters", min_value=-0.5, max_value=0.5, step=0.001, value = 0.081)
                                st.session_state['lower_button_pos'] = st.number_input(label = "Lower Button Postion/meters", min_value=-1.0, max_value=1.0, step=0.001, value = -0.618)

                
                
                motor = SolidMotor(
                    thrust_source="Cesaroni_M1670.eng",
                    dry_mass=1.815,
                    dry_inertia=(0.125, 0.125, 0.002),
                    nozzle_radius=st.session_state['nozzle_radius'],
                    grain_number=5,
                    grain_density=1815,
                    grain_outer_radius=st.session_state['grain_out_rad'],
                    grain_initial_inner_radius=st.session_state['grain_in_rad'],
                    grain_initial_height=st.session_state['grain_initial_height'],
                    grain_separation=st.session_state['grain_separation'],
                    grains_center_of_mass_position=0.397,
                    center_of_dry_mass_position=0.317,
                    nozzle_position=st.session_state['nozzle_pos'],
                    burn_time=3.9,
                    throat_radius=st.session_state['throat_radius'],
                    coordinate_system_orientation="nozzle_to_combustion_chamber",
                    )
                
        
                calisto = Rocket(
                        radius=st.session_state['calisto_radius'], #variable
                        mass=14.4,
                        inertia=(6.321, 6.321, 0.034),
                        power_off_drag="powerOffDragCurve.csv",
                        power_on_drag="powerOnDragCurve.csv",
                        center_of_mass_without_motor=0,
                        coordinate_system_orientation="tail_to_nose",
                    )
                rail_buttons = calisto.set_rail_buttons(
                        upper_button_position=st.session_state['upper_button_pos'],
                        lower_button_position=st.session_state['lower_button_pos'],
                        angular_position=45,)
                nose_cone = calisto.add_nose(
                        length=st.session_state['nosecone_length'], kind="vonKarman", position=st.session_state['nose_cone_pos'] #variable
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
                        top_radius=st.session_state['tail_topradius'], bottom_radius=st.session_state['tail_bottomradius'], length=0.060, position=-1.194656 #variable
                    )
                calisto.add_motor(motor, position=-1.255) 

                Main = calisto.add_parachute(
                    "Main",
                    cd_s=10.0,
                    trigger=800,
                    sampling_rate=105,
                    lag=1.5,
                    noise=(0, 8.3, 0.5),
                )
                
                Drogue = calisto.add_parachute(
                    "Drogue",
                    cd_s=1.0,
                    trigger="apogee",
                    sampling_rate=105,
                    lag=1.5,
                    noise=(0, 8.3, 0.5),
                )
                

        
                                
                
                                
        st.header("Plot Rocket")
        @st.experimental_dialog("More Info About Simulation")
        def moreinfo():
                st.write("To use this simulation, enter the desire valuers")
        if st.button("Click me for more info", key = 12):
                nozzleinfo()
        plottype = st.radio(label = "", options = ["Motor", "Rocket"], index = 0)
        
        if plottype == "Motor":
                motorp = _SolidMotorPlots(motor)
                motorp.draw()
                st.image('motor.jpg')
        else:
                rocketp = _RocketPlots(calisto)
                rocketp.draw()
                st.image('rocket.jpg')

        if st.button("Simulate Flight?"):
                st.session_state['SS'] = 3
                st.rerun()
                

        
                
elif st.session_state['SS'] == 3:

        lat = 32.9
        long = -106.9
        eleva = 1400

        env = Environment(latitude=lat, longitude=long, elevation=eleva)
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        env.set_date((tomorrow.year, tomorrow.month, tomorrow.day, 12))  # Hour given in UTC time
        #env.set_atmospheric_model(type="Forecast", file="GFS")

        grain_in = st.session_state['grain_in_rad']
        grain_out = st.session_state['grain_out_rad']
        motor = SolidMotor(
                    thrust_source="Cesaroni_M1670.eng",
                    dry_mass=1.815,
                    dry_inertia=(0.125, 0.125, 0.002),
                    nozzle_radius=st.session_state['nozzle_radius'],
                    grain_number=5,
                    grain_density=1815,
                    grain_outer_radius=float(grain_out),
                    grain_initial_inner_radius=grain_in,
                    grain_initial_height=st.session_state['grain_initial_height'],
                    grain_separation=st.session_state['grain_separation'],
                    grains_center_of_mass_position=0.397,
                    center_of_dry_mass_position=0.317,
                    nozzle_position=st.session_state['nozzle_pos'],
                    burn_time=3.9,
                    throat_radius=st.session_state['throat_radius'],
                    coordinate_system_orientation="nozzle_to_combustion_chamber",
                    )
                
        
        calisto = Rocket(
                radius=st.session_state['calisto_radius'], #variable
                mass=14.4,
                inertia=(6.321, 6.321, 0.034),
                power_off_drag="powerOffDragCurve.csv",
                power_on_drag="powerOnDragCurve.csv",
                center_of_mass_without_motor=0,
                coordinate_system_orientation="tail_to_nose",
            )
        rail_buttons = calisto.set_rail_buttons(
                upper_button_position=st.session_state['upper_button_pos'],
                lower_button_position=st.session_state['lower_button_pos'],
                angular_position=45,)
        nose_cone = calisto.add_nose(
                length=st.session_state['nosecone_length'], kind="vonKarman", position=st.session_state['nose_cone_pos'] #variable
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
                top_radius=st.session_state['tail_topradius'], bottom_radius=st.session_state['tail_bottomradius'], length=0.060, position=-1.194656 #variable
            )
        calisto.add_motor(motor, position=-1.255) https://github.com/RayanIsMe/StellarThrustRocketPy/blob/main/capstone.py

        Main = calisto.add_parachute(
            "Main",
            cd_s=10.0,
            trigger=800,
            sampling_rate=105,
            lag=1.5,
            noise=(0, 8.3, 0.5),
        )
        
        Drogue = calisto.add_parachute(
            "Drogue",
            cd_s=1.0,
            trigger="apogee",
            sampling_rate=105,
            lag=1.5,
            noise=(0, 8.3, 0.5),
        )

        test_flight = Flight(
                rocket=calisto, environment=env, rail_length=5.2, inclination=85, heading=0
                    )
        
        
        with st.button("Back"):
                st.sesssion_state['SS'] = 2
                st.rerun()
        with st.container(border = True):
                st.header("Simulated Flight Results")
                flightp = _FlightPlots(test_flight)
                flightp.trajectory_3d()
                flightp.angular_kinematics_data()
                flightp.aerodynamic_forces()
                flightp.energy_data()
                st.image('flight1.jpg')
                st.image('vital.png')
                st.image('flight3.jpg')
                st.image('flight5.jpg')

        test_flight.export_kml(file_name="test_flight.kml")
        with open("test_flight.kml",'rb') as file:
                st.download_button(
                    label = "Download KML File",
                    data = file,
                    file_name = "test_file.kml",
                    mime = "application/vnd.google-earth.kml+xml"
                )
