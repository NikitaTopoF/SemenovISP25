for bikov in range(11):       
    for korov in range(21):   
        for telyat in range(101):
            if (bikov + korov + telyat == 100) and (bikov * 10 + korov * 5 + telyat * 0.5 == 100):
                print("Быков:", bikov, "Коров:", korov, "Телят:", telyat)
