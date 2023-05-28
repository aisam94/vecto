import struct
import json

def convert_data(voltage, energy, current):
    numbers = [voltage, energy, current]
    packed_data = struct.pack('!HHH', *numbers)
    return packed_data

def read_bytes(data):
    padded_data = data.ljust(3, b'\x00')
    # Unpack the values from the 3-byte array
    voltage, energy, current = struct.unpack('!HHH', padded_data)

    decoded_data = {
        'Voltage': voltage,
        'Energy': energy,
        'Current': current
    }

    json_str = json.dumps(decoded_data)

    return json_str

# Example
voltage=254
energy=1450
current=1580

test_data = convert_data(voltage, energy, current)
print(test_data)
json_data = read_bytes(test_data)
print(json_data)

