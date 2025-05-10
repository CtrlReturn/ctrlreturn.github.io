var.bln = var([0,1,0,-1])

k1 >> play("V{[ V]          }]", amp=0.7, spack=1)
k2 >> play("V ", lpf=200, room=10, size=10)

t1 >> arpy(b1.degree+P[:3], oct=(5,7), dur=PDur(5,8), delay=0, shape=2, rate=1, amplify=1)

t1.amp=1/8

#polyrhytm 1/3

v1 >> play("!", spack=1, sample=4, dur=8, rate=4/5, amplify=2/3*var([1,0], [8,24]), amp=1)

var.brks = var([1,0],[28,4,30,2,60,4,16,16])

c9 >> play("#", spack=1, sample=18, dur=16, cut=1, rate=1, chop=0, room=3/4, mix=1/2, pan=(-2/3,2/3), amplify=8/5*var([1,0],[16,96]), amp=1).stop()

c0 >> play("#", spack=1, sample=16, dur=16, cut=1, rate=1, chop=0, room=3/4, mix=1/2, pan=(-2/3,2/3), amplify=8/5*var([0,1], [96,16]), amp=1).stop()

k4 >> play("A", spack=1, sample=8, dur=1, delay=[0, 0.25, 0, 0.5], chop=1, rate=[1,1,1,1.5], amplify=1/2, amp=1).stop()

#offbeat 
h8 >> play("-", spack=1, sample=1, dur=1, delay=1/2, echo=[0,1/2], echotime=[0,2], amplify=3/4).every(8,"stutter",2).stop()

k4 >> play("V", spack=1, sample=12, dur=2, delay=[0,1/4,0,1/2], chop=1, rate=[1,1,1,1.5], amplify=1*var.brks, amp=1).stop()

s1 >> play("o", spack=1, sample=4, dur=2, delay=1, echo=[0,[0,1/2]], cut=1, amplify=6/5*var.brks, amp=1).stop()

h2 >> play("s", spack=1, sample=6, dur=1/2, cut=1/8, amplify=1/2*P[2/3,1]*var.brks, amp=1).stop()

k6 >> play("V", spack=1, sample=21, dur=1, delay=[0.5, 0.5, 0, 0.5], chop=1, rate=[1,1,1,1.5], amplify=2/3*var.brks, amp=1).stop()

Scale.default = Scale.mixolydian

k2 >> play("W", spack=1, sample=1, dur=4, delay=0, rate=1, room=1/2, mix=0, amplify=3/4*var.brks, amp=1)
k2.amp=0

k3 >> play("v", spack=1, sample=6, dur=8, chop=2, rate=[-1,1], amplify=2/3*var([1,0],[8,24]), amp=1)
k3.amp=0

p8 >> pulse(p1.degree, oct=var([6,7],64), dur=PDur(3,[7,8]), sus=1/8, pan=PSine(32), room=3/4, mix=1/2, amplify=2/3, amp=1).stop()

p9 >> bass(0, oct=(4,5), dur=4, sus=2, amplify=3/4)
p9.amp=0

s3 >> play("i", spack=1, sample=4, dur=1, delay=1/2, shape=1/2, amplify=1/2, amp=1)
s3.amp=0

h1 >> play("~", spack=1, sample=7, dur=1/2, delay=1/2, cut=1/2, echo=[0,1/2], echotime=[0,2], amplify=2/3*P[2/3,1/2], amp=1)
h1.amp=0

k3 >> play("x", spack=1, sample=3, dur=4, chop=0, formant=Pvar([0,linvar([0,3],64)],128), lpf=800, lpr=1/3, room=2/3, mix=1/3, amplify=1/3, amp=1)

k4 >> play("h", spack=1, sample=var([2,4],4), dur=PDur(3,8), amplify=1/2, amp=1)

p8 >> tworgan4(p2.degree, oct=4, dur=4, delay=0, sus=2, chop=8, shape=2, room=3/4, mix=1/2, amplify=1/4*linvar([1/8,1],64)*PRand([1,0],[32,64,32,16]), amp=1)

b4.stop()

Clock.bpm=93


b1 >> play("VV...[VV]..", dur=0.5, rate=1.2, sample=-1, amplify=0.4)
b2 >> play("VV...[VV]..", dur=0.5, sample=linvar([0,5], 4), amplify=0.4)

b1.amp=0
b2.amp=0

py >> glass(p1.degree+var([0,1,0,-2], 64), oct=(5,6), dur=4, chop=16, amplify=3/4, amp=1)
pv >> charm(py.degree, oct=(5,6), dur=2, delay=1, amplify=3/5, amp=1)

py.amp=0
pv.amp=0

pw >> tubularbell(pv.degree, oct=(7,8), dur=[1,PDur(5,8)], cut=1/2, amplify=3/4)
pw.amp=0

print(SynthDefs)

b0 >> donk([-5], fmod=4, slide=0, oct=(1, [0, [2,3,4]]), dur=PDur([3,7],8), amp=1, room=0.5) 

b6 >> play, dur=Pvar([1,0.5,0.25,0.1], [16,8,4,4]), rate=0.75, sample=2, amplify=Pvar([0.4,0], [30,2]))
            
