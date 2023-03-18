# Modules example (continued):

# importing the entire converters module
import converters
converters.kg_to_lbs(5)


# importing one function in the converters module
from converters import lbs_to_kg
lbs_to_kg(5)  # We don't need to write converters. here



from converters import find_max
print(find_max([10, 3, 6, 2]))