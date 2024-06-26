from src.db.models.owner import Owner
#from src.db.models.book import Book
from typing import Optional

class MenuDisplay:
    @staticmethod
    def display_main_menu():
        print("""
            WELCOME TO MY READ APP
              
              MENU
              -----------
              1. DATA MANIPULATION
              2. DATA QUERY
              00.QUIT              
        """)

    @staticmethod
    def display_DM_menu():
        print("""
            MENU -> DATA MANIPULATION

            1. INSERT OWNER
            2. INSERT TENANT
            3. INSERT FLAT DETAILS
            99. BACK
        """)

    @staticmethod
    def display_DQ_menu():
        print("""
            MENU -> DATA QUERY

            1. How much is the monthly income of the owner 'Ravindra'? 
            2. How much is the monthly income of the owner 'Sayli'?
            3. Fetch details of specific tenant based on tenant id with owner ?:
            4. How many properties own by each owner?
            5. When Owner will notification to post the add or tenant for renewal of contract.?
            6. How much specific tenant spent on the rent yearly?  
            99. Back
        """)

class DataInput():

    @staticmethod
    def input_for_owner_insert():
        flat_owner_id = int(input('Enter flat_owner_id: '))
        flatno = int(input('Enter the flatno: '))
        bank_details = input('Enter bank_details first bank name and the account no: ')
        owner_first_name = (input("Enter Owner's First Name: "))
        owner_last_name = (input("Enter Owner's Last Name: "))
        owner_age = (input("Enter age: "))
        owner_gender = (input("Enter Gender 'F/N' : "))
        owner_contact_no = (input("Enter contact no: "))
        owner_email = (input("Enter email id: "))

        owner = {
            "first name" : owner_first_name,
            "last name" : owner_last_name,
            "age" : owner_age,
            "gender" :owner_gender,
            "contact no" : owner_contact_no,
            "email" : owner_email
        }

        return {
            "flat_owner_id": flat_owner_id,
            "flatno": flatno,
            "bank_details": bank_details,
            "owner": owner 
        }
    
    # @staticmethod
    # def input_for_DQ_option_one():
    #     format_ = input('Enter a format(ebook, hardcover): ')
    #     title = input('Enter title (Mr, Mrs, Dr): ')

    #     return {
    #         "format_": format_,
    #         "title": title
    #     }

def main():
    
    while True:
        MenuDisplay.display_main_menu()
        option: int = int(input('Choose an option to continue: '))

        if option == 1:
            # TODO: opertion for Manipulation
            while True:
                MenuDisplay.display_DM_menu()
                option: int = int(input('Choose an option to continue: '))

                if option == 1:
                    # TODO: INSERT READER
                    Owner_detail: dict[str,str] = DataInput.input_for_owner_insert()
                    owner: Optional['Owner'] = Owner.insert_data(**Owner_detail)

                    if owner:
                        print(f'Reader with username: {owner.flat_owner_id} inserted successfully')
                    else:
                        print('Insertion failed')                   
                elif option == 2:
                    # TODO: INSERT BOOK
                    pass
                elif option == 3:
                    # TODO: INSERT MYREAD
                    pass
                elif option == 99:
                    break
                else:
                    print('Option not recognized. Please, try again.')
        elif option == 2:
            # TODO: Operations for Query
            while True:
                MenuDisplay.display_DQ_menu()
                option: int = int(input('Choose an option to continue: '))

                if option == 1:
                    data = DataInput.input_for_DQ_option_one()
                    result = Book.list_title_by_format_and_reader_title(**data)
                    if result:
                        print('\nTitle\n','-'*20)
                        for title in result:
                            print(title)
                    else:
                        print('No data found')
                    
                    input('\nEnter to continue')

                elif option == 2:
                    pass
                elif option == 3:
                    pass
                elif option == 4:
                    break
                elif option == 5:
                    pass
                elif option == 99:
                    break
                else:
                    print('Option not recognized. Please, try again.')
        elif option == 0:
            print('Thanks for visiting.')
            break

        else:
            print('Option not recognized. Please, try again.')


if __name__ == '__main__':
    main()