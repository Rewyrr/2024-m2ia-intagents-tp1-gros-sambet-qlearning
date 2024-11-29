# RAPPORT

## Partie 1: Value Iteration

### Question 1 
*Préciser le détail du calcul des valeurs pour les 3 premières itérations de Value Iteration dans l'environnement BookGrid avec les paramètres par défaut*

itération k=1 :  

V1(<4,3>) = 1  

V1(<4,2>) = -1  

itération k=2 :   

s = V2(<3,3>)  
a = RIGHT, s' = {<4,3>, <3,3>, <3,2>} :  
    0.8 * [0.9 * 1 + y * 0] + 0.1 * [0.9 * 0 + y * 0] + 0.1 * [0.9 * 0 + y * 0] = 0.72  
a = LEFT, s' = {<2,3>, <3,3>, <3,2>} :  
    0.8 * [0.9 * 0 + y * 0] + 0.1 * [0.9 * 0 + y * 0] + 0.1 * [0.9 * 0 + y * 0] = 0  
a = UP, s' = {<3,3>, <4,3>, <2,3>} :  
    0.8 * [0.9 * 0 + y * 0] + 0.1 * [0.9 * 1 + y * 0] + 0.1 * [0.9 * 0 + y * 0] = 0.09  
a = DOWN, s' = {<3,2>, <4,3>, <2,3>} :  
    0.8 * [0.9 * 0 + y * 0] + 0.1 * [0.9 * 0 + y * 0] + 0.1 * [0.9 * 1 + y * 0] = 0.09  
V2(<3,3>) = max{0.72;0;0.09;0.09} = 0.72  

s = V2(<3,2>)  
a = RIGHT, s' = {<4,2>, <3,3>, <3,1>} :  
    0.8 * [0.9 * -1 + y * 0] + 0.1 * [0.9 * 0 + y * 0] + 0.1 * [0.9 * 0 + y * 0] = -0.72  
a = LEFT, s' = {<3,2>, <3,3>, <3,1>} :  
    0.8 * [0.9 * 0 + y * 0] + 0.1 * [0.9 * 0 + y * 0] + 0.1 * [0.9 * 0 + y * 0] = 0  
a = UP, s' = {<3,3>, <4,2>, <3,2>} :  
    0.8 * [0.9 * 0 + y * 0] + 0.1 * [0.9 * -1 + y * 0] + 0.1 * [0.9 * 0 + y * 0] = -0.09  
a = DOWN, s' = {<3,1>, <4,2>, <3,2>} :  
    0.8 * [0.9 * 0 + y * 0] + 0.1 * [0.9 * 0 + y * 0] + 0.1 * [0.9 * -1 + y * 0] = -0.09  
V2(<3,2>) = max{-0.72;0;-0.09;-0.09} = 0  

s = V2(<4,1>)  
a = RIGHT, s' = {<4,1>, <4,2>, <4,1>} :  
    0.8 * [0.9 * 0 + y * 0] + 0.1 * [0.9 * -1 + y * 0] + 0.1 * [0.9 * 0 + y * 0] = -0.09  
a = LEFT, s' = {<3,1>, <4,1>, <4,2>} :  
    0.8 * [0.9 * 0 + y * 0] + 0.1 * [0.9 * 0 + y * 0] + 0.1 * [0.9 * -1 + y * 0] = -0.09  
a = UP, s' = {<4,2>, <3,1>, <4,1>} :  
    0.8 * [0.9 * -1 + y * 0] + 0.1 * [0.9 * 0 + y * 0] + 0.1 * [0.9 * 0 + y * 0] = -0.72  
a = DOWN, s' = {<4,1>, <3,1>, <4,1>} :  
    0.8 * [0.9 * 0 + y * 0] + 0.1 * [0.9 * 0 + y * 0] + 0.1 * [0.9 * 0 + y * 0] = 0  
V2(<4,1>) = max{-0.72;0;-0.09;-0.09} = 0  

itération k=3 :   

s = V3(<3,3>)  
a = RIGHT, s' = {<4,3>, <3,3>, <3,2>} :  
    0.8 * [0.9 * 1 + y * 0] + 0.1 * [0.9 * 0.72 + y * 0] + 0.1 * [0.9 * 0 + y * 0] = 0.7848  
