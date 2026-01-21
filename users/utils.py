def est_gestionnaire(user):
    return hasattr(user, 'producteur') and user.producteur.role == 'GESTIONNAIRE'
