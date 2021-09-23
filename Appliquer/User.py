from enum import Enum

class UserRole(Enum):
    VISITOR = 'visitor'  # Peut consulter des articles
    WRITER = 'writer'  # Peut consulter des articles et en écrire
    ADMIN = 'admin'  # Peut consulter, écrire et supprimer des articles

class Permission(Enum):
    READ = 'read'
    WRITE = 'write'
    DELETE = 'delete'

class User:
    def __init__ (self, name):
        self.name = name

    def can(self, permission: Permission) -> bool:
        return True if permission == Permission.READ else False

class Admin(User):
    def __init__(self, name):
        super().__init__(name)

    def can(self, permission: Permission) -> bool:
        return True

class Writer(User):
    def __init__(self, name):
        super().__init__(name)

    def can(self, permission: Permission) -> bool:
        return False if permission == Permission.DELETE else True

class Visitor(User):
    def __init__(self, name):
        super().__init__(name)


def get_user(name: str) -> User:    
    if name == "chloe":
        return Admin(name)
    if name == "alya": 
        return Writer(name)
    if name == "visitor":
        return Visitor(name)

USERS = {
    "chloe": UserRole.ADMIN,
    "alya": UserRole.WRITER,
    "visitor": UserRole.VISITOR
}

class Article:
    def __init__(self, title, author, text):
        self.title = title
        self.author = author
        self.text = text

        
def display_article(article):
    print("")
    print("-" * 4 + article.title + "-" * 4)
    print(f"Auteur : {article.author.name}")
    print(f"\\n{article.text}\\n")
    print("-" * (len(article.title) + 8))
    print("")

def write_article():
    """
    Écriture et enregistrement d'un nouvel article
    """
    if not current_user.can(Permission.WRITE):
        return

    author = current_user

    print("Quel est le titre de l'article ?")
    title = input("> ")

    print("Quel est le contenu de l'article ?")
    text = input("> ")

    # TODO: créer un nouvel Article à partir des données collectées et l'ajouter à la variable `articles`




  
if __name__ == '__main__':
    print("---- Bienvenue dans le Low-Tech Blog! ----")

    while True:
        print(f"Qui va là ?")
        print(f"({', '.join([f'{u}: {r.value}' for u, r in USERS.items()])} – autre chose pour quitter)")
        user_name = "chloe"

        if user_name not in USERS:
            print("Y a rien à voir ici, circulez !")
            exit(1)
        
        # Récupère la bonne instance de User pour le nom entré
        current_user = get_user(user_name)
        
        print(f"Salut, {current_user.name} ! Que veux-tu faire aujourd'hui ?")

        # Liste les actions disponibles pour l'utilisateur courant
        # -> celles qui ne nécessitent aucune permission et celles que `current_user` a le droit d'effectuer
        possible_actions = [a for a in ACTIONS if a.get("permission") is None or current_user.can(a["permission"])]

        while True:
            # Affiche les actions disponibles à l'utilisateur
            for idx, action in enumerate(possible_actions):
                print(f"{idx + 1} -> {action['label']}")