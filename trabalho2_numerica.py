# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 00:28:33 2023

@author: rodri
"""
import sympy as sym
from sympy import symbols, integrate, pi, sin, cos, exp, log
import math

r = int(input("Quer fazer as regras do Trapézio, de Simpson e de Gauss para 3 pontos ou quer fazer as suas ordens de convergência? Responda 1 ou 2. ")) 
x = symbols('x')

if r == 1:
    a = float(input("Qual é o limite inferior do integral? "))
    b = float(input("Qual é o limite superior do integral? "))
    c = int(input("Qual é o número de pontos que quer? (Se escolher um número par de pontos para a regra de Simpson será adicionado mais um ponto. "))
    n = c - 1
if r == 2:
    a = float(input("Qual é o limite inferior do integral? "))
    b = float(input("Qual é o limite superior do integral? "))
    c = int(input("Qual é o número de pontos com que quer fazer o primeiro erro? "))
    n = c - 1


def pontos(X, h, c):   #cria os pontos a partir de h (espaçamento entre os pontos)
    for i in range(0, c):
        X.append(a + i * h)
    return X
    
def f(k):              #função que será aproximada/estudada
    return sin(2 * math.pi * (abs(k - 0.2) + abs(k - 0.4) + abs(k - 0.6)))

    
def trapezio_comp(n):  #regra do trapézio composta
    X = []
    h = (b - a)/n
    pontos(X, h, n+1)
    d = 0
    for j in range(1, n):
        d = d + f(X[j])
    return (h/2)*(f(a) + 2 * d + f(b))

def erro_trapezio(n):  #erro exato da regra do trapézio
    return abs(integrate(f(x), (x, a, b)) - trapezio_comp(n))

def ordem_conv_trapezio():   #cálculo da ordem de convergência para a regra do trapézio
    j = n
    quant = 7
    ordem_trap = []
    for i in range(0, quant):
        erro1 = erro_trapezio(j)
        erro2 = erro_trapezio(2*j)
        ordem_trap.append(log(erro2/erro1)/log(1/2))
        j = 2*j
    return ordem_trap
        
def simpson_comp(n):   #regra de simpson composta
    X = []
    n2 = n+1
    if n2 % 2 == 0:
        n2 = n2 + 1
    h = (b - a)/(n2 - 1)
    pontos(X, h, n2)
    k = 0
    for j in range(1, int((n2 + 1)/2)):
        k = k + f(X[2*j - 1])
    e = 0
    for i in range(1, int((n2 - 1)/2)):
        e = e + f(X[2*i])
        
    return (h/3)*(f(a) + 4*k + 2*e + f(b))    

def erro_simpson(n):  #erro exato da regra de simpson composta
    return abs(integrate(f(x), (x, a, b)) - simpson_comp(n))

def ordem_conv_simpson():   #cálculo da ordem de convergência para a regra de simpson composta
    q = n
    quant = 7
    ordem_simp = []
    for i in range(0, quant):
        erro1 = erro_simpson(q)
        erro2 = erro_simpson(2*q)
        ordem_simp.append(log(erro2/erro1)/log(1/2))
        q = 2*q
    return ordem_simp

def gauss_3pts_comp(n):   #regra de gauss para 3 pontos composta
    X = []
    m = 0
    v = (b - a)/n
    pontos(X, v, n+1)
    for i in range(1, n+1):
        h = (X[i] - X[i-1])/2
        m = m + h*((5/9) * f(-math.sqrt(3/5) * h + (X[i-1] + X[i])/2) + (8/9) * f((X[i-1] + X[i])/2) + (5/9) * f(math.sqrt(3/5) * h + (X[i-1] + X[i])/2)) 
    return m

def erro_gauss(n):   #erro exato da regra de gauss composta
    return abs(integrate(f(x), (x, a, b)) - gauss_3pts_comp(n))

def ordem_conv_gauss():  #cálculo da ordem de convergência para a regra de gauss para 3 pontos composta
    w = n
    quant = 7
    ordem_gauss = []
    for i in range(0, quant):
        erro1 = erro_gauss(w)
        erro2 = erro_gauss(2*w)
        ordem_gauss.append(log(erro2/erro1)/log(1/2))
        w = 2*w
    return ordem_gauss
        
    
def main(n):   #função que é chamada
    if r == 1:
        print("")
        print("Regra do trapézio:", trapezio_comp(n))
        print("Erro exato da regra do trapézio", erro_trapezio(n))
        print("")
        print("Regra de Simpson:", simpson_comp(n))
        print("Erro exato da regra de Simpson:", erro_simpson(n))
        print("")
        print("Regra de Gauss para 3 pontos composta:", gauss_3pts_comp(n))
        print("Erro exato da Regra de Gauss para 3 pontos composta:", erro_gauss(n))
    if r == 2:
        print("")
        print("Ordem de convergência da regra do Trapézio:", ordem_conv_trapezio())
        print("")
        print("Ordem de convergência da regra de Simpson:", ordem_conv_simpson())
        print("")
        print("Ordem de convergência da regra de Gauss:", ordem_conv_gauss())
    
main(n)