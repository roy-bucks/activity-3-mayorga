class compute(): 

    #compute the hp
    def hp(data):
        total_hp = (((2 * data["base"] + data["iv"] + (data["ev"]/4))* data["level"])/100) + (data["level"] + 10)
        return total_hp