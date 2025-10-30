### Changes to this file is NOT allowed!
### Submission of this file will be IGNROED by the autograder!


class ContactCard(object):
    def __init__(self, name, phone_number, age, city):
        self.name = name
        self.phone_number = phone_number
        self.age = age
        self.city = city
        self.next = None

    def getNext(self):
        """
        Get the next contact node
        :return:
        """
        return self.next

    def setNext(self, new_next):
        """
        Set the next contact node
        :param new_next:
        :return:
        """
        self.next = new_next

    def replicate(self):
        """
        Create a replicate node with the same attributes.
        Note: the replicated node will have next pointer points to None.
        :return: The replicated node
        """
        return ContactCard(self.name, self.phone_number, self.age, self.city)


    def __str__(self):
        return f"Contact Detail\nName: {self.name}\nPhone number: {self.phone_number}\nAge: {self.age}\nCity: {self.city}"


if __name__ == '__main__':
    node = ContactCard("test", "8881010010", 23, "Amherst")
    rep_node = node.replicate()

    assert rep_node.next is None
