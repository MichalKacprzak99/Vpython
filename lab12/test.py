tmp2=1+(math.sin(phi1-teta1))**2

    ball1_radio_acc=(-g1/L1*(2*math.sin(phi1)-math.sin(teta1)*math.cos(phi1-teta1))-1/2*ball1_radio_vel*math.sin(2*phi1-2*teta1))/tmp1
    ball2_radio_acc=(-g1/L1*(2*math.sin(teta1)-2*math.sin(phi1)*math.cos(phi1-teta1))+1/2*ball2_radio_vel*math.sin(2*phi1-2*teta1))/tmp1
    
    ball1_radio_vel=ball1_radio_vel+ball1_radio_acc*dt
    ball2_radio_vel=ball2_radio_vel+ball2_radio_acc*dt

    phi1=phi1+ball1_radio_vel*dt
    teta1=teta1+ball2_radio_vel*dt

    ball1.pos=vector(L1*math.sin(phi1),-L1*math.cos(phi1),0)
    ball2.pos=vector(L1*(math.sin(phi1)+math.sin(teta1)),-L1*(math.cos(phi1)+math.cos(teta1)),0)

    con1.axis=ball1.pos
    con2.pos=ball1.pos
    con2.axis=ball2.pos-ball1.pos