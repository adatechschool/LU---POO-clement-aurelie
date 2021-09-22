# Expliquer

Concepts

    Encapsulation
    Fonctions et variables reliées sont combinées en unité, appelé "objet". Les variables sont alors des "propriétés" (properties), et les fonctions des "méthodes".
    
    Abstraction
    Pour faciliter la compréhension, et / ou protéger certaines données, on cache l'implémentation de certains détails
    Ex en JS : utiliser des variables en let pour limiter le scope
    
    Héritage
    On peut récupérer les propriétés que d'1 seul parent.
    Permet d'éliminer du code redondant, en regroupant les fonctions identiques à plusieurs instances, dans la classe parent.
    
    Polymorphisme
    Un constructeur ou une fonction peut être adapté en fonction des classes. Favorise la refacto !
    
    Classe vs. Instance
    Il existe différentes strates de classes entre "parent" et "enfant". La classe représente l'objet (un moule), et l'instance est l'application (l'objet appliqué).



Éléments de programmation

    Classe
    Elle comprend le nom de l'objet, le constructeur qui reprend les propriétés (ou def __init__ en python), et les méthodes (fonctions) communes
    
    this / self : definit dans le constructeur (ou def __init__) pour rappeler les propriétés de la classe. JS utilise this, Python self.
    
    Constructeur : reprend les propriétés de la classe
    
    Méthode : représente les fonctions
    
    Attribut / propriété / membre : -attribut: Caractéristique de la classe  -propriété: variable définie dans une classe
    
    Interface :  squelette de la classe / ensemble des méthodes listé avant qu'elles n'aient été appelées

