import var
class Clientes():

    def validarDni(dni):
        '''
        Código que controla si el dni o el nie es correcto
        :return:
        '''
        try:
            tabla = 'TRWAGMYFPDXBNJZSQVHLCKE'
            dig_ext = 'XYZ'
            reemp_dig_ext = {'x': '0', 'Y': '1', 'Z': '2'}
            numeros = '0123456789'
            dni = dni.upper()
            if len(dni) == 9:
                dig_control = dni[8]
                dni = dni[:8]
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                return len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23 ] == dig_control

        except:
            print('Error módulo validar DNI')
            return None
    def validarDni(selfself):

        try:
            dni = var.ui.EditDNI.text()
            if Clientes.validarDni(dni):
                var.ui.LblValidar.setStylesheet('QLabel {color: green;}')
                var.ui.LblValidar.setText('V')
                var.ui.EditDNI.setText(dni.upper())
            else:
                var.ui.LblValidar.setStylesheet('QLabel {color: red;}')
                var.ui.LblValidar.setText('X')
                var.ui.EditDNI.setText(dni.upper())

        except:
            print('Error módulo validar DNI')
            return None