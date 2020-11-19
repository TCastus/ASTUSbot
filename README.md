# ASTUSbot

## Présenation

Bot discord pour la gestion du serveur de l'ASTUS  

 - Quelques comandes simple pour la gestion des rôles  
 - Commande d'aide avec des réponses rapide sur certains sujet qui sont aussi aborder dans [TChelp](https://github.com/TCastus/TChelp) 

## Docker run

 - Cloner le projet  
 ``git clone https://github.com/TCastus/ASTUSbot``
 - Racine du projet  
 ``cd ASTUSbot``
 - Docker build  
 ``docker build --tag astusbot .``
 - Changer les valeurs dans le fichier ``.env``
 - Docker run  
 ``docker run -itd --rm --env-file .env --name container_astusbot astusbot``