a = LEFT, s' = {<2,3>, <3,3>, <3,2>} :  
    0.8 * [0.9 * 0 + y * 0] + 0.1 * [0.9 * 0.72 + y * 0] + 0.1 * [0.9 * 0 + y * 0] = 0.0648  
a = UP, s' = {<3,3>, <4,3>, <2,3>} :  
    0.8 * [0.9 * 0.72 + y * 0] + 0.1 * [0.9 * 1 + y * 0] + 0.1 * [0.9 * 0 + y * 0] = 0.6084  
a = DOWN, s' = {<3,2>, <4,3>, <2,3>} :  
    0.8 * [0.9 * 0 + y * 0] + 0.1 * [0.9 * 0 + y * 0] + 0.1 * [0.9 * 1 + y * 0] = 0.09  
V3(<3,3>) = max{0.7848;0.0648;0.6084;0.09} = 0.7848  

s = V3(<3,2>)  
a = RIGHT, s' = {<4,2>, <3,3>, <3,1>} :  
    0.8 * [0.9 * -1 + y * 0] + 0.1 * [0.9 * 0.72 + y * 0] + 0.1 * [0.9 * 0 + y * 0] = -0.6552  
a = LEFT, s' = {<3,2>, <3,3>, <3,1>} :  
    0.8 * [0.9 * 0 + y * 0] + 0.1 * [0.9 * 0.72 + y * 0] + 0.1 * [0.9 * 0 + y * 0] = 0.0648  
a = UP, s' = {<3,3>, <4,2>, <3,2>} :  
    0.8 * [0.9 * 0.72 + y * 0] + 0.1 * [0.9 * -1 + y * 0] + 0.1 * [0.9 * 0 + y * 0] = 0.4284  
a = DOWN, s' = {<3,1>, <4,2>, <3,2>} :  
    0.8 * [0.9 * 0 + y * 0] + 0.1 * [0.9 * 0 + y * 0] + 0.1 * [0.9 * -1 + y * 0] = -0.09  
V3(<3,2>) = max{-0.72;0;-0.09;-0.09} = 0.4284  

s = V3(<4,1>)  
a = RIGHT, s' = {<4,1>, <4,2>, <4,1>} :  
    0.8 * [0.9 * 0 + y * 0] + 0.1 * [0.9 * -1 + y * 0] + 0.1 * [0.9 * 0 + y * 0] = -0.09  
a = LEFT, s' = {<3,1>, <4,1>, <4,2>} :  
    0.8 * [0.9 * 0 + y * 0] + 0.1 * [0.9 * 0 + y * 0] + 0.1 * [0.9 * -1 + y * 0] = -0.09  
a = UP, s' = {<4,2>, <3,1>, <4,1>} :  
    0.8 * [0.9 * -1 + y * 0] + 0.1 * [0.9 * 0 + y * 0] + 0.1 * [0.9 * 0 + y * 0] = -0.72  
a = DOWN, s' = {<4,1>, <3,1>, <4,1>} :  
    0.8 * [0.9 * 0 + y * 0] + 0.1 * [0.9 * 0 + y * 0] + 0.1 * [0.9 * 0 + y * 0] = 0  
V3(<4,1>) = max{-0.72;0;-0.09;-0.09} = 0  

s = V3(<2,3>)  
a = RIGHT, s' = {<3,3>, <2,3>, <2,3>} :  
    0.8 * [0.9 * 0.72 + y * 0] + 0.1 * [0.9 * -1 + y * 0] + 0.1 * [0.9 * 0 + y * 0] = 0.5184  
a = LEFT, s' = {<1,3>, <2,3>, <2,3>} :  
    0.8 * [0.9 * 0 + y * 0] + 0.1 * [0.9 * 0 + y * 0] + 0.1 * [0.9 * 0 + y * 0] = 0  
a = UP, s' = {<2,3>, <1,3>, <3,3>} :  
    0.8 * [0.9 * 0 + y * 0] + 0.1 * [0.9 * 0 + y * 0] + 0.1 * [0.9 * 0.72 + y * 0] = 0.0648  
