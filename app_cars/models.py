from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

# Create your models here.
state_choice = (
    ("AL", "Alabama"),
    ("AK", "Alaska"),
    ("AZ", "Arizona"),
    ("AR", "Arkansas"),
    ("CA", "California"),
    ("CO", "Colorado"),
    ("CT", "Connecticut"),
    ("DE", "Delaware"),
    ("FL", "Florida"),
    ("GA", "Georgia"),
    ("HI", "Hawaii"),
    ("ID", "Idaho"),
    ("IL", "Illinois"),
    ("IN", "Indiana"),
    ("IA", "Iowa"),
    ("KS", "Kansas"),
    ("KY", "Kentucky"),
    ("LA", "Louisiana"),
    ("ME", "Maine"),
    ("MD", "Maryland"),
    ("MA", "Massachusetts"),
    ("MI", "Michigan"),
    ("MN", "Minnesota"),
    ("MS", "Mississippi"),
    ("MO", "Missouri"),
    ("MT", "Montana"),
    ("NE", "Nebraska"),
    ("NV", "Nevada"),
    ("NH", "New Hampshire"),
    ("NJ", "New Jersey"),
    ("NM", "New Mexico"),
    ("NY", "New York"),
    ("NC", "North Carolina"),
    ("ND", "North Dakota"),
    ("OH", "Ohio"),
    ("OK", "Oklahoma"),
    ("OR", "Oregon"),
    ("PA", "Pennsylvania"),
    ("RI", "Rhode Island"),
    ("SC", "South Carolina"),
    ("SD", "South Dakota"),
    ("TN", "Tennessee"),
    ("TX", "Texas"),
    ("UT", "Utah"),
    ("VT", "Vermont"),
    ("VA", "Virginia"),
    ("WA", "Washington"),
    ("WV", "West Virginia"),
    ("WI", "Wisconsin"),
    ("WY", "Wyoming"),
)

feature_choices = (
    ('Cruise Control', 'Cruise Control'),
    ('Audi Interface', 'Audi Interface'),
    ('Airbags', 'Airbags'),
    ('Air Conditioning', 'Air Conditioning'),
    ('Seat Heating', 'Seat Heating'),
    ('Alarm System', 'Alarm System'),
    ('Park Assist', 'Park Assist'),
    ('Power Steering', 'Power Steering'),
    ('Reversing Camera', 'Reversing Camera'),
    ('Direct Fuel Injection', 'Direct Fuel Injection'),
    ('Auto Start/Stop', 'Auto Start/Stop'),
    ('Wind Deflector', 'Wind Deflector'),
    ('Bluetooth Handset', 'Bluetooth Handset'),
)

door_choices = (
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
)


class Car(models.Model):
    year_choices = []
    for r in range(2000, datetime.now().year + 1):
        year_choices.append((r, r))

    car_title = models.CharField(max_length=255)
    state = models.CharField(choices=state_choice, max_length=2)
    city = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    model = models.CharField('Car Model', max_length=100)
    year = models.IntegerField('Year of Manufacture', choices=year_choices)
    condition = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = RichTextField()
    car_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    car_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    body_style = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    interior = models.CharField(max_length=100)
    miles = models.PositiveIntegerField()
    doors = models.CharField(choices=door_choices, max_length=10)
    passengers = models.PositiveSmallIntegerField()  # Values from 0 to 32767
    vin_num = models.CharField(max_length=150)  # Vehicle Identification Number (VIN)
    milage = models.PositiveIntegerField()
    fuel_type = models.CharField(max_length=50)
    no_of_owners = models.PositiveSmallIntegerField()
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.car_title


test_choices = (
    ('Option 1', 'Option 1'),
    ('Option 2', 'Option 2'),
    ('Option 3', 'Option 3'),
)


class Test(models.Model):
    title = models.CharField(max_length=255)
    choices = MultiSelectField(choices=test_choices, default=())

    def save(self, *args, **kwargs):
        print(f"Saving Test instance: title={self.title}, choices={self.choices}")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
