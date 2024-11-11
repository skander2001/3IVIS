import csv
from django.core.management.base import BaseCommand
from charts.models import SalesData
from pathlib import Path


class Command(BaseCommand):
    help = 'Imports sales data from a CSV file located in the data folder'

    def handle(self, *args, **kwargs):
        data_file = Path(__file__).resolve().parent.parent.parent.parent / 'data' / 'sales_data.csv'

        # Print the full path to check if it's correct
        print(f"Looking for file at: {data_file}")

        if data_file.exists():
            with open(data_file, mode='r') as file:
                reader = csv.DictReader(file)

                # Debugging: print the fieldnames to verify column names
                print(f"CSV Column Names: {reader.fieldnames}")

                for row in reader:
                    try:
                        # Strip leading/trailing whitespace from the column names and values
                        month = row['Month'].strip()
                        sales = int(row[' Sales'].strip())  # Notice the extra space in ' Sales'

                        SalesData.objects.create(
                            month=month,
                            sales=sales
                        )
                    except KeyError as e:
                        print(f"Missing column in CSV: {e}")

            self.stdout.write(self.style.SUCCESS('Successfully imported sales data'))
        else:
            self.stdout.write(self.style.ERROR(f'CSV file not found at: {data_file}'))
