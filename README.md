# Pydantic Patient Information System

##### Structured Data Organization:
- Patient information is logically organized with nested models
- Address and vitals are separate models that can be reused

##### Comprehensive Validation:
- Field constraints (min/max values, string lengths)
- Automatic validation of nested models
- Custom validation examples included

###### Serialization Capabilities:
- Easy conversion to JSON with proper formatting
- Control over what data to include/exclude

###### Real-world Practicality:
- Includes timestamp for when vitals were recorded
- Well-formatted output for display purposes
- Examples of both valid and invalid data

###### Type Safety:
- Full type hints throughout the code
- IDE support for autocompletion and error detection

This implementation demonstrates how Pydantic's nested models help create clean, maintainable, and robust data structures for applications like healthcare systems.
