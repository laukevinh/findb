from src.orm.statements import delete_rows_by_year
from orm.tables import house
from orm.settings import CONNECTION
from sqlalchemy import create_engine
from ingest.house import get_page_source
from ingest.house import get_abs_paths
from ingest.house import get_years_from_url
from ingest.house import extract_zip_url_as_list
from orm.statements import insert_transactions
from orm.statements import get_data_by_year

base_url = "https://disclosures-clerk.house.gov/PublicDisclosure/FinancialDisclosure"

page_source = get_page_source(base_url)
abs_paths = get_abs_paths(page_source, base_url)
years = get_years_from_url(abs_paths)

data = {}
for (year, abs_path) in zip(years, abs_paths):
    data[year] = extract_zip_url_as_list(abs_path)

engine = create_engine(CONNECTION, future=True)
for year in years:
    delete_rows_by_year(engine, house, year)

for (year, transactions) in data.items():
    insert_transactions(engine, house, transactions)

print([(key, len(data[key])) for key in data.keys()], sep='\n')
print([(key, len(get_data_by_year(engine, house, key)))
      for key in data.keys()])
# zippath = 'C:\\Users\\lauke\\Downloads\\2016FD.zip'
