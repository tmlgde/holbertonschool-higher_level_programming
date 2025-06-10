Differences entre http et https:
    -Difference basique entre http et https:
        La requete http est moins s√©uris√√© car contrairement a la rete https, elle ne va pas envoyer les donn√es chiffr√es via SSL/TLS, elle va directement envoyer les dones (possibilite de modifier les mots
de passe) etc... Si les donnees se font "intercepter", les donnees seront tout de meme illisibles grace a la cle de dechiffrement

Les 4 methodes communes en http:
    -Get: Utilise pour recuperer une ressource, par exemple pour afficher une page web ou recuperer des donnees API
    -Post: Utilise pour envoyer des donnees pour creer une ressource, par exemple pour creer un nouvel utilisateur
    -Put: Utilise pour remplacer une ressource, par exemple pour mettre a jour un utilisateur deja existant
    -Delete: Utilise pour supprimer une ressource, par exemple pour supprimer un utilisateur

Les 5 codes status les plus communs en http:
    -Erreur 200: Requete reussie, tout s'est bien passe.
        Un utilisateur ouvre une application sur son telephone, une requete Get est envoye vers l'API qui renvoie les bonnes informations.
    -Erreur 201: Une nouvelle ressource a ete creer avec succes.
        Un utilisateur veut creer un compte sur un site, le serveur renvoie bien les informations du compte nouvellement creer.
    -Erreur 401: L'utilisateur n'est pas authentifie, ou le token est invalide.
        Un utilisateur tente de se connecter a son tableau de bord personnel, mais il a ete deconnecte. L'application renvoie l'utilisateur vers la page de connexion.
    -Erreur 404: La ressource demandee n'existe tout simplement pas.
        Un utilisateur tente de cliquer sur un lien qui n'existe plus ou qui a expire. Le site affiche un message qui explique le probleme.
    -Erreur 500: Une erreur interne est survenue cote serveur.
        Un utilisateur veut acheter quelque chose sur un site. Il clique donc sur "acheter". La demande est envoyee vers la base de donnees, mais le serveur est en panne. L'utilisateur voit donc un message
        "Une erreur est survenue. Veuillez reessayer plus tard."
