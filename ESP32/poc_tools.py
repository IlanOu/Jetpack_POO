def map_value(value, from_low, from_high, to_low, to_high):
    # Vérifier si la valeur est dans la plage source
    if value > from_high:
        value = from_high
    elif value < from_low:
        value = from_low
    
    # Calculer la plage effective pour la valeur
    from_range = from_high - from_low
    to_range = to_high - to_low
    
    # Déterminer si la valeur est négative
    is_negative = value < 0
    
    # Si la valeur est négative, la normaliser dans la plage positive
    if is_negative:
        normalized_value = value + abs(from_low)
    else:
        normalized_value = value - from_low
    
    # Calculer le pourcentage de la valeur dans la plage source
    percentage = normalized_value / from_range
    
    # Calculer la valeur dans la plage cible
    mapped_value = to_low + percentage * to_range
    

    
    return mapped_value
