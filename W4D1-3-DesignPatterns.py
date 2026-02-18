#Scenario: Presidents Offcial Pen
#Singleton design pattern
#why?
#only one class exsists
#prevents accidental duplication


class OfficialPen:
    __instance = None  # Private class variable

    def __new__(cls):
        if cls.__instance is None:
            print("Creating the President's Official Pen...")
            cls.__instance = super(OfficialPen, cls).__new__(cls)
            cls.__instance.ink_color = "Black"
            cls.__instance.serial_number = "PRES-001"
        return cls.__instance

    def sign_document(self, document_name):
        print(f"Signing '{document_name}' with the official pen (Serial: {self.serial_number}).")


# Usage
pen1 = OfficialPen()
pen2 = OfficialPen()

pen1.sign_document("Economic Reform Bill")
pen2.sign_document("International Treaty")

# Verify both variables reference the same instance
print(pen1 is pen2)

#Scenario: Car Manufacturing Plant
#