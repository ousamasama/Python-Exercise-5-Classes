# Create a class that contains information about employees of a company 
# and define methods to get/set employee name, job title, and start date.

class Company:
    """This represents a company in which people work"""

    def __init__(self, company_name, date_founded):
        self.company_name = company_name
        self.date_founded = date_founded
        self.employees = set()

    def get_company_name(self):
        """Returns the name of the company"""

        return self.company_name

    def __str__(self):
        company_string_output = [f'{emp.name}' for emp in self.employees]
        return f'{(" and ").join(company_string_output)} work at {self.company_name} which was founded in {self.date_founded}.'


class Employee:
    def __init__(self, name, job_title, start_date):
        self.name = name
        self.job_title = job_title
        self.start_date = start_date

corgi_dad = Company("Ousama's Stupid Dogs", "2012")

olive = Employee("Olive", "Stupid Corgi 1", "2/24/12")
marcy = Employee("Marcy", "Stupid Corgi 2", "8/16/13")

corgi_dad.employees.update([olive, marcy])

print(corgi_dad)