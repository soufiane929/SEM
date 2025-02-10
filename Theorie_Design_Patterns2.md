B# Theorie Design Patterns

In diesem Dokument werden zwei gängige Design Patterns vorgestellt: das Singleton-Pattern und das Observer-Pattern. Diese Muster helfen dabei, häufig auftretende Probleme auf eine strukturierte und wiederverwendbare Weise zu lösen.

## Singleton-Pattern

### Problem
Das Singleton-Pattern wird verwendet, um sicherzustellen, dass eine Klasse nur eine einzige Instanz hat und einen globalen Zugriffspunkt zu dieser Instanz bietet. Dies ist nützlich in Situationen, in denen genau ein Objekt benötigt wird, um die Koordination von Aktionen im System zu steuern, z.B. ein Konfigurationsmanager oder eine Datenbankverbindung.

### Umsetzung
Das Singleton-Pattern wird typischerweise durch eine private statische Variable und eine öffentliche statische Methode implementiert, die die einzige Instanz der Klasse zurückgibt. Der Konstruktor der Klasse ist privat, um zu verhindern, dass andere Klassen neue Instanzen erstellen.

### Idee dahinter
Die Idee hinter dem Singleton-Pattern ist es, eine zentrale Instanz zu haben, die von verschiedenen Teilen des Programms genutzt werden kann, ohne dass mehrere Instanzen erstellt werden. Dies spart Ressourcen und stellt sicher, dass alle Teile des Programms die gleiche Instanz verwenden.

```python
class Singleton:
    _instance = None

    @staticmethod
    def get_instance():
        if Singleton._instance is None:
            Singleton()
        return Singleton._instance

    def __init__(self):
        if Singleton._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Singleton._instance = self
