# StarLite II — déploiement du site éditorial (GitHub Pages)

## Ce que contient ce dossier
Un site éditorial complet À DÉPOSER autour de ton jeu, pour lever le refus AdSense
« contenu à faible valeur informative ». Ton jeu ne change pas — il passe juste
dans le sous-dossier /play/.

    index.html            → accueil éditorial (NE PAS régénérer)
    guide/index.html      → guide de prise en main
    factions/index.html   → encyclopédie des 39 unités (générée depuis UNIT_DATA)
    devlog/index.html      → journal de dev (netcode, perf, architecture)
    confidentialite.html  → politique de confidentialité (OBLIGATOIRE pour AdSense)
    contact.html          → page contact
    play/index.html       → TON JEU (avec <base href="/play/"> injecté)
    assets/site.css       → style du site (n'affecte pas le jeu)
    robots.txt, sitemap.xml

## Étape 1 — copier dans ton repo starlite-game
Copie TOUT le contenu de ce dossier à la racine de ton repo, en gardant CNAME,
ads.txt et ton dossier assets/ (les .glb du jeu) existants.

Ton assets/ du jeu et le assets/site.css cohabitent dans le même dossier — aucun
conflit de noms. Vérifie juste que assets/site.css est bien ajouté à côté des .glb.

## Étape 2 — le point technique à ne pas rater
Ton jeu charge ses .glb en chemins relatifs (./assets/...). En passant dans /play/,
la balise <base href="/play/"> (déjà injectée) fait que le jeu cherche ses assets
dans /play/assets/. DEUX options :

  A) le plus simple : garde ton dossier assets/ des .glb À LA RACINE, et change la
     base en <base href="/">  → le jeu dans /play/ ira chercher /assets/ (racine).
  B) ou copie/déplace ton dossier assets/ (les .glb) dans /play/assets/.

→ Recommandé : option A. Édite play/index.html, remplace
     <base href="/play/">   par   <base href="/">
   et laisse ton dossier assets/ (.glb) à la racine. Un seul assets/ pour tout.

## Étape 3 — mettre à jour le jeu plus tard (garde ton workflow 1 fichier)
Quand ton IA dev t'envoie un nouveau index.html du jeu :
  1. Renomme-le / place-le en play/index.html
  2. Réinjecte la balise base juste après <meta charset="utf-8"> :
        <base href="/">
  Le script inject_base.py fait ça automatiquement (voir ci-dessous).

## Étape 4 — AdSense
  1. Push, attends que GitHub Pages déploie.
  2. Ajoute une CMP de consentement certifiée Google (obligatoire trafic UE).
     Le plus simple : le message de consentement intégré d'AdSense
     (Confidentialité & messages → Message RGPD, dans ton compte AdSense).
  3. NE PLACE PAS d'annonces sur /play/ (écran fonctionnel). Uniquement sur les
     pages de contenu (accueil, guide, factions, devlog).
  4. Laisse Google recrawler quelques jours, coche « j'ai corrigé les problèmes »,
     demande un examen. Compte quelques jours à 2 semaines.
