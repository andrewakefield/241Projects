# Andrew Wakefield
from contact_card import ContactCard

class MyContacts(object):
    def __init__(self):
        self.head = None   # You have to store the head pointer in ``head'' variable.
        # No more instance variables are allowed.


    def loadFromFile(self, filename):
        """Creates a linked list of contacts from a user input text file

        Args: 
            filename: the name of the text file
        """
        with open(filename, "r") as f: # safely open the file in read mode
            prev = None
            for line in f:
                line = line.strip("\n") # remove new line characters to preserve format
                name, phone_number, age, city = line.split("|") # seperate and assign the instance variables
                c = ContactCard(name, phone_number, int(age), city) # create an instance of the class to store/manipulate contacts
                if self.head == None: self.head = c # if head hasn't been set yet, do so
                else: prev.setNext(c) # set next to create a linked list
                prev = c # update previous pointer
            

    def averageAge(self):
        """Calculates and returns the average age of the contacts in the linked list

        """
        current = self.head
        if current == None: return -1 # ensure the head of the list is not null
        sum = 0 # tracker for the sume of age
        count = 0 # tracker for the amount of people
        while current != None: # iterate through linked list
            sum += current.age # add the sum
            count += 1 # increment the count
            current = current.getNext()
        return sum / count # return and calculate the average


    def getContact(self, name):
        """Returns the contact card of a specific person

        Args:
            name: the name of the contact to retrieve

        Returns:
            str: the contact card of the person, None if not in list
        """
        current = self.head
        while current != None: # iterate through linked list
            if current.name == name: # filter out for the input name
                return current # if name is in list, return the contact
            current = current.getNext() 
        return None 


    def getContactsByCity(self, city):
        """Returns all of the contacts of a specific city

        Args:
            city: the city to retrieve contacts for

        Returns:
            linked list of contacts of specified city
        """
        head = None
        prev = None
        current = self.head
        while current != None: # iterate through the list
            if current.city == city: # ensure the current city is correct
                copy = current.replicate() # utilize replicate function to duplicate contact card
                if head == None: head = copy # set head if null
                else: prev.setNext(copy) # update next element creating a linked list
                prev = copy
            current = current.getNext()
        result = MyContacts() # create an instance object to return the linked list
        result.head = head
        return result
        

if __name__ == '__main__':
    pass