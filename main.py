from lanzador import Lanzador

if __name__ == '__main__':

    lanzador = Lanzador()
    lanzador.lanzar_scrappers()
    lanzador.lanzar_analisis()
    lanzador.lanzar_prediccion()
    
    lanzador.obtener_datos()
    lanzador.lanzar_apuestas('apuestas')
    lanzador.lanzar_clientes()
    lanzador.lanzar_cuotas()
    lanzador.lanzar_equipos()
    lanzador.lanzar_partidos()