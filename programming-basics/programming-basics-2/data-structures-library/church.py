# Church Class Implementation

class Church:
    """Represents a church in a database of wooden churches"""
    
    def __init__(self, name="", year=0, place="", material="wood"):
        """Initialize a new church with provided details"""
        self.name = name
        self.year = year
        self.place = place
        self.material = material
    
    def __str__(self):
        """Return a string representation of the church"""
        return f"Church: {self.name}, built in {self.year} in {self.place}"
    
    def __repr__(self):
        """Return a developer-friendly representation of the church"""
        return f"Church('{self.name}', {self.year}, '{self.place}', '{self.material}')"
    
    def get_age(self, current_year=2023):
        """Calculate the age of the church"""
        return current_year - self.year if self.year > 0 else 0
