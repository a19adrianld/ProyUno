import var

class Eventos():
    def Saludos(self):
        '''
        Módulo para cerrar el programa
        :return:
        '''
        try:
            sys.exit()
        except Exception as error:
            print('Error %s' % str(error))
