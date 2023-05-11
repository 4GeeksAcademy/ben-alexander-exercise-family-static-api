from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        self._members = [
            {
                "id": self._generateId(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers":[7, 13, 22]
            },
            {
                "id": self._generateId(),
                "first_name": "Jane",
                "last_name": last_name,
                "age": 35,
                "lucky_numbers":[10, 14, 3]
            },
            {
                "id": self._generateId(),
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": 5,
                "lucky_numbers":[1]
            }
        ]

    def _generateId(self):
        return randint(0, 99999999)

    
    def delete_member(self, id):
        members = list(filter(lambda x: x["id"] == id, self._members))
        return members
        

    def get_member(self, id):
        member = list(filter(lambda x: x["id"] == id, self._members))
        return member

    
    def get_all_members(self):
        return self._members
        
    def add_member(self, member):
        member["id"] = self._generateId()
        self._members.append(member)
        return None
