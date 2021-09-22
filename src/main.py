from house import get_page_source
from house import get_abs_paths
from house import get_years_from_url
from house import extract_zip_url_as_list

base_url = "https://disclosures-clerk.house.gov/PublicDisclosure/FinancialDisclosure"

page_source = get_page_source(base_url)
abs_paths = get_abs_paths(page_source, base_url)
years = get_years_from_url(abs_paths)

database = {}
for (year, abs_path) in zip(years, abs_paths):
    database[year] = extract_zip_url_as_list(abs_path)

print([(key, len(database[key])) for key in database.keys()], sep='\n')
# zippath = 'C:\\Users\\lauke\\Downloads\\2016FD.zip'
