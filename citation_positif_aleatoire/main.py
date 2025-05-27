import random

#TABLEAU POUR LES CITATION
tab_citation = [
    "Le meilleur moyen de prédire l'avenir est de le créer. de Peter Drucker",
    "La vie, ce n'est pas d'attendre que les orages passent, c'est d'apprendre à danser sous la pluie. de Sénèque ",
    "Croyez en vos rêves et ils se réaliseront. Croyez en vous et vous vous réaliserez. de Martin Luther King Jr",
    "L'optimisme est la foi qui mène au succès. Rien ne peut être fait sans espoir et confiance. de Helen Keller",
    "Ce n'est pas la force du corps qui compte, mais la force de l'esprit. de J.R.R. Tolkien ",
    "Commencez par faire le nécessaire, puis faites ce qu'il est possible de faire, et tout à coup, vous faites l'impossible. de Saint François d'Assise ",
     "Le succès n'est pas final, l'échec n'est pas fatal : c'est le courage de continuer qui compte. de Winston Churchill",
     "Ne craignez pas l'échec, craignez de ne pas essayer. de Roy T. Bennett",
     "Le bonheur ne se trouve pas, il se construit. de Epicure",
     "Soyez reconnaissant pour ce que vous avez ; vous finirez par en avoir plus. Si vous vous concentrez sur ce que vous n'avez pas, vous n'en aurez jamais assez. de Oprah Winfrey",
     "La joie de vivre vient de ce que l'on donne, non de ce que l'on reçoit. de Albert Einstein"

]

citation_choisie = random.choice(tab_citation)

print("Citation aleatoire :  ")
print(f" {citation_choisie}")