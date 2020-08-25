class Object1:
    name = ""

    def get_name(self):
        return self.name

    def print_name(self):
        print(self.name)


test_object = Object1()
test_object.name = "hat"

print(test_object.get_name())

test_object.print_name()
