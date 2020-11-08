class SportBuild:
    def __init__(self, number_of_seats=None, year_of_foundation=None, location=None, scale_of_field=None,
                 name_of_sport=None):
        self.number_of_seats = number_of_seats
        self.year_of_foundation = year_of_foundation
        self.location = location
        self.scale_of_field = scale_of_field
        self.name_of_sport = name_of_sport

    def __str__(self):
        return f"NumberOfSeats:{self.number_of_seats} YearOfFoundation:{self.year_of_foundation}" \
               f" Location:{self.location} ScaleOfField:{self.scale_of_field} NameOfSport:" \
               f"{self.name_of_sport} "
