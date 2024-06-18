import random
from colorama import *

print(Fore.CYAN + '''


██╗███╗   ███╗███████╗██╗
██║████╗ ████║██╔════╝██║
██║██╔████╔██║███████╗██║
██║██║╚██╔╝██║╚════██║██║
██║██║ ╚═╝ ██║███████║██║
╚═╝╚═╝     ╚═╝╚══════╝╚═╝
                                                                                           Ideaax
''')


country_data = {
    'Japan': {'mcc': '440', 'phone_number_length': 10},
    'UK': {'mcc': '234', 'phone_number_length': 10},
    'Canada': {'mcc': '302', 'phone_number_length': 10},
    'Philippines': {'mcc': '515', 'phone_number_length': 10},
    'China': {'mcc': '460', 'phone_number_length': 11},
    'Indonesia': {'mcc': '510', 'phone_number_length': 10},
    'Germany': {'mcc': '262', 'phone_number_length': 11},
    'Singapore': {'mcc': '525', 'phone_number_length': 8},
    'South Korea': {'mcc': '450', 'phone_number_length': 10},
    'France': {'mcc': '208', 'phone_number_length': 9},
    'USA': {'mcc': '310', 'phone_number_length': 10},
    'Albania': {'mcc': '276', 'phone_number_length': 9},
    'Algeria': {'mcc': '603', 'phone_number_length': 10},
    'Andorra': {'mcc': '213', 'phone_number_length': 9},
    'Angola': {'mcc': '631', 'phone_number_length': 9},
    'Antigua and Barbuda': {'mcc': '344', 'phone_number_length': 7},
    'Argentina': {'mcc': '722', 'phone_number_length': 10},
    'Armenia': {'mcc': '283', 'phone_number_length': 8},
    'Australia': {'mcc': '505', 'phone_number_length': 9},
    'Austria': {'mcc': '232', 'phone_number_length': 13},
    'Denmark': {'mcc': '238', 'phone_number_length': 8},
    'Djibouti': {'mcc': '631', 'phone_number_length': 8},
    'Dominica': {'mcc': '366', 'phone_number_length': 7},
    'Finland': {'mcc': '244', 'phone_number_length': 10},
    'Italy': {'mcc': '222', 'phone_number_length': 11},
    'Mexico': {'mcc': '334', 'phone_number_length': 10},
    'Norway': {'mcc': '242', 'phone_number_length': 8},
    'Poland': {'mcc': '260', 'phone_number_length': 9},
    'Peru': {'mcc': '716', 'phone_number_length': 9},
    'Romania': {'mcc': '226', 'phone_number_length': 10},
    'Rwanda': {'mcc': '635', 'phone_number_length': 9},
    'Ukraine': {'mcc': '255', 'phone_number_length': 9},
    'Russia': {'mcc': '250', 'phone_number_length': 10},
}


country_codes = {
    'Japan': '+81',
    'UK': '+44',
    'Canada': '+1',
    'Philippines': '+63',
    'China': '+86',
    'Indonesia': '+62',
    'Germany': '+49',
    'Singapore': '+65',
    'South Korea': '+82',
    'France': '+33',
    'USA': '+1',
    'Albania': '+355',
    'Algeria': '+213',
    'Andorra': '+376',
    'Angola': '+244',
    'Antigua and Barbuda': '+1',
    'Argentina': '+54',
    'Armenia': '+374',
    'Australia': '+61',
    'Austria': '+43',
    'Denmark': '+45',
    'Djibouti': '+253',
    'Dominica': '+1',
    'Finland': '+358',
    'Italy': '+39',
    'Mexico': '+52',
    'Norway': '+47',
    'Poland': '+48',
    'Peru': '+51',
    'Romania': '+40',
    'Rwanda': '+250',
    'Ukraine': '+380',
    'Russia': '+7',
}


def generate_phone_number_by_country(country_info):
    phone_number = ''.join([str(random.randint(0, 9)) for _ in range(country_info['phone_number_length'])])
    formatted_number = f"{country_codes[country_info['country']]}-{phone_number}"
    return formatted_number


def generate_imsi(mcc):
    mnc = random.randint(0, 99)
    msin = random.randint(100000000, 999999999)
    return f"{mcc}{mnc:02d}{msin}"

def generate_iccid(mcc):
    issuer_id = mcc
    individual_acc_num = random.randint(1000000000, 9999999999)
    check_digit = random.randint(0, 9)
    return f"89{issuer_id}{individual_acc_num}{check_digit}"

country_name = input("Enter the name of a country to display its details: ")

if country_name in country_data:
    country_info = country_data[country_name]
    country_info['country'] = country_name
    print("\nCountry Details:")
    print(f"Country: {country_name}")
    print(f"MCC: {country_info['mcc']}")
    print(f"Phone Number: {generate_phone_number_by_country(country_info)}")
    print(f"IMSI: {generate_imsi(country_info['mcc'])}")
    print(f"ICCID: {generate_iccid(country_info['mcc'])}")
else:
    print("Country not found in the database.")
