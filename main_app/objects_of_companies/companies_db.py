class AllCompanies:

    def __init__(self):
        self.companies = []

    def add_new_company_object(self, new_company):
        self.companies.append(new_company)

    def find_company(self, id):
        for company in self.companies:
            if company.name == id:
                return company

    def compare_two_list_of_documents(self, first_company, second_company, name):
        diff = []
        for invoice in first_company:
            if invoice not in second_company:
                diff.append(f"{invoice} missing in {name}")
                continue
            if first_company[invoice] != -second_company[invoice]:
                diff.append(f"{invoice} amount is not matched")
        return diff

    def difference_checker(self):
        differences = {} # Company: { comp : [reason1, reason2] }
        for company in self.companies:
            differences[company.name] = {}
            for ic in company.intercompany:
                find_company = self.find_company(ic)
                if find_company is None:
                    differences[ic] = {}
                    differences[company.name][ic] = f"All invoices are missing in {ic}"
                    continue
                if company.name not in find_company.intercompany:
                    continue

                diff = (
                    self.compare_two_list_of_documents(company.intercompany[find_company.name], find_company.intercompany[company.name], find_company.name))

                if not diff:
                    continue

                differences[company.name][ic] = diff

        return differences


class SingleCompany:

    def __init__(self, name: str):
        self.name = name
        self.intercompany = {}

    def check_if_company_exist(self, company_id):
        if company_id not in self.intercompany.keys():
            self.intercompany[company_id] = {}

    def add_invoices(self, invoice_number, price, company_name):
        self.intercompany[company_name][invoice_number] = price
