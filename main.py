from generator import SoapGenerator


if __name__ == "__main__": 

    words = ['Hola','oso','gato',"loro", "vehiculo"]

    soap = SoapGenerator(words)

    soap.create_soap()
    
    export_soap = soap.export()

    export_soap.to_image()
