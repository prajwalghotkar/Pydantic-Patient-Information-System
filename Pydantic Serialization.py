from pydantic import BaseModel, Field
from typing import Optional, List

class Address(BaseModel):
    """Address model with validation"""
    city: str = Field(..., min_length=2, description="City name")
    state: str = Field(..., min_length=2, description="State name")
    pin: str = Field(..., min_length=5, max_length=6, description="Postal code")

class Patient(BaseModel):
    """Patient model with nested address"""
    name: str = Field(..., description="Patient's full name")
    gender: str = Field(default='Male', description="Gender identity")
    age: int = Field(..., ge=0, le=120, description="Age in years")
    address: Address
    phone: Optional[str] = Field(None, description="Contact number")

address_dict = {'city': 'Austin', 'state': 'Texas', 'pin': '73301'}
address1 = Address(**address_dict)

patient_dict = {'name': 'Prajwal_G', 'age': 24, 'address': address1}
patient1 = Patient(**patient_dict)

print("=" * 60)
print("PYDANTIC SERIALIZATION EXAMPLES")
print("=" * 60)

print("\n1. Default model_dump():")
default_serialized = patient1.model_dump()
print(default_serialized)
print("Type:", type(default_serialized))

print("\n2. Exclude unset fields:")
exclude_unset_serialized = patient1.model_dump(exclude_unset=True)
print(exclude_unset_serialized)
print("Type:", type(exclude_unset_serialized))

print("\n3. Include only name and age:")
include_serialized = patient1.model_dump(include={'name', 'age'})
print(include_serialized)

print("\n4. Exclude address:")
exclude_serialized = patient1.model_dump(exclude={'address'})
print(exclude_serialized)

print("\n5. JSON serialization:")
json_serialized = patient1.model_dump_json()
print(json_serialized)
print("Type:", type(json_serialized))

print("\n6. JSON-compatible serialization:")
json_compatible = patient1.model_dump(mode='json')
print(json_compatible)

print("\n7. Exclude nested fields (pin from address):")
nested_exclude = patient1.model_dump(exclude={'address': {'pin'}})
print(nested_exclude)

print("\n" + "=" * 60)
print("PATIENT WITH ALL FIELDS SET")
print("=" * 60)

patient2_dict = {
    'name': 'Sarah Johnson',
    'gender': 'Female',
    'age': 30,
    'address': address1,
    'phone': '+1-555-0123'
}
patient2 = Patient(**patient2_dict)

print("All fields set - model_dump():")
print(patient2.model_dump())

print("\nAll fields set - exclude_unset=True:")
print(patient2.model_dump(exclude_unset=True))  # Will include phone since it's set

print("\n" + "=" * 60)
print("ADVANCED: USING FIELD ALIASES")
print("=" * 60)

class PatientWithAlias(BaseModel):
    """Patient model with field aliases"""
    full_name: str = Field(..., alias='name')
    gender: str = Field(default='Male')
    age: int = Field(..., ge=0, le=120)
    location: Address = Field(..., alias='address')
    
    class Config:
        populate_by_name = True

patient_alias = PatientWithAlias(
    name='Michael Chen',
    age=28,
    location=address1
)

print("With aliases - default (use field names):")
print(patient_alias.model_dump())

print("\nWith aliases - by_alias=True (use alias names):")
print(patient_alias.model_dump(by_alias=True))