a = DOWN, s' = {<2,3>, <3,3>, <1,3>} :  
    0.8 * [0.9 * 0 + y * 0] + 0.1 * [0.9 * 0.72 + y * 0] + 0.1 * [0.9 * 0 + y * 0] = 0.0648  
V3(<2,3>) = max{0.5184;0;0.0648;0.0648} = 0.5184  



### Question 2
*Modifier un seul des 2 paramètres (noise ou discount) pour obtenir une politique optimale qui permet à l'agent de traverser le pont (s'il n'était pas soumis au bruit). Préciser le paramètre modifié et sa valeur dans votre rapport et justifier votre choix.*

on modifie le paramètre noise à 0 qui permet d'assurer à l'agent de pouvoir se déplacer la où il le souhaite et donc de pouvoir atteindre la récompense avec la valeur la plus élever. Il va donc se rendre de l'autre côté du pont pour avoir le +10.  
Modifie le discount vers une valeur élevé pour l'attirer vers le +10 ne fonctionne pas car les bordures du ponts ont un négatif trop élevé.  

### Question 3
*Modifier un seul des 3 paramètres (noise, discount, livingReward) pour obtenir les politiques optimales ci-dessous. Préciser pour chaque politique, le paramètre modifié et sa valeur dans votre rapport et justifier votre choix.*

1. qui suit un chemin risqué pour atteindre l’état absorbant de récompense +1 ;  

Living reward = -4  
Avec un living reward négatif suffisament élevé on incite l'agent à explorer le moins possible. Il va donc prendre l'accès le plus rapide vers un état absorbant positif. Il ne faut pas le mettre trop bas sinon il va aller dans les états negatif et trop proche de 0 sinon il va considérer le +10.

2. qui suit un chemin risqué pour atteindre l’état absorbant de récompense +10 ;

noise = 0  
Réduire le bruit à 0 permet à l'agent de prendre le chemin le plus rapide vers la récompense la plus élevé.

3. qui suit un chemin sûr pour atteindre l’état absorbant de récompense +1 ;

discount = 0.2  
Un discount faible permet à l'agent de prioriser le présent et donc de prendre le choix avec la récompense la plus élevé la plus proche.
A 0 cela ne fonction pas car il ne considère plus que le présent et à 1 ou proche de 1 les récompense futur va rendre le +10 plus intéressant pour l'agent.

4. qui évite les états absorbants

living reward = 2  
Un living reward positif va faire que l'agent va explorer et non se rendre dans les états absorbants car l'exploration aura une meilleure récompense potentiel que de se rendre dans un état absorbant.

## Partie 2: QLearning tabulaire

### Question 4
*Précisez le détail du calcul des qvaleurs pour les 3 premiers épisodes.*

On a y = 0.9 et a = 0.5  

Episode 1  

Q(<4,3>,Est) = (1 - a) * Q(<4,3>,Est) + a * (1 + y * 0 ) = (1 - a) * 0 * + a * (1 + y * 0) = 0.5  

Episode 2  

Q(<4,3>,Est) = (1 - a) * Q(<4,3>,Est) + a * (1 + y * 0 ) = (1 - a) * 0.5 + a * (1 + y * 0 ) = 0.75  

Q(<3,3>,Est) = (1 - a) * Q(<3,3>,Est) + a * (0 + y * max(Q(<4,3>,actions)) ) = (1 - a) * 0 + a * (0 + y * 0.5 ) = 0.225  

Episode 3  

Q(<4,2>,Nord) = (1 - a) * Q(<4,2>,Nord) + a * (-1 + y * 0 ) = (1 - a) * 0 + a * (-1 + y * 0 ) = -0.5  

Episode 4  

Q(<4,2>,Nord) = (1 - a) * Q(<4,2>,Nord) + a * (1 + y * 0 ) = (1 - a) * -0.5 + a * (1 + y * 0 ) = -0.75  

Q(<4,1>,Nord) = (1 - a) * Q(<4,1>,Nord) + a * (0 + y * max(Q(<4,2>,actions)) ) = (1 - a) * 0 + a * (0 + y * -0.5 ) = -0.225  



### Question 5
*Expliquer les différences entre le résultat obtenu avec epsilon à 0.1 et à 0.9.*

