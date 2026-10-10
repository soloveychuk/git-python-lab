# iot_tool.py
# Collaborative engineering automation and embedded systems computation toolkit
import math

def print_banner():
    print("==========================================================")
    print("=== IoT & Embedded Systems Engineering Toolkit v1.0   ===")
    print("==========================================================")


# ====================================================================
# DEVELOPER ZONE: STUDENTS MUST WRITE CODE EXCLUSIVELY INSIDE THEIR FUNCTION
# ====================================================================

def calculate_variant_1():
    print("\n[Variant 1: Servomotor Control Systems]")
    # DEVELOPER 1: Read theta and omega. Calculate t = theta / omega.
    # Perform bitwise AND between integer theta and 0xFF. Servomotor name, list of angles.
    angle = float(input("Введіть кут повороту ротора (в градусах): "))
    angular_velocity = float(input("Введіть кутову швидкість ротора (в градусах на секунду): "))
    time = angle / angular_velocity
    print(f"Час повороту: {time}")
    a = int(angle) & 0xFF
    print(f"«Логічне множення» між цілочисельним значенням кута та маскою 0xFF у двійковій формі: {bin(a)}")

    name = input("Введіть назву сервопривода: ")
    print(" У назві є дефіс\n", f"Назва моделі: {name[(name.find('-') + 1):].upper()}") if '-' in name else print("У назві немає дефіса")

    angles = [0, 45, 90, 135, 180]
    angles[2] = 100
    angles.append(270)
    print(f"Допустимі кути: {angles}")

    voltage_range = (1.5, 5)
    print(f"Діапазон напруг: {voltage_range}")

    motor = {
     "id": 12345,
     "torque": 56.6,
     "modes": ["position", "speed", "position"]
     }

    unique_modes = set(motor["modes"])
    print(f"Унікальні режими: {unique_modes}")

    print("Так") if ("position" in unique_modes) and (motor["torque"] > 10) else print("Ні")
    pass


def calculate_variant_2():
    print("\n[Variant 2: Analog-to-Digital Conversion]")
    # DEVELOPER 2: Read 10-bit ADC and Vref = 5.0. Calculate V = (ADC / 1023) * Vref.
    # Apply bitwise left shift ADC << 2. Validate sensor marking, list of voltages.
    pass


def calculate_variant_3():
    print("\n[Variant 3: Battery Pack Monitoring]")
    # DEVELOPER 3: Read capacity E and power P. Calculate t = E / P.
    # Perform bitwise OR between integer E and P. Reverse LiFePO4 string, cell voltages.
    pass


def calculate_variant_4():
    print("\n[Variant 4: Stress and Strain Calculation]")
    # DEVELOPER 4: Read force F and area A. Mechanical stress sigma = F / A.
    # Apply bitwise right shift F >> 1. Material grade string and component strains.
    pass


def calculate_variant_5():
    print("\n[Variant 5: Unmanned Aerial Vehicle Telemetry]")
    H = float(input("Enter H value: "))
    V_z = float(input("Enter V_z value: "))
    t = H / V_z
    print(t)
    print(int(H) ^ int(V_z))
    pack = input("Enter telemetry pack: ")
    print("Pack is correct") if pack[0:6] == '$GPGGA' else print("Pack is incorrect")
    drone_dict = {'drone_id': '001', 'flight_mode': 'f3', 'active_sensors': ['IMU', 'CER', 'CAD', 'CER']}
    sensors_set = set(drone_dict['active_sensors'])
    print("Sensor exists") if ("IMU" in sensors_set) and H > 10 else print("Sensor doesn't exist")
    # DEVELOPER 5: Read altitude H and vertical speed Vz. Calculate t = H / Vz.
    # Perform bitwise XOR between H and Vz. Validate $GPGGA telemetry string, active sensors.
    pass


def calculate_variant_6():
    print("\n[Variant 6: Digital Communication Protocols]")
    # DEVELOPER 6: Read I2C bus frequency in kHz (F). Period T = 1000000 / (F * 1000).
    # Perform bitwise AND between frequency and 0x0F. USART_BAUDRATE string, rx buffer.
    pass


def calculate_variant_7():
    print("\n[Variant 7: Robot Kinematics Drive Calculation]")
    # DEVELOPER 7: Read gear ratio i and motor RPM Nin.
    # Output shaft Nout = Nin / i. Apply bitwise left shift Nin << 3. Manipulator link string.
    pass


def calculate_variant_8():
    print("\n[Variant 8: Hydraulics Parameter Control]")
    # DEVELOPER 8: Read pressure P and flow rate Q. Hydraulic power W = (P * Q) / 600.
    # Perform bitwise OR between integer P and Q. DTC diagnostic code, oil temperature list.
    pass


def calculate_variant_9():
    print("\n[Variant 9: Climate Control and Ventilation Systems]")
    # DEVELOPER 9: Read heater power (P) and runtime (t). Thermal energy Q = P * t.
    # Perform bitwise XOR between power and time. PLC_HVAC controller identifier string.
    print('Введіть значення потужності, а потім час роботи ТЕНа')
    P=int(input())
    t=int(input())
    Q=P*t
    print('Отриманий результат на завдання 1:')
    print(Q,P^t)
    print("Введіть значення PLC_HVAC_Cabinet_01:")
    PLC_HVAC_Cabinet_01=input()
    k=len(PLC_HVAC_Cabinet_01)
    a=(True if PLC_HVAC_Cabinet_01[k-2:k]=="01" else False)
    print('Отриманий результат на завдання 2:')
    print(a, PLC_HVAC_Cabinet_01[k-10:k].lower())
    pass


def calculate_variant_10():
    print("\n[Variant 10: Orientation and Navigation Systems (IMU)]")
    # DEVELOPER 10: Read Ax, Ay, Az. Total acceleration A = sqrt(Ax^2 + Ay^2 + Az^2).
    # Apply bitwise right shift Az >> 2. Raw data ACC:X=... string, Euler angles.
    pass


def calculate_variant_11():
    print("\n[Variant 11: BLDC Motor Control Systems]")
    # DEVELOPER 11: Read PWM duty cycle (DUTY) and supply voltage Vdc. Vphase = (DUTY/100)*Vdc.
    # Perform bitwise AND between integer DUTY and 0b11110000. Hall sensors state string.
    Duty = int(input('Duty='))
    Vdc = int(input('Vdc='))
    Vphase = (Duty/100)*Vdc
    print('Vphase=', Vphase)
    pass


def calculate_variant_12():
    print("\n[Variant 12: Optical Encoder Data Acquisition]")
    # DEVELOPER 12: Read PPR and total pulses N. Revolutions (N // PPR), remainder (N % PPR).
    # Apply bitwise left shift N << 1. ENC-OPT encoder serial number, measurement list.
    pass


def calculate_variant_13():
    print("\n[Variant 13: Industrial Modbus RTU Network]")
    # DEVELOPER 13: Read 16-bit Modbus register value R.
    # Split into High and Low bytes, print both in binary format.
    pass


# ====================================================================
# MAIN EXECUTION MODULE (TEAM LEAD UNCOMMENTS DURING INTEGRATION)
# ====================================================================
if __name__ == "__main__":
    print_banner()
    
    calculate_variant_1()
    # calculate_variant_2()
    # calculate_variant_3()
    # calculate_variant_4()
    calculate_variant_5()
    # calculate_variant_6()
    # calculate_variant_7()
    # calculate_variant_8()
    calculate_variant_9()
    # calculate_variant_10()
    # calculate_variant_11()
    # calculate_variant_12()
    # calculate_variant_13()
