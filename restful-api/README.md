## 🌐 Différences entre HTTP et HTTPS

- **HTTP** : Protocole non sécurisé. Les données sont envoyées en clair et peuvent être interceptées, modifiées ou volées.
- **HTTPS** : Version sécurisée de HTTP. Les données sont **chiffrées via SSL/TLS**, ce qui empêche les interceptions lisibles sans la clé de déchiffrement.  
  👉 Même si les données sont interceptées, elles resteront **illisibles**.

---

## ⚙️ Méthodes HTTP les plus courantes

| Méthode | Description |
|--------|-------------|
| **GET**    | Utilisée pour **récupérer** une ressource. Exemple : afficher une page web ou obtenir des données via une API. |
| **POST**   | Utilisée pour **envoyer des données** et **créer** une nouvelle ressource. Exemple : inscription d’un nouvel utilisateur. |
| **PUT**    | Utilisée pour **remplacer** entièrement une ressource existante. Exemple : mise à jour complète d’un profil utilisateur. |
| **DELETE** | Utilisée pour **supprimer** une ressource. Exemple : suppression d’un utilisateur ou d’un article. |

---

## 📡 Codes de statut HTTP courants et scénarios

### ✅ 200 OK
> La requête a réussi, tout s’est bien passé.

**Scénario** :  
Un utilisateur ouvre une application sur son téléphone. Une requête `GET` est envoyée à l’API, qui répond avec les bonnes informations à afficher.

---

### 🆕 201 Created
> Une nouvelle ressource a été créée avec succès.

**Scénario** :  
Un utilisateur s’inscrit sur un site. Le serveur crée le compte et renvoie les données du profil nouvellement créé.

---

### 🔐 401 Unauthorized
> L’utilisateur n’est pas authentifié ou le token est invalide.

**Scénario** :  
L’utilisateur tente d’accéder à son tableau de bord, mais sa session a expiré. Il est redirigé vers la page de connexion.

---

### ❌ 404 Not Found
> La ressource demandée est introuvable.

**Scénario** :  
L’utilisateur clique sur un ancien lien d’article supprimé. Le site affiche : "Cette page n’existe pas".

---

### 💥 500 Internal Server Error
> Une erreur interne est survenue côté serveur.

**Scénario** :  
L’utilisateur clique sur "Acheter" sur un site d’e-commerce. Une erreur côté base de données empêche la commande de s’exécuter. Le site affiche :  
_"Une erreur est survenue. Veuillez réessayer plus tard."_

---