Lorsque l'epsilon est à 0.1 le résultat est une politique qui oriente rapidement vers la case +1. Cela est du au fait que l'exploration est faible car l'epsilon est faible donc lorsqu'il trouve le bon chemin il va toujours s'y rediriger, alors que pour la case -1 il ne va plus y retourner.

Lorsque l'epsilon est à 0.9 le résultat est plus hasardeux car l'epsilon élevé fait que l'agent va beaucoup explorer et suivre la politique environ 1 fois sur 10 donc le résultat sera moins efficace mais on aura plus de données sur les autres cases.

### Question 6
*Préciser comment est modélisé l'environnement robot crawler sous forme de MDP (état, action, récompense). 
Quel est le comportement attendu de l'agent s'il suit sa politique optimale ?*

MDP du crawler :  
Les états du robots sont définis par 2 paramètres l'angle du bras et l'angle de la main. Donc le nombre totale d'états est le produit des deux, c'est à dire nArmStates=9 et nHandStates=13 donc 117 états au totals. L'états est une pair entre ces 2 angles.  

On a 4 actions possible :  
'arm-up' : Augmenter l'angle du bras.  
'arm-down' : Diminuer l'angle du bras.  
'hand-up' : Augmenter l'angle de la main.  
'hand-down' : Diminuer l'angle de la main.  

Ce sont les mouvement du bras et de la main et sont parfois limite lorsque l'angle est maximum ou minimum on ne peut pas faire une action qui augmente ou réduit l'angle du membres correspondant.  

Les récompenses dans ce système ce font en fonction de la différence entre l'ancienne position du robot en x et la nouvelle apres l'action effectué. Si l'action fait avance le robot le reward est positif et s'il le fait rester sur place ou reculer la récompense est nulle ou négative.  

L'environnement est déterministe car à chaque état une action donnée conduit toujours au même état suivant. chaque action faite dans un état donne un résultat prévisible.  

Une politique optimale dans cet environnement vise à maximiser la récompense totale, c'est-à-dire maximiser le déplacement horizontal du robot et donc de permettre au robot d'avancer.  

### Question 7
*Expliquer pourquoi le comportement appris est différent entre les versions 1 et 2.*

La différence entre les 2 versions est la modélisation du MDP dans la première le MDP contient uniquement les coordonnées et la direction des entités donc l'agent ne connait pas la position de la nourriture et capsule. Il doit donc agir uniquement en fonction des déplacement des fantômes et donc rend plus difficile la collecte.  

Le 2eme MDP contient les même informations mais en plus la position des collectible ainsi que le score. Donc l'agent à de meilleure information.

L'apprentissage est donc différents pour la 1er version l'agent va apprendre à eviter les fantômes alors que l'autre agent va apprendre à avoir un meilleure score. 

### Question 8
*Expliquer les principaux avantages du QLearning Approximé par rapport au QLearning tabulaire.*

Scalabilité : Le QLearning Approximé peut gérer de très grands espaces d’états en utilisant des caractéristiques (features), contrairement au QLearning Tabulaire qui stocke des Q-valeurs pour chaque état-action, ce qui devient impraticable dans des environnements complexes.  

Généralisation : L’approximation permet de généraliser l’apprentissage entre états similaires, accélérant ainsi l’apprentissage, alors que le QLearning Tabulaire doit explorer chaque état individuellement.  

Efficacité mémoire : Le QLearning Approximé utilise des vecteurs de poids pour les caractéristiques, réduisant l’utilisation de mémoire par rapport à la table de Q-valeurs du QLearning Tabulaire.  

Vitesse de convergence : En généralisant les apprentissages, le QLearning Approximé converge plus rapidement que la version tabulaire, surtout dans des environnements avec beaucoup d’états.  

Adaptabilité aux environnements continus : Le QLearning Approximé fonctionne bien dans des environnements continus ou dynamiques, contrairement au QLearning Tabulaire, qui est limité aux espaces d’états discrets.  

En résumé, le QLearning Approximé est plus efficace en termes de mémoire, d’apprentissage, et de généralisation dans des environnements complexes ou continus, ce qui en fait une solution supérieure au QLearning Tabulaire pour des problèmes à grande échelle.  


