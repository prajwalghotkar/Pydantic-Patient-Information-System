from pydantic import BaseModel, Field, ValidationError
from typing import Optional
import json
from datetime import datetime

class Address(BaseModel):
    """Address model representing a physical location"""
    city: str = Field(..., description="City name", example="Austin")
    state: str = Field(..., description="State or province", example="Texas")
    pin: str = Field(..., description="Postal code", example="73301", min_length=5, max_length=6)

class Vitals(BaseModel):
    """Vitals model representing patient health metrics"""
    blood_pressure: str = Field(..., description="Blood pressure reading", example="120/80")
    heart_rate: int = Field(..., description="Heart rate in BPM", example=72, ge=30, le=200)
    temperature: float = Field(..., description="Body temperature in Fahrenheit", example=98.6, ge=95.0, le=105.0)
    last_checked: datetime = Field(default_factory=datetime.now, description="When vitals were last recorded")

class Patient(BaseModel):
    """Patient model representing a medical patient"""
    name: str = Field(..., description="Full name of patient", example="Prawjal Ghotkar")
    gender: str = Field(..., description="Gender identity", example="male")
    age: int = Field(..., description="Age in years", example=24, ge=0, le=120)
    address: Address
    vitals: Optional[Vitals] = Field(None, description="Patient's vital signs")


address_dict = {'city': 'Austin', 'state': 'Texas', 'pin': '73301'}
address = Address(**address_dict)


vitals_dict = {
    'blood_pressure': '118/78',
    'heart_rate': 68,
    'temperature': 98.4
}
vitals = Vitals(**vitals_dict)

# Create patient instance for Prawjal Ghotkar
patient_dict = {
    'name': 'Prawjal Ghotkar', 
    'gender': 'male', 
    'age': 24, 
    'address': address,
    'vitals': vitals
}

patient = Patient(**patient_dict)

# Display the patient information
print("=" * 50)
print("PATIENT INFORMATION SYSTEM")
print("=" * 50)
print(f"Patient: {patient.name}")
print(f"Age: {patient.age}")
print(f"Gender: {patient.gender}")
print(f"Location: {patient.address.city}, {patient.address.state} {patient.address.pin}")

if patient.vitals:
    print("\nVITAL SIGNS:")
    print(f"Blood Pressure: {patient.vitals.blood_pressure}")
    print(f"Heart Rate: {patient.vitals.heart_rate} BPM")
    print(f"Temperature: {patient.vitals.temperature}°F")
    print(f"Last Checked: {patient.vitals.last_checked.strftime('%Y-%m-%d %H:%M')}")


print("\n" + "=" * 50)
print("SERIALIZED DATA (JSON)")
print("=" * 50)
print(json.dumps(patient.model_dump(), indent=2, default=str))


print("\n" + "=" * 50)
print("VALIDATION EXAMPLES")
print("=" * 50)


try:
    valid_address = Address(city="Austin", state="Texas", pin="73301")
    print("Valid address accepted")
except ValidationError as e:
    print("Valid address rejected:", e)


try:
    invalid_address = Address(city="A", state="T", pin="123")
    print("Invalid address accepted (unexpected)")
except ValidationError as e:
    print("Invalid address correctly rejected")


try:
    valid_patient = Patient(
        name="Prawjal Ghotkar",
        gender="male",
        age=24,
        address=address
    )
    print("Valid patient accepted")
except ValidationError as e:
    print("Valid patient rejected:", e)

try:
    invalid_patient = Patient(
        name="P",
        gender="unknown",
        age=150,
        address=address
    )
    print("Invalid patient accepted (unexpected)")
except ValidationError as e:
    print("Invalid patient correctly rejected")