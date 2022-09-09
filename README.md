# ASTUSbot

## Présenation

Bot discord pour la gestion du serveur de l'ASTUS  

- Quelques commandes simples pour la gestion des rôles  
- Commandes d'aide avec des réponses rapides sur certains sujets qui sont aussi abordés dans [TChelp](https://github.com/TCastus/TChelp)

## Lancement via Docker

- Cloner le projet ``git clone https://github.com/TCastus/ASTUSbot && cd ASTUSbot``
- Construire l'image de l'image `docker build --tag astusbot .`
- Changer les valeurs dans le fichier ``.env``
- Lancer l'image ``docker run -it --rm --env-file .env -v $PWD:/bot --name container_astusbot astusbot``

## Build pour multiple arch avec buildx

```bash
docker buildx build --push --platform linux/amd64,linux/arm64,linux/arm/v6,linux/arm/v7 --tag [registry]/astusbot .
```

## Lancement sur cluster swarm

```bash
docker service create --name astusbot --env-file .env --restart-condition any [registry]/astusbot
```
