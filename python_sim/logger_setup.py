import logging
from datetime import datetime
import os

#TODO man kann einen File Handler benutzen um verschiedene Files in verschieden Logs zu leiten, brauch ich prob. nicht
#TODO Jeder Log in einem eigenen File, alte Logs archivieren

"""
Logging sind prinzipiell nur für Informative Sachen z.B. für Fehler die zwar passieren aber nicht schlimm sind oder umgangen werden
Für Fehler einfach einen Fehler raisen()
CRITICAL - 50
ERROR - 40
WARNING - 30
INFO - 20
DEBUG - 10
"""

def setup_logging(log_dir = "../logs"):
    # Sicherstellen, dass das Log-Verzeichnis existiert, wenn es es gibt kommt kein Fehler
    os.makedirs(log_dir, exist_ok=True)

    # Entfernt die Standard Handler von VSCode damit sie meine eigenen Handler nicht blockieren
    # Falls es nur mit Python läuft passiert nichts da Python normalerweise keine Handler startet
    # Remove all handlers from all existing loggers
    for logger_name in list(logging.root.manager.loggerDict.keys()):
        logger = logging.getLogger(logger_name)
        logger.handlers.clear()

    datum = datetime.now().strftime("%Y-%m-%d")
    log_name = f'{log_dir}/simulation_{datum}.log'  # Baut den Pfad auf

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)  # Welche Messages die mind. ist die im Logging eingetragen wird

    file_handler = logging.FileHandler(log_name, encoding='utf-8')                          # Handeled wo das File hingespeichert wird, etc.
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')   # Handeled welche Formatierung die Log-Einträge haben soll, etc.
    file_handler.setFormatter(formatter)                                                    # Formatter ist Teil vom File Handler
    root_logger.addHandler(file_handler)                                                         # Handler zum Logger hinzufügen
"""
def get_logger(name = __name__, log_dir = "../logs"):

    Gibt einen Logger zurück, der automatisch in eine Datei schreibt.
    - name: Name des Loggers (typischerweise __name__ des aufrufenden Moduls) => steht dann im Log File
    - log_dir: Verzeichnis für die Logdatei

    # Sicherstellen, dass das Log-Verzeichnis existiert, wenn es es gibt kommt kein Fehler
    os.makedirs(log_dir, exist_ok=True)

    datum = datetime.now().strftime("%Y-%m-%d")
    log_name = f'{log_dir}/simulation_{datum}.log'  # Baut den Pfad auf

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # Welche Messages die mind. ist die im Logging eingetragen wird

    # basic setup Funktioniert nicht gut mit VSCode eigenen Setups
    # Falls man mehrere Logger erstellt, wird nur ein Handler erstellt => braucht nur einen
    if not logger.handlers:
        file_handler = logging.FileHandler(log_name, encoding='utf-8')                          # Handeled wo das File hingespeichert wird, etc.
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')   # Handeled welche Formatierung die Log-Einträge haben soll, etc.
        file_handler.setFormatter(formatter)                                                    # Formatter ist Teil vom File Handler
        logger.addHandler(file_handler)                                                         # Handler zum Logger hinzufügen

    return logger
"""
def get_logger(name = __name__):
    return logging.getLogger(name)

def test():
    logger = get_logger()
    logger.debug('This message should go to the log file')
    logger.info('So should this')
    logger.warning('And this, too')
    logger.error('And non-ASCII stuff, too, like Øresund and Malmö')
    logger.critical("Oh no :(, Error!")