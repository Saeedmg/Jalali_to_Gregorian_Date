import sys
import jdatetime

def convert_persian_to_english_date(persian_date):
    try:
        # Split the date input (year/month/day)
        year, month, day = map(int, persian_date.split('/'))
        gregorian_date = jdatetime.date(year, month, day).togregorian()
        
        # Format the date in full American format
        formatted_date = gregorian_date.strftime('%B %d, %Y')  # Full American format
        return formatted_date  # Return the formatted date as a string
    except Exception:
        return None  # Return None on error

def main():
    if len(sys.argv) != 2:
        return  # Exit if the incorrect number of arguments

    persian_date = sys.argv[1]  # Get the date from command line argument
    converted_date = convert_persian_to_english_date(persian_date)

    # Print the converted date to standard output, only if valid
    if converted_date:
        print(converted_date)

if __name__ == "__main__":
    main()