play("o.", dur=Pvar([1,0.5,0.25,0.1], [16,8,4,4]), rate=0.75, sample=2, amplify=Pvar([0.4,0], [30,2]))

b7 >> play("[-.-.][-.--][-...][-.-.][--..][-.-.][-.-.][-...]", dur=1, rate=1, sample=2, amplify=1)

b8 >> play("[ss]", rate=1, sample=2, shape=0.6, amplify=0.8, amp=1).every(PRand([2,4,8,16]),"stutter", PRand([2,3,5]))

b3 >> fuzz(p1.degree[0], dur=PDur(var([5, [7,8]],[6,2]),8), lpf=linvar([900, 4900], [24,0]), lpr=PWhite(0.01,1), room=linvar([1/2,3/4],[24,0]), mix=linvar([1/2,2/3],[24,0]), amplify=2/3) + [0,0,0,[6,7]]

b3.amp=0

b4 >> play("T", spack=1, dur=var(PDur[1,3],6),6]))

pa >> filthysaw(p1.degree, oct=3, dur=8, chop=4, room=1/2, mix=1/2, amplify=1, amp=1)

b0 >> dbass(p1.degree, dur=PDur(var([5, [7,8]],[6,2]),8), lpf=linvar([900, 4900], [24,0]), lpr=PWhite(0.01,1)) + [0,0,0,[6,7]]

p2 >> play(P["|X3|-X--X<--V>"][:4], amp=0.6, chop=var([0,1], [13,3]), amplify=2/3)

b4 >> feel(p1.degree, dur=1/2, chop=320, formant=0, shape=0.5, oct=(3,4), amp=0.4, slide=0.04, lpf=linvar([1500, 5600]), lpr=PWhite(0.1,1)).spread()

b4.amp=0

b2 >> play("i", spack=1, dur=var([PDur([3,5],8),8],[8,1]), sample=P[:8], pan=PWhite(-1,1), lpf=p2.formant*2000, lpr=p2.dur, room=1/2, mix=1/2, amplify=1/2, amp=1)

d4 >> play("#", rate=[-1/2,-1], hpf=1000, dur=4, amp=0.8, room=1, coarse=[32,16,8,4])

p1 >> charm([0,4,0,2], dur=PDur(3,8), sus=2, chop=4, room=0.5, amplify=1/2).every(3, "offadd", 2).every(5, "stutter", 4, dur=3, oct=6)

p1.amp=0

print(SynthDefs)
                                                                                    
b5.oct=[7,6,[4,5]]
b5.drive=1
b5.room=3/4
b5.mix=1/3
b5.amp=PRand([1,0],[32,64,32,128])


p7 >> 

p1 >> pluck(b5.pitch, oct=(4,6), dur=PDur([4,3], 4), shape=0.01*PRand(1,10), room=2/3, mix=1/2, amp=1, drive=0.1, delay=(0,0.5,1, 1.5)).often("stutter", PRand([1,5]), oct=PRand([4,6]), room=PRand([0,5]))
p1.oct=3

n2 >> play("{ 1234                     }", chop=PRand([1,3]), rate=PRand([1,-1])/PRand(1,3), amp=2/3).often("stutter", PRand([1,5]))


sl >> bell(P[:2]+[0,1,2], dur=1/4, oct=5, amp = 1, room=1, mix=1/2, amplify=1/4)

h1 >> play("-", spack=1, dur=var([1/4,1],64), hpf=5000, delay=sinvar([-.05,.05], 0.5), amplify=[3/5,2/3,1/2,4/3], amp=[0,1,0,0]).stop()

h2 >> play("-", spack=1, sample=3, hpf=5000, delay=sinvar([-.075,.075], .5), amp=[0, 0, 0,1]).stop()
h3 >> play("-", spack=1, sample=9, hpf=5000, amplify=2/3, amp=1).stop()
hihat1 = Group(h1,h2,h3)


o1 >> play("y", spack=1, sample=14, dur=1/4, cut=1/3, rate=1, amplify=1/3*P[0,1,1,1], amp=1).solo(0)



l2 >> play("l", spack=1, dur=[1/3,2/3,0.5], rate=2, amplify=[1,2/3,1,1/2], amp=1) # polyrhythm 2



l1 >> play(" {[asdd][asd][as⁠⁠yellow-dingo⁠sd][aasd]} ", lpf=700, hpf=1000, rate=0.5, drive=0.1) # consider removing :)


p1 >> pluck(var.bln+P[:3], oct=5, dur=0.25, amp=1, hpf=0, crush=10, room=1/2,  mix=linvar([3/4,1/2],64), amplify=var([4/5,1], 64), amp=1)

s1 >> play(" o", spack=1, sample=1, dur=1, delay=PRand([0,0,0,1,-1]), amplify=3/4, amp=1)

p2 >> rsin(0, oct=PRand(5,6), dur=4, chop=16, lpf=700, lpr=linvar([1/4,1/2], 64), room=3/4, mix=1/2, amplify=linvar([1/2,3/4],128), amp=1)


